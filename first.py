#!/bin/python3

#STRINGS
#print String
print("Hello,World!")
print("This string is "+"AWESOME") #We can also concatenate
print('\n')#new line
print('Test that new line out!!')


#MATH
print(50 + 50) #ADD
print(100 - 40) #SUBTRACT
print(50 * 50) #MULTIPLY
print( 100 / 2) #DIVIDE
print(7 ** 2) #EXPONENTS
print(50 + 50- 50 * 50 / 50) #PEMDAS
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with remainder (or a float)
print( 50 // 6) #no remainder
print('\n') #new line


#VARIABLES AND METHODS
quote = "Lara is a little girl" #quote is a VARIABLE
print(quote.upper()) #METHOD1 uppercase
print(quote.lower()) #METHOD2lowercase
print(quote.title()) #METHOD3 titlecase
print(len(quote)) #COUNT NO. OF CHARACTERS

name = "HANA" #STRING
age = 18 #AGE
GPA = 373 #float
print(int(age)) #NO DECIMALS
print(int(30.1))
print(int(30.9)) #WILL IT ROUND? NO
print("My name is " + name + " and i am " + str(age) + " years old.")
#CONCATENATING VARIABLES
age += 1 
print(age) #VARIABLE(AGE) IS +1 and VARIABLES CAN CHANGE
birthday = 1
age += birthday
print(age) #variable is +1
print('\n')


#FUNCTIONS
def who_am_i(): #this is a function without parameters
       name = "Hana" #local variable
       age = 18
       print("My name is " + name + " and i am " + str(age) + " years old.")
who_am_i()
def add_one_hundred(num):
       print(num + 100)
add_one_hundred(100)
def add(x,y):
       print(x + y)
add(7,7)
def multiply(x,y):
       return x * y
multiply(7,7)
print(multiply(7,7))
def square_root(x):
       print(x ** .5)
square_root(64)
def nl(): #new line
       print('\n')
nl()

# BOOLEAN EXPRESSIONS(VRAI OU FAUX)
bool1 = True #EXPRESSION
bool2 = 3*3 ==9
bool3 = False
bool4 = 3*3 !=9
print(bool1,bool2,bool3,bool4)
print(type(bool1))
bool5 = "True" #a string""
print(type(bool5))
nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than_equal = 5 < 7
geater_than_equal_to = 7 >= 7 
less_than_equal_to = 7 <= 7
test_and = (7>5) and (5<7) #True
test_and2 = (7>5) and (5>7) #False
test_or = (7>5) or (5>7)  #True
test_or2 = (7>5)or (5>7) #True
test_not = not True #False
nl()

#CONDITIONALS IF/ELSE
def drink(money):
         if money>= 2:
           return"You've got yourself a drink!" #RETURN INSTEAD OF PRINT
         else:
           return"No drink for you:("
print(drink(3))
print(drink(1))
def food(beef,chicken):
         if (beef >=5) and (chicken >=5):
             return "So Delicious:)"
         elif(beef <=5) and (chicken <=5):
             return "How Boring!?"
         else: 
             return "I'm Vegeterian"
print(food(7,9))
print(food(4,3))
print(food(5,5))
nl()

#LISTS - Have brackets []
movies = ["The Batman", "Van Helsing", "The Conjuring", "Annabelle"]
print(movies[1]) #RETURNS THE SECOND ITEM
print(movies[0]) #RETURNS THE FIRST ITEM
print(movies[1:3]) #RETURNS THE FIRST INDEX NO. GIVEN UNTIL THE LAST NO. GIVEN, but excluding the last
print(movies[:1])
print(movies[1:])
print(movies[-1]) #returns the last item in the list
print(len(movies)) #count items in the list
movies.append("Jaws")
print(movies) #appends to the END of the list
movies.insert(2,"the Big Short")
print(movies)
movies.pop() #removes the LAST item in the list
print(movies)
movies.pop(0) #removes the FIRST item
print(movies)
Lara_movies = ["Hotel Transylvania", "Moana", "Finding Nemo"]
our_favourite_movies = movies + Lara_movies
print(our_favourite_movies)
grades = [["Bob", 82] , ["Alice",90], ["Jeff", 73]]
Bobs_grade = grades[0][1]
print(Bobs_grade)
grades[0][1] = 83
print(grades)
nl()

#TUPLES - lists that don't change,()
grades = ("a","b","c","d","f")
print(grades[1])



