import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler


# Load the marks data
with open("marks.json", "r") as f:
    data = json.load(f)  # List of dictionaries


class handler(BaseHTTPRequestHandler):	
    def do_GET(self):
        # Parse query parameters
        query = urlparse(self.path).query
        params = parse_qs(query)
        names = params.get("name", [])  # List of requested names


        # Search for names in the data
        result = []
        for name in names:
            match = next((item["marks"] for item in data if item["name"] == name), "Not Found")
            result.append(match)


        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


        # Send the JSON response
        self.wfile.write(json.dumps({"marks": result}).encode("utf-8"))