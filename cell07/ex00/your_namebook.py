def array_of_names(d):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in d.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
    }

print(array_of_names(persons))