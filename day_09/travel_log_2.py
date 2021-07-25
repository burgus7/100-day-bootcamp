travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country_dict = {
        "country": country,
        "visits": visits,
        "cities": cities
    }

    print_new_entry(country, visits, cities)

    travel_log.append(new_country_dict)

def print_new_entry(country, visits, cities):
    print(f"You've visited {country} {visits} times.")

    cities_str = ""
    len_cities = len(cities)

    if len_cities == 1:
        cities_str = f"{cities[0]}."
    elif len_cities == 2:
        cities_str = f"{cities[0]} and {cities[1]}."
    else:
        for i in range(len_cities - 1):
            cities_str += f"{cities[i]}, "
        cities_str += f"and {cities[len_cities - 1]}."

    print(f"You've been to {cities_str}")


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



