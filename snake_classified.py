import curses
import random


class Snake():
    """Snake object"""

    def __init__(self, sw, sh, w):
        super(Snake, self).__init__()
        # Define initial snake head position
        self.width, self.height, self.window = sw, sh, w

        # Start position
        self.snk_x = self.width // 4
        self.snk_y = self.height // 2

        # Snake is a vector of coordinates
        self.snake = [[self.snk_y, self.snk_x], [self.snk_y, self.snk_x - 1],
                      [self.snk_y, self.snk_x - 2]]

    def move(self, key, food=False):
        self._point_head(key)
        self._check_alive()
        self._trail(food)
        self._draw()

    def _check_alive(self):
        if self.snake[0][0] in [0, self.height] or self.snake[0][1] in [
                0, self.width
        ] or self.snake[0] in self.snake[1:]:
            curses.endwin()
            exit()

    def _point_head(self, key):
        new_head = [self.snake[0][0], self.snake[0][1]]

        # Update new head based on key press
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        # Puts new head at the start of the snake
        self.snake.insert(0, new_head)

    def _trail(self, food=False):
        if not food:
            tail = self.snake.pop()
            self.window.addch(tail[0], tail[1], ' ')

    def _draw(self):
        self.window.addch(self.snake[0][0], self.snake[0][1], curses.ACS_CKBOARD)

    def __call__(self):
        # Head position
        return self.snake[0]

    get_pos = __call__


class Food():
    """Food object"""

    def __init__(self, sw, sh, w):
        super(Food, self).__init__()
        self.width, self.height, self.window = sw, sh, w

        self.food = [self.height // 2, self.width // 2]
        self._draw()

    def put(self, snake):
        # New food is placed within bounds of screen
        nf = [
            random.randint(1, self.height - 1),
            random.randint(1, self.width - 1)
        ]
        self.food = nf
        self._draw()

    def _draw(self):
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)

    def __call__(self):
        return self.food

    get_pos = __call__


s = curses.initscr()  # Initialize screen
curses.curs_set(0)  # Hide cursor
height, width = s.getmaxyx()  # Get height and width
window = curses.newwin(height, width, 0, 0)  # Define window
window.keypad(1)  # Enable Keyboard input
window.timeout(88)  # Refresh rate

snake = Snake(width, height, window)
food = Food(width, height, window)
# Initialize key
key = curses.KEY_RIGHT

while True:
    next_key = window.getch()  # Listen for keys
    key = key if next_key == -1 else next_key
    snake.move(key)

    if snake() == food():
        snake.move(key, food=True)
        food.put(snake())
