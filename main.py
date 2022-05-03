def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        # . . . .
        . . . # .
        # . . . .
        . . . . .
""")
basic.show_leds("""
    # . . . .
        # # . . .
        . . . . #
        # # . . .
        # . . . .
""")
basic.show_leds("""
    # # . . .
        # # # . .
        . . . . .
        # # # . .
        # # . . .
""")
basic.show_leds("""
    . # # # .
        # # # . .
        # # . . .
        # # # . .
        . # # # .
""")
for index in range(4):
    basic.show_leds("""
        . # # # .
                # # # # #
                # # . . .
                # # # # #
                . # # # .
    """)
    basic.show_leds("""
        . # # # #
                # # # # .
                # # . . .
                # # # # .
                . # # # #
    """)
basic.show_leds("""
    . . # # #
        . # # # #
        . # # . .
        . # # # #
        . . # # #
""")
basic.show_leds("""
    . . . # #
        . . # # #
        . . # # .
        . . # # #
        . . . # #
""")
basic.show_leds("""
    . . . . #
        . . . # #
        . . . # #
        . . . # #
        . . . . #
""")
basic.show_leds("""
    . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
