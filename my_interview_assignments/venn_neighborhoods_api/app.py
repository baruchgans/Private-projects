import json
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)


# Function to load neighborhoods data from json file
def get_neighborhoods_from_db():
    with open("neighborhoods_data.json", "r") as file:
        neighborhoods = json.load(file)
    return neighborhoods


# API endpoint for getting filtered and sorted neighborhoods
@app.route("/neighborhoods", methods=["POST"])
def get_neighborhoods():
    # Get filters and sort criteria from the request body
    filters = request.get_json().get("filters", [])
    sort_by = request.get_json().get("sort_by", None)

    # Get all neighborhoods from the file
    result = get_neighborhoods_from_db()

    # Apply filters to the neighborhoods list
    for f in filters:
        param = f.get("param")
        operator = f.get("operator")
        value = f.get("value")
        result = [n for n in result if operator_mapping[operator](n.get(param), value)]

    # Sort the neighborhoods list if sort_by criteria is provided
    if sort_by:
        result = sorted(result, key=lambda x: x.get(sort_by), reverse=True)

    # Return the filtered and sorted neighborhoods
    return {"neighborhoods": result}


# Functions for different operators
def gte(a, b):
    return a >= b


def lte(a, b):
    return a <= b


def eq(a, b):
    return a == b


# Mapping of operator names to functions
operator_mapping = {
    "gte": gte,
    "lte": lte,
    "eq": eq
}

if __name__ == "__main__":
    app.run(debug=True)
