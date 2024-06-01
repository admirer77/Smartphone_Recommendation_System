# Smartphone Recommendation System Project

## Overview
This project aimed to create a smartphone recommendation system by collecting data from various sources and building a machine learning model using Random Forest. The system utilizes data from 91mobiles website for mobile specifications and YouTube API for likes/views ratio to determine YouTube ratings.

## Project Steps

### 1. Data Collection
- **91mobiles Website:** Data was collected by web scraping the 91mobiles website to gather mobile specifications.
- **YouTube Data:** YouTube API was used with an API key to collect data on likes/views ratio for YouTube ratings.

### 2. Data Preprocessing
Before feeding the data into the machine learning model, several preprocessing steps were carried out:
- Handling missing values
- Data cleaning (removing duplicates, irrelevant data)
- Feature engineering (creating new features, encoding categorical variables)

### 3. Machine Learning Model
A Random Forest machine learning model was chosen for its ability to handle large datasets and provide accurate predictions. The model was trained on the preprocessed data to predict smartphone ratings based on specifications and YouTube ratings.

### 4. Web Application
The recommendation system was deployed using Flask to create a web interface where users can input their preferences and receive personalized smartphone recommendations.

## Repository Structure
- **data/**: Contains the collected and preprocessed data files.
- **models/**: Includes the trained machine learning model.
- **app.py**: Flask application for the web interface.
- **requirements.txt**: Lists the required libraries and dependencies.
- **README.md**: Instructions and overview of the project.

## Usage
1. Clone the repository:
