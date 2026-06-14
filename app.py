import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI Yogurt Digital Twin", layout="centered")

st.title("🥛 AI + IoT Yogurt Digital Twin System")

st.markdown("نظام ذكي لمحاكاة جودة الزبادي أثناء التخزين باستخدام الذكاء الاصطناعي والتوأم الرقمي")

# =========================
# Sensors (Simulation)
# =========================
temp = st.slider("🌡 Temperature (°C)", 2, 15, 4)
humidity = st.slider("💧 Humidity (%)", 50, 90, 70)

# =========================
# AI MODEL
# =========================
def model(day, temp, humidity):
    quality = 100 - (day * 2.3) - (temp - 4) * 3 - (humidity - 70) * 0.2
    quality = max(0, quality)

    ph = 4.6 - (day * 0.03) - (temp - 4) * 0.02
    ph = max(3.3, ph)

    risk = 100 - quality

    return quality, ph, risk


# =========================
# SIMULATION
# =========================
days = np.arange(1, 22)

q_list = []
ph_list = []
risk_list = []

for d in days:
    q, p, r = model(d, temp, humidity)
    q_list.append(q)
    ph_list.append(p)
    risk_list.append(r)

df = pd.DataFrame({
    "Day": days,
    "Quality": q_list,
    "pH": ph_list,
    "Risk": risk_list
})

# =========================
# RESULTS
# =========================
final_quality = df["Quality"].iloc[-1]
shelf_life = len(df[df["Quality"] > 60])

if final_quality > 80:
    status = "Excellent 🟢"
elif final_quality > 60:
    status = "Good 🟡"
elif final_quality > 40:
    status = "Risky 🟠"
else:
    status = "Spoiled 🔴"

# =========================
# DASHBOARD
# =========================
st.subheader("📊 Results Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Quality %", round(final_quality, 2))
col2.metric("Shelf Life (Days)", shelf_life)
col3.metric("Risk Level", status)

st.divider()

# =========================
# CHARTS
# =========================
st.subheader("📉 Quality Over Time")
st.line_chart(df["Quality"])

st.subheader("🦠 Spoilage Risk")
st.line_chart(df["Risk"])

st.subheader("⚗️ pH Change Over Time")
st.line_chart(df["pH"])

st.divider()

st.subheader("📄 Data Table")
st.dataframe(df)
