planet_list = ["Mercury", "Mars"]
planet_list.append("jupiter")
planet_list.append("saturn")
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
print(planet_list)
print(rocky_planets)
planet_list.remove("Pluto")
print(planet_list)
visited_list = planet_list[2:5]
print(visited_list)

new_list = []

x=0

for planet in visited_list:
    x += 1
    new_list.append((planet, f"probe {x}"))
    print(new_list)

for planet in new_list:
    print(planet[1])
