# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define config.layers = ['master', 'transient', 'screens', 'overlay', 'ontop']
# tbh it's ok to remove lines 6-7 ^

define mc = Character("[playername]", image="player")
define cashier = Character("Cashier")
define teacher = Character("Mr. Teacher")
define classmate = Character("classmate")
define b1 = Character("Bully 1", image="bully1")
define b2 = Character("Bully 2", image="bully2")
define n = Character("[narcissist]")

# character sprites
image define mc neutral = "side player neutral.png"

image cashier_neutral = "cashier.png"
image classmate_neutral = "billG.jpg"
image narcissist_neutral = "narcissist_neutral.png"

# image define b1 neutral = "bully1 neutral.png"
# image define b2 neutral = "bully2 neutral.png"

image b1_neutral = "bully1 neutral.png"
image b2_neutral = "bully2 neutral.png"

# define backgrounds
image bg school_street = "this_better_be_good_because_the_render_time_for_this_bg_is_horrendous_despite_having_a_render_farm.webp"
image bg cafe_outside = "cafe_memoria_outside_04_afternoon.webp"
image bg cafe = "cafe_memoria_inside_03_afternoon.webp"
image bg school_track = "school_track.webp"
image bg football_field = "football_field_day.webp"

# The game starts here.

label start:

    scene bg school_street with fade

    $ playername = "You"
    $ narcissist = "Guy Sitting By Himself"

    mc neutral "Wow, I'm sooooo thirsty..."
    
    scene bg cafe_outside with None

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
    
    $ met_narcissist = False

    mc neutral "(Okay... now it's time for first period. The first class is PE.)"
    mc neutral "(I should probably head to the field.)"
    scene bg school_track with fade

    # REPLACE WITH GYM COACH LATER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    show cashier_neutral:
        zoom 1.5
        xcenter 0.5
        yalign 1.0
    teacher "Hey! You're [playername], right?"
    teacher "Hurry and join the rest of the class for football."
    mc neutral "Yes, sir."
    hide cashier_neutral

    "You can already hear shouts and action from afar."
    menu:
        "Run and join the game.":
            $ choice = "join"
            jump episode_2_join
        "Wait on the sidelines for the next round.":
            jump episode_2_football
    return

label episode_2_football:
    scene bg football_field with fade

    mc neutral "Oh?"
    "While your classmates are having fun tackling each other in the heat, someone sits by themself on a bench."
    menu:
        "Approach them.":
            mc neutral "I'm not doing anything right now, anyways."
            $ choice = "care"
            jump episode_2_meeting

    return

label episode_2_meeting:

    scene bg football_field with fade

    if choice == "care":
        show narcissist_neutral
        $ met_narcissist = True
        n "*grumbling* This game is for brokies."
        "The way this guy pouts kind of reminds you of an elementary school student."

        menu:
            "Who are you?":
                mc neutral "Who are you?"
                show narcissist_neutral
                n "You don't know who I am?"
            "Weirdo...":
                mc deadpan "Weirdo..."
                show narcissist_neutral
                n "Are you talking to me, peasant?"
        
        n "THE DISRESPECT! Just wait until I tell my father, who is a CEO, by the way, about this insolence!"
        mc deadpan "And? Don't get on a high horse. My dad is a CEO too."
        
        "You notice the snobby guy's left eye twitch, but then he composes himself in a split second."

        $ narcissist = "Snobby Guy"
        show narcissist_neutral
        n "Hohoho! Why didn't you say so sooner?"

        "The classmates playing football suddenly erupt with laughter (and some groans)."
        show cashier_neutral:
            zoom 1.5
            xcenter 0.5
            yalign 1.0
        teacher "Good job, Team 1! Quick water break, and we'll start the next game in 2 minutes."
        "Mr. Teacher points at you and [narcissist]."
        show cashier_neutral:
            zoom 1.5
            xcenter 0.5
            yalign 1.0
        teacher "You two, join the next game—or else I can't give you points for the day."

        mc neutral "Yes, sir."
        n "*mumbling* Hmph, I wouldn't join otherwise."

        jump episode_2_join

    return

label episode_2_join:

    scene bg football_field with fade

    mc happy "I love American football!"
        # ig change neutral to shocked expression later? idk
        
        # b1 neutral "OHHHHHHH!!!"
        #IDKWHY the shorthand isn't working

        # btw we will probably need to come back and tweak the transformations
    show b1_neutral:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "OHHHHHH!!!"

    hide b1_neutral

    show b2_neutral:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    b2 "Don't yell right next to me."
    hide b2_neutral

    if met_narcissist:
        "Oh, it seems that two peasants have finally noticed your presence."
    else:
        "Gasp! It's your first official meeting with two of your classmates!"
        "Could this be..."
        "A chance to make friends already?!"

    show b1_neutral:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "That's the new student! The one from Beijing!"
    b2 "Oh foreal? I thought she would look, y'know, more classy. Isn't her dad a CEO or something?"
    # still debating whether to put this before or after the ball hit/nurse's office thing
    b1 "Oh fr?"
    "Before any words leave your mouth, a voice from behind speaks up."


    "You've reached the end :p" # mark so i can still go back while testing the game
    return

