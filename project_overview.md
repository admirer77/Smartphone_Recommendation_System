# Mobile Specs Analysis and YouTube Rating Prediction

## Project Overview

This project aims to analyze mobile specifications and predict YouTube ratings based on likes and views using machine learning. The project involves web scraping, data collection, model training, and deployment via a Flask web application.

## Table of Contents

- [Mobile Specs Analysis and YouTube Rating Prediction](#mobile-specs-analysis-and-youtube-rating-prediction)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Data Collection](#data-collection)
    - [Mobile Specifications](#mobile-specifications)
    - [YouTube Data](#youtube-data)
  - [Machine Learning Model](#machine-learning-model)
  - [Web Application](#web-application)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Data Collection

### Mobile Specifications

I collected data on mobile specifications by web scraping the 91mobiles website. This involved extracting various features such as model name, brand, specifications, price, etc.

### YouTube Data

Using the YouTube Data API, I collected data on video likes and views. This data was used to calculate the likes/views ratio to serve as a YouTube rating metric.

## Machine Learning Model

A Random Forest model was created to predict the YouTube rating based on the collected mobile specifications and YouTube data. The model was trained and evaluated to ensure its accuracy and reliability.

## Web Application

The project includes a web application built with Flask. The web app provides an interface for users to input mobile specifications and view predicted YouTube ratings.

## Installation

To get a local copy up and running, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/admirer77/Smartphone_Recommendation_System.git
