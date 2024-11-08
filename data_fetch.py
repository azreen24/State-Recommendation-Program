import requests


def get_weather_data(state, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{state}?key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract relevant weather data, including average temperature and precipitation
        avg_temp = data.get('days', [{}])[0].get('temp', 70)  # Default to 70 if missing
        avg_precipitation = data.get('days', [{}])[0].get('precip', 0)  # Default to 0 if missing

        return {
            'avg_temp': avg_temp,
            'precipitation': avg_precipitation  # Add precipitation as a factor
        }
    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data for {state}: {e}")
        return {}

def get_cost_of_living_data(state, api_key):
    url = #find url
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get cost of living data for {state}: {e}")
        return {}

def get_crime_data(state, api_key):
    url = #find url
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Extract relevant crime data, such as violent crime rate
        crime_rate = data.get('results', [{}])[0].get('violent_crime_rate', 0)
        return crime_rate
    except requests.exceptions.RequestException as e:
        print(f"Failed to get crime data for {state}: {e}")
        return 0  # Default to 0 if data is unavailable

def get_voting_data(state):
    # Use static data for voting demographics
    voting_demographics = {
    "Alabama": "Republican",
    "Alaska": "Republican",
    "Arizona": "Swing",
    "Arkansas": "Republican",
    "California": "Democratic",
    "Colorado": "Democratic",
    "Connecticut": "Democratic",
    "Delaware": "Democratic",
    "Florida": "Swing",
    "Georgia": "Swing",
    "Hawaii": "Democratic",
    "Idaho": "Republican",
    "Illinois": "Democratic",
    "Indiana": "Republican",
    "Iowa": "Swing",
    "Kansas": "Republican",
    "Kentucky": "Republican",
    "Louisiana": "Republican",
    "Maine": "Swing",
    "Maryland": "Democratic",
    "Massachusetts": "Democratic",
    "Michigan": "Swing",
    "Minnesota": "Democratic",
    "Mississippi": "Republican",
    "Missouri": "Republican",
    "Montana": "Republican",
    "Nebraska": "Republican",
    "Nevada": "Swing",
    "New Hampshire": "Swing",
    "New Jersey": "Democratic",
    "New Mexico": "Democratic",
    "New York": "Democratic",
    "North Carolina": "Swing",
    "North Dakota": "Republican",
    "Ohio": "Swing",
    "Oklahoma": "Republican",
    "Oregon": "Democratic",
    "Pennsylvania": "Swing",
    "Rhode Island": "Democratic",
    "South Carolina": "Republican",
    "South Dakota": "Republican",
    "Tennessee": "Republican",
    "Texas": "Republican",
    "Utah": "Republican",
    "Vermont": "Democratic",
    "Virginia": "Swing",
    "Washington": "Democratic",
    "West Virginia": "Republican",
    "Wisconsin": "Swing",
    "Wyoming": "Republican"
    }
    return voting_demographics.get(state, "Unknown")  # Default to "Unknown" if not listed
