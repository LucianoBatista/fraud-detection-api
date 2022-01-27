import pickle

from src.pipelines.pipelines import PreProcessingPipe

current_model_path = "src/models/21_01_22_lr_w_v3.sav"


# helpers functions
def download_data(download_link: str):
    print(download_link)


def predict(data):
    # Pre-processing Pipeline
    pre_processing_pipe = PreProcessingPipe(dataset=data, X_test=data)
    pre_processing_pipe.one_hot_encoder(["day_of_month", "type"], is_x_test=True)

    # x_test and y_test
    x_test = pre_processing_pipe.X_test

    with open(current_model_path, "rb") as f:
        model = pickle.load(f)

    y_hat_predict = model.predict(x_test)

    return y_hat_predict
