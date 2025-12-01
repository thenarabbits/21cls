# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define config.layers = ['master', 'transient', 'screens', 'overlay', 'ontop']
# tbh it's ok to remove lines 6-7 ^

# character define
define mc = Character("[playername]", image="player")
define cashier = Character("Cashier")
define p = Character("[performative]", image="kyren")
define n = Character("[narcissist]")
define w = Character("[weeb]")
# pnw = pacific northwest!
define teacher = Character("Mr. Teacher")
define classmate = Character("classmate")
define b1 = Character("Bully 1", image="bully1")
define b2 = Character("Bully 2", image="bully2")

# character sprites
image player neutral = "side player neutral.png"

image kyren neutral = "kyren_neutral.png"
image kyren angry = "kyren_angry.png"
image kyren sad = "kyren_sad.png"
image kyren happy = "kyren_happy.png"
image kyren shocked = "kyren_shocked.png"

image cashier_neutral = "cashier.png"
image classmate_neutral = "billG.jpg"

image narcissist_neutral = "narcissist_neutral.png"
image weeb_neutral = "weeb_neutral.png"

# image define b1 neutral = "bully1 neutral.png"
# image define b2 neutral = "bully2 neutral.png"

image b1_neutral = "bully1 neutral.png"
image b2_neutral = "bully2 neutral.png"

# define backgrounds
image bg school_street = "this_better_be_good_because_the_render_time_for_this_bg_is_horrendous_despite_having_a_render_farm.webp"
image bg cafe_outside = "cafe_memoria_outside_04_afternoon.webp"
image bg cafe = "cafe_memoria_inside_03_afternoon.webp"
image bg cafe_2 = "cafe_memoria_inside_01_afternoon.png"
image bg school_track = "school_track.webp"
image bg football_field = "football_field_day.webp"
image bg school_hallway_1 = "school_corridor_background.webp"
image bg school_hallway_2 = "uncle mugen school corridor morning.webp"
image bg school_nurse = "hospital.webp"

# The game starts here.

label start:

    scene bg school_street with fade

    $ playername = "You"
    $ performative = "???"
    $ narcissist = "Guy Sitting By Himself"
    $ weeb = "Guy With Disheveled Hair"

    mc neutral "Finally arrived at school... I'm so thirsty..."
    mc neutral "It's 7:15, I still have fifteen minutes until my first class."
    mc neutral "I should try to find a drink somewhere."
    
    scene bg cafe_outside with fade

    mc happy "Oh look, a cafe! So coincidental, I think I want a cup of coffee."

    scene bg cafe with fade

    show cashier_neutral with dissolve:
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

    hide cashier_neutral #with dissolve
    # current style is show w/ dissolve but no transition when hiding

    "It hasn't been long since you have transferred here to Milkyway High School from a private school in Beijing."
    "Surprisingly, even though this is a huge school in New York City, you are the only exchange student."
    "Hopefully, the year goes smoothly, and you can successfully focus on your academics to make your CEO father, lawyer mother, doctor brother, and engineer sister proud!"

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "I have an order for [playername]!"
    mc happy "Thank you kindly."
    cashier "Enjoy!"

    hide cashier_neutral
    
    jump episode_1
    # jump testinglol
    return

# label testinglol:
#     show kyren neutral with dissolve:
#         zoom 0.25
#         xcenter 0.5
#         yalign 1.0
#     # show p_neutral:
#     #     zoom 0.25
#     #     xcenter 0.5
#     #     yalign 1.0
#     p neutral "yo"
#     p happy "BRUH"
#     p sad "bruh..."

#     "END"
#     return


