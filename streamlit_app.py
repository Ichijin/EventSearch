import streamlit as st

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")
my_bar = st.progress(0)

import pandas as pd
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine='python',
        na_values='-',
        header=None)
    
    st.markdown('### アクセスログ（先頭5件）')
    st.write(df.head(5))

    st.map(df)
