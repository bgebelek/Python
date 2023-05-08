#HackerEarth - Zoos


def similar_to_zoo(word):
    if len(word) <= 20:
        if word.count("z") * 2 == word.count("o"):
            return "Yes"
        return "No"
    return "Word must be 20 characters or less"


print(similar_to_zoo("zzzooooo"))
