import click
import requests
import os
import json

from info import Info
from record import Record
from records import RecordCollection
from config import currPath



__author__ = "Harikrushna Adiecha"

@click.group()
def main():
    """
    Simple CLI for querying books on Google Books by Oyetoke Toby
    """
    pass

@main.command()
def list():
    """ This function will show list of frizzed files """
    info = Info()
    info.display()


@main.command()
@click.argument('filepath')
def add(filepath):
    """ This function will add file to frizzed files list """

    # check if given file exists or not
    src = currPath(filepath)

    if os.path.isfile(src):
        info = Info()
        if info.exists(src):
            print("file '{}' already freezed !".format(src))
        else:
            r = Record(src)
            r.backup()
            info.addRecord(r)
            info.save()
            print("file '{}' freezed.".format(src))
    else:
        print("file '{}' not exists".format(src))

@main.command()
def check():
    """ This function will check changes and revert if required """
    info = Info()
    info.check()


if __name__ == "__main__":
    main()
