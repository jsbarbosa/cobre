import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._map = {}

    def fit(self, X, y=None):
        self._map = {
            col: X[col].value_counts()
            for col in X
        }
        return self

    def transform(self, X):
        return pd.concat(
            [
                X[col].map(self._map[col])
                for col in X
            ],
            axis=1
        )

    def get_feature_names_out(self, *args):
        return list(self._map.keys())


class DateEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        in_days = X / (24 * 60 * 60)

        return pd.concat(
            [
                in_days.astype(int).rename('day'),
                ((in_days % 1) * 24).rename('time'),
                (in_days % 7).astype(int).rename('day_of_week'),
                (in_days % 31).astype(int).rename('day_of_month')
            ],
            axis=1
        ).values

    def get_feature_names_out(self, *args):
        return [
            'day', 'time', 'day_of_week', 'day_of_month'
        ]
        