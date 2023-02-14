'''
# Example: push, pop, isEmpty
class Stack():
    def __init__(self): # constructor
        self.items = []
    def push(self, x):
        self.items.append(x) # the sky is the limit
    def pop(self):
        x = self.items[-1] # what happens if it is empty?
        del self.items[-1]
        return x
    def isEmpty(self):
        return len(self.items) == 0 # Boolean result

if __name__=="__main__":
    x=Stack()
    x.push("holi")
    x.push(2)
    print(x.items)
    x.pop()
    print(x.items)


# Exc0: SquareManager

import numpy as np

class SquareManager:
    def __init__(self,lenght):
        self.l=lenght

    def side(self):
        x=str(self.l)
        return x

    def perimeter(self):
        return self.l*4
    
    def area(self):
        return self.l^2

    def diagonal(self):
        dia=np.sqrt(2*(self.l**2))
        return dia

if __name__=="__main__":
 sm=SquareManager(3)
 print(f"The area of the square with side {sm.side()} = {sm.area()}")
 print(f"The perimeter of the square with side {sm.side()} = {sm.perimeter()}")
 print(f"The diagonal of the square with side {sm.side()} = {sm.diagonal():.3f}")

#Exc1: Point class
import numpy as np
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,other):
        dist= np.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 )
        return dist
    
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        return self.x,self.y
    
    
    # Optional
	# this built-in method is executed when we ask to print an oject of this class
	# we need to return the string representation of the object
	# as P: (x,y)
	# we can use the repr method to do this
    # if we do, we should delete return from move and it will work in any case

    def __repr__(self):
        return f"P: {self.x}, {self.y}"
    

if __name__=="__main__":
    # create 2 points and calculate distance among them
    a= Point(7,1)
    b= Point(1,1)
    print(a.distance(b))
    # move a point according to a vector (x,y)
    print(a.move(2,2))

# Exc2: Line
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,other):
        dist= np.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 )
        return dist
    
    def move(self,dx,dy):
        self.x += dx
        self.y += dy    

    def __repr__(self):
        return f"P: {self.x}, {self.y}"

class Line:
    def __init__(self,m=0,q=0):
        #Line stored as y=mx+q
        self.m = m
        self.q = q

    def line_from_points(self,pointA,pointB):
        m=(pointB.y-pointA.y)/(pointB.x-pointA.x)
        q=-((pointB.y-pointA.y)/(pointB.x-pointA.x))*pointA.x+pointA.y
        return Line(m,q)

    def distance(self,point):
        dist = (abs(point.y-(self.m*point.x+self.q))/np.sqrt(1+self.m**2))
        return dist

    def intersection(self,other):
        # intersection(otherLine)
        if self.m==other.m:
            print('The lines are parallel')
            return None
        else:
            x=(other.q-self.q)/(self.m-other.m)
            y=self.m*((other.q-self.q)/(self.m-other.m))+self.q
            return Point(x,y)
	# Optional
	# this method is executed when we ask to print an object of this class
	# we need to return the string representation of the object
	# as l : y=mx+q
    def __repr__(self):
        return f"l: y = {self.m}x + {self.q}"

if __name__=="__main__":
    # 1 Simple creation
    l1 = Line(m=3,q=2)
    print(l1)

    #2 Create line from 2 points
    a=Point(0,1)
    b=Point(2,2)
    l2=Line().line_from_points(a,b)
    print(l2)

    #3 Function for distance from point 
    # and intersection with another line
    l=Line(m=1,q=0)
    a=Point(1,5)
    print(l.distance(a)) 
    m=Line(-1,0)
    i=l.intersection(m)
    print(i)

# Exc3: deck
import random

suits = ["Heart", "Diamond", "Club", "Spades"]
values =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Card:
    #  Each a card has a suit and a value defined when it's created
    def __init__(self,suits,value):
        self.suits = suits
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suits}"

class Deck:
    """
    The deck is composed by 13 cards for each of the 4 suits. 
    It also has:
        a shuffle() method that returns the shffled deck
        a draw(n) method that returns a list of n cards """
    
    def __init__(self):
        self.cards=[ Card(s,v) for s in suits for v in values]

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)
    
    def draw(self,n=1):
        """Returns n cards, 1 if n is not specified"""
        # we check if n is lower than the number of cards in the deck
        # if it is, we return the n cards
        if n<=len(self.cards):            
            drawn=[]
            for i in range(n):
                drawn.append(self.cards.pop())
            return drawn
        # if n is greater than the number of cards in the deck, we return all the cards
        elif n>len(self.cards) and len(self.cards)>0:
            # we can do this in two ways:
            #1
            # we return the remaining cards that will be equal to the number of cards
            # remaining in the deck ( len(cards))
            drawn=[]
            for i in range(len(self.cards)):
                drawn.append(self.cards.pop())
            return drawn
            #2
            # we could obtain the same result by calling the draw() method again
            # with the number of cards remaining in the deck
            # return self.draw(len(self.cards))
        else:
            return None

    def __repr__(self):
        return f"{self.cards}"

if __name__=="__main__":
    deck= Deck()
    print(f"Initial deck: {deck}")
    
    deck.shuffle()
    print(deck)
    con= 0
    while con != "q":
        con = input("Inser number of cards to get or 'q' to quit: ")
        if con != "q":
            print(f"This were the cards drawed: {deck.draw(int(con))}")
            print(f"This are the remain cards in the desk: {deck}")
        else:
            pass


#Exc.4 y Exc.5: JSON
import json

class Contact():
	"""Contact defined by his name surname and emal"""
	def __init__(self,name,surname,mail):
		self.name=name
		self.surname=surname
		self.mail=mail
	def __repr__(self):
		return "{},{},{}".format(self.name,self.surname,self.mail)

class AddressBook():

    """
    Collection of object of the class Contact
    The available methods are:

	show():shows the list of contacts
	find_by_name():returns all the contact with that name
	find_by_surname():returns all the contact with that surname
	add_contact(name,surname,email):adds the contact to the book
	remove_contact(name): remove all the contacts with the given name
	save():saves the book
    """

    def __init__(self,fileName):
        self.contacts = json.load(open(fileName,'r'))
        self.fileName=fileName

    def show(self):
        for contact in self.contacts["contacts"]:
            print(contact)
    
    def add_contact(self, name, surname, mail):
        """
        add_contact(name,surname,email): adds the contact to the book
        """
        self.contacts["contacts"].append({"name": name, "surname": surname, "mail": mail})

    def find(self,surname):
        """find(surname):returns all the contact with that surname"""
        results=[contact for contact in self.contacts["contacts"] if contact["surname"]==surname]
        print("I found the following results:\n")
        for x in results:
            print(x)
    
    def remove_contact(self, name):
        """remove_contact(name): remove all the contacts with the given name"""
        for contact in self.contacts["contacts"][:]:
            if contact["name"] == name:
                self.contacts["contacts"].remove(contact)
    
    def save(self):
        """save():saves the book"""
        json.dump(self.contacts,open(self.fileName,'w',1), indent=2)
    
    def update_contact(self,name,surname):
        """update_contact(name,surname): find the contact with given name and surname and allows edit of the email"""
        updated=False
        i=0
        while not updated:
            print(self.contacts["contacts"][i]["name"])
            if self.contacts["contacts"][i]["name"]==name and self.contacts["contacts"][i]["surname"]==surname:
                self.contacts["contacts"][i]["email"]=input(f"Insert the new mail of {name} {surname}: ")
                updated=True
            i+=1
    

if __name__=="__main__":
    
    book=AddressBook("contacts.json") #create an object of the class
    print('Welcome to the application to manage your contacts')
    c=''
    helpMessage="Press 's' tho show the list of contacts\nPress 'n' to add a contact\nPress 'u' to update a contact\nPress 'f' to find a contact\nPress 'd' to delete a contact\nPress 'q'to save end exit"
	
    while True:
        print(helpMessage)
        command=input()
        if command=='s':
            book.show()
        elif command=='n':
            name=input('Write the name of the contact : ')
            surname=input('Write the surname of the contact : ')
            mail=input('Write the mail of the contact : ')
            book.add_contact(name,surname,mail)
            print('Contact Added')
        elif command=='d':
            name=input('Write the name of the contact you want to delete : ')
            book.remove_contact(name)
        elif command=='f':
            surname=input('Write the surname of the contact : ')
            book.find(surname)
        elif command=='u':
            name=input('Write the name of the contact : ')
            surname=input('Write the surname of the contact : ')
            book.update_contact(name,surname)
        elif command=='q':
            book.save()
            break
        else:
            print('Command not available')

#Exc.6: NBA
import json

class NBAStats():
	def __init__(self,filename):
		self.filename = filename
		self.file_content = json.load(open(filename,'r',encoding='utf-8'))
	def get_players(self):
		return self.file_content['players']

	def average_heigth(self):
		players = self.get_players()
		heigths = [p['hgt']/39.37 for p in players]
		return sum(heigths)/len(heigths)

	def average_weigth(self):
		players = self.get_players()
		weigths = [p['weight']/2.205 for p in players]
		return sum(weigths)/len(weigths)

	def average_ratings(self):
		players = self.get_players()
		num_players = len(players)
		avg_ratings = dict.fromkeys(players[0]['ratings'][0],0)
		for player in players:
			player_ratings=player[ 'ratings'][0]
			for key in player_ratings.keys():
				avg_ratings[key]+=player_ratings[key]/num_players
		return avg_ratings
				
	def average_age(self):
		players = self.get_players()
		ages = [2020-p['born']['year'] for p in players]
		return sum(ages)/len(ages)

if __name__=="__main__":
	nba=NBAStats('playerNba.json')
	print(nba.average_heigth())
	print(nba.average_weigth())
	print(nba.average_ratings())
	print(nba.average_age())

# Exc 7: parents and child classes

# As exercise on polymorpishm and inheritance you can create the
# parent-class "Circle"and the child-class "Cylinder". The Circle
# class must have the methods to calculate area and perimeter while
# the Cylinder class must have the method to calculate area and
# volume

import numpy as np

class Circle(object):
	"""Create a circle knowing his radius"""
	def __init__(self, radius):
		self.radius=radius
	def perimeter(self):
		"""Returns the perimeter of the circle"""
		return (2*np.pi*self.radius)
	def area(self):
		"""Returns the area of the circle"""
		return (np.pi*self.radius**2)

class Cylinder(Circle):
	""""Create a cylinder knowing his radius and his height"""
	def __init__(self, radius,height):
		Circle.__init__(self,radius)
		self.height=height
	def area(self):
		"""Returns the area of the cylinder"""
		return (self.perimeter()*self.height+2*Circle(self.radius).area())
	def volume(self):
		"""Returns the volume of the cylinder"""
		return (Circle(self.radius).area()*self.height)

if __name__ == '__main__':
	a=Circle(3)
	print(a.perimeter())
	print(a.area())
	b=Cylinder(3,8)
	print(b.area())
	print(b.volume())
'''

