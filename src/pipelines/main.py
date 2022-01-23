from flask_sqlalchemy import model
import pip
from src.pipelines import utils
from src.pipelines import pipelines
from src.database.crud import model_crud
import pandas as pd


def run_pipeline(download_link: str, training_queue_id: int):
    # reading downloaded data
    df = pd.read_csv(download_link)

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

    # comparing the models
    # get_metrics from the actual model
    metrics_obj = model_crud.get_metrics()
    f1_enabled_model = metrics_obj.f1
    f1_trained_model = metrics.get("testing").get("f1")
    # compare the f1 metric
    if f1_trained_model > f1_enabled_model:
        # update if the f1 score is higher than the actual model
        model_crud.update_model(model_id=metrics_obj.id)

        # model to add
        model = {
            "modelname": f"model_{training_queue_id}",
            "accuracy": metrics.get("accuracy"),
            "recall": metrics.get("recall"),
            "precision": metrics.get("precision"),
            "f1": metrics.get("f1"),
            "time": 12,
            "auc": 123,
        }

        model_crud.add_new_model(model)
        # update queued model
