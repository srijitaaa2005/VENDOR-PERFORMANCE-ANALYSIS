import os
import time
import logging
import pandas as pd
from sqlalchemy import create_engine

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

engine = create_engine("sqlite:///inventory.db")


def ingest_db(df, table_name, engine, if_exists="replace"):
    """Ingest dataframe into SQLite database"""
    df.to_sql(
        table_name,
        con=engine,
        if_exists=if_exists,
        index=False,
        method="multi",
        chunksize=1000
    )


def load_raw_data():
    start = time.time()
    data_path = "data"

    if not os.path.exists(data_path):
        logging.error(f"Data folder '{data_path}' not found.")
        print(f"ERROR: Data folder '{data_path}' not found.")
        return

    csv_files = sorted(f for f in os.listdir(data_path) if f.endswith(".csv"))

    if not csv_files:
        logging.warning(f"No CSV files found in '{data_path}'.")
        print(f"No CSV files found in '{data_path}'.")
        return

    for file in csv_files:
        file_path = os.path.join(data_path, file)
        file_size = os.path.getsize(file_path) / (1024 * 1024)   # MB
        table_name = file[:-4]

        print(f"\nProcessing: {file} ({file_size:.2f} MB)")
        logging.info(f"Processing {file} ({file_size:.2f} MB)")

        try:
            # Large files -> chunked ingestion
            if file_size > 100:
                first_chunk = True
                chunk_no = 1
                chunk_size = 200000 if file_size > 500 else 50000

                for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
                    ingest_db(
                        chunk,
                        table_name,
                        engine,
                        if_exists="replace" if first_chunk else "append"
                    )
                    print(f"   Chunk {chunk_no} inserted ({len(chunk)} rows)")
                    logging.info(f"{file} -> Chunk {chunk_no} inserted ({len(chunk)} rows)")
                    first_chunk = False
                    chunk_no += 1

            # Small files -> direct load
            else:
                df = pd.read_csv(file_path, low_memory=False)
                ingest_db(df, table_name, engine)
                print(f"   {file} inserted successfully ({len(df)} rows)")
                logging.info(f"{file} inserted successfully ({len(df)} rows)")

        except Exception as e:
            logging.error(f"Failed to process {file}: {e}")
            print(f"   ERROR processing {file}: {e}")
            continue

    end = time.time()
    print(f"\nCompleted in {(end-start)/60:.2f} minutes")
    logging.info("------------- Ingestion Complete -------------")
    logging.info(f"Total Time: {(end-start)/60:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()