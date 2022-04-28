import json
import flask  
from flask import request, jsonify
from Animal import *
from Customer import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Customers = []
Pets = []

reader = open("owners.json", "r")
PetOwners = json.load(reader)
reader.close()

def toString(itemList):
    if len(itemList) == 1:
        return itemList[0].name
    else:
        string = []
        for item in itemList:
            string.append(item.name)
        return string

for owner in PetOwners:
    id = owner.get("customerID")
    name = owner.get("name")
    age = owner.get("age")
    pets = owner.get("petIDs")
    obj = Customer(id,name,age,pets)
    Customers.append(obj)
    result = toString(Customers)

print(result)


reader = open("pets.json", "r")
Pets = json.load(reader)
reader.close()

@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to the Virtual vet program.</h1><p>Search for details about animals and customers.</p>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/customers/all', methods=['GET'])
def all_customers():
    return jsonify(PetOwners)

@app.route('/api/pets/all', methods=['GET'])
def all_pets():
    return jsonify(Pets)

@app.route('/api/customers', methods=['GET'])
def get_owner_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Customer is not in database."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for owner in PetOwners:
        if owner['customerID'] == id:
            results.append(owner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/pets', methods=['GET'])
def get_pet_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Pet is not in database."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for pet in Pets:
        if pet['petID'] == id:
            results.append(pet)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/customer/pets', methods=['GET'])
def get_pets_by_customer():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Pet is not in database."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for pet in Pets:
        if pet['ownerID'] == id:
            results.append(pet)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()