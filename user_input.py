def get_user_preferences():
    print("Please enter your preferences:")

    # Validate temperature input
    while True:
        try:
            # Ask the user for their preferred average temperature
            temperature = int(input("Preferred average temperature (e.g., 70 for 70°F): "))
            # Ensure the input is within a realistic range
            if -30 <= temperature <= 120:
                break  # Exit the loop if input is valid
            else:
                print("Enter a realistic temperature between -30 and 120°F.")
        except ValueError:
            # Handle non-numeric input gracefully
            print("Invalid input. Please enter a number.")

    # Validate climate preference
    while True:
        # Ask the user for their climate preference (dry or rainy)
        climate = input("Do you prefer a dry or rainy climate? (dry/rainy): ").strip().lower()
        # Ensure input matches one of the valid options
        if climate in ["dry", "rainy"]:
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter 'dry' or 'rainy'.")

    # Validate cost of living preference
    while True:
        # Ask the user for their cost of living preference
        cost_of_living = input("Cost of living preference (low/medium/high): ").strip().lower()
        # Ensure input matches one of the valid options
        if cost_of_living in ["low", "medium", "high"]:
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")

    # Ask the user for their preferred job industry
    job_industry = input("Preferred job industry (e.g., Healthcare, Technology): ").strip().lower()

    # Validate crime tolerance
    while True:
        # Ask the user for their crime tolerance level
        crime_tolerance = input("Crime rate tolerance (low/medium/high): ").strip().lower()
        # Ensure input matches one of the valid options
        if crime_tolerance in ["low", "medium", "high"]:
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")

    # Ask the user for their voting demographic preference
    voting_preference = input("Voting preference (Democratic/Republican/Swing): ").strip().capitalize()

    # Add validation for City/Suburb/Rural preference
    while True:
        # Ask the user for their lifestyle preference
        lifestyle_preference = input(
            "Do you prefer to live in a City, Suburb, or Rural area? (City/Suburb/Rural): ").strip().capitalize()
        # Ensure input matches one of the valid options
        if lifestyle_preference in ["City", "Suburb", "Rural"]:
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter 'City', 'Suburb', or 'Rural'.")

    # Validate rankings
    print("\nRank the following factors from 1 (most important) to 7 (least important):")
    rankings = {}  # Dictionary to store factor rankings
    factors = [
        "Temperature", "Climate (dry/rainy)", "Cost of Living", "Crime Rate", "Voting Demographic", "Job Industry",
        "City/Suburb/Rural"
    ]
    for factor in factors:
        while True:
            try:
                # Ask the user to rank each factor
                rank = int(input(f"{factor}: "))
                # Ensure the rank is unique and within the valid range
                if 1 <= rank <= 7 and rank not in rankings.values():
                    rankings[factor.lower()] = rank  # Store the rank
                    break  # Exit the loop if input is valid
                else:
                    print("Enter a unique number between 1 and 7.")
            except ValueError:
                # Handle non-numeric input gracefully
                print("Invalid input. Please enter a number between 1 and 7.")

    # Return all collected preferences as a dictionary
    return {
        "temperature": temperature,  # User's preferred average temperature
        "climate": climate,  # User's climate preference (dry/rainy)
        "cost_of_living": cost_of_living,  # User's cost of living preference
        "job_industry": job_industry,  # User's preferred job industry
        "crime_tolerance": crime_tolerance,  # User's crime tolerance level
        "voting_preference": voting_preference,  # User's voting demographic preference
        "lifestyle_preference": lifestyle_preference,  # User's lifestyle preference (City/Suburb/Rural)
        "rankings": rankings  # Rankings of the factors by importance
    }
