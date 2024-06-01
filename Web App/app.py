from flask import Flask, request, render_template
import pandas as pd
import joblib

# Load the dataset and the trained model
data = pd.read_csv('Preprocessed_Final_Data.csv')
model = joblib.load('random_forest_model.pkl')
ratings = joblib.load('ratings.pkl')

app = Flask(__name__)

# Default values for numerical inputs
default_values = {
    'Price': 150000,
    'Battery': 5000,
    'Refresh Rate': 120,
    'RAM': 12
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.to_dict()

    # Set default values for missing numerical inputs
    for key, default in default_values.items():
        if user_input.get(key) == '' or user_input.get(key) is None:
            user_input[key] = default
        else:
            user_input[key] = float(user_input[key])  # Ensure numerical inputs are floats
    
    user_os = user_input.get('os')
    user_brand = user_input.get('Brand')

    # Filter the dataset based on the OS input
    filtered_data = data[data['os'] == user_os]

    if filtered_data.empty:
        return render_template('result.html', mobile=None, message=f"No mobiles found for OS: {user_os}")

    # Further filter the dataset based on the Brand input if provided
    if user_brand:
        filtered_data = filtered_data[filtered_data['Brand'] == user_brand]

    if filtered_data.empty:
        return render_template('result.html', mobile=None, message=f"No mobiles found for OS: {user_os} and Brand: {user_brand}")

    # Define the features and target
    categorical_features = ['OS', 'Brand', 'Core', 'Processor', 'Display Type', 'Display Size', 'Camera Details', 'Flash Type', 'Screen flash', 'Fast charging', 'Type-C', 'os']
    numerical_features = ['Price', 'Battery', 'Refresh Rate', 'RAM']
    target = 'Name'

    X = filtered_data[categorical_features + numerical_features]
    y = filtered_data[target]

    # Train the model on the filtered data
    model.fit(X, y)

    # Prepare the user input for prediction
    user_data = pd.DataFrame([user_input])

    # Preprocess and predict
    prediction = model.predict(user_data)[0]

    # Find the best rated mobile among the predicted ones
    recommended_mobiles = ratings[ratings['Name'] == prediction]
    best_mobile = recommended_mobiles.sort_values(by='Final Rating', ascending=False).iloc[0]

    best_mobile_details = data[data["Name"] == best_mobile["Name"]].iloc[0].to_dict()

    return render_template('result.html', mobile=best_mobile_details)

if __name__ == '__main__':
    app.run(debug=True)
