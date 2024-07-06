def Strongest_Extension(class_name, extensions):
    strongest = max(
        extensions,
        key=lambda x: sum(1 for c in x if c.isupper())
        - sum(1 for c in x if c.islower()),
    )
    return f"{class_name}.{strongest}"