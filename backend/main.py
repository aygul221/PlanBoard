

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


aufgaben = [] #speichern hier die Aufgaben vorrübergehend



class Aufgabe(BaseModel): #basemodel definiert welche Attribute die Aufgabe hat
    titel: str
    beschreibung: str
    prioritaet: str


@app.get("/")
def startseite():
    return {"message": "Willkommen bei PlanBoard!"}



@app.post("/tasks")   # Daten an den Server senden
def aufgabe_erstellen(aufgabe: Aufgabe):
    neue_aufgabe = {
        "id": len(aufgaben) + 1,
        "titel": aufgabe.titel,
        "beschreibung": aufgabe.beschreibung,
        "prioritaet": aufgabe.prioritaet,
        "erledigt": False
    }

    aufgaben.append(neue_aufgabe) # stellt neue 

    return neue_aufgabe


# Alle Aufgaben anzeigen
@app.get("/tasks")
def alle_aufgaben():
    return aufgaben
