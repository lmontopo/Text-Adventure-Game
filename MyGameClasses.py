from sys import exit
from random import randint

x = 0 
y = 0 
s = 0

# Here I define arrays of acceptable user inputs

call_out = ["call", "calling", "yell"]
walking = ["continue", "walking", "walk"]
run = ["run", "running", "away"]
ask = ["ask", "asking"]
dig = ["dig", "digging", "hole"]
would_not = ["wouldn't", "not", "don't"]

possibilities = [call_out, walking, run, ask, dig, would_not]

# This is an array for the jelly beans 
jelly = ['green', 'orange', 'red', 'black']


# Here are two global functions which are called in some classes:

def get_direction():
	global x 
	global y
	
	direction = raw_input('> ').lower()
	if direction == "east":
		x += 1 
	elif direction == "west":
		x -= 1
	elif direction == "north":
		y += 1
	elif direction == "south":
		y -= 1
	else:
		print "I don't recognize that."
		print "Please type in 'east', 'west', north', or 'south'."
		return get_direction()
	return x,y


def get_action():
	action = raw_input("> ").lower()
	action = action.split()

	for act in action:
		if act in possibilities[5]:
			print "Please don't tell me what you WOULDN'T do."
			print "Just tell me what you WOULD do."
			return get_action()

		if act in call_out:
			return "call"
		if act in walking:
			return "walk"
		if act in run:
			return "run"
		if act in ask:
			return "ask"
		if act in dig: 
			return "dig"
	print "That was not an option.  Lets assume you keep walking."
	return "walk"
		

def  call_or_walk(action):
	if action in call_out:
		print "After calling out 'hello! is anybody here?' you get a jiberish response."
		return insane_man.enter()
	elif (action in walking):
		return a_map.enter()
	else:
		print "Sorry, I don't recognize that as an option."
		print "Lets assume you continue walking."
		return a_map.enter()



# Here are all the different "scenes" that one can encounter in the game:

class Death(object):
	
	def enter(self):
		print "You Died."
		exit(1)

class Death_Other(object):
	
	
	#here we have an array, which can be indexed.  dicts can't be?!!
	ways_to_die = [
		"You walked over a landmine and die.  Game Over.",
		"You become dehydrated and die. Game Over.",
		"You die from a random heart attack.  Game Over."
		]
	
	def enter(self):
		print Death_Other.ways_to_die[randint(0, len(self.ways_to_die)-1)]
		exit(1)


class Lost(object):
	
	def enter(self):
		print "You have been walking in a forest for a few hours."
		print "You realize now that you are completely lost and dont' know"
		print "how to get home.  You are scared because it will soon be getting dark."
		print "You can call out for help or continue walking." 
		print "What do you do?"  
		
		action = get_action()
		
		return call_or_walk(action)

class InsaneMan(object):

	def __init__(self):
		self.a = 0

	def enter(self):
		self.a += 1
		print self.a
		if self.a == 1:
			print "A man appears, walking towards you."
			print "His shirt is torn, his hair is ratty and he is saying nonsense words." 
		else:
			print "You see the same insane man as before."
			print "Again, he is saying nonsense words." 
		
		print "Do you run away or ask for help?" 
		
		action = get_action()
		
		if (action in run):
			return a_map.enter()
		elif ((action not in ask) and (action not in run)):
			return a_map.enter()
		else:
			print "The man takes your hand in his and leads you through the forest..."
			return shovel.enter()
					

