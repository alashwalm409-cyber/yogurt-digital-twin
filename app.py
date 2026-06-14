import streamlit as st
import numpy as np
import pandas as pd

st.title("🥛 Yogurt Digital Twin")

temp = st.slider("Temperature (°C)", 2, 15, 4)
humidity = st.slider("Humidity (%)", 50, 90, 70)

def model(day, temp, humidity):
    quality = 100 - (day * 2.2) - (temp - 4) * 3 - (humidity - 70) * 0.2
    return max(0, quality)

days = np.arange(1, 22)
quality = [model(d, temp, humidity) for d in days]

st.line_chart(quality)
