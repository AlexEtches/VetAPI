from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    id = None
    age = None
    name = None
    colour = None
    isAlive = True
    owner = None

    #Constructors
    def __init__(self, id, name, age, owner):
        self.value = "Animal"
        self.id = id
        self.name = name
        self.age = age
        self.owner = owner


    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    def sleep(self):
        return("I am sleeping")

    def die(self):
        self.isAlive = False
        return

    def type(self):
        return(self.value)

class Mammal(Animal):
    #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Mammal"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    def movement(self):
        return("I walk on land")

    def breathe(self):
        return("I breathe in air")

    def reproduce(self):
        return("I give birth")

    def type(self):
        return(self.value)

class Bird(Animal):
    #Attributes
    wingspan = None

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Bird"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    def breathe(self):
        return("I breathe in air")

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Fish(Animal):
    #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Fish"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    def movement(self):
        return("I swim in water")

    def breathe(self):
        return("I breathe underwater")

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Mollusk(Animal):
    #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Mollusk"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def movement(self):
        pass
    
    @abstractmethod
    def breathe(self):
        pass

    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)


class Cat(Mammal):
     #Attributes


    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Cat"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return("I eat mice")

class Dog(Mammal):
     #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Dog"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return("I eat dog food")

class Budgie(Bird):
     #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Budgie"

    #Methods
    def type(self):
        return(self.value)

    def movement(self):
        return("I can fly")    

    def eat(self):
        return("I eat grains")

class Goldfish(Fish):
    #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Goldfish"

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return("I eat algae")

class Snail(Mollusk):
    #Attributes

    #Constructors
    def __init__(self,id,name,age,owner):
        super().__init__(id,name,age,owner)
        self.value = "Snail"

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return("I eat organic matter")

    def movement(self):
        return("I move on land")

    def breathe(self):
        return("I breathe air")