
#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my CPT game for the edgebadge

import ugame
import stage


def game_scene():

    # load the background image
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp"
    )
    # creates the 10 by 8 image grid, sets the background image to background
    background = stage.Grid(image_bank_background, 10, 8)

    # 60 means it will update it 60 times a second
    game = stage.Stage(ugame.display, 60)
    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [background]
    # takes layers and shows them on the screen
    game.render_block()
    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input

        # update game logic
        pass


if __name__ == "__main__":
    game_scene()