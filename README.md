# Weather App Readme

## Overview

This Weather App is a simple Django-based web application that provides current weather information. It utilizes the OpenWeatherMap API to fetch real-time weather data based on user-provided location queries.

## Features

- **Current Weather Information:** Users can enter a city name or coordinates to get the current weather conditions, including temperature, humidity, wind speed, and more.

- **Responsive Design:** The app is designed to be responsive and accessible on various devices, including desktops, tablets, and mobile phones.

- **OpenWeatherMap API Integration:** The app fetches weather data from the OpenWeatherMap API, ensuring accurate and up-to-date information.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YeghiazarianVahe/weatherapp
   ```

2. Navigate to the project directory:

   ```bash
   cd WeatherApp
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up environment variables:

   Copy the `.env.example` file to `.env` and update the values with your OpenWeatherMap API key:

   ```bash
   cp .env.example .env
   ```

7. Run migrations:

   ```bash
   python manage.py migrate
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Visit `http://127.0.0.1:8000/` in your web browser to access the Weather App.

## Configuration

- **OpenWeatherMap API Key:** You need to sign up for an OpenWeatherMap API key [here](https://openweathermap.org/appid) and update the `.env` file with your API key.

## Usage

1. Access the Weather App in your web browser.

2. Enter a city name or coordinates in the search bar and click the "Get Weather" button.

3. View the current weather information for the specified location.


## License

This Weather App is open-source and available under the [MIT License](LICENSE).

