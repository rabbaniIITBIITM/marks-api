from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

# Load student data from marks.json
def load_marks():
    with open("marks.json", "r") as file:
        marks_data = json.load(file)
        # Create a dictionary with names as keys and marks as values
        marks_dict = {entry["name"]: entry["marks"] for entry in marks_data}
    return marks_dict

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = load_marks()  # Load the marks data
    result = {"marks": [marks.get(n, "Not Found") for n in name]}  # Fetch marks for given names
    return result
