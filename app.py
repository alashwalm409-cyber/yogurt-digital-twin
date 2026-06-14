import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# =========================
# PAGE CONFIG (Startup Style)
# =========================
st.set_page_config(
    page_title="FoodAI Startup",
    layout="wide",
    page_icon="🚀"
)

# =========================
# LANDING (Investor View)
# =========================
st.title("🚀 FoodAI – Smart Food Intelligence Platform")

st.markdown("""
### 💡 Investment-Ready AI Startup
FoodAI is a Digital Twin + AI platform that predicts food spoilage 
and optimizes cold chain logistics in real time.

---

#### 🔴 Problem
- Food waste exceeds billions annually
- No predictive system for freshness

#### 🟢 Solution
- AI-based shelf-life prediction
- IoT sensor integration
- Real-time monitoring dashboard

---
""")

st.divider()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙ System Control")

product = st.sidebar.selectbox("Product Type", ["Yogurt", "Milk", "Juice"])
temp = st.sidebar.slider("Temperature (°C)", 2, 15, 4)
humidity = st.sidebar.slider("Humidity (%)", 50, 90, 70)

# =========================
# DATA + AI MODEL
# =========================
np.random.seed(42)

data = []
for t in range(4, 13):
    for d in range(1, 22):
        q = 100 - (d * 2.3) - (t - 4) * 3 + np.random.normal(0, 1)
        q = max(0, q)
        data.append([d, t, q])

df = pd.DataFrame(data, columns=["Day", "Temp", "Quality"])

X = df[["Day", "Temp"]]
y = df["Quality"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestRegressor(n_estimators=500, random_state=42)
model.fit(X_scaled, y)

# =========================
# PREDICTION ENGINE
# =========================
days = np.arange(1, 22)

input_scaled = scaler.transform(pd.DataFrame({
    "Day": days,
    "Temp": [temp] * len(days)
}))

pred = model.predict(input_scaled)

final_quality = pred[-1]
shelf_life = len([x for x in pred if x > 60])
risk = 100 - final_quality

# =========================
# INVESTOR KPIs
# =========================
st.markdown("## 📊 Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Expected Shelf Life", f"{shelf_life} days")
c2.metric("Quality Score", f"{final_quality:.2f}%")
c3.metric("Risk Level", f"{risk:.2f}%")
c4.metric("Product", product)

st.divider()

# =========================
# INSIGHTS (INVESTOR VALUE)
# =========================
st.subheader("📈 Business Insight")

if final_quality > 70:
    st.success("High commercial viability – suitable for cold chain optimization markets")
elif final_quality > 50:
    st.warning("Moderate risk – requires monitoring optimization")
else:
    st.error("High spoilage risk – critical market opportunity")

# =========================
# DASHBOARD
# =========================
tab1, tab2, tab3 = st.tabs(["📊 AI Forecast", "⚠ Risk Analysis", "📁 Data Model"])

with tab1:
    st.line_chart(pred)

with tab2:
    st.line_chart(100 - pred)

with tab3:
    st.dataframe(df)

# =========================
# FOOTER (INVESTOR BRANDING)
# =========================
st.markdown("---")
st.caption("FoodAI Startup © 2026 | Investment Prototype | AI + Digital Twin for Food Industry")
