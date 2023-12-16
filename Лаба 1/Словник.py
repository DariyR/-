typeofgame = {
    "voleyball": {
        "Type of game" : "Don`t contact",
        "Number of players" : 6,
        "Instrument for playing" : "Hands"
    },
    "football": {
        "Type of game" : "Contact",
        "Number of players" : 11,
        "Instrument for playing" : "Legs"
    },
    "basketball": {
        "Type of game" : "Contact",
        "Number of players" : 8,
        "Instrument for playing" : "Hands"
    }
}

key = input('введіть ключ:')
if key in typeofgame:
    print(typeofgame[key])
else:
    print("there is not such key in vocabulary")