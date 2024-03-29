# import pygame
# import sys
# import random

# pygame.init()

# # Set up the game window
# window_width = 1440
# window_height = 900
# game_window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption('Python Snake Game')

# #Game Loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#             #Display the game over message and final score
#             game_over_font = pygame.font.Font(None, 48)
#             game_over_text = game_over_font.render('Game Over', True, (255, 255, 255))

#             score_font = pygame.font.Font(None, 36)
#             score_text = score_font.render('Score: ' + str(score), True, (255, 255, 255))

#             game_window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
#             game_window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2 - score_text.get_height() // 2 + 50))
#             pygame.display.update()

#             restart_font = pygame.font.Font(None, 36)
#             restart_text = restart_font.render('Press R to restart', True, (255, 255, 255))

#             game_window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 - restart_text.get_height() // 2 + 100))
#             pygame.display.update()

#             while True:

#             #Food Properties
#             food_color = (255, 0, 0) #red
#             food_size = 20

#             #Place the food at a random position
#             food_x = random.randint(0, window_width - food_size)
#             food_y = random.randint(0, window_height - food_size)

#             #draw food
#             food = pygame.Rect(food_x, food_y, food_size, food_size)

#             #Detect collision between the snake and the food
#             if snake.colliderect(food):
#                 #Update the snake's length and score
#                 snake_size += 1
#                 score += 1

#                 #Place the food at a random position
#                 food.x = random.randint(0, window_width - food_size)
#                 food.y = random.randint(0, window_height - food_size)

#             #update the snake's length
#                 snake_body.append(pygame.Rect(snake.x, snake.y, snake_size, snake_size))
#                 if len(snake_body) > snake_size:
#                     del snake_body[0]

#                     snake_body = []

#                     #Check for collision between the snake's head and its body
#                     if len(snake_body) > 1 and snake.colliderct(snake_body[i] for i in range(1, len(snake_body))):
#                         running = False


#             #Snake properties
#             snake_color = (0, 255, 0) #green
#             snake_size = 20
#             snake_x =  window_width // 2
#             snake_y = window_height // 2
#             snake_speed = 5

#             #Snake movement
#             snake_dx = 0
#             snake_dy = 0

#             #Snake control
#             snake_speed_multiplier = 1

#             #Draw snake
#             snake  = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

#             #Update snake position
#             snake.x += snake_dx * snake_speed * snake_speed_multiplier
#             snake.y += snake_dy * snake_speed * snake_speed_multiplier

#             #Check if the snake hits the window boundaries
#             if snake.x < 0 or snake.x + snake_size > window_width or snake.y < 0 or snake.y + snake_size > window_height:
#                 running = False



#             #Quit pygame properly
#             pygame.quit()
#             sys.exit()

import turtle
import time
import random

delay = 0.1

#Score

Score = 0
high_score = 0

#Set up the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off the screen updates

#Define the snake's head using a turtle obj
#Set its initial positition to (0, 0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("Square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("Circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#Define the function to control the snake's movement
#Set up the keyboard bindings for controls

#Fucntions

def go_up():
 if head.direction != "down":
     head.direction = "up"

def go_down():
  if head.direction != "up":
      head.direction = "down"

def go_left():
  if head.direction != "right":
      head.direction = "left"

def go_right():
  if head.direction != "left":
      head.direction = "right"

def move():
  if head.direction == "up":
    y = head.ycor()
    head/sety(y + 20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

  #Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Create a loop to keep the game running,
#Check for collisions between the snake and the food

#Main game loop
while True:
  wn.update()

    #Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
      #Move the food to a random position
      x = random.randint(-290, 290)
      y = random.randint(-290, 290)
      food.goto(x, y)

      #Add a segment to the snake
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("square")
      new_segment.color("grey")
      new_segment.penup()
      segments.append(new_segment)

      #Shorten the delay
      delay -= 0.001

      #Increase the score
      score += 10

      if score > high_score:
        high_score = Score

        pen_clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #Move the end segments first in reverse order
        for index in range(len(segments) -1, 0, -1):
          x = segments[index - 1].xcor()
          y = segments[index - 1].ycor()
          segments[index].goto(x, y)

        #Move segment 0 to where the head is
        if len(segments) > 0:
          x = head.xcor()
          y = head.ycor()
          segments[0].goto(x, y)

      move()
