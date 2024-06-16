# Smartphone Recommendation System

This project implements a smartphone recommendation system that utilizes data from various sources to suggest the best phone based on user preferences.

https://nehanthadmirer.medium.com/building-a-smartphone-recommendation-system-harnessing-web-scraping-and-youtube-data-555c515c2b08

## Project Description

This system combines ratings from two sources:

* **91mobiles:** Smartphone specifications and user ratings are collected through web scraping techniques from the 91mobiles website.
* **YouTube:**  Views and likes for smartphone review videos are retrieved using the YouTube Data API. And used it to display the youtube vedios in the webpage.

The YouTube rating is calculated as `likes / views * 10`. To compensate for potential outliers, the difference between the highest YouTube rating and 10 is added to each YouTube rating.

The final rating for each phone is determined by a weighted sum:

* **70%:** Weight given to the 91mobiles rating
* **30%:** Weight given to the adjusted YouTube rating

The data is preprocessed and used to train a Random Forest classification model using Python libraries. The front-end is built with Flask, HTML, and CSS to provide a user interface for inputting desired phone specifications and receiving the recommended phone with the highest final rating.

## Technologies Used

* Programming Language: Python
* Web Scraping: (Library: selenium)
* YouTube Data API
* Machine Learning Library: scikit-learn (Random Forest)
* Web Framework: Flask
* Front-end Development: HTML, CSS

## References

* 91mobiles website
* YouTube Data API Documentation
* OpenAI

## How to Run the Project

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`. 
3. Set up the YouTube Data API by following the instructions in the documentation and obtain your API key. 
4. Run the Flask application using `cd Web App` and `python app.py`.
5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Contributing

Feel free to contribute to this project by creating pull requests. Make sure to follow the coding style and document any changes made.

## License

This project is licensed under the MIT.
