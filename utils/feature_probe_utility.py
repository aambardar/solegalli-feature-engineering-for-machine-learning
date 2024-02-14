import pandas as pd


class FeatureExploratoryAnalysis:

    def group_by_datatypes(df: pd.DataFrame):
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        numerical_columns = df.select_dtypes(include=['int', 'float']).columns.tolist()
        boolean_columns = df.select_dtypes(include=['bool']).columns.tolist()
        datetime_columns = df.select_dtypes(include=['datetime']).columns.tolist()

        dtype_data = {"categorical_columns": categorical_columns, "numerical_columns": numerical_columns,
                      "boolean_columns": boolean_columns, "datetime_columns": datetime_columns}

        # dtype_df = pd.DataFrame(dtype_data, index=["columns"])
        dtype_df = pd.DataFrame(dtype_data)
        return dtype_df
