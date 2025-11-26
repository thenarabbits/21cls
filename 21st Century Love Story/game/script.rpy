# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define config.layers = ['master', 'transient', 'screens', 'overlay', 'ontop']

define mc = Character("[playername]", image="player")
define cashier = Character("Cashier")
define teacher = Character("Mr. Teacher")

# character sprites
image define mc neutral = "side player neutral.png"


image cashier_neutral = "cashier.png"

# define backgrounds
image bg cafe_outside = "cafe_memoria_outside_04_afternoon.webp"
image bg cafe = "cafe_memoria_inside_03_afternoon.webp"
image bg football_field = "football_field_day.webp"

# The game starts here.

label start:

    $ playername = "You"

    mc neutral "Wow, I'm sooooo thirsty..."
    
    scene bg cafe_outside with fade

    mc happy "Oh look, a cafe! So coincidental, I think I want a cup of coffee."

    scene bg cafe with None

    show cashier_neutral:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Welcome, what can I get for you today?"

    menu:
        "Can I get a matcha latte?":
            $ choice = "matchalatte"
            jump intro
        "Can I get a frappuccino?":
            $ choice = "frappuccino"
            jump intro

    return

label intro:

    if choice == "matchalatte":
        cashier "Good choice!"
        cashier "Our matcha is the best of the best!"
        jump intro2
    elif choice == "frappuccino":
        cashier "Are you sure? I think I'll give you a matcha latte instead."
        mc deadpan "Um..."
        menu:
            "That's fine.":
                jump intro2
            "No, I said what I said.":
                jump intro2

    return

label intro2:

    $ playername = renpy.input("Alright then, can I get a name for your order?", length=32) # length=32 is optional
    $ playername = playername.strip() # remove leading/trailing whitespace
    # Set a default name if the player leaves it blank
    if not playername:
        $ playername = "You"

    # use character to say their name
    mc neutral "It's [playername]."
    cashier "Okay, I'll have it ready soon."

    hide cashier_neutral

    "It hasn't been long since you have transferred here to Milkyway High School from a private school in Beijing."
    "Surprisingly, even though this is a huge school in New York City, you are the only exchange student."
    "Hopefully, the year goes smoothly, and you can successfully focus on your academics to make your CEO father, lawyer mother, doctor brother, and engineer sister proud!"

    show cashier_neutral:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "I have an order for [playername]!"
    mc happy "Thank you kindly."
    cashier "Enjoy!"

    hide cashier_neutral
    # REPLACE EPISODE 2 WITH ACTUAL FIRST EPISODE LATER!!!!!!!!!!!!!!!!!!!!!!!!!!!
    jump episode_2
    return

# THIS SECTION IS A SKIP TO THE NARCISSIST SCENE

label episode_2:
    mc neutral "(Okay... now it's time for first period. The first class is PE.)"
    mc neutral "(I should probably head to the field.)"
    scene bg football_field with fade

    # REPLACE WITH GYM COACH LATER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    show cashier_neutral
    teacher "Hey! You're [playername], right?"
    teacher "Hurry and join the rest of the class for football."
    mc neutral "Yes, sir."
    hide cashier_neutral

    return

