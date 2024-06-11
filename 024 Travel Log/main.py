# Define a list named travel_log containing dictionaries of countries and their travel details
travel_log = [
    {
        "country": "Pakistan",            # The name of the country
        "visits": 2,                      # Number of times visited
        "cities": ["Islamabad", "Lahore", "Balochistan", "Punjab"]  # List of cities visited in the country
    }, 
    {
        "country": "Iran",                # The name of another country
        "visits": 6,                      # Number of times visited
        "cities": ["Tehran", "Isfahan", "Shiraz", "Tabriz"]  # List of cities visited in the country
    }
]

# Define a function to add a new travel log entry
def add_travel_log(country, visits, cities_list):
    # Create a new dictionary with the given country, visits, and cities_list
    new_log = {
        "country": country,                # The name of the new country to add
        "visits": visits,                  # Number of times visited the new country
        "cities": cities_list              # List of cities visited in the new country
    }

    # Append the new dictionary to the travel_log list
    travel_log.append(new_log)

# Call the function to add a travel log entry for China
add_travel_log("China", 4, cities_list=["Beijing", "Shanghai"])

# Print the updated travel_log list to the console
print(travel_log)