class Shovel(object):

	def __init__(self):
		self.a = 0 
		

	def enter(self):
		global s
		s += 1
		self.a += 1 
		
		if (s > 1 and self.a == 1): 
			print "You find another shovel beside another half dug hole."
			print "It seems there are more than one around here."
		elif (s == 1 and self.a ==1):
			print "You find a shovel leaning against a tree."
			print "Beside it is a hole that is half dug." 
		elif (s > 1 and self.a > 1): 
			print "You are back at the same shovel and half dug hole as before."
		
		print "Do you start digging the hole, or do you continue walking in hopes" 
		print "of finding your way home?"
		
		action = get_action()
		
		if action in dig:
			print "You find a bag of jelly beans in the hole.  There are 4 of them."
			print "A green one, an orange one, a red one and a black one."
			print "Which kind of jelly bean do you eat?"
			
			action = raw_input('> ').lower()
		
			if action == jelly[3]:
				print "Nice! After eating the jelly bean a giant beanstock growns,"
				print "right next to you!"
				return beanstalk.enter()
			else:
				print "uh oh! That one was poisonous!"
				return death.enter()
		
		else:
			return a_map.enter()
				
						
class CellPhone(object):
	
	def enter(self):
		print "You find a cellphone on the ground."
		print "Do you pick it up and try to call home?"


		while True:	
			decide = raw_input('> ').lower()		

			if decide == "no": 
				print "Would you like to continue walking or call for help?"
				action = get_action()
				return call_or_walk(action)
					
			elif decide == "yes":
				print "You pick it up and try to call home." 
				print "It explodes in your ear!"
				return death.enter()
			else:
				print "Please just type 'yes' or 'no'."
	

class Beanstalk(object):

	def enter(self):
		print "You climb to the top of the beanstalk."
		print "From there you have a great view!"
		print "You can see where the park ends, and you now know how to get home!"
		print "You now climb down and successfully find your way home."
		print "WELL DONE! YOU WIN!"
		exit(0)


class Nothing(object):
	
	def enter(self):
			print "You walk around for a while, but you see nothing."
			print "You are getting very tired."
			print "Do you keep walking or call for help?"
			action = get_action()
			return call_or_walk(action)			


class Home(object):

	def enter(self):
		print "You arrive home safe and sound.  You win!"
		exit(0)
		
class Note(object):

	def __init__(self):
		self.a = 0 

	def enter(self):
		self.a += 1
		if self.a < 2:
			print "You find a note that reads: 'black magic is good'."
		else:
			print "You are back at the same spot where you found the note."
		print "Would you like to keep walking or call for help?"
		action = get_action()
		
		if action in call_out:
			"After calling out 'hello! is anybody here?' you get a jiberish response."
			return insane_man.enter()
		elif (action in walking):
			return a_map.enter()

insane_man = InsaneMan()
shovel1 = Shovel()	
shovel2 = Shovel()
shovel3 = Shovel()	
note = Note()

class Map(object):

	places = {
			 (0,0) : Lost(),
			 (1,0): note,
			 (2,0): Nothing(),
			 (3,0): Death_Other(),
			 (-1,0): Nothing(),
			 (-2,0): Nothing(),
			 (-3,0): Home(),
			 (0, -1): CellPhone(),
			 (0,-2): Nothing(),
			 (0,-3): Death_Other(),
			 (0,1): shovel2,
			 (0,2): Nothing(),
			 (1,1): shovel1,
			 (1,2): Nothing(),
			 (-1,1): shovel3,
			 (-1,2): Nothing(),
			 (-2,1): insane_man,
			 (2,1): insane_man,
			 (0,3): Nothing(),
			 (-1,-1): Nothing(),
			 (-2,-1): CellPhone(),
			 (-1,-2): Nothing(),
			 (1,-1): Nothing(),
			 (2,-1): Nothing(),
			 (1,-2): Nothing()		 
	}

	def next_scene(self):
		global x 
		global y 
		if abs(x)+ abs(y) < 4:
			next = a_map.places.get((x,y))
			return next.enter()
		else:
			return Death_Other().enter()
			
	def enter(self):
		global x 
		global y 
		
		print "which direction would you like to go?"
		get_direction()
		return a_map.next_scene()
		
	
# Here we create instances for all of the "scenes"		
cell_phone = CellPhone()
beanstalk = Beanstalk()		
death = Death_Other()
keep_walking = Nothing()
lost = Lost() 
a_map = Map()
home = Home()

if __name__ == "__main__":	
	lost.enter()