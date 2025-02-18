import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

data_day = pd.read_csv("../Dataset/day.csv")
data_hour = pd.read_csv("../Dataset/hour.csv")

data_day['dteday'] = pd.to_datetime(data_day['dteday'])

min_date = data_day['dteday'].min()
max_date = data_day['dteday'].max()

data_hour['dteday'] = pd.to_datetime(data_hour['dteday'])
data_hour['weekday_label'] = data_hour['weekday'].map({
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 
    4: 'Friday', 5: 'Saturday', 6: 'Sunday'
})
data_hour['month_label'] = data_hour['mnth'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
})

with st.sidebar:
    st.image('data:image/jpeg;base64,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')
    st.title("Bike Rent Dashboard")
    start_date, end_date = st.date_input(
        label = "Rentang waktu",
        min_value = min_date,
        max_value = max_date,
        value = [min_date, max_date]
    )

    # Season filter
    season_filter = st.multiselect(
        "Pilih Musim",
        options=[1, 2, 3, 4],
        format_func=lambda x: {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}[x],
        default=[1, 2, 3, 4]
    )

# Filter data based on user input
df = data_day[(data_day['dteday'] >= pd.to_datetime(start_date)) & (data_day['dteday'] <= pd.to_datetime(end_date))]

if season_filter:
    df = df[df['season'].isin(season_filter)]


# Main dashboard
st.title("Bike Rent Analysis")

# Tabs
tab1, tab2, tab3= st.tabs(["Data Day", "Data Hour", "RFM Analysis"])

with tab1:
    st.title("Visualisasi Data Day")

    # Total Rentals by Season
    st.subheader("Total Penyewaan Berdasarkan Musim")
    season_data = (
        df.groupby('season')['cnt']
        .sum()
        .rename(index={1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
        .sort_values()
    )
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x=season_data.index,
        y=season_data.values,
        palette=sns.color_palette("pastel"),
        ax=ax
    )
    ax.set_title("Total Rentals by Season")
    ax.set_ylabel("Total Rentals")
    ax.set_xlabel("Season")
    ax.tick_params(axis='x', rotation=0)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}')) 
    st.pyplot(fig)

    # AVG Rentals by Working Day
    st.subheader("Rata-Rata Penyewaan: Hari Kerja vs Hari Libur")
    workingday_avg = df.groupby('workingday')['cnt'].mean()
    workingday_avg.index = ['Non-Working Day', 'Working Day']

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x=workingday_avg.index,
        y=workingday_avg.values,
        palette=sns.color_palette("muted"),
        ax=ax1
    )
    ax1.set_title("Average Rentals: Working Day vs Non-Working Day")
    ax1.set_ylabel("Average Rentals")
    ax1.set_xlabel("Day Type")
    ax1.tick_params(axis='x', rotation=0)
    st.pyplot(fig1)

    # Total Rentals by Working Day
    st.subheader("Total Penyewaan: Hari Kerja vs Hari Libur")
    workingday_total = df.groupby('workingday')['cnt'].sum()
    workingday_total.index = ['Non-Working Day', 'Working Day']

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x=workingday_total.index,
        y=workingday_total.values,
        palette=sns.color_palette("bright"),
        ax=ax2
    )
    ax2.set_title("Total Rentals: Working Day vs Non-Working Day")
    ax2.set_ylabel("Total Rentals")
    ax2.set_xlabel("Day Type")
    ax2.tick_params(axis='x', rotation=0)
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))  
    st.pyplot(fig2)

    # Casual Vs Registered User
    st.subheader("Proporsi Pengguna Kasual vs Terdaftar")
    user_type_data = df[['casual', 'registered']].sum()
    fig, ax = plt.subplots(figsize=(6, 6))
    user_type_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightskyblue'], ax=ax)
    ax.set_title("Proportion of Casual vs Registered Users")
    ax.set_ylabel("")
    st.pyplot(fig)

    # rental berdasarkan cuaca
    st.subheader("Jumlah Penyewaan Berdasarkan Kondisi Cuaca")
    weather_labels = {
        1: 'Clear/Few Clouds',
        2: 'Mist/Cloudy',
        3: 'Light Snow/Rain',
        4: 'Heavy Rain/Snow'
    }
    df['weathersit_label'] = df['weathersit'].map(weather_labels)
    weather_data = (
        df.groupby('weathersit_label')['cnt']
        .sum()
        .sort_values(ascending = False)
    )

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x=weather_data.values,
        y=weather_data.index,
        palette=sns.color_palette("deep"),
        ax=ax,
        orient="h"
    )
    ax.set_title("Total Rentals by Weather Condition")
    ax.set_xlabel("Total Rentals")
    ax.set_ylabel("Weather Condition")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)

