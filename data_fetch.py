import requests

# Static weather data
# Each state has predefined values for average temperature and precipitation
static_weather_data = {
    "Alabama": {"avg_temp": 65, "precipitation": 50},
    "Alaska": {"avg_temp": 30, "precipitation": 20},
    "Arizona": {"avg_temp": 75, "precipitation": 10},
    "Arkansas": {"avg_temp": 68, "precipitation": 45},
    "California": {"avg_temp": 70, "precipitation": 15},
    "Colorado": {"avg_temp": 50, "precipitation": 30},
    "Connecticut": {"avg_temp": 55, "precipitation": 60},
    "Delaware": {"avg_temp": 60, "precipitation": 55},
    "Florida": {"avg_temp": 75, "precipitation": 70},
    "Georgia": {"avg_temp": 67, "precipitation": 60},
    "Hawaii": {"avg_temp": 77, "precipitation": 80},
    "Idaho": {"avg_temp": 45, "precipitation": 25},
    "Illinois": {"avg_temp": 52, "precipitation": 50},
    "Indiana": {"avg_temp": 54, "precipitation": 50},
    "Iowa": {"avg_temp": 50, "precipitation": 40},
    "Kansas": {"avg_temp": 55, "precipitation": 35},
    "Kentucky": {"avg_temp": 58, "precipitation": 50},
    "Louisiana": {"avg_temp": 68, "precipitation": 65},
    "Maine": {"avg_temp": 45, "precipitation": 60},
    "Maryland": {"avg_temp": 58, "precipitation": 55},
    "Massachusetts": {"avg_temp": 52, "precipitation": 60},
    "Michigan": {"avg_temp": 48, "precipitation": 55},
    "Minnesota": {"avg_temp": 42, "precipitation": 40},
    "Mississippi": {"avg_temp": 67, "precipitation": 65},
    "Missouri": {"avg_temp": 56, "precipitation": 50},
    "Montana": {"avg_temp": 45, "precipitation": 30},
    "Nebraska": {"avg_temp": 50, "precipitation": 35},
    "Nevada": {"avg_temp": 60, "precipitation": 10},
    "New Hampshire": {"avg_temp": 48, "precipitation": 60},
    "New Jersey": {"avg_temp": 58, "precipitation": 55},
    "New Mexico": {"avg_temp": 60, "precipitation": 20},
    "New York": {"avg_temp": 52, "precipitation": 60},
    "North Carolina": {"avg_temp": 63, "precipitation": 55},
    "North Dakota": {"avg_temp": 40, "precipitation": 30},
    "Ohio": {"avg_temp": 53, "precipitation": 50},
    "Oklahoma": {"avg_temp": 60, "precipitation": 45},
    "Oregon": {"avg_temp": 55, "precipitation": 50},
    "Pennsylvania": {"avg_temp": 52, "precipitation": 55},
    "Rhode Island": {"avg_temp": 55, "precipitation": 60},
    "South Carolina": {"avg_temp": 65, "precipitation": 60},
    "South Dakota": {"avg_temp": 45, "precipitation": 35},
    "Tennessee": {"avg_temp": 60, "precipitation": 55},
    "Texas": {"avg_temp": 70, "precipitation": 40},
    "Utah": {"avg_temp": 55, "precipitation": 20},
    "Vermont": {"avg_temp": 48, "precipitation": 60},
    "Virginia": {"avg_temp": 58, "precipitation": 55},
    "Washington": {"avg_temp": 55, "precipitation": 60},
    "West Virginia": {"avg_temp": 55, "precipitation": 55},
    "Wisconsin": {"avg_temp": 48, "precipitation": 45},
    "Wyoming": {"avg_temp": 45, "precipitation": 20}
}

