from config import STEP_SIZE
from utils import convert_coord_to_grid_pos


class MoveObject:

    def __init__(self, game, allowed_through_portal, start_position):
        self.game = game
        self.position = start_position
        self.allowed_through_portal = allowed_through_portal
        self.goto_start_position(start_position)

    def get_possible_positions(self):

        up_position = (self.position[0], self.position[1] + 1)
        right_position = (self.position[0] + 1, self.position[1])
        left_position = (self.position[0] - 1, self.position[1])

        valid_directions = []
        if self.game.current_world.cell_is_empty(up_position):
            valid_directions.append(0)
        if self.game.current_world.cell_is_empty(right_position):
            valid_directions.append(90)
        if self.game.current_world.cell_is_empty(left_position):
            valid_directions.append(270)
        return valid_directions

    def move_forward(self):
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = (self.position[0], self.position[1] + 1)
        if direction == 0.0:  # facing right
            new_pos = (self.position[0] + 1, self.position[1])
        if direction == 270.0:  # facing down
            new_pos = (self.position[0], self.position[1] - 1)
        if direction == 180.0:  # facing left
            new_pos = (self.position[0] - 1, self.position[1])

        # check there is no obstacle there
        if not self.game.current_world.cell_contains_obstacle(new_pos):
            if not self.game.current_world.cell_contains_portal(new_pos) and \
                not self.game.current_world.cell_contains_key(new_pos):
                self.position = new_pos
                self.forward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos) and \
                self.game.myrtle.has_key:
                self.position = new_pos
                self.forward(STEP_SIZE)
                self.enter_portal()
            if self.game.current_world.cell_contains_key(new_pos):
                self.position = new_pos
                self.forward(STEP_SIZE)
                self.pickup_key()

            if self.is_collision():
                self.goto_start_position((0, 0))  # TODO work out coordinates

    def is_collision(self):
        for bird in self.game.birds:
            if self.position == bird.position:
                return True
        return False

    def move_backward(self):  # challenge for them to add themselves?
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = (self.position[0], self.position[1] - 1)
        if direction == 0.0:  # facing right
            new_pos = (self.position[0] - 1, self.position[1])
        if direction == 270.0:  # facing down
            new_pos = (self.position[0], self.position[1] + 1)
        if direction == 180.0:  # facing left
            new_pos = (self.position[0] + 1, self.position[1])

        # check there is no obstacle there
        if not self.game.current_world.cell_contains_obstacle(new_pos):
            if not self.game.current_world.cell_contains_portal(new_pos) and \
                not self.game.current_world.cell_contains_key(new_pos):
                self.position = new_pos
                self.backward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos) and \
                self.game.myrtle.has_key:
                self.position = new_pos
                self.backward(STEP_SIZE)
                self.enter_portal()    
            if self.game.current_world.cell_contains_key(new_pos):
                self.position = new_pos
                self.backward(STEP_SIZE)
                self.pickup_key()

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def enter_portal(self):
        self.game.find_next_world()

    def goto_start_position(self, coordinates):
        self.penup()
        self.hideturtle()
        start_position = convert_coord_to_grid_pos(coordinates)
        self.position = coordinates
        self.goto(start_position)
        self.showturtle()

    def pickup_key(self):
        self.game.current_world.key.hideturtle()
        self.game.myrtle.color('orange')
        self.game.myrtle.has_key = True