# Exc 9: encapsulation

# the name can't be changed after the creation of the object, but it
# can be retrieved
# the speed can be set to any value less than 250 (if greater it will
# be changed to 250) and can be retrieved
# the gear can go from 1 to 6 and can be changed only up and
# down by one (it's set to 1 when the object is created) and can be
# retrieved

class Car():
    maxGear=6
    minGear=1
    maxSpeed=250
    minSpeed=0
    def __init__(self, name):
        self.__name = name
        self.__gear =1
        self.__speed=0
    
    def getName(self):
        return self.__name
    
    def getSpeed(self):
        return self.__speed

    def getGear(self):
        return self.__gear

    def setSpeed(self,newSpeed):
        self.__speed=min([Car.maxSpeed,max([newSpeed,Car.minSpeed])])
        return self.getSpeed()

    def increaseGear(self):
        self.__gear=min([Car.maxGear,max([Car.minGear,self.__gear+1])])
        return self.getGear()

    def decreaseGear(self):
        self.__gear=min([Car.maxGear,max([Car.minGear,self.__gear-1])])
        return self.getGear()

if __name__=="__main__":
    c=Car("Panda")
    print(f"Car name: {c.getName()}")
    print(f"Initial speed: {c.getSpeed()}")
    print(f"Initial gear: {c.getGear()}")
    
    c.setSpeed(100)
    print(f"Speed :{c.getSpeed()}")

    c.increaseGear()
    print(f"Gear: {c.getGear()}")
    c.decreaseGear()
    print(f"Gear: {c.getGear()}")

    #trying to go over limits
    #gear
    for i in range(10):
        c.increaseGear()
    print(f"Gear: {c.getGear()}")

    #speed
    c.setSpeed(300)
    print(f"Speed :{c.getSpeed()}")
