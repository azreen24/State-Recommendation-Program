State Recommendation Program
- Overview
    The State Recommendation Program is a simple Python application that recommends the best U.S. states for users based on their personal preferences.
    By answering a few questions about users lifestyle, climate, and living preferences, the program will suggest the top three states that best match
    what the user is looking for.

Features
    Easy-to-Use Interface: Input your preferences through simple questions.
    Personalized Scoring: States are scored based on how closely they match users preferences.
    Top Recommendations: Get the top three states that fit users needs.
    Factors Considered:
        Temperature
        Climate (dry or rainy)
        Cost of living
        Crime tolerance
        Job industry
        Voting preference
        Lifestyle (City, Suburb, or Rural)

How It Works
    User Input:
        User will be asked about their preferences for temperature, climate, cost of living, etc.
        Rank the importance of each factor (e.g., 1 for most important, 7 for least important).

  State Data:
        The program uses a built-in dataset for information like state temperatures, crime rates, and job industries.
    Scoring:
        Each state is given a score based on how well it matches your preferences.
        Higher scores mean a better match for user.
    Recommendations:
        The program displays the top three states with the highest scores.

Installation/Program Requirements
    Python 3.7 or higher
    import requests
    internet for fetching live crime rate data

Files in This Project
    main.py
        The main file that runs the program.
        Collects user preferences and calculates state recommendations.
    data_fetch.py
        Stores data for each state, like:
        Average temperature and precipitation, Cost of living, Crime rate, Voting trends, Job industries, Lifestyle (City, Suburb, Rural)
    user_input.py
        Handles asking questions and validating user input.
        Collects all the preferences needed for recommendations.
    recommendation_engine.py
        Contains the scoring logic.
        Compares state data with user preferences and calculates scores.

How to Use the Program
    Start the Program:
    Run python main.py.
    Answer the Questions:
    The program will ask about your preferences for temperature, climate, cost of living, and more.
    Rank the importance of each factor.
    View Recommendations:
    After processing all states, the program will show the top three states that best fit your preferences.

Example Output
    Welcome to the State Recommendation Program!
    Please enter your preferences:
        Preferred average temperature (e.g., 70 for 70°F): 75
        Do you prefer a dry or rainy climate? (dry/rainy): rainy
        Cost of living preference (low/medium/high): medium
        Preferred job industry (e.g., Healthcare, Technology): Technology
        Crime rate tolerance (low/medium/high): medium
        Voting preference (Democratic/Republican/Swing): Swing
        Do you prefer to live in a City, Suburb, or Rural area? (City/Suburb/Rural): City
        Rank the following factors from 1 (most important) to 7 (least important):
            Temperature: 1
            Climate (dry/rainy): 4
            Cost of Living: 3
            Crime Rate: 5
            Voting Demographic: 2
            Job Industry: 6
            City/Suburb/Rural: 7

  Fetching data for all states...
  Progress: 50/50 states processed...

  Top recommended states based on your preferences:
        1. California: Score: 92.5
        2. New York: Score: 88.4
        3. Washington: Score: 85.2

Customization
    To change the data or add new features, here’s how:
    Update State Data:
        Edit data_fetch.py to add or modify state information.
    Adjust Scoring:
        Edit the scoring logic in recommendation_engine.py.
    Add More Factors:
        Add new questions in user_input.py.
        Include the new factor in the scoring logic.

Authors: Andrew, Emma, Azreen, Madi