# Generalized industry data for each state, representing the most prominent industry
# Each state has a single value indicating the key industry
generalized_industry_data = {
    "Alabama": "Healthcare",
    "Alaska": "Oil, Gas, and Mining",
    "Arizona": "Healthcare",
    "Arkansas": "Healthcare",
    "California": "Technology/Telecommunications",
    "Colorado": "Computer & Electronic Products",
    "Connecticut": "Insurance",
    "Delaware": "Insurance",
    "Florida": "Healthcare",
    "Georgia": "Healthcare",
    "Hawaii": "Accommodation",
    "Idaho": "Computer & Electronic Products",
    "Illinois": "Insurance",
    "Indiana": "Chemical/Manufacturing",
    "Iowa": "Insurance",
    "Kansas": "Federal Government",
    "Kentucky": "Healthcare",
    "Louisiana": "Oil, Gas, and Mining",
    "Maine": "Healthcare",
    "Maryland": "Federal Government",
    "Massachusetts": "Healthcare",
    "Michigan": "Chemical/Manufacturing",
    "Minnesota": "Healthcare",
    "Mississippi": "Healthcare",
    "Missouri": "Healthcare",
    "Montana": "Oil, Gas, and Mining",
    "Nebraska": "Insurance",
    "Nevada": "Accommodation",
    "New Hampshire": "Healthcare",
    "New Jersey": "Insurance",
    "New Mexico": "Oil, Gas, and Mining",
    "New York": "Finance",
    "North Carolina": "Healthcare",
    "North Dakota": "Oil, Gas, and Mining",
    "Ohio": "Insurance",
    "Oklahoma": "Oil, Gas, and Mining",
    "Oregon": "Technology/Telecommunications",
    "Pennsylvania": "Chemical/Manufacturing",
    "Rhode Island": "Healthcare",
    "South Carolina": "Healthcare",
    "South Dakota": "Federal Government",
    "Tennessee": "Healthcare",
    "Texas": "Oil, Gas, and Mining",
    "Utah": "Technology/Telecommunications",
    "Vermont": "Healthcare",
    "Virginia": "Federal Government",
    "Washington": "Technology/Telecommunications",
    "West Virginia": "Oil, Gas, and Mining",
    "Wisconsin": "Insurance",
    "Wyoming": "Oil, Gas, and Mining"
}
# Lifestyle data categorizing each state as City, Suburb, or Rural
# Each state is categorized by the predominant lifestyle setting
city_suburb_rural_data = {
    "Alabama": "Rural",
    "Alaska": "Rural",
    "Arizona": "City",
    "Arkansas": "Rural",
    "California": "City",
    "Colorado": "Suburb",
    "Connecticut": "Suburb",
    "Delaware": "Suburb",
    "Florida": "City",
    "Georgia": "City",
    "Hawaii": "City",
    "Idaho": "Rural",
    "Illinois": "City",
    "Indiana": "Rural",
    "Iowa": "Rural",
    "Kansas": "Rural",
    "Kentucky": "Rural",
    "Louisiana": "Rural",
    "Maine": "Rural",
    "Maryland": "Suburb",
    "Massachusetts": "City",
    "Michigan": "City",
    "Minnesota": "City",
    "Mississippi": "Rural",
    "Missouri": "Suburb",
    "Montana": "Rural",
    "Nebraska": "Rural",
    "Nevada": "City",
    "New Hampshire": "Rural",
    "New Jersey": "Suburb",
    "New Mexico": "Rural",
    "New York": "City",
    "North Carolina": "City",
    "North Dakota": "Rural",
    "Ohio": "Suburb",
    "Oklahoma": "Rural",
    "Oregon": "Suburb",
    "Pennsylvania": "Suburb",
    "Rhode Island": "Suburb",
    "South Carolina": "Rural",
    "South Dakota": "Rural",
    "Tennessee": "Suburb",
    "Texas": "City",
    "Utah": "Suburb",
    "Vermont": "Rural",
    "Virginia": "Suburb",
    "Washington": "City",
    "West Virginia": "Rural",
    "Wisconsin": "Rural",
    "Wyoming": "Rural"
}

# Function to get weather data for a state
def get_weather_data(state):
    # Returns weather data for the given state or default values if not found
    return static_weather_data.get(state, {"avg_temp": 70, "precipitation": 0})

