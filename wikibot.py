import click
from mylib.bot import scrape

@click.command()
@click.option("--name", default="Sweden", help="Name")
@click.option("--length", default=2, help="number of sentences.")
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f'{result}', fg='green'))

if __name__ == '__main__':
    cli()

