import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("india_flood_curated_2000_2026.csv")

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

df["Month"]=df["Month"].map(month_names)

st.title("🌊 India Flood Analytics Dashboard")

st.write(
    "Explore historical flood events, affected population, damage and major flood causes across India."
)

with st.sidebar:

    st.header("🎛️ Dashboard Filters")

    st.caption("Use the below filters to explore flood events.")

    st.divider()

    #YEAR
    st.subheader("📅 Time")

    min_year = int(df["Year"].min())
    max_year = int(df["Year"].max())

    selected_year_range=st.slider(
        "Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )

    #STATE
    st.subheader("📍 Location")

    state_options=sorted(df["State"].unique())

    selected_state=st.multiselect(
        "State",
        options=state_options,
        default=state_options,
        placeholder="Select states"
    )

    #FLOOD TYPE
    st.subheader("🌊 Flood Type")

    flood_options=sorted(
        df["Flood_Type"].unique()
    )

    selected_flood_type=st.multiselect(
        "Flood Type",
        options=flood_options,
        default=flood_options,
        placeholder="Select flood types"
    )

    # ---------------- SEVERITY ----------------
    st.subheader("⚠️ Severity")

    severity_options = sorted(
        df["Severity"].dropna().unique()
    )

    selected_severity = st.multiselect(
        "Severity",
        options=severity_options,
        default=severity_options,
        placeholder="Select severity"
    )


filtered_df=df[
    (df["Year"] >= selected_year_range[0]) &
    (df["Year"] <= selected_year_range[1]) &
    (df["State"].isin(selected_state)) &
    (df["Flood_Type"].isin(selected_flood_type)) &
    (df["Severity"].isin(selected_severity))
]

total_events=len(filtered_df)

total_people=filtered_df["People_Affected"].sum()

total_deaths=filtered_df["Deaths"].sum()

total_houses=filtered_df["Houses_Damaged"].sum()


col1, col2, col3, col4=st.columns(4)

col1.metric(
    "🌊 Flood Events",
    f"{total_events}"
)

col2.metric(
    "👥 People Affected",
    f"{total_people:,}"
)

col3.metric(
    "⚠️ Deaths",
    f"{total_deaths:,}"
)

col4.metric(
    "🏠 Houses Damaged",
    f"{total_houses:,}"
)

#Number of event per year
yearly_events = filtered_df["Year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=yearly_events.index,y=yearly_events.values)
ax.set_ylabel("Number of Events")
ax.set_title("Events per Year")
plt.show()


#Flood event by state
state_counts = (filtered_df["State"].value_counts().head(10))
fig,ax=plt.subplots(figsize=(10, 6))
sns.barplot(x=state_counts.values,y=state_counts.index,ax=ax)
ax.set_title("Top 10 States by Flood Events")
ax.set_xlabel("Number of Flood Events")
ax.set_ylabel("State")
st.pyplot(fig)



#People affected by flood
affected = (filtered_df.groupby("Year")["People_Affected"].sum().sort_index())
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=affected.index,y=affected.values,marker="o",ax=ax)
ax.set_title("People Affected by Floods Over the Years")
ax.set_xlabel("Year")
ax.set_ylabel("People Affected")
st.pyplot(fig)



#House damage cause by flood
damage = (filtered_df.groupby("Year")["Houses_Damaged"].sum().sort_values(ascending=False).head(5))

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=damage.index.astype(str),y=damage.values,ax=ax)
ax.set_title("Top 5 Years by Houses Damaged")
ax.set_xlabel("Year")
ax.set_ylabel("Total Houses Damaged")
st.pyplot(fig)


#Cause of flood
causes = (filtered_df["Main_Cause"].value_counts().head(5))
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(causes.values,labels=causes.index,autopct="%1.1f%%")
ax.set_title("Top 5 Main Causes of Floods")
st.pyplot(fig)



#Total Death over a year
year_deaths = (filtered_df.groupby("Year")["Deaths"].sum().sort_values(ascending=False).head(10))

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=year_deaths.index.astype(str),y=year_deaths.values,ax=ax)
ax.set_title("Top 10 Years by Flood-Related Deaths")
ax.set_xlabel("Year")
ax.set_ylabel("Total Deaths")
st.pyplot(fig)

