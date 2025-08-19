import os

import pandas as pd

class ParquetFormat:
    def __init__(self, input_csv_path, output_parquet_path, stats_output_csv_path):
        self.input_csv_path = input_csv_path
        self.output_parquet_path = output_parquet_path
        self.stats_output_csv_path = stats_output_csv_path
        self.df = None

    def read_and_convert_to_parquet(self):
        df = pd.read_csv(self.input_csv_path, encoding='UTF-8')
        df.to_parquet(self.output_parquet_path, index=False)

    def compute_stats(self):
        # input Parquet
        df = pd.read_parquet(self.parquet_path, engine='pyarrow')
        numeric_df = df.select_dtypes(include=['number'])

        # calculate
        stats = pd.DataFrame({
            "max": numeric_df.max(),
            "min": numeric_df.min(),
            "mean": numeric_df.mean(),
            "abs_max": numeric_df.abs().max(),
            "abs_min": numeric_df.abs().min(),
            "abs_mean": numeric_df.abs().mean()
        })

        # save to csv
        stats_path = os.path.splitext(self.parquet_path)[0] + '_stats.csv'
        stats.to_csv(stats_path)

        print(f"finish：{stats_path}")
        print(stats)

if __name__ == '__main__':
     obj = ParquetFormat("D:/black/AirQualityUCI.csv","D:/class_project/personnel_develop/test01/week3/data.parquet","D:/black/result.csv")
     # obj.read_csv()
     obj.compute_stats()