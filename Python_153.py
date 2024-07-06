def Strongest_Extension(class_name, extensions):
    strongest = None
    max_strength = float("-inf")

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = len(extension) - cap
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest = extension

    return f"{class_name}.{strongest}"