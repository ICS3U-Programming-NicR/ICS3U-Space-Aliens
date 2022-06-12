
#!/usr/bin/env python3
# Created By: Nicolas Riscalas
# Date: 03/25/2022
# Description: CPT game EdgeBadge

import constants
import stage
import ugame


def game_scene():

    # load the background image
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp"
    )
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # creates the 10 by 8 image grid, sets the background image to background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    # 60 means it will update it 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)
    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [ship] + [background]
    # takes layers and shows them on the screen
    game.render_block()
    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # When button b pressed print that it is pressed
        if keys & ugame.K_X:
            print("button B pressed")
        # When button a is pressed print that it is pressed
        if keys & ugame.K_O:
            print("button A pressed")
        # When the start button is pressed print that it is pressed
        if keys & ugame.K_START:
            print("Start")
        # when the right button is pressed move right
        if keys & ugame.K_RIGHT:
            if ship.x != constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
                print("right")
        # when the left button is pressed move left 
        if keys & ugame.K_LEFT:
            if ship.x != 0:
                ship.move(ship.x - 1, ship.y)
                print("left")
        # when the up button is pressed move up
        if keys & ugame.K_UP:
            if ship.y != 0:
                ship.move(ship.x, ship.y - 1)
                print("up")
        # when the down button is pressed move down
        if keys & ugame.K_DOWN:
            if ship.y != constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, ship.y + 1)
                print("down")
        game.render_sprites([ship])
        game.tick()
        # update game logic


if __name__ == "__main__":
    game_scene()
   
