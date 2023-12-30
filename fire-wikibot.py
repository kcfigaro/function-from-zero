"""
This is the Wikibot CLI using Fire
"""
import fire
from mylib.bot import scrape

if __name__ == '__main__':
    fire.Fire(scrape)
