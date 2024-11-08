from user_input import get_user_preferences
from data_fetch import get_weather_data, get_cost_of_living_data, get_crime_data, get_voting_data
from recommendation_engine import calculate_state_score

def main():
    # Step 1: Gather user preferences
    print("Welcome to the State Recommendation Program!")
    user_prefs = get_user_preferences()

    # List of all 50 states
    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico", "New York",
        "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
        "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
        "West Virginia", "Wisconsin", "Wyoming"
    ]

    # Step 2: Fetch data for each state and calculate scores
    scores = []
    for state in states:
        print(f"Fetching data for {state}...")

        # Replace with your actual API keys
        weather_data = get_weather_data(state, "EPA47EKTTEBM5EXSNTP7EZMG6")
        cost_of_living_data = get_cost_of_living_data(state, "YOUR_COST_API_KEY")
        crime_rate = get_crime_data(state, "YOUR_CRIME_API_KEY")
        voting_data = get_voting_data(state)

        # Example state data structure for scoring
        state_data = {
            'avg_temp': weather_data.get('avg_temp', 70),
            'precipitation': weather_data.get('precipitation', 0),
            'cost_of_living': cost_of_living_data.get('cost_of_living', 'medium'),
            'crime_rate': crime_rate,
            'voting': voting_data
        }

        # Calculate score based on user preferences
        score = calculate_state_score(state_data, user_prefs)
        scores.append((state, score))

    # Step 3: Sort states by score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Step 4: Display top recommended states
    print("\nTop recommended states based on your preferences:")
    for state, score in scores[:3]:  # Display top 3 recommendations
        print(f"{state} with a score of {score}")

if __name__ == "__main__":
    main()
