import turtle

# Creating as turtle window and setting background as black
turtle_window=turtle.Screen()
turtle_window.bgcolor("#000000")

# Setting our turtle speed to 0 so we don't see the movements
speed = 0

# Creating all our turtles, one for the border, goal, grid and the robot
border=turtle.Turtle()
grid=turtle.Turtle()
robot=turtle.Turtle()
goal=turtle.Turtle()

# Creating the array for the x, y cordinates and the grid and robot positions
xgrid = [-245, -195, -145, -95, -45, 5, 55, 105, 155, 205, 255]
ygrid = [-205, -155, -105, -55, -5, 45, 95, 145, 195, 245, 295]
grid_position = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
robot_position = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]


# Hides the turtles
border.ht()
grid.ht()
robot.ht()
goal.ht()

# Creates the room environment around the grid environment
border.speed(speed)
border.color("#000000","#FFFFFF")
border.up()
border.goto(250,250)
border.down()
border.begin_fill()
for z in range(4):
  border.rt(90)
  border.fd(500)
border.end_fill()

# Creates the 10x10 grid
grid.speed(speed)
grid.color("#888888")
for p in range(9):
  grid.up()
  grid.goto(-250,grid_position[p])
  grid.down()
  grid.fd(500)
  grid.lt(90)
  grid.up()
  grid.goto(grid_position[p],-250)
  grid.down()
  grid.fd(500)
  grid.rt(90)

# Sets the cordinates for the goal to x =4, y = 4
goalgridx = 4
goalgridy = 4
goalx = xgrid[goalgridx]
goaly = ygrid[goalgridy]

# Makes the goal object
goal.speed(speed)
goal.color("red")
goal.up()
goal.goto(goalx,goaly)
goal.down()
goal.begin_fill()
for z in range(4):
  goal.fd(40)
  goal.rt(90)
goal.end_fill()

# Sets the starting position for the robot to be x = 0 and y = 0
robotx = roboty = 0
goal = 1


# Function that checks if the goal is equal to 1 or 0 and decides what 0 and 1 will do
def goal_checker():
  global goalgridx; global goalgridy; global goal
  if robotx == goalgridx and roboty == goalgridy:
    goal.clear()
    goal -= 1
    goalgridx = goalgridy = -1

  if goal == 0:
      done()


# Robot location function
def set_robot():
  goal_checker()
  robot.clear()
  robot.speed(speed)
  robot.up()
  robot.goto(robot_position[robotx],robot_position[roboty])
  robot.dot(20,"#ABCDEF")

set_robot()

# Function that moves the robot up
def up():
  global roboty
  if roboty < 9:
    roboty += 1
    set_robot()

# Function that moves the robot down
def down():
  global roboty
  if roboty > 0 and roboty < 10:
    roboty -= 1
    set_robot()

# Function that moves the robot to the left
def left():
  global robotx
  if robotx > 0 and robotx < 10:
    robotx -= 1
    set_robot()

# Function that moves the robot to the right
def right():
  global robotx
  if robotx < 9:
    robotx += 1
    set_robot()

# Function that decides what happens when the goal is reached
def done():
    robot.clear()

# Function that goes up a specific amount of times using a binary equation
def y_up():
    times = ((10-0)//2+0)
    for i in range(times):
     up()

# Function that goes down a specific amount of times using a binary equation
def y_down():
    times = ((10-0)//2+0)
    for i in range(times):
        down()

# Function that search for the goal using a binary search method
def binary_search():
    y_up()
    right()
    y_down()
    right()
    y_up()
    right()
    y_down()
    right()
    y_up()

# Runs the binary search function
binary_search()

