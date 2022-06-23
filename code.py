#!/usr/bin/env python3
# Created By: Nicolas Riscalas
# Date: 03/25/2022
# Description: CPT game EdgeBadge

import random
import time

import constants
import stage
import supervisor
import ugame


def end_game(
    game,
    trex,
    clouds,
    small_cactus_1,
    small_cactus_2,
    big_cactus_1,
    big_cactus_2,
    array_big_cactus_1_1,
    array_big_cactus_1_2,
    array_big_cactus_2_1,
    array_big_cactus_2_2,
    array_small_cactus_1_1,
    array_small_cactus_1_2,
    array_small_cactus_2_1,
    array_small_cactus_2_2,
    points,
):
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    end_game_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    floor = stage.Sprite(
        image_bank_sprites, 1, 0 * constants.SPRITE_SIZE, constants.FLOOR_Y
    )
    floor2 = stage.Sprite(
        image_bank_sprites, 1, (1 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor3 = stage.Sprite(
        image_bank_sprites, 1, (2 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor4 = stage.Sprite(
        image_bank_sprites, 1, (3 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor5 = stage.Sprite(
        image_bank_sprites, 1, (4 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor6 = stage.Sprite(
        image_bank_sprites, 1, (5 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor7 = stage.Sprite(
        image_bank_sprites, 1, (6 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor8 = stage.Sprite(
        image_bank_sprites, 1, (7 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor9 = stage.Sprite(
        image_bank_sprites, 1, (8 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor10 = stage.Sprite(
        image_bank_sprites, 1, (9 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    with open("highscore.txt", "r") as reader:
        highscore_num = reader.read()
        highscore = int(highscore_num)
    if points > highscore:
        try:
            with open("/highscore.txt", "w") as fp:
                fp.write("{}".format(points))
        except:
            print("unable to save")
            pass
    # set the complete floor
    complete_floor = (
        [floor]
        + [floor2]
        + [floor3]
        + [floor4]
        + [floor5]
        + [floor6]
        + [floor7]
        + [floor8]
        + [floor9]
        + [floor10]
    )

    # move it to the center
    end_game_text.move(10, 10)
    end_game_text.text("Press <SELECT> to \nrestart the game")
    game.layers = (
        [end_game_text]
        + [trex]
        + complete_floor
        + [clouds]
        + [small_cactus_1]
        + [array_small_cactus_1_1]
        + [array_small_cactus_1_2]
        + [small_cactus_2]
        + [array_small_cactus_2_1]
        + [array_small_cactus_2_2]
        + [big_cactus_1]
        + [array_big_cactus_1_1]
        + [array_big_cactus_1_2]
        + [big_cactus_2]
        + [array_big_cactus_2_1]
        + [array_big_cactus_2_2]
        + [background]
    )
    game.render_block()
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # When the start button is pressed or the up button start the game
        if keys & ugame.K_SELECT:
            supervisor.reload()
        game.render_sprites(
            [trex]
            + [clouds]
            + [big_cactus_1]
            + [big_cactus_2]
            + [small_cactus_1]
            + [small_cactus_2]
            + [array_big_cactus_1_1]
            + [array_big_cactus_1_2]
            + [array_big_cactus_2_1]
            + [array_big_cactus_2_2]
            + [array_small_cactus_1_1]
            + [array_small_cactus_1_2]
            + [array_small_cactus_2_1]
            + [array_small_cactus_2_2]
            + complete_floor
        )
        game.tick()


def move_cactus(
    small_cactus_1,
    small_cactus_2,
    big_cactus_1,
    big_cactus_2,
    array_big_cactus_1_1,
    array_big_cactus_1_2,
    array_big_cactus_2_1,
    array_big_cactus_2_2,
    array_small_cactus_1_1,
    array_small_cactus_1_2,
    array_small_cactus_2_1,
    array_small_cactus_2_2,
    speed,
    big_cactus_1_moving,
    big_cactus_2_moving,
    small_cactus_1_moving,
    small_cactus_2_moving,
    two_cactus_big1_moving,
    two_cactus_big2_moving,
    two_cactus_big3_moving,
    two_cactus_big4_moving,
    two_cactus_small1_moving,
    two_cactus_small2_moving,
    two_cactus_small3_moving,
    two_cactus_small4_moving,
    two_cactus_small_big1_moving,
    two_cactus_small_big2_moving,
    two_cactus_small_big3_moving,
    two_cactus_small_big4_moving,
    two_cactus_big_small1_moving,
    two_cactus_big_small2_moving,
    two_cactus_big_small3_moving,
    two_cactus_big_small4_moving,
    three_cactus_big1_moving,
    three_cactus_big2_moving,
    three_cactus_big3_moving,
    three_cactus_big4_moving,
    three_cactus_big5_moving,
    three_cactus_big6_moving,
    three_cactus_big7_moving,
    three_cactus_big8_moving,
    three_cactus_small1_moving,
    three_cactus_small2_moving,
    three_cactus_small3_moving,
    three_cactus_small4_moving,
    three_cactus_small5_moving,
    three_cactus_small6_moving,
    three_cactus_small7_moving,
    three_cactus_small8_moving,
):
    if big_cactus_1_moving == True:
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif big_cactus_2_moving == True:
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif small_cactus_1_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif small_cactus_2_moving == True:
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_big1_moving == True:
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_big2_moving == True:
        array_big_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_big3_moving == True:
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_big4_moving == True:
        array_big_cactus_2_1.move(array_big_cactus_2_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_small1_moving == True:
        array_small_cactus_1_1.move(array_small_cactus_1_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_small2_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_small3_moving == True:
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_small4_moving == True:
        array_small_cactus_2_1.move(array_small_cactus_2_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_small_big1_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_small_big2_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_small_big3_moving == True:
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_small_big4_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_big_small1_moving == True:
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_big_small2_moving == True:
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif two_cactus_big_small3_moving == True:
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif two_cactus_big_small4_moving == True:
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_big1_moving == True:
        array_big_cactus_1_2.move(array_big_cactus_1_2.x - speed, constants.TREX_Y)
        array_big_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_big2_moving == True:
        array_big_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_big3_moving == True:
        array_big_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_big4_moving == True:
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
        array_big_cactus_2_1.move(array_big_cactus_2_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_big5_moving == True:
        array_big_cactus_2_2.move(array_big_cactus_2_2.x - speed, constants.TREX_Y)
        array_big_cactus_2_1.move(array_big_cactus_2_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_big6_moving == True:
        array_big_cactus_2_1.move(array_big_cactus_2_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_big7_moving == True:
        array_big_cactus_2_1.move(array_big_cactus_2_1.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_big8_moving == True:
        big_cactus_2.move(big_cactus_2.x - speed, constants.TREX_Y)
        array_big_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        big_cactus_1.move(big_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_small1_moving == True:
        array_small_cactus_1_2.move(array_small_cactus_1_2.x - speed, constants.TREX_Y)
        array_small_cactus_1_1.move(array_small_cactus_1_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_small2_moving == True:
        array_small_cactus_1_1.move(array_small_cactus_1_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_small3_moving == True:
        array_small_cactus_1_1.move(array_small_cactus_1_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_small4_moving == True:
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        array_small_cactus_2_1.move(array_small_cactus_2_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_small5_moving == True:
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
        array_small_cactus_1_1.move(array_big_cactus_1_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_small6_moving == True:
        array_small_cactus_2_1.move(array_small_cactus_2_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
    elif three_cactus_small7_moving == True:
        array_small_cactus_2_1.move(array_small_cactus_2_1.x - speed, constants.TREX_Y)
        small_cactus_1.move(small_cactus_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)
    elif three_cactus_small8_moving == True:
        array_small_cactus_2_2.move(array_small_cactus_2_2.x - speed, constants.TREX_Y)
        array_small_cactus_2_1.move(array_small_cactus_2_1.x - speed, constants.TREX_Y)
        small_cactus_2.move(small_cactus_2.x - speed, constants.TREX_Y)


def gravity(
    trex,
    game,
    clouds,
    small_cactus_1,
    small_cactus_2,
    big_cactus_1,
    big_cactus_2,
    array_big_cactus_1_1,
    array_big_cactus_1_2,
    array_big_cactus_2_1,
    array_big_cactus_2_2,
    array_small_cactus_1_1,
    array_small_cactus_1_2,
    array_small_cactus_2_1,
    array_small_cactus_2_2,
    speed,
    big_cactus_1_moving,
    big_cactus_2_moving,
    small_cactus_1_moving,
    small_cactus_2_moving,
    two_cactus_big1_moving,
    two_cactus_big2_moving,
    two_cactus_big3_moving,
    two_cactus_big4_moving,
    two_cactus_small1_moving,
    two_cactus_small2_moving,
    two_cactus_small3_moving,
    two_cactus_small4_moving,
    two_cactus_small_big1_moving,
    two_cactus_small_big2_moving,
    two_cactus_small_big3_moving,
    two_cactus_small_big4_moving,
    two_cactus_big_small1_moving,
    two_cactus_big_small2_moving,
    two_cactus_big_small3_moving,
    two_cactus_big_small4_moving,
    three_cactus_big1_moving,
    three_cactus_big2_moving,
    three_cactus_big3_moving,
    three_cactus_big4_moving,
    three_cactus_big5_moving,
    three_cactus_big6_moving,
    three_cactus_big7_moving,
    three_cactus_big8_moving,
    three_cactus_small1_moving,
    three_cactus_small2_moving,
    three_cactus_small3_moving,
    three_cactus_small4_moving,
    three_cactus_small5_moving,
    three_cactus_small6_moving,
    three_cactus_small7_moving,
    three_cactus_small8_moving,
    points,
    points_text,
):
    while trex.y < constants.TREX_Y:
        move_cactus(
            small_cactus_1,
            small_cactus_2,
            big_cactus_1,
            big_cactus_2,
            array_big_cactus_1_1,
            array_big_cactus_1_2,
            array_big_cactus_2_1,
            array_big_cactus_2_2,
            array_small_cactus_1_1,
            array_small_cactus_1_2,
            array_small_cactus_2_1,
            array_small_cactus_2_2,
            speed,
            big_cactus_1_moving,
            big_cactus_2_moving,
            small_cactus_1_moving,
            small_cactus_2_moving,
            two_cactus_big1_moving,
            two_cactus_big2_moving,
            two_cactus_big3_moving,
            two_cactus_big4_moving,
            two_cactus_small1_moving,
            two_cactus_small2_moving,
            two_cactus_small3_moving,
            two_cactus_small4_moving,
            two_cactus_small_big1_moving,
            two_cactus_small_big2_moving,
            two_cactus_small_big3_moving,
            two_cactus_small_big4_moving,
            two_cactus_big_small1_moving,
            two_cactus_big_small2_moving,
            two_cactus_big_small3_moving,
            two_cactus_big_small4_moving,
            three_cactus_big1_moving,
            three_cactus_big2_moving,
            three_cactus_big3_moving,
            three_cactus_big4_moving,
            three_cactus_big5_moving,
            three_cactus_big6_moving,
            three_cactus_big7_moving,
            three_cactus_big8_moving,
            three_cactus_small1_moving,
            three_cactus_small2_moving,
            three_cactus_small3_moving,
            three_cactus_small4_moving,
            three_cactus_small5_moving,
            three_cactus_small6_moving,
            three_cactus_small7_moving,
            three_cactus_small8_moving,
        )
        if (
            (
                array_small_cactus_2_2.x <= trex.x + 7
                and array_small_cactus_2_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                array_small_cactus_2_1.x <= trex.x + 8
                and array_small_cactus_2_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                small_cactus_2.x <= trex.x + 8
                and small_cactus_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                array_small_cactus_1_2.x <= trex.x + 7
                and array_small_cactus_1_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                array_small_cactus_1_1.x <= trex.x + 8
                and array_small_cactus_1_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                small_cactus_1.x <= trex.x + 8
                and small_cactus_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                array_big_cactus_2_2.x <= trex.x + 7
                and array_big_cactus_2_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                array_big_cactus_2_1.x <= trex.x + 8
                and array_big_cactus_2_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 7
            )
            or (
                big_cactus_2.x <= trex.x + 8
                and big_cactus_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 16
            )
            or (
                array_big_cactus_1_2.x <= trex.x + 7
                and array_big_cactus_1_2.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 16
            )
            or (
                array_big_cactus_1_1.x <= trex.x + 8
                and array_big_cactus_1_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 16
            )
            or (
                big_cactus_1.x <= trex.x + 8
                and big_cactus_1.x >= trex.x - 8
                and trex.y >= constants.TREX_Y - 16
            )
        ):
            end_game = True
            return end_game
        else:
            points = points + 1
            points_text.clear()
            points_text.cursor(0, 0)
            points_text.move(1, 1)
            points_text.text("Score: {}".format(points))
        clouds.move(clouds.x - 0.1, clouds.y)
        trex.move(trex.x, trex.y + (constants.JUMP_HEIGHT / constants.SPRITE_SIZE))
        game.render_sprites(
            [trex]
            + [clouds]
            + [big_cactus_1]
            + [big_cactus_2]
            + [small_cactus_1]
            + [small_cactus_2]
            + [array_big_cactus_1_1]
            + [array_big_cactus_1_2]
            + [array_big_cactus_2_1]
            + [array_big_cactus_2_2]
            + [array_small_cactus_1_1]
            + [array_small_cactus_1_2]
            + [array_small_cactus_2_1]
            + [array_small_cactus_2_2]
        )
        game.tick()


def splash_scene():
    # this shows the splash screen
    # use the coin sound
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # show the same image as the normal level
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # load the background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # used this program to split the image into tile:

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white
    # set the game scene
    game = stage.Stage(ugame.display, constants.FPS)
    # choose the order of display
    game.layers = [background]
    game.render_block()
    while True:
        # Get user input
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # this shows the main menu screen
    # show the same image as the normal level
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # load the background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    trex = stage.Sprite(image_bank_sprites, 4, constants.TREX_X, constants.TREX_Y)

    floor = stage.Sprite(
        image_bank_sprites, 1, 0 * constants.SPRITE_SIZE, constants.FLOOR_Y
    )
    floor2 = stage.Sprite(
        image_bank_sprites, 1, (1 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor3 = stage.Sprite(
        image_bank_sprites, 1, (2 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor4 = stage.Sprite(
        image_bank_sprites, 1, (3 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor5 = stage.Sprite(
        image_bank_sprites, 1, (4 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor6 = stage.Sprite(
        image_bank_sprites, 1, (5 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor7 = stage.Sprite(
        image_bank_sprites, 1, (6 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor8 = stage.Sprite(
        image_bank_sprites, 1, (7 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor9 = stage.Sprite(
        image_bank_sprites, 1, (8 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor10 = stage.Sprite(
        image_bank_sprites, 1, (9 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    # add the text objects
    text = []
    # create the first text
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move it to the center
    text1.move(10, 10)
    text1.text("Riscing Developers")
    # append it to the text array
    text.append(text1)

    # create the second text
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move it where I want it
    text2.move(32, 26)
    text2.text("PRESS <START>")
    # append it to the text array
    text.append(text2)
    # set the game scene
    game = stage.Stage(ugame.display, constants.FPS)
    # choose the order of display
    game.layers = (
        [trex]
        + [floor]
        + [floor2]
        + [floor3]
        + [floor4]
        + [floor5]
        + [floor6]
        + [floor7]
        + [floor8]
        + [floor9]
        + [floor10]
        + text
        + [background]
    )
    game.render_block()
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # When the start button is pressed or the up button start the game
        if keys & ugame.K_START:
            game_scene()
        if keys & ugame.K_UP:
            game_scene()
        if keys & ugame.K_O:
            game_scene()
        # render the t-rex
        game.render_sprites([trex])
        game.tick()


def game_scene():
    # set the starting speed
    speed = 2
    # set the starting points
    points = 0
    # boolean for checking if jump
    big_cactus_1_moving = True
    big_cactus_2_moving = False
    small_cactus_1_moving = False
    small_cactus_2_moving = False
    two_cactus_big1_moving = False
    two_cactus_big2_moving = False
    two_cactus_big3_moving = False
    two_cactus_big4_moving = False
    two_cactus_small1_moving = False
    two_cactus_small2_moving = False
    two_cactus_small3_moving = False
    two_cactus_small4_moving = False
    two_cactus_small_big1_moving = False
    two_cactus_small_big2_moving = False
    two_cactus_small_big3_moving = False
    two_cactus_small_big4_moving = False
    two_cactus_big_small1_moving = False
    two_cactus_big_small2_moving = False
    two_cactus_big_small3_moving = False
    two_cactus_big_small4_moving = False
    three_cactus_big1_moving = False
    three_cactus_big2_moving = False
    three_cactus_big3_moving = False
    three_cactus_big4_moving = False
    three_cactus_big5_moving = False
    three_cactus_big6_moving = False
    three_cactus_big7_moving = False
    three_cactus_big8_moving = False
    three_cactus_small1_moving = False
    three_cactus_small2_moving = False
    three_cactus_small3_moving = False
    three_cactus_small4_moving = False
    three_cactus_small5_moving = False
    three_cactus_small6_moving = False
    three_cactus_small7_moving = False
    three_cactus_small8_moving = False

    # load the background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # load the t-rex
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # button states
    up_button = constants.button_state["button_up"]

    # import the sound
    jump_sound = open("jump_sound.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # creates the 10 by 8 image grid, sets the background image to background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    highpoints_num = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move it where I want it
    highpoints_num.move(1, 13)
    with open("highscore.txt", "r") as reader:
        highscore_num = reader.read()
    highpoints_num.text("Highscore: {}".format(highscore_num))

    # # open the highpoints
    points_text = stage.Text(width=29, height=14)
    points_text.clear()
    points_text.cursor(0, 0)
    points_text.move(1, 1)
    points_text.text("Score: {0}".format(points))
    score = stage.Stage(ugame.display, constants.FPS)
    score.layer = [points_text]
    score.render_block()
    trex = stage.Sprite(image_bank_sprites, 4, constants.TREX_X, constants.TREX_Y)
    # create the floor
    floor = stage.Sprite(
        image_bank_sprites, 1, 0 * constants.SPRITE_SIZE, constants.FLOOR_Y
    )
    floor2 = stage.Sprite(
        image_bank_sprites, 1, (1 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor3 = stage.Sprite(
        image_bank_sprites, 1, (2 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor4 = stage.Sprite(
        image_bank_sprites, 1, (3 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor5 = stage.Sprite(
        image_bank_sprites, 1, (4 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor6 = stage.Sprite(
        image_bank_sprites, 1, (5 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor7 = stage.Sprite(
        image_bank_sprites, 1, (6 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor8 = stage.Sprite(
        image_bank_sprites, 1, (7 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor9 = stage.Sprite(
        image_bank_sprites, 1, (8 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    floor10 = stage.Sprite(
        image_bank_sprites, 1, (9 * constants.SPRITE_SIZE), constants.FLOOR_Y
    )
    # set the complete floor
    complete_floor = (
        [floor]
        + [floor2]
        + [floor3]
        + [floor4]
        + [floor5]
        + [floor6]
        + [floor7]
        + [floor8]
        + [floor9]
        + [floor10]
    )
    # create the cloud sprite
    clouds = stage.Sprite(image_bank_sprites, 3, constants.CLOUDS_X, constants.CLOUDS_Y)
    # create the star sprite
    stars = stage.Sprite(image_bank_sprites, 2, constants.CLOUDS_X, constants.STARS_Y)
    # create all the different types of cacti
    big_cactus_1 = stage.Sprite(
        image_bank_sprites, 5, constants.BIG_CACTUS_X, constants.TREX_Y
    )
    array_big_cactus_1_1 = stage.Sprite(
        image_bank_sprites, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_big_cactus_1_2 = stage.Sprite(
        image_bank_sprites, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    big_cactus_2 = stage.Sprite(
        image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_big_cactus_2_1 = stage.Sprite(
        image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_big_cactus_2_2 = stage.Sprite(
        image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    small_cactus_1 = stage.Sprite(
        image_bank_sprites, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_small_cactus_1_1 = stage.Sprite(
        image_bank_sprites, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_small_cactus_1_2 = stage.Sprite(
        image_bank_sprites, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    small_cactus_2 = stage.Sprite(
        image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_small_cactus_2_1 = stage.Sprite(
        image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    array_small_cactus_2_2 = stage.Sprite(
        image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )
    # 60 means it will update it 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)
    # accesses the first layer(background) and makes the list of images for the background
    game.layers = (
        [trex]
        + complete_floor
        + [clouds]
        + [stars]
        + [array_big_cactus_1_1]
        + [array_big_cactus_1_2]
        + [array_big_cactus_2_1]
        + [array_big_cactus_2_2]
        + [array_small_cactus_1_1]
        + [array_small_cactus_1_2]
        + [array_small_cactus_2_1]
        + [array_small_cactus_2_2]
        + [big_cactus_1]
        + [big_cactus_2]
        + [small_cactus_1]
        + [small_cactus_2]
        + [points_text]
        + [highpoints_num]
        + [background]
    )
    # takes layers and shows them on the screen
    game.render_block()
    # this is the game loop so it is supposed to loop forever
    while True:
        points = points + 1
        points_text.clear()
        points_text.cursor(0, 0)
        points_text.move(1, 1)
        points_text.text("Score: {}".format(points))
        # incrementally increase the speed
        speed = speed + 0.0001
        # if there is no cactus on screen then spawn another
        if (
            big_cactus_1.x <= -16
            and big_cactus_2.x <= -16
            and small_cactus_1.x <= -16
            and small_cactus_2.x <= -16
        ):
            # stop the cacti from moving
            big_cactus_1_moving = False
            big_cactus_2_moving = False
            small_cactus_1_moving = False
            small_cactus_2_moving = False
            two_cactus_big1_moving = False
            two_cactus_big2_moving = False
            two_cactus_big3_moving = False
            two_cactus_big4_moving = False
            two_cactus_small1_moving = False
            two_cactus_small2_moving = False
            two_cactus_small3_moving = False
            two_cactus_small4_moving = False
            two_cactus_small_big1_moving = False
            two_cactus_small_big2_moving = False
            two_cactus_small_big3_moving = False
            two_cactus_small_big4_moving = False
            two_cactus_big_small1_moving = False
            two_cactus_big_small2_moving = False
            two_cactus_big_small3_moving = False
            two_cactus_big_small4_moving = False
            three_cactus_big1_moving = False
            three_cactus_big2_moving = False
            three_cactus_big3_moving = False
            three_cactus_big4_moving = False
            three_cactus_big5_moving = False
            three_cactus_big6_moving = False
            three_cactus_big7_moving = False
            three_cactus_big8_moving = False
            three_cactus_small1_moving = False
            three_cactus_small2_moving = False
            three_cactus_small3_moving = False
            three_cactus_small4_moving = False
            three_cactus_small5_moving = False
            three_cactus_small6_moving = False
            three_cactus_small7_moving = False
            three_cactus_small8_moving = False
            # print("hello")
            # select a random cactus to show
            random_cactus = random.randint(1, 36)
            # check which one is chosen and spawn it to the beginning
            if random_cactus == 1:
                big_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_1_moving = True
            elif random_cactus == 2:
                big_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_2_moving = True
            elif random_cactus == 3:
                small_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_1_moving = True
            elif random_cactus == 4:
                small_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_2_moving = True
            elif random_cactus == 5:
                big_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big1_moving = True
            elif random_cactus == 6:
                array_big_cactus_1_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big2_moving = True
            elif random_cactus == 7:
                big_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big3_moving = True
            elif random_cactus == 8:
                array_big_cactus_2_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big4_moving = True
            elif random_cactus == 9:
                array_small_cactus_1_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small1_moving = True
            elif random_cactus == 10:
                small_cactus_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small2_moving = True
            elif random_cactus == 11:
                small_cactus_2.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small3_moving = True
            elif random_cactus == 12:
                array_small_cactus_2_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small4_moving = True
            elif random_cactus == 13:
                small_cactus_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small_big1_moving = True
            elif random_cactus == 14:
                small_cactus_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small_big2_moving = True
            elif random_cactus == 15:
                small_cactus_2.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small_big3_moving = True
            elif random_cactus == 16:
                small_cactus_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 6, constants.TREX_Y)
                two_cactus_small_big4_moving = True
            elif random_cactus == 17:
                big_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big_small1_moving = True
            elif random_cactus == 18:
                big_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big_small2_moving = True
            elif random_cactus == 19:
                big_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big_small3_moving = True
            elif random_cactus == 20:
                big_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 9, constants.TREX_Y)
                two_cactus_big_small4_moving = True
            elif random_cactus == 21:
                array_big_cactus_1_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                array_big_cactus_1_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big1_moving = True
            elif random_cactus == 22:
                array_big_cactus_1_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big2_moving = True
            elif random_cactus == 23:
                array_big_cactus_1_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big3_moving = True
            elif random_cactus == 24:
                big_cactus_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                array_big_cactus_2_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big4_moving = True
            elif random_cactus == 25:
                array_big_cactus_2_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                array_big_cactus_2_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big5_moving = True
            elif random_cactus == 26:
                array_big_cactus_2_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big6_moving = True
            elif random_cactus == 27:
                array_big_cactus_2_1.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_2.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big7_moving = True
            elif random_cactus == 28:
                big_cactus_2.move(constants.BIG_CACTUS_X, constants.TREX_Y)
                array_big_cactus_1_1.move(constants.BIG_CACTUS_X + 9, constants.TREX_Y)
                big_cactus_1.move(constants.BIG_CACTUS_X + 18, constants.TREX_Y)
                three_cactus_big8_moving = True
            elif random_cactus == 29:
                array_small_cactus_1_2.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                array_small_cactus_1_1.move(
                    constants.SMALL_CACTUS_X + 6, constants.TREX_Y
                )
                small_cactus_1.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small1_moving = True
            elif random_cactus == 30:
                array_small_cactus_1_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small2_moving = True
            elif random_cactus == 31:
                array_small_cactus_1_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small3_moving = True
            elif random_cactus == 32:
                small_cactus_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                array_small_cactus_2_1.move(
                    constants.SMALL_CACTUS_X + 6, constants.TREX_Y
                )
                small_cactus_2.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small4_moving = True
            elif random_cactus == 33:
                small_cactus_2.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                array_small_cactus_1_1.move(
                    constants.SMALL_CACTUS_X + 6, constants.TREX_Y
                )
                small_cactus_1.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small5_moving = True
            elif random_cactus == 34:
                array_small_cactus_2_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small6_moving = True
            elif random_cactus == 35:
                array_small_cactus_2_1.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                small_cactus_1.move(constants.SMALL_CACTUS_X + 6, constants.TREX_Y)
                small_cactus_2.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small7_moving = True
            elif random_cactus == 36:
                array_small_cactus_2_2.move(constants.SMALL_CACTUS_X, constants.TREX_Y)
                array_small_cactus_2_1.move(
                    constants.SMALL_CACTUS_X + 6, constants.TREX_Y
                )
                small_cactus_2.move(constants.SMALL_CACTUS_X + 12, constants.TREX_Y)
                three_cactus_small8_moving = True
        # check which one is spawned and move it at the speed of speed
        move_cactus(
            small_cactus_1,
            small_cactus_2,
            big_cactus_1,
            big_cactus_2,
            array_big_cactus_1_1,
            array_big_cactus_1_2,
            array_big_cactus_2_1,
            array_big_cactus_2_2,
            array_small_cactus_1_1,
            array_small_cactus_1_2,
            array_small_cactus_2_1,
            array_small_cactus_2_2,
            speed,
            big_cactus_1_moving,
            big_cactus_2_moving,
            small_cactus_1_moving,
            small_cactus_2_moving,
            two_cactus_big1_moving,
            two_cactus_big2_moving,
            two_cactus_big3_moving,
            two_cactus_big4_moving,
            two_cactus_small1_moving,
            two_cactus_small2_moving,
            two_cactus_small3_moving,
            two_cactus_small4_moving,
            two_cactus_small_big1_moving,
            two_cactus_small_big2_moving,
            two_cactus_small_big3_moving,
            two_cactus_small_big4_moving,
            two_cactus_big_small1_moving,
            two_cactus_big_small2_moving,
            two_cactus_big_small3_moving,
            two_cactus_big_small4_moving,
            three_cactus_big1_moving,
            three_cactus_big2_moving,
            three_cactus_big3_moving,
            three_cactus_big4_moving,
            three_cactus_big5_moving,
            three_cactus_big6_moving,
            three_cactus_big7_moving,
            three_cactus_big8_moving,
            three_cactus_small1_moving,
            three_cactus_small2_moving,
            three_cactus_small3_moving,
            three_cactus_small4_moving,
            three_cactus_small5_moving,
            three_cactus_small6_moving,
            three_cactus_small7_moving,
            three_cactus_small8_moving,
        )

        # move the clouds
        if clouds.x > 0 - constants.SPRITE_SIZE:
            clouds.move(clouds.x - 0.1, clouds.y)
        else:
            clouds.move(160, clouds.y)
        # Get user input
        keys = ugame.buttons.get_pressed()
        # When button b pressed print that it is pressed
        if keys & ugame.K_X:
            pass
        # When button a is pressed print that it is pressed
        if keys & ugame.K_O:
            # if statements to check what state the button is in
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
                # makes the trex jump
                sound.play(jump_sound)
                while trex.y != (constants.TREX_Y - constants.JUMP_HEIGHT):
                    # while the trex is in the air keep on moving the clouds and the cacti
                    clouds.move(clouds.x - 0.1, clouds.y)
                    move_cactus(
                        small_cactus_1,
                        small_cactus_2,
                        big_cactus_1,
                        big_cactus_2,
                        array_big_cactus_1_1,
                        array_big_cactus_1_2,
                        array_big_cactus_2_1,
                        array_big_cactus_2_2,
                        array_small_cactus_1_1,
                        array_small_cactus_1_2,
                        array_small_cactus_2_1,
                        array_small_cactus_2_2,
                        speed,
                        big_cactus_1_moving,
                        big_cactus_2_moving,
                        small_cactus_1_moving,
                        small_cactus_2_moving,
                        two_cactus_big1_moving,
                        two_cactus_big2_moving,
                        two_cactus_big3_moving,
                        two_cactus_big4_moving,
                        two_cactus_small1_moving,
                        two_cactus_small2_moving,
                        two_cactus_small3_moving,
                        two_cactus_small4_moving,
                        two_cactus_small_big1_moving,
                        two_cactus_small_big2_moving,
                        two_cactus_small_big3_moving,
                        two_cactus_small_big4_moving,
                        two_cactus_big_small1_moving,
                        two_cactus_big_small2_moving,
                        two_cactus_big_small3_moving,
                        two_cactus_big_small4_moving,
                        three_cactus_big1_moving,
                        three_cactus_big2_moving,
                        three_cactus_big3_moving,
                        three_cactus_big4_moving,
                        three_cactus_big5_moving,
                        three_cactus_big6_moving,
                        three_cactus_big7_moving,
                        three_cactus_big8_moving,
                        three_cactus_small1_moving,
                        three_cactus_small2_moving,
                        three_cactus_small3_moving,
                        three_cactus_small4_moving,
                        three_cactus_small5_moving,
                        three_cactus_small6_moving,
                        three_cactus_small7_moving,
                        three_cactus_small8_moving,
                    )
                    if (
                        (
                            array_small_cactus_2_2.x <= trex.x + 5
                            and array_small_cactus_2_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_2_1.x <= trex.x + 8
                            and array_small_cactus_2_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            small_cactus_2.x <= trex.x + 8
                            and small_cactus_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_1_2.x <= trex.x + 5
                            and array_small_cactus_1_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_1_1.x <= trex.x + 5
                            and array_small_cactus_1_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            small_cactus_1.x <= trex.x + 8
                            and small_cactus_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_big_cactus_2_2.x <= trex.x + 5
                            and array_big_cactus_2_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_big_cactus_2_1.x <= trex.x + 8
                            and array_big_cactus_2_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            big_cactus_2.x <= trex.x + 8
                            and big_cactus_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            array_big_cactus_1_2.x <= trex.x + 5
                            and array_big_cactus_1_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            array_big_cactus_1_1.x <= trex.x + 8
                            and array_big_cactus_1_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            big_cactus_1.x <= trex.x + 8
                            and big_cactus_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                    ):
                        end_game(
                            game,
                            trex,
                            clouds,
                            small_cactus_1,
                            small_cactus_2,
                            big_cactus_1,
                            big_cactus_2,
                            array_big_cactus_1_1,
                            array_big_cactus_1_2,
                            array_big_cactus_2_1,
                            array_big_cactus_2_2,
                            array_small_cactus_1_1,
                            array_small_cactus_1_2,
                            array_small_cactus_2_1,
                            array_small_cactus_2_2,
                            points,
                        )
                    else:
                        points = points + 1
                        points_text.clear()
                        points_text.cursor(0, 0)
                        points_text.move(1, 1)
                        points_text.text("Score: {}".format(points))

                    trex.move(
                        trex.x, trex.y - (constants.JUMP_HEIGHT / constants.SPRITE_SIZE)
                    )
                    game.render_sprites(
                        [trex]
                        + [clouds]
                        + [big_cactus_1]
                        + [big_cactus_2]
                        + [small_cactus_1]
                        + [small_cactus_2]
                        + [array_big_cactus_1_1]
                        + [array_big_cactus_1_2]
                        + [array_big_cactus_2_1]
                        + [array_big_cactus_2_2]
                        + [array_small_cactus_1_1]
                        + [array_small_cactus_1_2]
                        + [array_small_cactus_2_1]
                        + [array_small_cactus_2_2]
                    )
                    game.tick()
            else:
                if up_button == constants.button_state["button_still_pressed"]:
                    up_button = constants.button_state["button_released"]
                else:
                    up_button = constants.button_state["button_up"]
        # When the start button is pressed print that it is pressed
        if keys & ugame.K_START:
            pass
        # when the right button is pressed pass
        if keys & ugame.K_RIGHT:
            pass
        # when the left button is pressed pass
        if keys & ugame.K_LEFT:
            pass
        # when the up button is pressed move up
        if keys & ugame.K_UP:
            # if statements to check what state the button is in
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
                # makes the trex jump
                sound.play(jump_sound)
                while trex.y != (constants.TREX_Y - constants.JUMP_HEIGHT):
                    # while the trex is in the air keep on moving the clouds and the cactus
                    move_cactus(
                        small_cactus_1,
                        small_cactus_2,
                        big_cactus_1,
                        big_cactus_2,
                        array_big_cactus_1_1,
                        array_big_cactus_1_2,
                        array_big_cactus_2_1,
                        array_big_cactus_2_2,
                        array_small_cactus_1_1,
                        array_small_cactus_1_2,
                        array_small_cactus_2_1,
                        array_small_cactus_2_2,
                        speed,
                        big_cactus_1_moving,
                        big_cactus_2_moving,
                        small_cactus_1_moving,
                        small_cactus_2_moving,
                        two_cactus_big1_moving,
                        two_cactus_big2_moving,
                        two_cactus_big3_moving,
                        two_cactus_big4_moving,
                        two_cactus_small1_moving,
                        two_cactus_small2_moving,
                        two_cactus_small3_moving,
                        two_cactus_small4_moving,
                        two_cactus_small_big1_moving,
                        two_cactus_small_big2_moving,
                        two_cactus_small_big3_moving,
                        two_cactus_small_big4_moving,
                        two_cactus_big_small1_moving,
                        two_cactus_big_small2_moving,
                        two_cactus_big_small3_moving,
                        two_cactus_big_small4_moving,
                        three_cactus_big1_moving,
                        three_cactus_big2_moving,
                        three_cactus_big3_moving,
                        three_cactus_big4_moving,
                        three_cactus_big5_moving,
                        three_cactus_big6_moving,
                        three_cactus_big7_moving,
                        three_cactus_big8_moving,
                        three_cactus_small1_moving,
                        three_cactus_small2_moving,
                        three_cactus_small3_moving,
                        three_cactus_small4_moving,
                        three_cactus_small5_moving,
                        three_cactus_small6_moving,
                        three_cactus_small7_moving,
                        three_cactus_small8_moving,
                    )
                    if (
                        (
                            array_small_cactus_2_2.x <= trex.x + 5
                            and array_small_cactus_2_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_2_1.x <= trex.x + 8
                            and array_small_cactus_2_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            small_cactus_2.x <= trex.x + 8
                            and small_cactus_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_1_2.x <= trex.x + 5
                            and array_small_cactus_1_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_small_cactus_1_1.x <= trex.x + 8
                            and array_small_cactus_1_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            small_cactus_1.x <= trex.x + 8
                            and small_cactus_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_big_cactus_2_2.x <= trex.x + 5
                            and array_big_cactus_2_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            array_big_cactus_2_1.x <= trex.x + 8
                            and array_big_cactus_2_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 7
                        )
                        or (
                            big_cactus_2.x <= trex.x + 8
                            and big_cactus_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            array_big_cactus_1_2.x <= trex.x + 5
                            and array_big_cactus_1_2.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            array_big_cactus_1_1.x <= trex.x + 8
                            and array_big_cactus_1_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                        or (
                            big_cactus_1.x <= trex.x + 8
                            and big_cactus_1.x >= trex.x - 8
                            and trex.y >= constants.TREX_Y - 16
                        )
                    ):
                        end_game(
                            game,
                            trex,
                            clouds,
                            small_cactus_1,
                            small_cactus_2,
                            big_cactus_1,
                            big_cactus_2,
                            array_big_cactus_1_1,
                            array_big_cactus_1_2,
                            array_big_cactus_2_1,
                            array_big_cactus_2_2,
                            array_small_cactus_1_1,
                            array_small_cactus_1_2,
                            array_small_cactus_2_1,
                            array_small_cactus_2_2,
                            points,
                        )
                    else:
                        points = points + 1
                        points_text.clear()
                        points_text.cursor(0, 0)
                        points_text.move(1, 1)
                        points_text.text("Score: {}".format(points))
                    # move the clouds while the trex is jumping
                    clouds.move(clouds.x - 0.1, clouds.y)
                    # make the trex jump
                    trex.move(
                        trex.x, trex.y - (constants.JUMP_HEIGHT / constants.SPRITE_SIZE)
                    )
                    # render everything
                    game.render_sprites(
                        [trex]
                        + [clouds]
                        + [big_cactus_1]
                        + [big_cactus_2]
                        + [small_cactus_1]
                        + [small_cactus_2]
                        + [array_big_cactus_1_1]
                        + [array_big_cactus_1_2]
                        + [array_big_cactus_2_1]
                        + [array_big_cactus_2_2]
                        + [array_small_cactus_1_1]
                        + [array_small_cactus_1_2]
                        + [array_small_cactus_2_1]
                        + [array_small_cactus_2_2]
                    )
                    # tick the game
                    game.tick()
            else:
                if up_button == constants.button_state["button_still_pressed"]:
                    up_button = constants.button_state["button_released"]
                else:
                    up_button = constants.button_state["button_up"]
        # when the down button is pressed move down
        if keys & ugame.K_DOWN:
            pass
        # update game logic
        # checks if the trex is in the air if it is it falls due to gravity
        if trex.y == (constants.TREX_Y - constants.JUMP_HEIGHT):
            finish_game = gravity(
                trex,
                game,
                clouds,
                small_cactus_1,
                small_cactus_2,
                big_cactus_1,
                big_cactus_2,
                array_big_cactus_1_1,
                array_big_cactus_1_2,
                array_big_cactus_2_1,
                array_big_cactus_2_2,
                array_small_cactus_1_1,
                array_small_cactus_1_2,
                array_small_cactus_2_1,
                array_small_cactus_2_2,
                speed,
                big_cactus_1_moving,
                big_cactus_2_moving,
                small_cactus_1_moving,
                small_cactus_2_moving,
                two_cactus_big1_moving,
                two_cactus_big2_moving,
                two_cactus_big3_moving,
                two_cactus_big4_moving,
                two_cactus_small1_moving,
                two_cactus_small2_moving,
                two_cactus_small3_moving,
                two_cactus_small4_moving,
                two_cactus_small_big1_moving,
                two_cactus_small_big2_moving,
                two_cactus_small_big3_moving,
                two_cactus_small_big4_moving,
                two_cactus_big_small1_moving,
                two_cactus_big_small2_moving,
                two_cactus_big_small3_moving,
                two_cactus_big_small4_moving,
                three_cactus_big1_moving,
                three_cactus_big2_moving,
                three_cactus_big3_moving,
                three_cactus_big4_moving,
                three_cactus_big5_moving,
                three_cactus_big6_moving,
                three_cactus_big7_moving,
                three_cactus_big8_moving,
                three_cactus_small1_moving,
                three_cactus_small2_moving,
                three_cactus_small3_moving,
                three_cactus_small4_moving,
                three_cactus_small5_moving,
                three_cactus_small6_moving,
                three_cactus_small7_moving,
                three_cactus_small8_moving,
                points,
                points_text,
            )
            if finish_game:
                end_game(
                    game,
                    trex,
                    clouds,
                    small_cactus_1,
                    small_cactus_2,
                    big_cactus_1,
                    big_cactus_2,
                    array_big_cactus_1_1,
                    array_big_cactus_1_2,
                    array_big_cactus_2_1,
                    array_big_cactus_2_2,
                    array_small_cactus_1_1,
                    array_small_cactus_1_2,
                    array_small_cactus_2_1,
                    array_small_cactus_2_2,
                    points,
                )
        if (
            (
                stage.collide(
                    array_small_cactus_2_2.x + 5,
                    array_small_cactus_2_2.y + 7,
                    array_small_cactus_2_2.x + 10,
                    array_small_cactus_2_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_small_cactus_2_1.x + 5,
                    array_small_cactus_2_1.y + 7,
                    array_small_cactus_2_1.x + 10,
                    array_small_cactus_2_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    small_cactus_2.x + 5,
                    small_cactus_2.y + 7,
                    small_cactus_2.x + 10,
                    small_cactus_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_small_cactus_1_2.x + 5,
                    array_small_cactus_1_2.y + 7,
                    array_small_cactus_1_2.x + 10,
                    array_small_cactus_1_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_small_cactus_1_1.x + 5,
                    array_small_cactus_1_1.y + 7,
                    array_small_cactus_1_1.x + 10,
                    array_small_cactus_1_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    small_cactus_1.x + 5,
                    small_cactus_1.y + 7,
                    small_cactus_1.x + 10,
                    small_cactus_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_big_cactus_2_2.x + 4,
                    array_big_cactus_2_2.y,
                    array_big_cactus_2_2.x + 12,
                    array_big_cactus_2_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_big_cactus_2_1.x + 4,
                    array_big_cactus_2_1.y,
                    array_big_cactus_2_1.x + 12,
                    array_big_cactus_2_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    big_cactus_2.x + 4,
                    big_cactus_2.y,
                    big_cactus_2.x + 12,
                    big_cactus_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_big_cactus_1_2.x + 4,
                    array_big_cactus_1_2.y,
                    array_big_cactus_1_2.x + 12,
                    array_big_cactus_1_2.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    array_big_cactus_1_1.x + 4,
                    array_big_cactus_1_1.y,
                    array_big_cactus_1_1.x + 12,
                    array_big_cactus_1_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
            or (
                stage.collide(
                    big_cactus_1.x + 7,
                    big_cactus_1.y,
                    big_cactus_1.x + 12,
                    big_cactus_1.y + 16,
                    trex.x,
                    trex.y,
                    trex.x + 16,
                    trex.y + 16,
                )
            )
        ):
            end_game(
                game,
                trex,
                clouds,
                small_cactus_1,
                small_cactus_2,
                big_cactus_1,
                big_cactus_2,
                array_big_cactus_1_1,
                array_big_cactus_1_2,
                array_big_cactus_2_1,
                array_big_cactus_2_2,
                array_small_cactus_1_1,
                array_small_cactus_1_2,
                array_small_cactus_2_1,
                array_small_cactus_2_2,
                points,
            )

        game.render_sprites(
            [trex]
            + [clouds]
            + [big_cactus_1]
            + [big_cactus_2]
            + [small_cactus_1]
            + [small_cactus_2]
            + [array_big_cactus_1_1]
            + [array_big_cactus_1_2]
            + [array_big_cactus_2_1]
            + [array_big_cactus_2_2]
            + [array_small_cactus_1_1]
            + [array_small_cactus_1_2]
            + [array_small_cactus_2_1]
            + [array_small_cactus_2_2]
        )
        game.tick()


if __name__ == "__main__":

    splash_scene()
