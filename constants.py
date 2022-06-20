#!/usr/bin/env python3
 
# Created by: Nicolas Riscalas
# Created on: June 2022
# This is the constants file for CPT
 
# PyBadge screen size is 160 x 128
# set the x max
SCREEN_X = 160
# set the y max
SCREEN_Y = 128
# set the grid x max
SCREEN_GRID_X = 10
# set the grid y max
SCREEN_GRID_Y = 8
# set the sprite max size
SPRITE_SIZE = 16
# set the maximum aliens
TOTAL_NUMBER_OF_ALIENS = 5
# set the max FPS
FPS = 60
# set the sprite's movement speed
SPRITE_MOVEMENT_SPEED = 1
# set the floor
FLOOR_Y = 111
# cloud height
CLOUDS_Y = 32
# cloud start x
CLOUDS_X = 144
# stars y
STARS_Y = 0
# t-rex y
TREX_Y = 95
# cactus max
TOTAL_CACTUS = 7
# off screen constant
OFF_SCREEN_X = -16
OFF_SCREEN_Y = -16
# cactus max x
BIG_CACTUS_X = 148
SMALL_CACTUS_X = 150
# set the jump height
JUMP_HEIGHT = 24
 
 
#button state dictionary
button_state = {
    "button_up" : "up",
    "button_just_pressed" : "just pressed",
    "button_still_pressed" : "still pressed",
    "button_released" : "released"
}
 
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
