from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to load marks from marks.json
def load_marks():
    file_path = os.path.join(os.path.dirname(__file__), "marks.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    # Convert the list into a dictionary for quick lookup:
    return {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks_lookup = load_marks()
    # For each name in the query, get its mark (default to 0 if not found)
    marks = [marks_lookup.get(n, 0) for n in name]
    return {"marks": marks}
