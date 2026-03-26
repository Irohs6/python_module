import click

@click.command()
def demander_age():
    age = click.prompt("Veuillez entrer votre âge", type=int)
    click.echo(f"Vous avez {age} {'ans' if age > 1 else 'an'}.")

demander_age()