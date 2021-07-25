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
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visited_times, visited_cities):
    new_city = {}
    new_city["country"] = country
    new_city["visits"] = visited_times
    new_city["cities"] = visited_cities
    
    travel_log.append(new_city)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



