from random import sample
from threading import local
import pandas as pd
from pandas import DataFrame, Series
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class PreProcessingPipe:
    def __init__(self, dataset: DataFrame) -> None:
        self.dataset = dataset
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def validate_columns(self) -> bool:
        columns = self.dataset.columns
        if list(columns) != [
            "step",
            "type",
            "amount",
            "nameOrig",
            "oldbalanceOrg",
            "newbalanceOrig",
            "nameDest",
            "oldbalanceDest",
            "newbalanceDest",
            "isFraud",
            "isFlaggedFraud",
        ]:
            return False
        else:
            return True

    def drop_columns(self, columns: list) -> None:
        self.dataset.drop(columns, axis=1, inplace=True)

    def filter_type_classes(self, classes: list):
        self.dataset = self.dataset[~self.dataset["type"].isin(classes)]

    def train_test_splitting(self, sample_test_size: float):
        X_dataset = self.dataset.drop(["isFraud"], axis=1)
        y_target = self.dataset[["isFraud"]]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_dataset,
            y_target,
            test_size=sample_test_size,
            random_state=10,
            stratify=y_target,
        )

    def label_encoding(self):
        le = preprocessing.LabelEncoder()
        le.fit(self.X_train["type"])

        # looking at the classes
        print(list(le.classes_))

        self.X_train["type"] = le.transform(self.X_train["type"])
        self.X_test["type"] = le.transform(self.X_test["type"])

    def scaling(self):
        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))

        scaler.fit(self.X_train)
        X_train_np = scaler.transform(self.X_train)
        x_test_np = scaler.transform(self.X_test)

        self.X_train = pd.DataFrame(X_train_np, columns=self.X_train.columns)
        self.X_test = pd.DataFrame(x_test_np, columns=self.X_test.columns)


class Training:
    def __init__(
        self,
        X_train: DataFrame,
        X_test: DataFrame,
        y_train: Series,
        y_test: Series,
    ) -> None:
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.lrc = None
        self.y_pred_train = None
        self.y_pred_test = None

    def fit_logistic_regression(self):
        # logistic regression classifier, default threshold is 0.5
        self.lrc = LogisticRegression()

        # fitting on training data
        _ = self.lrc.fit(self.X_train, self.y_train)

    def predict_logistic_regression(self):
        self.y_pred_train = self.lrc.predict(self.X_train)
        self.y_pred_test = self.lrc.predict(self.X_test)

    def calculate_metrics(self):
        # train
        accuracy_training = (accuracy_score(self.y_train, self.y_pred_train),)
        precision_training = precision_score(self.y_train, self.y_pred_train)
        recall_training = recall_score(self.y_train, self.y_pred_train)
        auc_training = roc_auc_score(self.y_train, self.y_pred_train)

        # test
        accuracy_testing = (accuracy_score(self.y_test, self.y_pred_test),)
        precision_testing = precision_score(self.y_test, self.y_pred_test)
        recall_testing = recall_score(self.y_test, self.y_pred_test)
        auc_testing = roc_auc_score(self.y_test, self.y_pred_test)

        metrics_training = {
            "training": {
                "accuracy": accuracy_training,
                "recall": recall_training,
                "precision": precision_training,
                "auc": auc_training,
            },
            "testing": {
                "accuracy": accuracy_testing,
                "recall": recall_testing,
                "precision": precision_testing,
                "auc": auc_testing,
            },
        }

        return metrics_training
