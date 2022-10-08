import click


def show_progress(how_many, character='*'):
    click.echo(click.style(character * how_many, bg='blue', fg='white'))
    return None


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')
input()
