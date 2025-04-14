import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


# Get Snowflake connection details from user
user = input('🔐 Enter Snowflake user: ')
password = input('🔑 Enter your Snowflake Password: ')
account = input('🏢 Enter your Snowflake Account: ')
warehouse = input('📦 Enter your Warehouse: ')
database = input('🗃️ Enter your Database Name: ')
schema = input('📂 Enter your Schema Name: ')
table = input('📋 Enter your Table Name: ')
print()

def load():
    conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )

    # Load cleaned input file
    input_file = input('📄 Enter your cleaned data input file path: \n').strip('"')
    df = pd.read_csv(input_file)

    # Upload to Snowflake
    print()
    print("📤 Uploading data to Snowflake...")
    success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name=table,
            schema=schema,
            database=database,
            auto_create_table=True
        )

    if success:
        print(f"🎉 Successfully loaded {nrows} rows into Snowflake! 🚀")
    else:
        print("❌ Upload failed. Please check your table or data format.")

    print("========================================================================")