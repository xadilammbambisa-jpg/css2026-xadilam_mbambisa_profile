import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Xadilam's Research Profile",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------
# BASIC INFO
# -------------------------------
NAME = "Xadilam Mbambisa"
FIELD = "Physics & Computer Science"
INSTITUTION = "Walter Sisulu University"

INTERESTS = [
    "Astrophysics",
    "Space Physics",
    "Quantum Mechanics",
    "AI in Science",
    "Data Analysis",
    "Scientific Computing"
]

EMAIL = "xadilammbambisa@gmail.com"   # Change later
Github = "https://github.com/xadilammbambisa-jpg"
# -------------------------------
# TITLE
# -------------------------------
st.title("🚀 Research & Portfolio Dashboard")
st.subheader("Personal STEM Profile")

# -------------------------------
# PROFILE SECTION
# -------------------------------
st.header("👨🏽‍🔬 Profile Overview")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Name:** {NAME}")
    st.write(f"**Field:** {FIELD}")
    st.write(f"**Institution:** {INSTITUTION}")

with col2:
    st.write("### Research Interests")
    for interest in INTERESTS:
        st.write(f"- {interest}")

st.image(
    "https://cdn.pixabay.com/photo/2016/11/29/09/32/space-1867616_1280.jpg",
    caption="Exploring the Universe"
)

# -------------------------------
# PROJECTS / PUBLICATIONS
# -------------------------------
st.header("📚 Projects & Publications")

uploaded_file = st.file_uploader(
    "Upload your projects/publications CSV",
    type="csv"
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")
    st.dataframe(df)

    # Search
    keyword = st.text_input("🔍 Search by keyword")

    if keyword:
        filtered = df[
            df.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]

        st.write(f"Results for: **{keyword}**")
        st.dataframe(filtered)

# -------------------------------
# RESEARCH TRENDS
# -------------------------------
st.header("📈 Research Activity")

if uploaded_file and "Year" in df.columns:
    year_counts = df["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)
else:
    st.info("Upload a CSV with a 'Year' column to see trends.")

# -------------------------------
# SAMPLE SCIENCE DATA
# -------------------------------
st.header("🔬 STEM Data Explorer")

# Sample datasets
space_data = pd.DataFrame({
    "Satellite": ["ISS", "Hubble", "JWST", "Starlink", "NOAA-19"],
    "Altitude (km)": [408, 547, 1500000, 550, 870],
    "Launch Year": [1998, 1990, 2021, 2019, 2009]
})

quantum_data = pd.DataFrame({
    "Experiment": ["Qubit Test", "Spin Analysis", "Wavefunction Sim", "Noise Study"],
    "Accuracy (%)": [91, 87, 94, 82],
    "Date": pd.date_range("2024-01-01", periods=4)
})

weather_sa = pd.DataFrame({
    "City": ["Cape Town", "Johannesburg", "Durban", "Pretoria", "Bloemfontein"],
    "Temp (°C)": [24, 28, 26, 30, 22],
    "Humidity (%)": [65, 45, 70, 40, 50]
})

# Dataset selector
option = st.selectbox(
    "Choose dataset",
    ["Space Missions", "Quantum Experiments", "South Africa Weather"]
)

# -------------------------------
# DATA VIEWS
# -------------------------------
if option == "Space Missions":

    st.subheader("🛰 Space Missions")
    st.dataframe(space_data)

    alt_range = st.slider(
        "Filter by Altitude (km)",
        0,
        2000000,
        (0, 2000000)
    )

    filtered = space_data[
        space_data["Altitude (km)"].between(*alt_range)
    ]

    st.dataframe(filtered)


elif option == "Quantum Experiments":

    st.subheader("⚛ Quantum Research")
    st.dataframe(quantum_data)

    acc = st.slider(
        "Minimum Accuracy (%)",
        0,
        100,
        80
    )

    filtered = quantum_data[
        quantum_data["Accuracy (%)"] >= acc
    ]

    st.dataframe(filtered)


elif option == "South Africa Weather":

    st.subheader("🌦 SA Weather Data")
    st.dataframe(weather_sa)

    temp = st.slider(
        "Temperature Range",
        0,
        40,
        (15, 35)
    )

    filtered = weather_sa[
        weather_sa["Temp (°C)"].between(*temp)
    ]

    st.dataframe(filtered)

# -------------------------------
# CONTACT
# -------------------------------
st.header("📬 Contact")

st.write(f"📧 Email: {EMAIL}")
st.write(f"🌍 GitHub: {Github}")


