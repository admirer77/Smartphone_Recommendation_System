from flask import Flask, request, render_template, url_for
import pandas as pd
import joblib
from googleapiclient.discovery import build

# Load the dataset and the trained model
data = pd.read_csv('Preprocessed_Final_Data.csv')
model = joblib.load('random_forest_model.pkl')
ratings = joblib.load('ratings.pkl')

# Replace 'YOUR_API_KEY' with your actual YouTube API key
API_KEY = 'xxx'
youtube = build('youtube', 'v3', developerKey=API_KEY)

app = Flask(__name__)

def search_videos(query, max_results=5):
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response['items']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.to_dict()

    # Debugging: Print the received form data
    print("Received user input:", user_input)

    # Remove default values for missing numerical inputs and ensure inputs are treated as floats if provided
    for key in ['Price', 'Battery', 'Refresh Rate', 'RAM']:
        if user_input.get(key) == '' or user_input.get(key) is None:
            user_input[key] = None
        else:
            user_input[key] = float(user_input[key])

    # Filter the dataset based on the provided inputs
    filtered_data = data.copy()

    filter_columns = ['os', 'OS', 'Brand', 'Core', 'Processor', 'Camera Details', 'Display Type', 'Display Size', "Flash Type", "Screen flash", "Fast charging", "Type-C"]
    for col in filter_columns:
        if user_input.get(col):
            filtered_data = filtered_data[filtered_data[col] == user_input[col]]

    # Apply numerical filters with a tolerance range
    for key in ['Price', 'Battery', 'Refresh Rate', 'RAM']:
        if user_input[key] is not None:
            # Define a tolerance range, for example, +/- 10% of the input value
            tolerance = 0.1 * user_input[key]
            filtered_data = filtered_data[(filtered_data[key] >= user_input[key] - tolerance) & 
                                        (filtered_data[key] <= user_input[key] + tolerance)]

    # Debugging: Print the filtered data
    print("Filtered data:", filtered_data)

    # If the filtered data is empty, return a message indicating no mobile found
    if filtered_data.empty:
        return render_template('result.html', message="No mobile found")

    # Define the features and target
    categorical_features = ['os', 'Brand', 'OS', 'Core', 'Processor', 'Display Type', 'Display Size', 'Camera Details', 'Flash Type', 'Screen flash', 'Fast charging', 'Type-C']
    numerical_features = ['Price', 'Battery', 'Refresh Rate', 'RAM']
    features = categorical_features + numerical_features
    target = 'Name'

    # Ensure the user input DataFrame has the correct columns
    user_data = pd.DataFrame([user_input])
    missing_columns = set(features) - set(user_data.columns)
    for col in missing_columns:
        user_data[col] = ''

    user_data = user_data[features]

    # Convert numerical columns to the correct type
    for col in numerical_features:
        user_data[col] = pd.to_numeric(user_data[col], errors='coerce')

    # Debugging: Print the user data
    print("User data for prediction:", user_data)

    # Preprocess and predict
    prediction = model.predict(user_data.fillna(0))[0]  # Fill missing numerical values with 0 for the prediction

    # Sort by the rating within filtered data
    recommended_mobiles = ratings[ratings['Name'].isin(filtered_data['Name'])]
    best_mobile = recommended_mobiles.sort_values(by='Final Rating', ascending=False).iloc[0]

    best_mobile_details = data[data["Name"] == best_mobile["Name"]].iloc[0].to_dict()

    # Search for YouTube videos related to the best mobile
    video_query = f"{best_mobile_details['Name']} review by prasad tech in telugu"
    videos = search_videos(video_query)

    return render_template('result.html', mobile=best_mobile_details, videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