label episode_1:

    scene bg cafe_2 with fade 

    "You take a sip as you walk towards the closest empty table."
    "As the drink makes contact with your tongue, the taste of artificial sweetness floods your mouth."

    mc neutral "(This tastes pretty cheap compared to what I usually get back home... How many strange chemicals are in this thing?)"
    mc happy "(It's fine. I shouldn't be too picky with American products...)"

    "You sit down at an empty table and begin to take your laptop out of your backpack when your elbow accidentally tips over your drink."
    "Thankfully, you have fast reflexes, and you were able to catch the drink before it completely fell."
    "...However, a splash still managed to escape from the cup and onto the table."

    mc angry "...Are you kidding me?"
    mc neutral "Ugh, I need a napkin..."

    "Looking around the cafe, you try to locate where the napkins were stored, but you hear a series of footsteps approaching."

    $ performative = "???"

    p neutral "Excuse me, you needed a napkin, right?"

    "An unfamiliar voice directs itself to you. You look up to see who it is."

    $ performative = "Guy Wearing Quarter Zip-up"
    show kyren neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0

    "Extending a napkin to you, the boy gently smiles as he takes a sip out of his own drink that seems to exude the faint scent of low quality matcha."
    
    mc neutral "Oh, thank you."
    hide per_neutral
    p happy "Of course. Mind if I take a seat?"
    mc deadpan "...Go ahead."
    p neutral "Thank you."

    "The strange boy takes a seat directly across from you, but not before you notice a strange keychain dangling from his belt loop."
    "He sets a book down on the table that reads \"Feminist Literature by Cyx Sehvyn\" and hangs his tote bag on his chair."

    $ performative = "Kyren"

    p neutral "I'm Kyren, what's your name?"
    mc neutral "[playername]."
    p neutral "It's nice to meet you."
    p neutral "I saw you deciding between matcha and a frappuccino when I was waiting in line earlier. I've been drinking matcha before it became popular."
    mc deadpan "...Thanks for sharing."
    p neutral "Please forgive me if this sounds weird, but are you a foreign exchange student?"
    mc neutral "Yes, from China."
    p happy "Oh, China! I've always wanted to visit. I'd say I'm pretty familiar with your culture."
    mc happy "Really? I have always been proud of my culture and-"
    p neutral "I'm such a fan of \"The Drawing of War\" by Moon Tzu. It's such a beautiful and philosophical piece."
    mc deadpan "...What?"
    p neutral "And Chinese food is so delicious, I go to Tiandilao every week. But obviously authentic Chinese food is way better."
    p neutral "Chinese music is also incredible, I like pretty niche artists. You know... like Wackson Jang and Cay Jhou."
    p happy "Oh, and I can't forget to mention that mahjong just happens to be one of my favorite games."
    mc shocked "..."
    
    "You can't believe what you're hearing right now."
    "This guy just doesn't stop talking!"
    "You wonder if this guy even knows what he's talking about. Does he realize he just called THE Wackson Jang and Cay Jhou \"niche\"?"

    mc deadpan "What's your favorite Chinese song?"
    p shocked "...Huh?"
    p neutral "Haha, there's too many to choose from! I can't pick one when all of them are so good."
    mc deadpan "(...This guy doesn't know what he's talking about.)"
    p happy "Anyway, what do you like to do for fun?"
    mc neutral "Um... I like to..."

    menu:
        "Listen to music":
            p happy "I love music too! Like Keshy, Beebahdoobee, Klairo..." 
            p neutral "You can say I'm pretty niche."
        "Draw and paint":
            p happy "That's so fun! I love art too. It's a shame that AI art is getting so popular..."
            p sad "It's really taking away from true talent in this age."
        "Play video games":
            p neutral "I love video games too! I like Balorant and Weague of Wegends."
            p happy "Let's play sometime!"
        "Read books":
            p happy "I love feminist literature. I read it all the time, as you can see."
            p angry "Men these days have such fragile masculinity, good thing I'm not like them."
        "Collect blind boxes":
            p happy "I really like collecting blind boxes too."
            p neutral "Especially Smyskeez and Wabubus."

    p happy "Wow, we have so much in common!"
    mc deadpan "...Sure."
    p neutral "Can I get your UsChat?"
    mc neutral "Since when do Americans use UsChat?"
    p neutral "Heh, I'm pretty cultured and open-minded."
    p happy "I've been like this because of all the feminist literature I've read since I was young."

    menu:
        "Give him your UsChat":
            mc neutral "...Alright, scan my QR code."
            p happy "Thanks! Or, should I say, xiexie!"
        "Don't give him your UsChat":
            p shocked "Huh? I'm not like other guys who ask for your socials, promise."
            p neutral "I just want to be friends with someone with common interests."
            mc deadpan "...Alright, scan my QR code."

    "You take out your phone and notice that it's 7:25. Your first class starts in only five minutes!"
    "Quickly opening UsChat, Kyren scans your QR code and sends you a friend request. You reluctantly accept the friend request before throwing your bag over your shoulders."

    mc neutral "...School is starting soon. See you."
    p shocked "Wait, do you also like to go thrifting-"


    jump episode_2
    return

