pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

def list_taker():
    for pirate in pirates:
        if pirate["gold"] > 15 and pirate["has_wooden_leg"] == True:
             print(pirate['Name'])

list_taker()

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold
