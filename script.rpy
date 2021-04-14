# This file contains the main script.

image bg black = "#000000"

label start:

    # Transition from main menu ------------------------------------------------

    stop music fadeout 0.5
    window hide

    scene bg black with dissolve
    pause 0.5

    # Main Aquarium Screen -----------------------------------------------------

    # INSERT BACKGROUND MUSIC/SFX HERE
    # $renpy.sound.play("sounds/INSERT_SOUND_FILE_HERE.MP3", loop=True)

    # Ocean background image
    scene background with dissolve

    # Seaweed (background, behind the characters)
    show bgSeaweed:
        xalign 0.35 yalign 1.0

    # Show bubbles and floating particles
    label bubbles:
        show bubbles_xs
        show bubbles_s
        show bubbles_sv2
        show bubbles_m
        show bubbles_l
        show bubbles_xl

    # CHARACTERS ----------------------------------------------------------------

    # HIM - Powerpuff Girls Villain
    show HIM:
        xalign 0.96 yalign 0.75
        flip_HIM

    # Smile - Ping Pong
    show smile:
        smile_spectate

    # Akagi - AKAGI
    show akagi:
        akagi_spectate

    # Rin - Yuru Camp
    show rin:
        truecenter
        swim

    # Oroch-eel-maru (Orochimaru from Naruto haha)
    show orochimaru:
        truecenter
        swim

    # Ozu - Tatami Galaxy
    show ozu:
        truecenter
        swim

    # Renge - Non Non Biyori
    show renge:
        truecenter
        swim

    # Iggly - Nintendo's Animal Crossing
    show iggly:
        truecenter
        swim

    # Other --------------------------------------------------------------------

    # Seaweed (foreground, in front of characters)
    show fgSeaweed:
        xalign -0.05 yalign 1.0

    # --------------------------------------------------------------------------


    # This pause line keeps the game from ending unless the user clicks.
    pause

    return
