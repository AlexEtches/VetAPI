class Customer:

    customerID = None
    age = None
    name = None
    age = None
    pets = []

    def __init__(self,id,name,age,pets):
        self.customerID = id
        self.name = name
        self.age = age
        self.pets = pets

    def getCustomerId(self):
        return self.customerID
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPetList(self):
        return self.pets

    
