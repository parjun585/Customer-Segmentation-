# Market Segmentation of Customer Data

## Overview
This project analyzes customer segmentation using machine learning to understand and group customer behavior based on their credit card usage. The primary goal is to enable targeted marketing by identifying customer groups with similar characteristics.

## Table of Contents
- [Overview](#overview)
- [Project Motivation](#project-motivation)
- [Project Files](#project-files)
- [Installation](#installation)
- [Data Description](#data-description)
- [Methods and Models Used](#methods-and-models-used)
- [Results](#results)
- [How to Use](#how-to-use)
- [Future Work](#future-work)


## Project Motivation
The project aims to assist in understanding customer behavior by segmenting them into clusters. Market segmentation helps businesses target specific customer groups and tailor their marketing strategies. This can lead to improved customer satisfaction and increased sales.

## Project Files
- \`Market_Segmentation_Customer_Data.ipynb\`: The main Jupyter notebook file containing all analysis steps, model training, and evaluation.

## Installation
1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/parjun585/Customer-Segmentation-/tree/main/Credit%20Card%20User%20Segmentation
   cd Customer-Segmentation-/Credit\ Card\ User\ Segmentation
   \`\`\`

2. **Set up a virtual environment**:
   \`\`\`bash
   python3 -m venv env
   source env/bin/activate
   \`\`\`

3. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Data Description
The dataset includes information on the usage patterns of approximately 9000 active credit card holders, such as:
- **Balance**: Average balance amount
- **Purchases**: Total amount of purchases
- **Cash Advance**: Amount of cash advance taken
- **Transactions**: Number and frequency of transactions
- **Payments**: Payments made towards the balance

## Methods and Models Used
1. **Exploratory Data Analysis (EDA)**: Initial data analysis to understand distributions, trends, and relationships.
2. **Clustering using K-Means**: Clustered customers into groups based on their usage patterns.
3. **Decision Tree Classifier**: Further classified customers based on specific features for enhanced targeting and insights.
4. **Deployment with Streamlit**: Deployed a Streamlit app allowing users to predict the cluster of a new customer based on input features.

## Results
The K-Means clustering algorithm successfully grouped customers into four distinct clusters:
- **Cluster 0**: Low engagement users with minimal purchases.
- **Cluster 1**: High-spending users with a high number of purchases.
- **Cluster 2**: Frequent users with moderate purchases and consistent payments.
- **Cluster 3**: Occasional users primarily relying on cash advances.

The model aids in segmenting customers into actionable categories, which businesses can use for marketing and customer relationship strategies.

## How to Use
To use the Streamlit app for this project:
1. Run the app locally:
   \`\`\`
   streamlit run app.py
   \`\`\`
2. Input new customer data and get a prediction of the cluster.

## Future Work
- Expand the model to include additional classification algorithms for comparison.
- Explore deeper feature engineering to identify new customer behaviors.
- Integrate customer segmentation with real-time business data for live predictions.



