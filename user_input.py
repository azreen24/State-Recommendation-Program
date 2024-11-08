def get_user_preferences():
    print("Please enter your preferences:")

    # Collect preferences for temperature and rain
    weather_pref = int(input("Preferred average temperature (e.g., 70 for 70°F): "))
    rain_pref = input("Do you prefer a dry or rainy climate? (dry/rainy): ").strip().lower()

    # Collect preferences for cost of living
    cost_of_living_pref = input("Cost of living preference (low/medium/high): ").strip().lower()

    # Collect job industry preference
    job_pref = input("Preferred job industry (e.g., Tech, Healthcare): ").strip()

    # Collect crime rate tolerance
    crime_tolerance = input("Do you prefer a low, medium, or high tolerance for crime rates? (low/medium/high): ").strip().lower()

    # Collect voting demographic preference
    voting_preference = input("Do you prefer to live in a Democratic, Republican, or Swing state? ").strip().capitalize()

    # Optional preference for a specific state or region
    state_pref = input("Do you have a preferred state or region (e.g., Florida, West Coast)? If none, press Enter: ").strip()

    return {
        'weather': weather_pref,
        'rain_pref': rain_pref,
        'cost_of_living': cost_of_living_pref,
        'job_industry': job_pref,
        'crime_tolerance': crime_tolerance,
        'voting_preference': voting_preference,
        'state_pref': state_pref  # Optional field for state preference
    }