# THIS SECTION IS A SKIP TO THE NARCISSIST SCENE

label episode_2:
    
    $ met_narcissist = False

    scene bg school_track with fade

    "After exiting the nurse's office, you think about your interaction with Kyren."

    mc deadpan "(That guy was odd... Whatever)"
    mc neutral "(Okay... now it's time for first period. My first class is PE.)"

    # REPLACE WITH GYM COACH LATER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0
    teacher "Hey! You're [playername], right?"
    teacher "Hurry and join the rest of the class for football."
    mc neutral "Yes, sir."
    hide cashier_neutral with dissolve

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

# lol i just realized i probably don't need to use show and hide so many times...
# maybe i'll rewrite this later - Kaylee

label episode_2_meeting:

    scene bg football_field with fade

    if choice == "care":
        show narcissist_neutral with dissolve
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
        
        $ narcissist = "Snobby Guy"
        n "THE DISRESPECT! Just wait until I tell my father, who is a CEO, by the way, about this insolence!"
        mc deadpan "(...Did I ever ask?)"
        n "And since you're uneducated, I'll show some mercy and inform you about WHO I am exactly."
        $ narcissist = "Ronan"
        n "I am Ronan, Ronan X.Y. Sinclair! The first in line to inherit the reputable Sinclair X.Y. Industries!"
        mc neutral "(Sinclair X.Y. Industries... kind of rings a bell. I think they source parts from dad's company?)"
        mc deadpan "And? Don't get on a high horse. My father is a CEO too."
        
        n "Ha! Tell me, then, what famous company is your father the CEO of?"
        mc deadpan "Fuyu Group."
        n "..."
        n "...Huh?"
        mc happy "(Exactly.)"

        "You notice the snobby guy's left eye twitch, but then he composes himself in a split second."

        show narcissist_neutral
        n "...Ahem! Hohoho! Why didn't you say so sooner?"

        "Amidst your conversation, it appears that the football game has just ended."
        hide narcissist_neutral
        show cashier_neutral with dissolve:
            zoom 1.5
            xcenter 0.5
            yalign 1.0
        teacher "Good job, Team 1! Quick water break, and we'll start the next game in 2 minutes."
        "Mr. Teacher points at you and [narcissist]."
        show cashier_neutral with dissolve:
            zoom 1.5
            xcenter 0.5
            yalign 1.0
        teacher "You two, join the next game—or else I can't give you points for the day."
        hide cashier_neutral

        mc neutral "Yes, sir."
        show narcissist_neutral
        n "*mumbling* Hmph, I wouldn't join otherwise."
        hide narcissist_neutral

        jump episode_2_join

    return

