from data_fetch import get_weather_data, get_cost_of_living_data, get_crime_rate, get_voting_data, generalized_industry_data, city_suburb_rural_data
from recommendation_engine import calculate_state_score
from user_input import get_user_preferences


def main():
    print("Welcome to the State Recommendation Program!")

    # Step 1: Get user preferences
    user_prefs = get_user_preferences()  # Collect preferences like temperature, cost of living, etc.

    # List of all states to process
    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
        "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
        "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]

    print("\nFetching data for all states...")  # Notify the user that data is being fetched
    scores = []  # Initialize a list to store scores for each state

    for i, state in enumerate(states, start=1):
        # Display progress every 10 states or at the end
        if i % 10 == 0 or i == len(states):
            print(f"Progress: {i}/{len(states)} states processed...")

        try:
            # Fetch various attributes for the current state
            weather_data = get_weather_data(state)  # Temperature and precipitation data
            cost_of_living_data = get_cost_of_living_data(state, user_prefs["cost_of_living"])  # Cost of living data
            crime_data = get_crime_rate(state)  # Crime rate data
            voting_data = get_voting_data(state)  # Voting demographic data
            industry_data = generalized_industry_data.get(state, "Unknown")  # Major industry in the state
            lifestyle_data = city_suburb_rural_data.get(state, "Unknown")  # Lifestyle preference (City/Suburb/Rural)

            # Combine all fetched data into a single dictionary for scoring
            state_data = {
                "avg_temp": weather_data.get("avg_temp", 70),  # Default temperature to 70°F if missing
                "precipitation": weather_data.get("precipitation", 0),  # Default precipitation to 0 if missing
                "cost_of_living": cost_of_living_data.get("cost_of_living", "unknown"),  # Default to unknown if missing
                "crime_rate": crime_data.get("crime_rate", 0),  # Default crime rate to 0 if missing
                "voting": voting_data,  # Voting demographic (e.g., Democratic, Republican, Swing)
                "industry": industry_data,  # Industry data (e.g., Healthcare, Technology)
                "lifestyle": lifestyle_data  # Lifestyle preference (e.g., City, Suburb, Rural)
            }

            # Calculate a score for the state based on user preferences
            score = calculate_state_score(state_data, user_prefs)
            scores.append((state, score))  # Append the state and its score to the list
        except Exception as e:
            # Handle any exceptions gracefully and continue processing other states
            print(f"Error processing state {state}: {e}")

    # Step 2: Sort states by scores in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Step 3: Display the top 3 recommended states to the user
    print("\nTop recommended states based on your preferences:")
    for state, score in scores[:3]:  # Show only the top 3 states
        print(f"{state}: Score: {score}")


if __name__ == "__main__":
    main()  # Entry point of program
