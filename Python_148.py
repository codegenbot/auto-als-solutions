def bf(planet1, planet2):
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    if planet1 not in planets or planet2 not in planets:
        return ()
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    return tuple(
        sorted([p for p in planets[i1 + 1 : i2] if p != planet1 and p != planet2])
    )