# This file defines the images, assets, and transformations used in the main script file.

init:
    python:

        import random

# IMAGE POSITIONING ------------------------------------------------------------

# displays image in the horizontal and vertical center of the screen
transform truecenter:
    xalign 0.5 yalign 0.5

# PAUSE FUNCTIONS --------------------------------------------------------------

default timer = renpy.random.random()
default smile_timer = renpy.random.random()

init python:

    # pause for a random number of seconds (2~7)
    def timer_2_7(trans, st, at):
        global timer

        if st >= timer:
            timer = renpy.random.uniform(2,7)
            return None
        else:
            return 0

    # pause for a random number of seconds (10~30) - used for character 'Smile'
    def timer_10_30(trans, st, at):
        global smile_timer

        if st >= smile_timer:
            smile_timer = renpy.random.uniform(10, 30)
            return None
        else:
            return 0

# IMAGES, ANIMATIONS, AND ASSETS -----------------------------------------------

# Ocean background - 4 frames added for lighting effect
image background:

    "bg aquarium2.png" with Dissolve(2.25)
    pause 2.25
    "bg aquarium.png" with Dissolve(2.75)
    pause 2.75
    "bg aquarium3.png" with Dissolve(2.75)
    pause 2.75
    "bg aquarium4.png" with Dissolve(2.25)
    pause 2.25

    repeat

# Floating Bubbles

# Bubbles (Extra Small Size)
image bubbles_xs:
    SnowBlossom("object puff_xs.png", count=15, border=30, xspeed=(-100,100), yspeed=(-30, 30))

# Bubbles (Small Size)
image bubbles_s:
    SnowBlossom("object puff_s.png", 10, border=50, xspeed=(-100,100), yspeed=(-50, 50))

# Bubbles (Small Size, Version 2)
image bubbles_sv2:
    SnowBlossom("object puff_s2.png", 2, border=50, xspeed=(-100,100), yspeed=(-50, 50))

# Bubbles (Medium Size)
image bubbles_m:
    SnowBlossom("mediumbubble.png", 3, border=100, xspeed=(-10,10), yspeed=(-300, -600))

# Bubbles (Large Size)
image bubbles_l:
    SnowBlossom("object puff_l.png", 2, border=100, xspeed=(-10,10), yspeed=(-300, -600))

# animated bubble (Extra Large Size)
image bubble_xl:
    "XLbubble3.png"
    pause 0.2
    "XLbubble2.png"
    pause 0.2
    repeat

# Bubbles (Extra Large Size)
image bubbles_xl:
    SnowBlossom("bubble_xl", 1, border=200, xspeed=(-20,20), yspeed=(-300, -600))

# Seaweed in the background (behind the characters)
# needs to be shown before all "fish" are shown, in order to appear on bottom
image bgSeaweed:

    parallel:
        alpha 0.5
        xzoom -0.7 yzoom 0.7

    parallel:
        "seaweed2-1.png" with Dissolve(1.7)
        pause 1.7
        "seaweed2-2.png" with Dissolve(1.3)
        pause 1.3
        "seaweed2-3.png" with Dissolve(1.0)
        pause 1.0
        "seaweed2-1.png" with Dissolve(2.0)
        pause 2.0
        "seaweed2-3.png" with Dissolve(1.7)
        pause 1.7

        repeat

# Seaweed in the foreground (in front of the characters)
# needs to be shown after all "fish" are shown, in order to appear on top
image fgSeaweed:

    parallel:
        alpha 0.5

    parallel:
        "seaweed1.png" with Dissolve(1.0)
        pause 1.0
        "seaweed2.png" with Dissolve(1.0)
        pause 1.0
        "seaweed3.png" with Dissolve(1.0)
        pause 1.0
        "seaweed2.png" with Dissolve(1.0)
        pause 1.0
        "seaweed1.png" with Dissolve(1.0)
        pause 1.0

        repeat

# Smile - Ping Pong
image smile:
    "smile1.png"
    pause 1.6

    "smile2.png"
    pause 0.13

    "smile1.png"
    pause 3.6

    "smile2.png"
    pause 0.13

    repeat

# Akagi - AKAGI
image akagi:
    "akagi1.png"
    pause 2.5
    "akagi2.png"
    pause 0.1
    "akagi1.png"
    pause 1.5

    "akagi2.png"
    pause 0.1
    "akagi1.png"
    pause 0.15
    "akagi2.png"
    pause 0.1
    "akagi1.png"
    pause 1.0

    repeat

# Rin - Yuru Camp
image rin:
    "rin1.png"
    pause 0.1
    "rin2.png"
    pause 0.1

    repeat

# Ozu - Tatami Galaxy
image ozu:
    "ozu1.png"
    pause 0.3
    "ozu2.png"
    pause 0.3

    repeat

