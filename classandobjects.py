# Superclass

class Animal():
    # Constructor

    def __init__(self):
        self.age= None
        self.species= None
        self.fur= None

    # Methods

    def eat(self):
        print("The animal is eating")

    def breed(self):
        print("The animal is breeding")

# Subclass        

class Dog(Animal):
    # Constructor
    
    def __init__(self,color,race,name):
        super().__init__()
        self.size= None
        self.age=0
        self.color= color
        self.race= race
        self.name= name

    # Methods

    def bark(self):
        print("{} is barking".format(self.name))

    def check_hunger(self,hunger):
        if hunger:
            self.eat()
        else:
            print("{} is not hungry".format(self.name))



    def play(self):
        print("{} is playing".format(self.name))

    #setter/getter

    def change_name(self, name):
        self.name= name
        print("The dog is calle {}".format(self.name))

    def set_age(self, age):
        self.age=age
        print("{} is {} years old".format(self.name,self.age))
    
    def birthday(self):
        self.age +=1
        print("{} is {} years old".format(self.name,self.age))



# Instantiate an object

my_dog= Dog("White","Pitbull","Simon")
print(my_dog.name)
my_dog.eat()
my_dog.birthday()
my_dog.check_hunger(True)

my_dog2= Dog("Brown","BullTerrier","Jack")
print(my_dog2.name)
my_dog2.play()
my_dog2.set_age(5)
my_dog2.check_hunger(False)



    
        