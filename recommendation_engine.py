def calculate_state_score(state_data, user_preferences):
    score = 0

    # Match average temperature preference
    if 'avg_temp' in state_data and abs(state_data['avg_temp'] - user_preferences['weather']) < 5:
        score += 10

    # Match cost of living preference
    if 'cost_of_living' in state_data and state_data['cost_of_living'] == user_preferences['cost_of_living']:
        score += 10

    # Match rain preference
    if 'precipitation' in state_data:
        if user_preferences['rain_pref'] == 'rainy' and state_data['precipitation'] > 0:
            score += 10
        elif user_preferences['rain_pref'] == 'dry' and state_data['precipitation'] == 0:
            score += 10

    # Match crime rate preference (lower crime rates are given higher scores)
    if 'crime_rate' in state_data and user_preferences.get('crime_tolerance') == 'low':
        score += (100 - state_data['crime_rate']) // 10  # Scale crime rate to a 0-10 range

    # Match voting preference
    if 'voting' in state_data and state_data['voting'] == user_preferences.get('voting_preference'):
        score += 10

    return score
