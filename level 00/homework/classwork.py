from turtle import*


#we want to paint a house

#step 1:  draw a square
speed(25)
width(8)
color("green")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing of a door
begin_fill()
forward(70)
color("brown")
left(90)
forward(120) #height of a door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing of a window

color("black")
begin_fill()
left(30)
forward(75)
left(90)
forward(60)
left(90)
forward(75)
color("blue")
right(90)
forward(80)
color("black")
right(90)
forward(75)
left(90)
forward(60)
left(90)
forward(75)
end_fill()
exitonclick()