label episode_2_join:

    scene bg football_field with fade

    mc happy "I love American football!"
        # ig change neutral to shocked expression later? idk
        
        # b1 neutral "OHHHHHHH!!!"
        #IDKWHY the shorthand isn't working

        # btw we will probably need to come back and tweak the transformations
    "Though you don't get much action besides walking back and forth, it's already tiring to keep watching where the ball goes."
    # mc angry "Hey! Not everyone can be athletically gifted."
    # "...My bad."
    "Interrupting you from zoning out, someone points their finger your way."
    mc neutral "Huh?"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "OHHHHHH!!!"

    hide b1_neutral

    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    b2 "Don't yell right next to me."
    hide b2_neutral

    if met_narcissist:
        mc deadpan "(Do these people also have a CEO father?)"
    # else:
    #     "The commotion of your classmates catches your attention."
    #     "Seems like they noticed you too!"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "That's the new student! The one from Beijing!"
    hide b1_neutral
    mc deadpan "(Am I some kind of zoo animal? (-_-;))"
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    b2 "For real? I thought she would look, y'know, more classy. Isn't her dad a CEO or something?"
    # still debating whether to put this before or after the ball hit/nurse's office thing
    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "Oh, really? Why would she would move here? Away from her luxurious mansion?"

    hide b1_neutral
    "Before any words leave your mouth, a voice from behind speaks up."

    if met_narcissist == False:
        $ narcissist = "???"

    show narcissist_neutral with dissolve
    n "Peasants, disperse!"
    hide narcissist_neutral

    "In some unexplainable supernatural phenomenon, a burst of light shines upon you."
    mc shocked "What the..."
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    b2 "Ronan!!! Your drip!!!! The bling!!!! It's so blinding!!!!"
    $ narcissist = "Ronan"

    hide b2_neutral
    
    if met_narcissist == False:
        mc neutral "(So his name is Ronan...)"
        mc "(But is this a normal occurrence?)"
    else:
        mc neutral "(Is this a normal occurrence?)"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "Hey, watch out-"
    hide b1_neutral
    "The peasant tries to warn the other of the incoming tackle, but their efforts are futile."
    "A peasant is struck down before the two leave just as quickly as how you met them."

    show narcissist_neutral with dissolve
    n "Hmph! That's more like it."
    
    "Then, Ronan and you make eye contact."

    # 2do: update character n so we can use the emotion shorthand thingies
    show narcissist_neutral with dissolve
    if met_narcissist:
        n "Oh, it's that insolent brat."
        menu:
            "Excuse me?":
                n "You're excused!"
                mc deadpan "..."
                mc "(He's not supposed to be in elementary school, right...?)"
            "(Pretend like you didn't hear anything.)":
                mc neutral "..."
        "Ronan slicks his hair back. It's, like, the equivalent of a cool girl's hair flip."
        n "Hmph! I forgive you for your transgressions."
        n "After all, I'm young, rich, tall, handsome, AND nice."
        n "I recognize my kind when I see one."
        "He sent you a wink~☆ but unfortunately, you blinked right then, so you didn't notice."
        mc deadpan "What? (-_-;;)"
        n "Dear me. You're quite slow. Be grateful for this opportunity to network with me, that is, RONAN X.Y. SINCLAIR!"
    else:
        mc neutral "Uh, I'm [playername]. And I don't believe we've met before."
        n "What, have you been living under a rock all your life? Or do you really not know who I am?"
        $ narcissist = "Ronan"
        n "I am Ronan, Ronan X.Y. Sinclair! The first in line to inherit the reputable Sinclair X.Y. Industries!"
        mc neutral "(Sinclair X.Y. Industries... kind of rings a bell. I think they source parts from dad's company?)"
        mc deadpan "And? Don't get on a high horse. My father is a CEO too."
        
        n "Ha! Tell me, then, what famous company is your father the CEO of?"
        mc deadpan "Fuyu Group."
        n "..."
        n "...Huh?"
        mc happy "(Exactly.)"

        "You notice the snobby guy's left eye twitch, but then he composes himself in a split second."

    "Then Ronan looks at you expectantly, waiting for you to initiate the handshake and say \"It's an honor to meet you\" and whatnot."
    "But pity, you can't read his mind. And he doesn't realize that not everyone can read his mind since his closest attendants are so used to his habits and daily schedule."
    "So there's just 10 seconds of silent, awkward eye contact, until..."
    
    mc shocked "WATCH OUT!!!!!"
    "*THWACK*"
    "In a perfect parabolic path, the football flies by and slaps Ronan right in the cheek."
    "As graceful as a swan, Ronan falls to the ground. And in slow motion, too. But at least he landed in the lush football field of fake grass."
    
    hide narcissist_neutral

    "*tweet*"
    "It's Mr. Teacher, blowing the whistle and dashing over."

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0
    teacher "Tsk tsk. You guys can't just stand around and chit-chat!"

    hide cashier_neutral
    "Mr. Teacher glances down at the fallen Ronan, who's out cold. He presses his finger against his temple and sighs."
    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0
    teacher "[playername], could you take him to the nurse's office? I can excuse your participation points for the day."
    mc shocked "Yes, sir. But where may I find the nurse's office?"
    teacher "Right, sorry. You're new. The nurse's office is just over there, next to the teachers' office."
    "Mr. Teacher points to the main building."
    teacher "Take this as an opportunity to familiarize yourself with the campus."
    mc neutral "Yes, sir."

    "You load the fainted Ronan onto your back, and Mr. Teacher goes back to monitoring the football game."

    hide cashier_neutral

    "Of course, not without prying eyes."

    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5 
        yalign 1.0
    b2 "Hey, look."

    hide b2_neutral

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "Oh my gosh." # :P
    b1 "Olivia's gonna tweak if she hears about this."
    
    jump episode_2_nurse
    return

