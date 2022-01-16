import pip
from src.pipelines import utils
from src.pipelines import pipelines
import pandas as pd


def run_pipeline(download_link: str):
    # downloading the data
    utils.download_data(download_link)

    # reading downloaded data
    df = pd.read_csv("data/fraud_detection_dataset.csv")

    # preprocessing on the dataset
    pre_processing_pipe = pipelines.PreProcessingPipe(dataset=df)
    pre_processing_pipe.drop_columns(
        columns=["isFlaggedFraud", "step", "nameOrig", "nameDest"]
    )
    pre_processing_pipe.filter_type_classes(classes=["PAYMENT", "CASH_IN", "DEBIT"])
    pre_processing_pipe.train_test_splitting(sample_test_size=0.40)
    pre_processing_pipe.label_encoding()
    pre_processing_pipe.scaling()

    # training
    training_pipe = pipelines.Training(
        X_train=pre_processing_pipe.X_train,
        X_test=pre_processing_pipe.X_test,
        y_train=pre_processing_pipe.y_train,
        y_test=pre_processing_pipe.y_test,
    )
    training_pipe.fit_logistic_regression()
    training_pipe.predict_logistic_regression()
    metrics = training_pipe.calculate_metrics()

    print(metrics)