# Iggly - Nintendo's Animal Crossing
image iggly:
    "iggly1.png"
    pause 0.5
    "iggly2.png"
    pause 0.5

    repeat

# Renge - Non Non Biyori
image renge:
    "renge1.png"
    pause 0.7
    "renge2.png"
    pause 0.7

    repeat

# HIM - Powerpuff Girls Villain
image HIM:
    "HIM1.png"
    pause 0.6
    "HIM2.png"
    pause 0.6

    repeat

# Oroch-eel-maru (Orochimaru from Naruto haha)
image orochimaru:

    "orochimaru1.png"
    pause 0.2
    "orochimaru2.png"
    pause 0.2

    repeat

# TRANSFORMS -------------------------------------------------------------------

# Custom transform for Smile, who "goes up for air" sometimes
transform smile_spectate:

    xalign 0.97

    # floating in place
    parallel:
        easeout 3 yoffset -8
        easeout 1.33 yoffset 0
        repeat

    # "going up for air every 8~30sec" transform
    parallel:

        yalign 0.0

        function timer_10_30

        easeout 1.0 yalign -1.0

        function timer_10_30

        yalign -1.0

        pause 1.0

        easein 2.5 yalign 0.0

        repeat

# Custom transform for Akagi, who can stay underwater with his snorkel
transform akagi_spectate:

    xalign 0.75 yalign 0

    parallel:
        easeout 2 yoffset -5
        easeout 2 yoffset 0
        repeat


# General Swimming Transform function
transform swim:

# Note:
# ATL transforms are declarative (once a random int function is evaluated in a
# transform block, that value is stored and it does not re-evaluate when called
# again), so some statements have been duplicated in the swim transforms.

# I don't know that it's currently possible to incorporate it with a randomly
# generated t time for a varying swim speed, unfortunately.

# Suggestions are welcome, if anyone knows of a more elegant way to code this!

    # Characters swimming across the screen (X and Y)
    parallel:
        swim_LeftAndRight
    parallel:
        swim_UpAndDown

    #Gently float up and down a little, repeat
    parallel:
        swim_Float

    # Change image direction randomly
    parallel:
        flip

transform swim_LeftAndRight:

    choice:
        linear random.uniform(4,10) xalign random.uniform (-0.5, 0.5)

    choice:
        easein random.uniform(4,10) xalign random.uniform (0.5, 1.3)

    choice:
        easein random.uniform(4,10) xalign random.uniform (-0.5, 0.5)

    choice:
        easein random.uniform(4,10) xalign random.uniform (0.25, 0.75)

    choice:
        linear random.uniform(4,10) xalign random.uniform (0.25, 0.75)

    choice:
        easein random.uniform(4,10) xalign random.uniform (0.25, 0.75)

    choice:
        easeout random.uniform(4,10) xalign 0.0

    choice:
        easeout random.uniform(4,10) xalign 1.0

    # duplicates below -----------------

    choice:
        easeout random.uniform(4,10) xalign random.uniform (-0.5, 0.5)

    choice:
        easeout random.uniform(4,10) xalign random.uniform (0.5, 1.3)

    choice:
        easein random.uniform(4,10) xalign random.uniform (-0.5, 0.5)

    choice:
        easein random.uniform(4,10) xalign random.uniform (0.5, 1.3)

    repeat


transform swim_UpAndDown:

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.0, 0.5)

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.5, 1.3)

    choice:
        ease  random.uniform(4,10) yalign random.uniform (0.0, 0.5)

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.5, 1.3)

    choice:
        ease random.uniform(4,10) yalign 0.0

    choice:
        ease random.uniform(4,10) yalign 1.0

    # duplicates below -----------------

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.0, 0.5)

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.5, 1.3)

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.0, 0.5)

    choice:
        ease random.uniform(4,10) yalign random.uniform (0.5, 1.3)

    choice:
        pause 1.0

    choice:
        pause 1.0

    repeat

#Gently float up and down a little, constantly
transform swim_Float:
    easeout 2 yoffset 17
    easeout 2 yoffset -17
    repeat

# Change image direction after random number of seconds
transform flip:

    # pause 1.0 half the time for a more natural swimming look
    choice:
        pause 1.0
        linear 1.5 xzoom -1.0

    choice:
        function timer_2_7
        linear 1.5 xzoom -1.0

    choice:
        pause 1.0
        linear 1.5 xzoom 1.0

    choice:
        function timer_2_7
        linear 1.5 xzoom 1.0

    repeat

# Custom flip for character HIM (image flip slightly faster)
transform flip_HIM:

    choice:
        pause 1.0
        linear 0.5 xzoom -1.0

    choice:
        pause 1.0
        linear 0.5 xzoom -1.0

    choice:

        function timer_2_7
        linear 0.5 xzoom -1.0

    choice:

        function timer_2_7
        linear 0.5 xzoom 1.0

    repeat
