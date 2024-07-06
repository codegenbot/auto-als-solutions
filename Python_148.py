```
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    index1 = planets.index(planet1)
    if index1 == -1 or index2 := planets.index(planet2) == -1:
        return ()
    start = min(index1, index2)
    end = max(index1, index2)
    return tuple(planets[i] for i in range(start+1, end))