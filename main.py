import json

from generator import dossier
from database.database import update_table


if __name__ == "__main__":
    person = json.loads(dossier())
    print(person)
    update_table(person)
