import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import json
import pandas as pd

@st.cache_data
def load_json_data(selected_indicator):
    with open("./breadth_data.json", "r") as f:
        data = json.load(f)

    return data[selected_indicator]["line"]

@st.cache_data
def generate_names_list():
    with open("./breadth_data.json", "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df.columns.to_list()

indicators = generate_names_list()
selected_indicator = st.selectbox("Select a indicator", indicators)

data = load_json_data(selected_indicator)

print(data[0:2])

chartOptions = {
    "height": 400,
    "layout": {
        "textColor": "#333",
        "background": {"type": "solid", "color": "white"},
    },
    "grid": {
        "vertLines": {"color": "#e1ecf2"},
        "horzLines": {"color": "#e1ecf2"},
    },
    "timeScale": {
        "borderColor": "rgba(197, 203, 206, 0.6)",
        "minBarSpacing": 1.5,
        "rightOffset": 10,
    },
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.1,
            "bottom": 0.1,
        },
        "mode": 0,
        "borderColor": "rgba(197, 203, 206, 0.6)",
    },
}

seriesLineChart = [
    {
        "type": "Line",
        "data": data,
        "options": {
            "lineWidth": 2,
        },
    }
]

st.subheader("Testing Lightweight Charts")

renderLightweightCharts([{"chart": chartOptions, "series": seriesLineChart}], "line")
