from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import cli


def test_scrape():
    assert "Amazon.com" in scrape("Amazon", 2)


# Add click test
def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Amazon", "--length", "2"])
    assert "Amazon.com" in result.output
    assert result.exit_code == 0
