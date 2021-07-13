import streamlit as st
import s3fs
import os
import pandas as pd
import boto3
AWS_S3_BUCKET = "polemics"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
fs = s3fs.S3FileSystem(anon=False)
# Retrieve file contents.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename, 'rb') as f:
         df = pd.read_csv(f)
    return df

df = read_file("s3://polemics/roles.csv")
df = df[(df['parliament'] == 43) & (df['status'] == 'active')] # lets just look at 43
df_cabinet = df[df['Role']== "Minister"] #excludes PM
st.write(df_cabinet)

save = st.button("save")
if save:
    s3_resource = boto3.resource('s3')
    s3_resource.Object('polemics', 'cabinet.csv').put(Body=df_cabinet.getvalue())
    #df.to_csv('s3://polemics/cabinet.csv', index=False)
    st.balloons()
