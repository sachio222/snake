"""
From this video by Engineer Man:
https://www.youtube.com/watch?v=rbasThWVb-c&feature=youtu.be
"""

import curses
import random

s = curses.initscr()  # Initialize screen
curses.curs_set(0)  # Hide cursor
sh, sw = s.getmaxyx()  # Get height and width
w = curses.newwin(sh, sw, 0, 0)  # Define window
w.keypad(1)  # Enable Keyboard input
w.timeout(127)  # Refresh rate

# Define initial snake head position
snk_x = sw // 3
snk_y = sh // 2

# Snake is a vector of coordinates
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

# Food is a cordinate
food = [sh // 2, sw // 2]

# Add initial food to screen with add character
w.addch(food[0], food[1], curses.ACS_PI)

# Initialize key
key = curses.KEY_RIGHT

while True:
    next_key = w.getch()  # Listen for keys

    # If no keypress during loop (key = -1)
    key = key if next_key == -1 else next_key

    # Check if snake dead
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw
                                                ] or snake[0] in snake[1:]:
        #     # End behavior
        curses.endwin()
        quit()

    # draw
    new_head = [snake[0][0], snake[0][1]]

    # Update new head based on key press
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # draw
    # Array operation
    snake.insert(0, new_head)  # Puts new head at the start of the snake

    # Check if snake has eaten food
    if snake[0] == food:
        food = None
        while food is None:
            # New food is placed within bounds of screen
            nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
            # Place the food anywhere on the screen, unless it's in snake
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Keep snake moving, pop off last bit
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Draw snake
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
