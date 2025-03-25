import os
import re
import gzip
import pickle
import pandas as pd
from . import constants
from app.config.settings import BASE_PATH


with gzip.open(os.path.join(BASE_PATH, 'assets', 'model.gz'), 'rb') as file:
    MODEL = pickle.load(file)


def calculate_score(identity, transactions):
    data = pd.DataFrame(
        pd.concat(
            [
                pd.Series(identity),
                pd.Series(transactions)
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

    transformed = pd.Series(
        MODEL[0].transform(
            data.astype(
                dtypes
            )
        )[0],
        index=MODEL[0].get_feature_names_out()
    )
    
    score = MODEL[1].predict_proba(
        [
            transformed.values
        ]
    )[0, 1]

    return {
        'score': score,
        'features': transformed.to_dict()
    }
    
    