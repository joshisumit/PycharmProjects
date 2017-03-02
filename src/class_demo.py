class Pet:
    def __init__(self,name,species): # commented constructor
       self.name=name
       self.species=species
    # def setName(self,name):
    #     self.name=name
    # def setSpecies(self,species):
    #     self.species=species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def __str__(self): # What to display when printing the instances of Object
        return "%s is a %s"%(self.name,self.species)

class Dog(Pet):
    def __init__(self,name,chase_cats):
        Pet.__init__(self,name,"Dog")
        self.chase_cats=chase_cats
    def chaseCats(self):
        return self.chase_cats

class Cat(Pet):
    def __init__(self,name,hates_dogs):
        Pet.__init__(self,name,"Cat")
        self.hates_dogs=hates_dogs
    def hateDogs(self):
        return self.hates_dogs
