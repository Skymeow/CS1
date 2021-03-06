# Copy your Animal class here and modify it to automatically count population
# Hint: Modify the initializer method to count the number of animals created
class Animal(object):
    population = 0
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
        # self.population = population
        Animal.population += 1

    def populationCount(cls):
        return cls.population

    populationCount = classmethod(populationCount)

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print(self.name+" eats "+food)
        if food == self.favoriteFood:
            print("YUM! "+self.name+" wants more "+food)
        else:
            return
# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
       super().__init__(name, "meat")
        # self.name = name
        # self.favoriteFood = "meat"

# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        super().__init__(name, "fish")


    def sleep(self):
        print(self.name + " hibernates for 4 months")


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        super().__init__(name, "marshmallows")



    def sleep(self):
        print(self.name + " sleeps in a cloud")



# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        super().__init__(name, "leaves")

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "leaves":
            print("YUM! "+self.name+" wants more "+"leaves")
        else:
            print("YUCK! "+self.name+" spits out "+food)

# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        super().__init__(name, "pollen")

    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "pollen":
            print("YUM! "+self.name+" wants more "+"pollen")
        else:
            print("YUCK! "+self.name+" spits out "+food)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name


    def feedAnimals(self, animals, food):
          print(self.name +" is feeding " + food + " to "+ str(len(animals))+" of "+str(Animal.populationCount())+ " total animals")
          for i in animals:
            i.eat(food)
            i.sleep()

# Copy your Zookeeper class here and modify its feedAnimals method to show
# the total number of animals using the Animal.populationCount class method




# Copy your Animal class here
class Animal(object):
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print(self.name+" eats "+food)
        if food == self.favoriteFood:
            print("YUM! "+self.name+" wants more "+food)
        else:
            return
# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"

    def sleep(self):
        print(self.name + " hibernates for 4 months")


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "marshmallows"


    def sleep(self):
        print(self.name + " sleeps in a cloud")



# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "leaves"

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "leaves":
            print("YUM! "+self.name+" wants more "+"leaves")
        else:
            print("YUCK! "+self.name+" spits out "+food)

# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "pollen"
    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "pollen":
            print("YUM! "+self.name+" wants more "+"pollen")
        else:
            print("YUCK! "+self.name+" spits out "+food)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name


    def feedAnimals(self, animals, food):
          print(self.name +" is feeding " + food + " to "+ str(len(animals)) + " animals ")
          for i in animals:
            i.eat(food)
            i.sleep()




# Copy your Animal class here
class Animal(object):
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print(self.name+" eats "+food)
        if food == self.favoriteFood:
            print("YUM! "+self.name+" wants more "+food)
        else:
            return
# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"

    def sleep(self):
        print(self.name + " hibernates for 4 months")


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "marshmallows"


    def sleep(self):
        print(self.name + " sleeps in a cloud")



# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "leaves"

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "leaves":
            print("YUM! "+self.name+" wants more "+"leaves")
        else:
            print("YUCK! "+self.name+" spits out "+food)

# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "pollen"
    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name+" eats "+food)
        if food == "pollen":
            print("YUM! "+self.name+" wants more "+"pollen")
        else:
            print("YUCK! "+self.name+" spits out "+food)
