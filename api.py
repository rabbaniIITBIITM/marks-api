import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the marks data from marks.json
with open('marks.json') as f:
    marks_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Extract names from query parameters
    names = request.args.getlist('name')
    
    # Get the marks corresponding to the names
    response = {"marks": [student["marks"] for student in marks_data if student["name"] in names]}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
