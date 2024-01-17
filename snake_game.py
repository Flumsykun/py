import pygame
import sys
import random

pygame.init()

# Set up the game window
window_width = 1440
window_height = 900
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Python Snake Game')

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #Display the game over message and final score
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render('Game Over', True, (255, 255, 255))

            score_font = pygame.font.Font(None, 36) 
            score_text = score_font.render('Score: ' + str(score), True, (255, 255, 255))

            game_window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
            game_window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2 - score_text.get_height() // 2 + 50))
            pygame.display.update()

            restart_font = pygame.font.Font(None, 36)
            restart_text = restart_font.render('Press R to restart', True, (255, 255, 255))

            game_window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 - restart_text.get_height() // 2 + 100))
            pygame.display.update()

            while True:

            #Food Properties
            food_color = (255, 0, 0) #red
            food_size = 20

            #Place the food at a random position
            food_x = random.randint(0, window_width - food_size)
            food_y = random.randint(0, window_height - food_size)

            #draw food
            food = pygame.Rect(food_x, food_y, food_size, food_size)

            #Detect collision between the snake and the food
            if snake.colliderect(food):
                #Update the snake's length and score
                snake_size += 1
                score += 1

                #Place the food at a random position
                food.x = random.randint(0, window_width - food_size)
                food.y = random.randint(0, window_height - food_size)

            #update the snake's length 
                snake_body.append(pygame.Rect(snake.x, snake.y, snake_size, snake_size))
                if len(snake_body) > snake_size:
                    del snake_body[0]

                    snake_body = []
                    
                    #Check for collision between the snake's head and its body
                    if len(snake_body) > 1 and snake.colliderct(snake_body[i] for i in range(1, len(snake_body))):
                        running = False


            #Snake properties
            snake_color = (0, 255, 0) #green
            snake_size = 20
            snake_x =  window_width // 2
            snake_y = window_height // 2
            snake_speed = 5

            #Snake movement
            snake_dx = 0
            snake_dy = 0
            
            #Snake control
            snake_speed_multiplier = 1

            #Draw snake
            snake  = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

            #Update snake position
            snake.x += snake_dx * snake_speed * snake_speed_multiplier
            snake.y += snake_dy * snake_speed * snake_speed_multiplier

            #Check if the snake hits the window boundaries
            if snake.x < 0 or snake.x + snake_size > window_width or snake.y < 0 or snake.y + snake_size > window_height:
                running = False

                

            #Quit pygame properly
            pygame.quit()
            sys.exit()