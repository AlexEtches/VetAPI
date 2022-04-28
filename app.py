import json
from operator import contains
from flask import Flask, request, jsonify
from Animal import *
from Customer import *

app = Flask(__name__)
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
        print("ERROR: The vet isn't able to treat a " + type )

    petsList.append(obj)

@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    output = "<h1>Welcome to the Virtual vet program.</h1>"
    output += "<p>Choose from the options below!<br>On each page, view a specific record by ID e.g. add ?id=0 to the URL</p>"
    output += "<a href='/api/pets')>View all of our pets here</a><br>"
    output += "<a href='/api/customers')>View all of our customers here</a><br>"
    output += "<a href='/api/pets/show_owner')>Search for a specific pet's owner by pet ID here</a><br>"
    output += "<a href='/api/customers/show_pets')>Search for a specific owner's pets by customer ID here</a><br>"

    return output

# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/customers', methods=['GET'])
def get_customers():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return (jsonify(PetOwners))

    results = []

    if id < len(customerList) and id >= 0:
        for owner in PetOwners:
            if owner['customerID'] == id:
                results.append(owner)
        return jsonify(results)
    else:
        "ERROR: Use a valid ID number"


@app.route('/api/pets', methods=['GET'])
def get_pets():
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return jsonify(Pets)

    results = []

    if id < len(petsList) and id >= 0:
        for pet in Pets:
            if pet['petID'] == id:
                results.append(pet)
        return jsonify(results)
    else:
        return "ERROR: Use a valid ID number"

@app.route('/api/customers/show_pets', methods=['GET'])
def get_pets_by_customer():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Add a customer ID to the URL to search for their pets e.g. ?id=0"

    if id < len(customerList) and id >= 0:
        for owner in customerList:
            if owner.id == id:
                petIDList = owner.pets
                output = owner.name + " has " + str(len(petIDList)) + " pet(s). "
                for pet in petsList:
                    for petID in petIDList:
                        if petID == pet.id:
                            output += str(pet.name + ",")
                            if output[-1]==',':
                                result = output[:-1] 
                            else:
                                output
                return result
    else:
        return "ERROR: Use a valid ID number"

@app.route('/api/pets/show_owner', methods=['GET'])
def get_owner_by_pet():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Add a pet ID to the URL to search for their owner e.g. ?id=0"

    if id < len(petsList) and id >= 0:
        for pet in petsList:
            if pet.id == id:
                check = pet.owner
                for owner in customerList:
                    if owner.id == check:
                        return "The owner of " + pet.name + ", the " + str(pet.age) +" year old "+ pet.value.lower() + ", is " + owner.name
    else:
        return "ERROR: Use a valid ID number"
        
if __name__ == '__main__': 
    app.run()