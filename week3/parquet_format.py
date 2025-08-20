import pandas as pd

class ParquetFormat:
    def __init__(self, input_csv_path, output_parquet_path, stats_output_csv_path):
        self.input_csv_path = input_csv_path
        self.output_parquet_path = output_parquet_path
        self.stats_output_csv_path = stats_output_csv_path

    def read_and_convert_to_parquet(self):
        df = pd.read_csv(
            self.input_csv_path,
            sep=';',
            encoding='utf-8',
            na_values=['::', ':', '']
        )
        df.to_parquet(self.output_parquet_path, index=False, engine='pyarrow')

    def compute_stats(self):
        df = pd.read_parquet(self.output_parquet_path, engine='pyarrow')
        numeric_df = df.select_dtypes(include=['number'])
        stats = pd.DataFrame({
            "max": numeric_df.max(numeric_only=True),
            "min": numeric_df.min(numeric_only=True),
            "mean": numeric_df.mean(numeric_only=True),
            "abs_max": numeric_df.abs().max(numeric_only=True),
            "abs_min": numeric_df.abs().min(numeric_only=True),
            "abs_mean": numeric_df.abs().mean(numeric_only=True),
        })

        stats.to_csv(self.stats_output_csv_path, encoding='utf-8')

        print(f"finish: {self.stats_output_csv_path}")
        print(stats)
        return stats

if __name__ == '__main__':
    obj = ParquetFormat(
        "D:/black/AirQualityUCI.csv",
        "D:/class_project/personnel_develop/test01/week3/data.parquet",
        "D:/black/result.csv"
    )
    obj.read_and_convert_to_parquet()
    obj.compute_stats()