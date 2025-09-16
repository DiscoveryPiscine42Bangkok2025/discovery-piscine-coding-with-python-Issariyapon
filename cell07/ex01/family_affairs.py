def find_the_redheads(family: dict) -> list:
    return list(filter(lambda name: family.get(name) == "red", family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
    }

print(find_the_redheads(dupont_family))
