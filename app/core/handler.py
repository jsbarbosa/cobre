import os
import re
import gzip
import json
import pickle
import requests
import pandas as pd

from . import constants
from sqlalchemy import text
from app.config.connections import get_connection
from app.config.settings import BASE_PATH, SLACK_WEBHOOK_URL


with gzip.open(os.path.join(BASE_PATH, 'assets', 'model.gz'), 'rb') as file:
    MODEL = pickle.load(file)


class ScoreHandler:
    @staticmethod
    def merge(identity, transaction):
        data = pd.DataFrame(
            pd.concat(
                [
                    pd.Series(identity),
                    pd.Series(transaction)
                ]
            )
        ).T.rename(
            columns={
                'device_type': 'DeviceType',
                'device_info': 'DeviceInfo',
                'transaction_dt': 'TransactionDT',
                'transaction_amt': 'TransactionAmt',
                'product_cd': 'ProductCD',
                'r_emaildomain': 'R_emaildomain',
                'p_emaildomain': 'P_emaildomain'
            }
        )

        data.columns = [
            col.title() if re.match(r'[cmvd]\d+', col) else col
            for col in data.columns
        ]

        dtypes = dict(
            constants.IDENTITY_COLUMN_TYPES,
            **constants.TRANSACTION_COLUMN_TYPES
        )

        del dtypes['TransactionID']
        del dtypes['isFraud']

        return data.astype(
            dtypes
        )
    
    @staticmethod
    def get_features(data):
        return pd.Series(
            MODEL[0].transform(
                data
            )[0],
            index=MODEL[0].get_feature_names_out()
        )
    
    @staticmethod
    def calculate_score(features: pd.Series):
        """
        Calculates the probability of a transaction being fraud
        """
        
        return MODEL[1].predict_proba(
            [
                features.values
            ]
        )[0, 1]
        
    @staticmethod
    def get_from_db(transaction_id: int):
        with get_connection() as conn:
            result = conn.execute(
                text(
                    f"""
                    SELECT
                        score
                    FROM
                        fraud_details
                    WHERE
                        transaction_id = {transaction_id}
                    """
                )
            )
            
            result = result.fetchall()
        
        if result:
            return result[0][0]
    
    @staticmethod
    def write_to_db(transaction_id: int, score: float, data: pd.Series, features: pd.Series):
        features['transaction_id'] = transaction_id
        features['score'] = score
        
        df = pd.concat(
            [
                data.loc[0, constants.FREQUENCY_ENCODER_COLUMNS + constants.ONEHOT_ENCODER_COLUMNS],
                features.rename(
                    {
                        col: f'fe_{col}'
                        for col in constants.FREQUENCY_ENCODER_COLUMNS
                    }
                )
            ]
        ).to_frame().T
        
        with get_connection() as conn:
            df.to_sql(
                'fraud_details',
                conn,
                if_exists='append',
                index=False
            )

    @classmethod
    def run(cls, transaction_id: int, identity, transaction):
        score = cls.get_from_db(transaction_id)
    
        if score is None:
            merged = cls.merge(identity, transaction)
            features = cls.get_features(merged)
            score = cls.calculate_score(features)
            cls.write_to_db(transaction_id, score, merged, features.round(6))
            
        return {
            'score': score
        }
        

def send_slack_alert(message: str):
    """
    Sends an alert message to a Slack channel via a webhook.
    """
    
    response = requests.post(
        SLACK_WEBHOOK_URL, 
        data=json.dumps(
            {
                "text": message
            }
        ), 
        headers={
            "Content-Type": "application/json"
        }
    )
    
    if response.status_code == 200:
        return {
            'status': response.status_code,
            'text': 'Alert sent successfully!'
        }
    else:
        return {
            'status': response.status_code,
            'text': f'Failed to send alert. Status code: {response.status_code}, Response: {response.text}'
        }

