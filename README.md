# Cost-Of-Living-Index-Globally

## Overview

This Streamlit app is a data visualization tool that allows users to explore and compare the cost of living indices across different countries. The app takes in a dataset of cost of living indices for various countries and provides an interactive interface for users to select specific indices and countries to visualize.

## Table of Contents

[Features](features)

[Installation](installation)

[Running the App](runningtheapp)

[Configuration](configuration)

[Usage](usage)

[Power Bi](power-bi)

[Visualization](visualization)

## Features

    1) Interactive dropdown menus to select cost of living indices (e.g. Rent Index, Cost of Living Index, Groceries Index) and countries.
    
    2) Bar charts to visualize the selected indices for each country
    
    3) Ability to compare multiple countries and indices in a single chart
    
    4) Customizable title and color scheme for the charts

## Getting Started

### Installation

To run this app, you'll need to have Streamlit installed. You can install Streamlit using pip:
  
  pip install streamlit

### Running the App

To run the app, simply execute the following command in your terminal: 

   streamlit run app.py

Replace app.py with the name of your Python script.

## Configuration

The app uses a CSV file as input data. You can configure the app by modifying the following variables:

  **data_file:** The path to the CSV file containing the cost of living indices data.
   **columns:**  A list of column names in the CSV file that correspond to the different cost of living indices.

## Usage

    Select a cost of living index from the dropdown menu.
    Select one or more countries from the dropdown menu.
    The app will generate a bar chart showing the selected index for each country.
    You can customize the title and color scheme of the chart by modifying the code.

## Power Bi

![power bi](https://github.com/user-attachments/assets/569d1a90-0b98-4097-a81a-ee62441f3c44)

## Visualization

![Bar graph](https://github.com/user-attachments/assets/89514d16-ccd4-416c-a164-34757f5e01d5)

![groceries by country](https://github.com/user-attachments/assets/55721f7e-d698-467b-a8f9-befac21bece0)

![index](https://github.com/user-attachments/assets/285e279c-6897-4ff6-bc72-d8b15e666492)


## Contributing

Contributions are welcome! If you'd like to add new features or improve the app, please fork this repository and submit a pull request.

## Acknowledgments

  **Streamlit** for providing an amazing framework for building data science apps.
    **Matplotlib** for providing a powerful plotting library.
