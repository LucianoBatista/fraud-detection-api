from src.pipelines import utils
import pandas as pd


def run_pipeline(download_link: str):
    # downloading the data
    utils.download_data(download_link)

    # reading downloaded data
    df = pd.read_csv("data/fraud_detection_dataset.csv")
    print(df)
