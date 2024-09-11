import streamlit as st
import pandas as pd
import json
from datetime import timedelta, datetime

st.set_page_config(
    page_title="Screener"
)


def load_json_data(selected_indicator):
    with open("./breadth_data.json", "r") as f:
        data = json.load(f)

    line_data = data[selected_indicator]["line"]
    df = pd.DataFrame(line_data)
    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)

    return df


def generate_names_list():
    with open("./breadth_data.json", "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df.columns.to_list()



indicators = generate_names_list()
selected_indicator = st.selectbox("Select a indicator", indicators)

data = load_json_data(selected_indicator)

data["MA(20)"] = data["value"].rolling(window=20).mean()

min_date = data.index.min().to_pydatetime()
max_date = data.index.max().to_pydatetime()

start_date = max_date - timedelta(days=665)

interval = st.slider(
    "Período",
    min_value=min_date,
    max_value=max_date,
    value=(start_date, max_date),
    step=timedelta(days=30),
)

print(generate_names_list())

data = data.loc[interval[0] : interval[1]]

st.line_chart(data[["value", "MA(20)"]])
