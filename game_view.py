"""The view of the main game window"""

import arcade
import key_controller
import snake
from maps import Maps

#Note to self, for camera, for the game to fit like we want it to:
#width should be 960 and height is 720
# Constants
# WINDOW_WIDTH = 960
# WINDOW_HEIGHT = 720
# WINDOW_TITLE = "Cracked_Snake"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.tile_map = None

        #creates snakes, no clue if the coords are what we want them to be or not yet though
        self.snake1 = snake.Snake(start_position=(5, 4))
        self.snake2 = snake.Snake(start_position=(15, 4), direction=(-1, 0))
        
        #vars for snake points, for now assuming 2
        self.snake1_points = 0
        self.snake2_points = 0

        self.player_count = 2

        #im going to figure out a way to declare number of players, but this is the generic case
        if self.playercount == 2:
            self.score_snake1 = arcade.Text(f"Sore: {self.snake1_points}", x=-10, y = 10)
            self.score_snake2 = arcade.Text(f"Sore: {self.snake2_points}", x=10, y = 10)


        self.scene = None

    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.handle_movement(player, direction)

    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            snake = self.snake1
        elif player == 2:
            snake = self.snake2
        else:
            return None
        # sets snake direction
        snake.direction = direction

        # tells snake where to move
        new_x = snake.segments[0][0] + snake.direction[0]
        new_y = snake.segments[0][1] + snake.direction[1]
        snake.segments.insert(0, (new_x, new_y))
        snake.segments.pop()

    def on_show_view(self):
        """
        We load all the snake games maps here
        """
        layer_options = {
            "Walls": {"use_spatial_hash": True,
                      "scaling": 1.0},
            "Background": {"use_spatial_hash": False,
                           "scaling": 1.0},
            }
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
       # self.physics_engine = arcade.PhysicsEngineSimple(walls=self.scene["Walls"])

    def on_draw(self):
        """Render the screen."""
        self.clear()

        #draw the score text, need to move this around
        self.score.draw()
        
        self.scene.draw()


    def on_update(self, delta_time):


        #note this only works for an individual case, we need to check this for each snake
        #in the instance we have multiple, but this is the basics for now

        #check for collisions w/ any walls in the list, as well as with opponent
        collision_list_snake1 = arcade.check_for_collision_with_list(self.snake1, self.wall_list)
        collision_list_snake1 = arcade.check_for_collision_with_list(self.snake1, self.snake2)

        collision_list_snake2 = arcade.check_for_collision_with_list(self.snake2 self.wall_list)
        collision_list_snake2 = arcade.check_for_collision_with_list(self.snake2 self.snake1)


        #add points to relevent var and change round to over
        if any() in collision_list_snake1: 
            snake2_points += 1
            round_over += 1

        if any() in collision_list_snake2: 
            snake1_points += 1
            round_over += 1


        if round_over != 0:
            self.setup()


        




