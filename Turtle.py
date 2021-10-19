import turtle
from config import STEP_SIZE, NUM_GRID_ROWS
from World import WORLDS


class CustomTurtle(turtle.Turtle):

    def __init__(self, colour, speed, current_world, next_world):
        super().__init__()
        self.color(colour)
        self.speed(speed)
        self.shape('turtle')
        self.penup()
        self.x_pos = 0
        self.y_pos = 0
        self.next_world = next_world
        self.update_world_settings(current_world)

    def update_world_settings(self, current_world):
        self.current_world = current_world

    def move_forward(self):
        # figure out new position
        direction = self.heading()
        print(self.x_pos, self.y_pos)
        if direction == 90.0:  # facing up
            new_pos = (self.x_pos, self.y_pos + 1)
        if direction == 0.0:  # facing right
            new_pos = (self.x_pos + 1, self.y_pos)
        if direction == 270.0:  # facing down
            new_pos = (self.x_pos, self.y_pos - 1)
        if direction == 180.0:  # facing left
            new_pos = (self.x_pos - 1, self.y_pos)

        # check there is no obstacle there
        if self.is_clear(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.forward(STEP_SIZE)
            print(new_pos, self.current_world.portal_position)
            if new_pos == self.current_world.portal_position:
                self.enter_portal()

    def move_backward(self):  # challenge for them to add themselves?
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = (self.x_pos, self.y_pos - 1)
        if direction == 0.0:  # facing right
            new_pos = (self.x_pos - 1, self.y_pos)
        if direction == 270.0:  # facing down
            new_pos = (self.x_pos, self.y_pos + 1)
        if direction == 180.0:  # facing left
            new_pos = (self.x_pos + 1, self.y_pos)

        # check there is no obstacle there
        if self.is_clear(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.backward(STEP_SIZE)
            if new_pos == self.current_world.portal_position:
                self.enter_portal()

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def is_clear(self, new_pos):
        if new_pos in self.current_world.obstacle_positions:
            return False
        if new_pos[0] < 0 or new_pos[0] >= NUM_GRID_ROWS:
            return False
        if new_pos[1] < 0 or new_pos[1] >= NUM_GRID_ROWS:
            return False
        return True

    def enter_portal(self):
        print('portal')
        self.next_world()
