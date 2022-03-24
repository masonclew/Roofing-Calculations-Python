"""
Mason Clewis     2021-2022
This program is meant to help solar site surveyors calculate how many solar panels will fit on a given roof face.
The program is not perfect
"""
import math

shape=input("What is the shape of the roof face? (triangle, rectangle, trapeziod)")

#this code calculates the area of a triangle

def triangle():
    side_a=float(input("What is the length of one of the sides(ft)"))
    side_b=float(input("What is the length of another one of the sides(ft)"))
    side_c=float(input("What is the length of another one of the sides(ft)"))
    #this calulcates perimeter which is needed for area calculation
    perimeter=float(((side_a + side_b + side_c)*0.5))
    #delete the comment on the following command for help troubleshooting
    #print(perimeter)
    area_squared=(perimeter*(perimeter-side_a)*(perimeter-side_b)*(perimeter-side_c))
    area=(area_squared**0.5)
    area=(round(area,2))
    print("The area is " + str(area) + "square feet")
    return area

#this code will caclulate the panel size

def panelsize():
    panel_length=float(input("What is the length of the panel?(in)"))
    panel_width=float(input("What is the width of the panel?(in)"))
    panel_length = (panel_length*0.08333333333)
    panel_width = (panel_width*0.08333333333)
    panel_area=(panel_length*panel_width)
    panel_area=round(panel_area,2)
    return panel_area
    print("Each panel has an area of " + str(panel_area) + " square feet")
    #this code will calculate how many panels will fit on this face
    
def suggested(x,y):
    suggested_panels = float(x)//float(y)
    return int(suggested_panels)

#this code calculates the area of a trapeziod

def trapeziod():
    height = float(input("What is the height of the trapeziod?(ft)"))
    long_side = float(input("What is the length of the long side?(ft)"))
    short_side = float(input("What is the length of the short side?(ft)"))
    area=((height*(long_side + short_side))*0.5)
    area=(round(area,2))
    return area
    print("The area is " + str(area) + "square feet")
    
#this code calculates the area of a rectangle
    
def rectangle():
    side1= float(input("What is the length of one of the sides?(ft)"))
    side2= float(input("What is the length of one of the sides?(ft)"))
    area=(side1*side2)
    area=(round(area,2))
    print("The area is " + str(area) + "square feet")
    return area

if shape =="triangle":
    print("You can fit " + str(suggested(triangle(),panelsize())) + " panels.")
elif shape =="trapeziod":
    print("You can fit " + str(suggested(trapeziod(),panelsize())) + " panels.")
elif shape == "rectangle":
    print("You can fit " + str(suggested(rectangle(),panelsize())) + " panels.")
else: 
    print("invalid shape ")