label episode_2_nurse:
    
    scene bg school_nurse with fade

    "20 minutes later..."

    show narcissist_neutral
    n "Ugh, my head..."
    # "Wincing, Ronan tossed and turned until, finally, he could think more clearly. To some extent."
    "Slowly coming to, Ronan sat himself up."
    "He winced and rubbed his right cheek, which was oddly numb. And cold."
    n "Am...I dead?"
    #shaking head gif maybe?
    n "*shakes head* No, no! I can't die now. I still need to join Dad in the shareholders' meeting after school!"
    # "Ronan smirks and does his Cool Hair Flip."
    
    mc happy "What a miracle. You're totally fine."

    "Ronan glances around and is vaguely able to identify you, who has just returned a warmed-down ice pack to the school nurse. A wave of relief washes over him."
    $ playername_length = len(playername)

    if playername_length >= 4:
        $ playername_twisted = playername[0:3]
        n "Who are you again? [playername_twisted]—no, my SAVIOR!"
    else:
        n "Insolent brat? No, I mean, my savior!"
        mc deadpan "(Dude, make up your mind.)"
    n "Hmph. I give credit where it is due, and I commend your dedication to safeguard the life of the Sinclair X.Y. Industries heir."
    n "That is me, Ronan X.Y. Sinclair! *Cool Hair Flip*"



    # n "Listen, I don't do this often, but "
    # does narcissist give mc a reward? that's what i was thinking, but i wanna make the story more interesting

    jump episode_3
    return

# ep3 AFTER mc's interactions w/ ronan
label episode_3:

    scene bg school_hallway_1 with fade

    "After exiting the nurse's office, you think about your interaction with Ronan."

    mc neutral "(That guy is so irritating when he's fully conscious.)"
    mc deadpan "(He really is like an elementary school student.)"

    "Taking your phone out, you see that there is only ten more minutes of class."

    mc neutral "(There's no point in heading back. Maybe I should just stay in the restroom until the bell rings-)"

    "*BANG!*"
    "\"Loser! Who do you think you are?!\""

    mc shocked "What was that?"

    "Right as when you were about to head towards the restroom, a loud bang echoed through the halls."
    "Will you investigate what the commotion is?"

    menu:
        "Choose to investigate":
            mc neutral "(I should see what's going on.)"
            jump episode_3_meeting
        "Choose not to investigate":
            mc deadpan "(Not my problem.)"
            jump episode_3_meeting_2

    return

