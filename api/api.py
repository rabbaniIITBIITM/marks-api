from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the marks data from marks.json
with open('marks.json') as f:
    marks_data = json.load(f)

@app.route('/', methods=['GET'])
def get_marks():
    # Extract names from query parameters
    names = request.args.getlist('name')
    
    # Filter and maintain original order
    filtered_students = [s for s in marks_data if s["name"] in names]
    
    # Create response with marks in original CSV order
    response = {
        "marks": [student["marks"] for student in filtered_students]
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)