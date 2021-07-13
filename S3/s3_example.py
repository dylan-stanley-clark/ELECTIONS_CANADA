import streamlit as st
import s3fs
import os
import pandas as pd
import boto3
AWS_S3_BUCKET = "polemics"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return pd.read_csv(f)

df = read_file('s3://polemics/roles.csv')
df = df[(df['parliament'] == 43) & (df['status'] == 'active')] # lets just look at 43
df_cabinet = df[df['Role']== "Minister"] #excludes PM

save = st.button("save")
if save:
    df_cabinet.to_csv(
        f"s3://{AWS_S3_BUCKET}/cabinet.csv",
        index=False,
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY
            #"token": AWS_SESSION_TOKEN,
        },
    )
