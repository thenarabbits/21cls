# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[playername]")
define cashier = Character("Cashier")
screen mc_neutral():
    add "mc_neutral.jpg" xalign 0.0 yalign 1.0 zorder 100.0
image cashier_neutral = "cashier.png"
image bg cafe = "cafe_memoria_inside_01_afternoon.png"

# The game starts here.

label start:

    $ playername = "You"
    scene bg cafe
    show screen mc_neutral

    mc "Wow, I'm sooooo thirsty..."
    mc "Oh look, a cafe! So coincidental, I think I want a cup of coffee."

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
        mc "Um..."
        menu:
            "That's fine.":
                $ choice = "frappe"
                jump intro2
            "No, I said what I said.":
                $ choice = "matcha"
                jump intro2

    return

label intro2:

    $ playername = renpy.input("Alright then, can I get a name for your order?", length=32) # length=32 is optional
    $ playername = playername.strip() # remove leading/trailing whitespace
    # Set a default name if the player leaves it blank
    if not playername:
        $ playername = "You"

    # use character to say their name
    mc "It's [playername]."
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
    mc "Thank you kindly."
    cashier "Enjoy!"

    hide cashier_neutral

