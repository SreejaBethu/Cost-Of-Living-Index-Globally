import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r'C:\Users\Sreeja\Downloads\Cost_of_Living_Index_by_Country_2024.csv')

# Create a Streamlit app
st.title("Cost of Living Index by Country")

# Print the columns names
st.write(df.columns)

# Select a country
country_select = st.selectbox("Select a country", df['Country'].unique())

# Filter the data for the selected country
country_df = df[df['Country'] == country_select]

# Get the column names
columns = ['Rent Index', 'Cost of Living Index', 'Groceries Index', 'Restaurant Price Index', 'Local Purchasing Power Index']

# Create a chart for each index

for column in columns:

    if column in df.columns:

        st.header(column)
        fig, ax = plt.subplots(figsize=(15, 8))  # Adjust the figure size
        ax.bar(country_df['Country'], country_df[column], color=['blue' if column == 'Rent Index' else 'green' if column == 'Cost of Living Index' else 'red' if column == 'Groceries Index' else 'yellow'])  # Change the bar color for each column
        ax.set_xlabel('Country')  # Add x-axis label
        ax.set_ylabel(column)  # Add y-axis label
        ax.set_title(f"{column} by Country")  # Add title
        plt.xticks(rotation=45, ha='right', fontsize=8)  # Rotate the x-axis labels
        st.pyplot(fig)

    else:

        st.write(f"Column '{column}' does not exist in the DataFrame.")


# Group the data by country and calculate the mean of each index
grouped_df = df.groupby('Country').mean()


# Create a chart for each index, grouped by country

for column in columns:
    if column in df.columns:
        st.header(f"{column} by Country")
        fig, ax = plt.subplots(figsize=(15, 8))  # Adjust the figure size
        ax.bar(grouped_df.index, grouped_df[column], color=['blue' if column == 'Rent Index' else 'green' if column == 'Cost of Living Index' else 'red' if column == 'Groceries Index' else 'Orange'])  # Change the bar color for each column
        ax.set_xlabel('Country')  # Add x-axis label
        ax.set_ylabel(column)  # Add y-axis label
        ax.set_title(f"{column} by Country")  # Add title
        plt.xticks(rotation=90, ha='right', fontsize=8)  # Rotate the x-axis labels
        st.pyplot(fig)

    else:

        st.write(f"Column '{column}' does not exist in the DataFrame.")