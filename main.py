# This is a Python script for Favorite City

def favorite_city(name):
    if name == "Chicago":
        print("One of my favorite cities is The Windy City, " + name)
    elif name == "New York":
        print("One of my favorite cities is The Big Apple, " + name)
    elif name == "Boston":
        print("One of my favorite cities is Beantown,  " + name)
    return favorite_city(name)
