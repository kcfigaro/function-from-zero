from wikibot import scrape

def test_scrape(): 
    assert "Amazon.com" in scrape("Amazon", 2)