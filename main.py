import turtle
import time


WIDTH, HEIGHT = 500, 500 #constant values are denoted in caps because theyll never change

def get_number_of_turtles(): #get the number of turtles. 
    turtles = 0 
    while True: #this is meant to allow the user to keep inputing a valid number
        turtles = input("Enter the number of turtles to race (2 - 5):  ") #prompts the user to input a number between 2 and 10
        if turtles.isdigit(): #if the string is numeric
            turtles = int(turtles) 
        else:
            print("Input must be a number.") #this check gives this error if the number is not an integer
            continue #this brings us back to the beginning of the while loop

        if 2 <= turtles <=5: #if the digit is less than 2 or more than 5: Initially I had 10, but who is creating 10 racinf turtles surely?
            return turtles
        else:
            print("You input is not in the 2-5 range.") #we print this error message. 

def __init__turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title = ("Turtle Race")

turtles = get_number_of_turtles()
__init__turtle()

turtle1 = turtle.Turtle() #here we're making the turtles and moving them. 

turtle1.speed(1)
turtle1.penup()
turtle1.shape("turtle") #for turtle shape you can use turtle, circle and arrow.  
turtle1.color("red")
turtle1.forward(100)
turtle1.left(90)
turtle1.pendown()
turtle1.forward(100)
turtle1.left(90)
turtle1.backward(100)            
#time.sleep(10) #this will pause the program for 10 secs it doesn't immediately close the turtle window. 

turtle2 = turtle.Turtle()

turtle2.speed(0)
turtle2.penup()
turtle2.shape("turtle") 
turtle2.color("cyan")
turtle2.forward(150)
turtle2.left(90)
turtle2.pendown()
turtle2.forward(100)
turtle2.left(90)
turtle2.backward(150)            
#time.sleep(10)

turtle3 = turtle.Turtle()
turtle3.speed(3)
turtle3.penup()
turtle3.shape("turtle") 
turtle3.color("yellow")
turtle3.forward(120)
turtle3.left(90)
turtle3.pendown()
turtle3.forward(100)
turtle3.left(90)
turtle3.backward(150)            
#time.sleep(10)

turtle4 = turtle.Turtle()
turtle4.speed(6)
turtle4.penup()
turtle4.shape("turtle")  
turtle4.color("purple")
turtle4.forward(100)
turtle4.left(90)
turtle4.pendown()
turtle4.forward(100)
turtle4.left(90)
turtle4.backward(130)            
#time.sleep(10)

turtle5 = turtle.Turtle()
turtle5.speed(10)
turtle5.penup()
turtle5.shape("pink") 
turtle5.color("red")
turtle5.forward(170)
turtle5.left(90)
turtle5.pendown()
turtle5.forward(100)
turtle5.left(90)
turtle5.backward(100)            
#time.sleep(10)



#turtle speeds according to google. fastest-0, fast-10, normal-6, slow-3, slowest-1
# the turtle is now the arrow pointer on the window.
#11:05 pm Im only getting one turtle on the screen instead of 5. 11/20/2026
#11:12 pm I commented the sleep. So the turtles work. one of them is also too fast I need to slow down the speeds.





   # cd "C:\Users\USER\Desktop\my projects\Turtle racing"
# python main.py