# Function to get cost of living data for a state
def get_cost_of_living_data(state, user_pref):
    # Dictionary containing cost of living indices for each state
    cost_of_living_indices = {
        "Alabama": 88.8, "Alaska": 123.4, "Arizona": 112.8, "Arkansas": 87.5, "California": 144.7,
        "Colorado": 102.7, "Connecticut": 111.7, "Delaware": 100.2, "Florida": 102.4, "Georgia": 91.5,
        "Hawaii": 184.6, "Idaho": 102.0, "Illinois": 95.5, "Indiana": 91.3, "Iowa": 90.4,
        "Kansas": 86.7, "Kentucky": 94.9, "Louisiana": 94.9, "Maine": 113.5, "Maryland": 98.9,
        "Massachusetts": 146.9, "Michigan": 92.3, "Minnesota": 99.3, "Mississippi": 87.5, "Missouri": 89.0,
        "Montana": 95.4, "Nebraska": 92.1, "Nevada": 100.1, "New Hampshire": 111.5, "New Jersey": 114.8,
        "New Mexico": 92.9, "New York": 123.4, "North Carolina": 92.9, "North Dakota": 92.1, "Ohio": 91.3,
        "Oklahoma": 87.9, "Oregon": 110.0, "Pennsylvania": 94.9, "Rhode Island": 112.4, "South Carolina": 95.2,
        "South Dakota": 92.3, "Tennessee": 90.0, "Texas": 92.6, "Utah": 109.5, "Vermont": 114.1,
        "Virginia": 100.5, "Washington": 113.6, "West Virginia": 84.8, "Wisconsin": 99.3, "Wyoming": 95.4
    }
    # Retrieve cost of living index for the state
    cost_index = cost_of_living_indices.get(state, None)
    if cost_index is None:
        return {"cost_of_living": "unknown"}  # Return "unknown" if state not found
    # Match the user's preference to the cost of living index range
    if user_pref == "low" and cost_index < 90:
        return {"cost_of_living": "low"}
    elif user_pref == "medium" and 90 <= cost_index <= 110:
        return {"cost_of_living": "medium"}
    elif user_pref == "high" and cost_index > 110:
        return {"cost_of_living": "high"}
    else:
        return {"cost_of_living": "mismatch"}  # Return mismatch if it doesn't align

# Function to get crime rate data for a state
# For lines 203-226 used AI to help generate code, so it could properly handle errors and get data for the crime rate
def get_crime_rate(state):
    # Fetch crime data from an external API
    url = "https://ncosbm.opendatasoft.com/api/records/1.0/search/"
    params = {
        "dataset": "state-comparison-crime-data",
        "refine.area_name": state,
        "rows": 1,
        "sort": "year"
    }
    try:
        # Make a request to the API with parameters
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()  # Parse the JSON response
        # Extract crime rate value if available
        if data.get("records"):
            record = data["records"][0]["fields"]
            return {"crime_rate": record.get("value", 0)}
        else:
            return {"crime_rate": 0}  # Default crime rate if no data found
    except requests.exceptions.RequestException as e:
        # Handle network or API errors gracefully
        print(f"Error fetching crime data for {state}: {e}")
        return {"crime_rate": 0}  # Default crime rate in case of error

# Function to get voting demographic data for a state
def get_voting_data(state):
    # Dictionary mapping each state to its predominant voting demographic
    voting_demographics = {
        "Alabama": "Republican", "Alaska": "Republican", "Arizona": "Swing", "Arkansas": "Republican",
        "California": "Democratic", "Colorado": "Democratic", "Connecticut": "Democratic", "Delaware": "Democratic",
        "Florida": "Swing", "Georgia": "Swing", "Hawaii": "Democratic", "Idaho": "Republican",
        "Illinois": "Democratic", "Indiana": "Republican", "Iowa": "Swing", "Kansas": "Republican",
        "Kentucky": "Republican", "Louisiana": "Republican", "Maine": "Swing", "Maryland": "Democratic",
        "Massachusetts": "Democratic", "Michigan": "Swing", "Minnesota": "Democratic", "Mississippi": "Republican",
        "Missouri": "Republican", "Montana": "Republican", "Nebraska": "Republican", "Nevada": "Swing",
        "New Hampshire": "Swing", "New Jersey": "Democratic", "New Mexico": "Democratic", "New York": "Democratic",
        "North Carolina": "Swing", "North Dakota": "Republican", "Ohio": "Swing", "Oklahoma": "Republican",
        "Oregon": "Democratic", "Pennsylvania": "Swing", "Rhode Island": "Democratic", "South Carolina": "Republican",
        "South Dakota": "Republican", "Tennessee": "Republican", "Texas": "Republican", "Utah": "Republican",
        "Vermont": "Democratic", "Virginia": "Swing", "Washington": "Democratic", "West Virginia": "Republican",
        "Wisconsin": "Swing", "Wyoming": "Republican"
    }
    return voting_demographics.get(state, "Unknown") # Return voting demographic for the state or "Unknown" if not found
