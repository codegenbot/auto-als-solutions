```
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    if index1 > 7 or index2 > 7:
        return []

    result = []
    for i in range(min(index1, index2) + 1, max(index1, index2)):
        result.append(planets[i])

    return tuple(result)