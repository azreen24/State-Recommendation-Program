# Used AI to help with understanding how we could implement a scoring system that gives a higher score
# based on users ranking of factors, as well as give partial "points" to users input
# if it was a close match (e.g. state has avg 70 degree temp but user put 72)
def calculate_state_score(state_data, user_preferences):
    # Initialize the score to zero
    score = 0

    # Extract rankings from user preferences
    rankings = user_preferences["rankings"]

    # Normalize rankings into weights and scale to 100
    # Higher-ranked factors (lower rank value) get higher weights
    total_weight = sum((7 - rank) for rank in rankings.values())  # Total weight sum for normalization
    weights = {factor: ((7 - rank) / total_weight) * 100 for factor, rank in
               rankings.items()}  # Convert to percentage weights

    # Temperature preference scoring
    # Compare the user's preferred temperature with the state's average temperature
    temp_diff = abs(state_data.get("avg_temp", 70) - user_preferences["temperature"])
    if temp_diff <= 5:  # Exact match
        score += weights["temperature"]
    elif temp_diff <= 10:  # Close match (partial points)
        score += weights["temperature"] * 0.5
    else:  # No match
        score += 0

    # Climate preference scoring (dry/rainy)
    # Compare the user's climate preference with the state's precipitation
    precipitation = state_data.get("precipitation", 0)
    if user_preferences["climate"] == "rainy" and precipitation > 30:  # Match for rainy preference
        score += weights["climate (dry/rainy)"]
    elif user_preferences["climate"] == "dry" and precipitation <= 30:  # Match for dry preference
        score += weights["climate (dry/rainy)"]
    elif abs(precipitation - 30) <= 10:  # Close match
        score += weights["climate (dry/rainy)"] * 0.5
    else:  # No match
        score += 0

    # Cost of living preference scoring
    # Check if the state's cost of living matches the user's preference
    if user_preferences["cost_of_living"] == state_data["cost_of_living"]:  # Exact match
        score += weights["cost of living"]
    elif state_data["cost_of_living"] != "unknown":  # Partial match
        score += weights["cost of living"] * 0.5
    else:  # No match
        score += 0

    # Crime tolerance preference scoring
    # Compare the state's crime rate with the user's crime tolerance
    crime_rate = state_data["crime_rate"]
    if user_preferences["crime_tolerance"] == "low" and crime_rate < 30:  # Match for low crime tolerance
        score += weights["crime rate"]
    elif user_preferences["crime_tolerance"] == "medium" and 30 <= crime_rate <= 70:  # Match for medium tolerance
        score += weights["crime rate"]
    elif user_preferences["crime_tolerance"] == "high" and crime_rate > 70:  # Match for high tolerance
        score += weights["crime rate"]
    elif abs(crime_rate - 50) <= 20:  # Close match
        score += weights["crime rate"] * 0.5
    else:  # No match
        score += 0

    # Lifestyle preference scoring (City/Suburb/Rural)
    # Compare the user's lifestyle preference with the state's lifestyle category
    if user_preferences["lifestyle_preference"].lower() == state_data["lifestyle"].lower():  # Exact match
        score += weights["city/suburb/rural"]
    else:  # Partial match
        score += weights["city/suburb/rural"] * 0.5

    # Voting demographic preference scoring
    # Compare the user's voting preference with the state's voting tendency
    if state_data.get("voting", "").lower() == user_preferences["voting_preference"].lower():
        score += weights["voting demographic"]
    else:  # No match
        score += 0

    # Job industry preference scoring
    # Check if the user's preferred job industry exists in the state's industry data
    if user_preferences["job_industry"].lower() in state_data["industry"].lower():  # Match found
        score += weights["job industry"]
    else:  # No match
        score += 0

    # Normalize the final score to a maximum of 100
    return min(100, round(score, 2))