# choosing to investigate, seeing lucien get beat
label episode_3_meeting:

    scene bg school_hallway_2 with fade

    mc neutral "(What the...)"

    "You head over to where you heard the loud bang and yelling..."
    "...only to see two familiar faces standing in front of the lockers."

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "You think you're tough? Walking on MY turf as if you own the place?"

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5 
        yalign 1.0

    b2 "Our turf."

    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "Shut up!"

    hide b1_neutral

    "As your two classmates continue yelling at each other, you're not sure what to do."
    "However, you notice someone slumped on the ground against the lockers."

    mc deadpan "(What is going on? Aren't these two supposed to still be in class?)"
    mc neutral "(And who is that?)"

    show weeb_neutral with dissolve

    w "Y-y-y-y-y-y-y-you cannot threaten me! This pure love is everlasting!"

    hide weeb_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "Tch, what are you saying?!"
    b1 "Don't you understand that she's MY girlfriend?! Keep your filthy paws away from her!"
    b1 "I saw how you were looking at her so shamelessly!"

    mc deadpan "(I should get a teacher-)"

    "*POW!*"
    "Your classmate punches the poor guy in the face, knocking his glasses off his face!"
    "Right before you were about to go find a teacher to break apart the conflict, you can't help but notice the guy is..."
    "...oddly good looking for someone so disheveled?"

    b1 "You freak, don't you-"
    b1 "...Huh?"

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5 
        yalign 1.0
    
    b2 "Why do you look so..."

    hide b2_neutral
    show weeb_neutral with dissolve

    w "Y-y-you... *sniff* you cannot break us apart!"
    w "I've been reading \"That Time I Got Reincarnated 21 Times in a Fantasy World\" since the first volume came out!"
    w "A-a-and I've been loyal to my waifu, Suzuki Haruka, ever since!"
    w "N-n-n-n-n-n-n-no matter what you do, you cannot tear this love apart!"
    w "This love, so fresh and whole, is bound to last forever!!!"
    w "I will not allow you to take my waifu away from me!!"

    mc shocked "..."

    hide weeb_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    
    b1 "..."

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5 
        yalign 1.0
    
    b2 "..."
    
    hide b2_neutral

    "..."

    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "Bro, what are you talking about?"
    b1 "What is That Time I Got... whatever world? What is a Suzu... what?"

    hide b1_neutral
    show weeb_neutral

    w "No! Call her by her full name!"
    w "She is Princess Suzuki Haruka!"

    hide weeb_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5 
        yalign 1.0

    b2 "What in the world are you talking about?"

    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "Yeah bro, what?"
    b1 "We're talking about how your lame self was hitting on my girl, Sophia."

    hide b1_neutral
    show weeb_neutral with dissolve

    w "...Huh? Who's Sophia?"
    mc shocked "..."

    hide weeb_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "..."

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0

    b2 "..."

    hide b2_neutral

    "..."

    "What are any of these people talking about?"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "...My girlfriend?"

    hide b1_neutral
    show weeb_neutral with dissolve

    w "Huh? I don't want her. My heart only belongs to my waifu!"

    hide weeb_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0

    b2 "Then why were you looking so intensely?"

    hide b2_neutral
    show weeb_neutral with dissolve

    w "..."
    w "The poster on the wall above her had my waifu-"

    hide weeb_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "I'm sick of this kid! And you smell horrible! Trying to act crazy as an excuse or what?!"
    
    "YOu stare in confusion as the rowdy bully suddenly lifts a leg, about to kick the poor kid."

    mc deadpan "(Maybe I should intervene...)"

    menu:
        "Try to resolve the conflict with words":
            mc neutral "Shouldn't you two be in class still?"
        "Run away with the disheveled guy":
            mc deadpan "..."


    return


# choosing to ignore, seeing lucien running away
label episode_3_meeting_2:

    scene bg school_hallway_1 with fade

    mc neutral "(Now... where is the restroom...)"

    "As you walk through the halls trying to find where the restroom is, a series of quick footsteps gets closer."
    "...And as you turn the corner, you accidentally bump into someone, sending the both of you falling to the ground."

    mc shocked "Ow!"

    show weeb_neutral with dissolve

    w "A-ah!"

    "Looking up from the ground, you see a boy with extremely disheveled hair, wearing clothes that... probably haven't been washed in a while."
    "The lenses of his glasses are foggy, preventing you from seeing his eyes."
    
    mc deadpan "(...Does this guy not look where he's going?)"
    
    "Brushing off your clothes, you stand up and extend a hand out to the boy."

    mc neutral "Are you alright?"
    w "..."
    mc deadpan "...Hello?"

    "Without responding to you, the boy takes off his glasses with shaky hands and wipes the lenses with the bottom of his shirt before finally making eye contact with you."
    "And before you could repeat yourself, you can't help but notice the guy is..."
    "...oddly good looking for someone so disheveled?"

    mc deadpan "Um, I said, are you alright?"
    w "..."
    mc angry "Can't you hear me? I asked if-"
    w "Suzuki Haruka?!"
    mc deadpan "...What?"
    w "Y-y-y-you... y-y-y-you're a carbon copy!! She's... she's real!!!"
    mc angry "What are you talking about? Are you alright or not?"
    w "Oh my god, oh my god, oh my god..."

    hide weeb_neutral

    "Before you could question what on earth this guy was talking about, a rowdy yell interrupts:"
    "\"Ugh, where did that kid go?!\""

    mc neutral "(Huh? That voice sounds a bit familiar.)"

    show b1_neutral with dissolve

    b1 "Hey punk! Where are you running off to?!"
    b1 "Huh?"
    b1 "Nepo baby! Why are you here?"

    hide b1_neutral
    show weeb_neutral with dissolve

    w "G-G-GAH!!!"

    "In the blink of an eye, the disheveled guy gets up from the floor and runs to hide behind you."

    w "P-p-p-please save meeeeeeeeeeeeee!!!!!!"

    return