with tab2:
    st.title("Visualisasi Data Hour")
    

    #Rata-rata Penyewaan per Hari dalam Seminggu
    st.subheader("Rata-rata Penyewaan per Hari dalam Seminggu")
    weekday_avg = data_hour.groupby('weekday_label')['cnt'].mean().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=weekday_avg.index, y=weekday_avg.values, marker='o', ax=ax)
    ax.set_title("Average Rentals per Day of the Week", fontsize=14)
    ax.set_xlabel("Day of the Week", fontsize=12)
    ax.set_ylabel("Average Rentals", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Rata-rata Penyewaan per Bulan
    st.subheader("Rata-rata Penyewaan per Bulan")
    month_avg = data_hour.groupby('month_label')['cnt'].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=month_avg.index, y=month_avg.values, marker='o', ax=ax)
    ax.set_title("Average Rentals per Month", fontsize=14)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Average Rentals", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Rata-rata Penyewaan per Jam Berdasarkan Working days dan Non-Working days
    st.subheader("Rata-rata Penyewaan per Jam Berdasarkan Hari Kerja dan Non-Hari Kerja")
    hour_workingday_avg = data_hour.groupby(['hr', 'workingday'])['cnt'].mean().unstack()
    hour_workingday_avg.index += 1
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=hour_workingday_avg.index, y=hour_workingday_avg[0], label='Non-Working Day', marker='o', ax=ax)
    sns.lineplot(x=hour_workingday_avg.index, y=hour_workingday_avg[1], label='Working Day', marker='o', ax=ax)
    ax.set_title("Average Rentals per Hour by Working and Non-Working Day", fontsize=14)
    ax.set_xlabel("Hour", fontsize=12)
    ax.set_ylabel("Average Rentals", fontsize=12)
    ax.legend(title="Day Type")
    st.pyplot(fig)
    
with tab3:
    st.title("RFM Analysis")

    rfm_data = data_day[['dteday', 'casual', 'registered', 'cnt']].copy()

    snapshot_date = rfm_data['dteday'].max() + pd.Timedelta(days=1)

    rfm_table = rfm_data.groupby('dteday').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()

    rfm_table['Recency'] = (snapshot_date - rfm_table['dteday']).dt.days
    rfm_table['Frequency'] = rfm_table['casual'] + rfm_table['registered']
    rfm_table['Monetary'] = rfm_table['cnt']

    # sample tabel RFM
    st.write("### RFM Table Sample")
    st.dataframe(rfm_table[['dteday', 'Recency', 'Frequency', 'Monetary']].head())

    # Distribusi Recency
    st.subheader("Distribusi Recency")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.histplot(rfm_table['Recency'], bins=20, color='blue', ax=ax1)
    ax1.set_title("Distribution of Recency", fontsize=14)
    ax1.set_xlabel("Days Since Last Transaction", fontsize=12)
    ax1.set_ylabel("Count", fontsize=12)
    st.pyplot(fig1)

    # Frequency
    st.subheader("Distribusi Frequency")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.histplot(rfm_table['Frequency'], bins=20,  color='green', ax=ax2)
    ax2.set_title("Distribution of Frequency", fontsize=14)
    ax2.set_xlabel("Number of Transactions", fontsize=12)
    ax2.set_ylabel("Count", fontsize=12)
    st.pyplot(fig2)

    # Monetary
    st.subheader("Distribusi Monetary")
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.histplot(rfm_table['Monetary'], bins=20, color='orange', ax=ax3)
    ax3.set_title("Distribution of Monetary", fontsize=14)
    ax3.set_xlabel("Total Rentals (Monetary Proxy)", fontsize=12)
    ax3.set_ylabel("Count", fontsize=12)
    st.pyplot(fig3)

st.caption('Copyright © Azhar 2024')