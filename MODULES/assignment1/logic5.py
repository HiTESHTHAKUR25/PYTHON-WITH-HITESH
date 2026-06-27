def vowels(name):
    x = filter(lambda x: x.startswith("a") or x.startswith("e"),name)
    return list(x)
