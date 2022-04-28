import json
import flask  
from flask import request, jsonify
from Animal import *
from Customer import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

customerList = []
petsList = []

reader = open("owners.json", "r")
PetOwners = json.load(reader)
reader.close()

for owner in PetOwners:
    id = owner.get("customerID")
    name = owner.get("name")
    age = owner.get("age")
    pets = owner.get("petIDs")
    obj = Customer(id,name,age,pets)
    customerList.append(obj)

reader = open("pets.json", "r")
Pets = json.load(reader)
reader.close()

for pet in Pets:
    petID = pet.get("petID")
    name = pet.get("name")
    type = pet.get("type")
    age = pet.get("age")
    ownerID = pet.get("ownerID")

    if type == "Cat":
        obj = Cat(petID,name,age,ownerID)
    elif type == "Dog":
        obj = Dog(petID,name,age,ownerID)
    elif type == "Budgie":
        obj = Budgie(petID,name,age,ownerID)
    elif type == "Goldfish":
        obj = Goldfish(petID,name,age,ownerID)    
    elif type == "Snail":
        obj = Snail(petID,name,age,ownerID)
    else:
        print("The vet doesn't treat that animal type.")

    petsList.append(obj)

@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to the Virtual vet program.</h1><p>Choose from the options below!.</p><a href='/api/pets')>View all of our pets here</a><p></p><a href='/api/customers')>View all of our customers here</a><p></p><a href='/api/pets/show_owner')>Search for a specific pet's owner by ID here</a>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/customers', methods=['GET'])
def all_customers():
    return jsonify(PetOwners)

@app.route('/api/pets', methods=['GET'])
def get_pets():
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return jsonify(Pets)

    results = []

    for pet in Pets:
        if pet['petID'] == id:
            results.append(pet)

    return jsonify(results)


@app.route('/api/customers', methods=['GET'])
def get_owner_by_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Customer is not in database."

    results = []

    for owner in PetOwners:
        if owner['customerID'] == id:
            results.append(owner)

    return jsonify(results)

@app.route('/api/pets', methods=['GET'])
def get_pet_by_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Pet is not in database."

    results = []

    for pet in Pets:
        if pet['petID'] == id:
            results.append(pet)

    return jsonify(results)

@app.route('/api/pets/show_owner', methods=['GET'])
def get_pets_by_customer():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Add a pet ID to the URL to search for their owner e.g. ?id=0"

    results = []
    if id < len(petsList) and id >= 0:
        for pet in petsList:
            if pet.id == id:
                check = pet.owner
                for owner in customerList:
                    if owner.id == check:
                        return "The owner of " + pet.name + ", the " + str(pet.age) +" year old "+ pet.value.lower() + ", is " + owner.name
    
        return jsonify(results)
    else:
        return "Use a valid ID number"

app.run()