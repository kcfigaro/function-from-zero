import wikipedia

def scrape(name="Sweden", length=2):
    result = wikipedia.summary(name, sentences=length)
    return result