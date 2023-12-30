import wikipedia


def scrape(name="Sweden", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape("Amazon", 2))
