import os
import asyncio
import datetime
import aiohttp
import aiofiles
import pandas as pd
from pathlib import Path
from tqdm.asyncio import tqdm
from google.cloud import storage

BUCKET_NAME = 'chum_bucket_stuff'
TARGET_DIR = Path('./images')

_client = storage.Client()
_bucket = _client.bucket(BUCKET_NAME)

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)


async def download_sample_df():
    async with aiohttp.ClientSession() as session:
        signed_url = generate_signed_url(BUCKET_NAME, "pics/sample_df.csv")
        await download_file(session, signed_url, TARGET_DIR / 'sample_df.csv')


async def main():
    await download_sample_df()
    df = pd.read_csv(TARGET_DIR / 'sample_df.csv')
    await download_files_from_dataframe(df)


if __name__ == "__main__":
    asyncio.run(main())
