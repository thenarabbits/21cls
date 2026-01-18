# The script of the game goes in this file.

# TODO: in episode 2 (ronan), remove bullies and replace with turtleneck overheating scene
# TODO: maybe also revise episode 4? @thenarabbits feel free to edit anything to make story smoother

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define config.layers = ['master', 'transient', 'screens', 'overlay', 'ontop']

    transform blur_screen:
        blur 0.0
        easeout 0.5 blur 16.0

    # far left side
    transform move_left:
        easeout 0.3 xalign 0.25

    # right side
    transform olivia_move_left:
        easeout 0.3 xalign 0.75
    
    transform move_back_to_middle:
        easeout 0.3 xalign 0.5

default playername = "You"
default performative = "Kyren"
default narcissist = "Ronan"
default weeb = "Lucien"
default gymbro = "King"
default meangirl = "Olivia"
# if this is true, then olivia becomes your enemy - otherwise, you become friends
default olivia_ticked_off = False

# character define
define mc = Character("[playername]", image="player")
define cashier = Character("Cashier")
define p = Character("[performative]", image="kyren")
define n = Character("[narcissist]")
define w = Character("[weeb]")
define g = Character("[gymbro]", image="king")
define teacher = Character("Mr. Teacher")
define classmate = Character("classmate")
define b1 = Character("Bully 1", image="bully1")
define b2 = Character("Bully 2", image="bully2")
# mean gurlz
define o = Character("[meangirl]", image="olivia")

# character sprites
image player neutral = "side player neutral.png"

image kyren neutral = "kyren_neutral.png"
image kyren angry = "kyren_angry.png"
image kyren sad = "kyren_sad.png"
image kyren happy = "kyren_happy.png"
image kyren shocked = "kyren_shocked.png"

image king neutral = "gymbro_neutral.png"
image king disgusted = "gymbro_disgusted.png"
image king angry = "gymbro_angry.png"

image cashier_neutral = "cashier.png"
image classmate_neutral = "billG.jpg"

image narcissist_neutral = "narcissist_neutral.png"
image weeb_neutral = "weeb_neutral.png"
image b1_neutral = "bully1 neutral.png"
image b2_neutral = "bully2 neutral.png"

image olivia neutral = "olivia neutral.png"
image olivia happy = "olivia happy.png"
image olivia angry = "olivia angry.png"
image olivia sad = "olivia sad.png"
image olivia shocked = "olivia shocked.png"

# cutscene images
image manga = "manga.png"
image manga_run = "manga_run_cutscene.png"

# define backgrounds
    # general backgrounds
image bg black_background = "black-background.png"
    # school backgrounds
image bg school_street = "this_better_be_good_because_the_render_time_for_this_bg_is_horrendous_despite_having_a_render_farm.webp"
image bg cafe_outside = "cafe_memoria_outside_04_afternoon.webp"
image bg cafe = "cafe_memoria_inside_03_afternoon.webp"
image bg cafe_2 = "cafe_memoria_inside_01_afternoon.png"
image bg school_track = "school_track.webp"
image bg football_field = "football_field_day.webp"
image bg school_hallway_1 = "school_corridor_background.webp"
image bg school_hallway_2 = "uncle mugen school corridor morning.webp"
image bg school_nurse = "hospital.webp"
image bg classroom_04 = "Classroom_04_day.webp"
image bg library_1 = "library___1_by_houseofimagistudio_df8thpa-pre.jpg"
# image bg classroom_morning = "classroom_morning.webp" it dont work its too small
image bg quad_outside_arts_building = "monele_arts_building.webp"
image bg rooftop_afternoon = "rooftop.png"
    # house backgrounds
image bg bedroom_afternoon = "room_afternoon_light_off.jpg"
image bg bedroom_dusk = "room_dusk_light_on.jpg"
image bg bedroom_morning = "room_morning_light_off.jpg"
image bg bedroom_night = "room_night_light_off.jpg"
image bg dining_room = "condo_Day 03.jpg"
image bg living_room = "condo_Day 05.jpg"

# ========================AURA STUFF=============================
    
# aura points/level for route percentage
default p_aura = 1
# default p_points = 0
default n_aura = 1
# default n_points = 0
default g_aura = 1
# default g_points = 0
default w_aura = 1
# default w_points = 0

# AURAAAAAAAAA SYSTEM ICONS
screen p_heart_box():
    add "kyren_heart.png":
        xpos 0.92
        ypos 0.1
    if (p_aura < 10) or (p_aura < 0):
        text "[p_aura]":
            # just eyeballing...
            xpos 0.9435
            ypos 0.13
    else:
        text "[p_aura]":
            xpos 0.9385
            ypos 0.13

# idea: hearts appear on screen with each encounter? not implemented yet

screen n_heart_box():
    add "ronan_heart.png":
        xpos 0.92
        ypos 0.22
    
    if (n_aura < 10) or (n_aura < 0):
        text "[n_aura]":
            xpos 0.9435
            ypos 0.25
    else:
        text "[n_aura]":
            xpos 0.9385
            ypos 0.25


screen w_heart_box():
    add "lucien_heart.png":
        xpos 0.92
        ypos 0.34

    if (w_aura < 10) or (w_aura < 0):
        text "[w_aura]":
            xpos 0.9435
            ypos 0.37
    else:
        text "[w_aura]":
            xpos 0.9385
            ypos 0.37


screen g_heart_box():
    add "king_heart.png":
        xpos 0.92
        ypos 0.46
    
    if (g_aura < 10) or (g_aura < 0):
        text "[g_aura]":
            xpos 0.9435
            ypos 0.49
    else:
        text "[g_aura]":
            xpos 0.9385
            ypos 0.49

# The game starts here.

label start:

    show screen p_heart_box
    show screen n_heart_box
    show screen g_heart_box
    show screen w_heart_box

    $ playername = "You"
    $ performative = "???"
    $ narcissist = "Guy Sitting By Himself"
    $ weeb = "Guy With Disheveled Hair"
    $ gymbro = "Tough-Looking Guy"
    $ meangirl = "???"

    scene bg black_background

    # i think it'll be cute if we add a "prologue" scene b4 everything of alice getting ready
    "Thursday, 5:00 AM."
    "Enveloped by the fluffy warmth of a blanket, you shuffle in your bed as the sun's soft rays caress your face through the window."
    "Softly breathing, you pull the blanket closer and allow slumber to consume you further."
    "What were you dreaming about just now?"

    menu:
        "Eating fancy desserts on a cloud":
            "Ah, yes. You imagine yourself on soft, feathery shades of white as you take a bite of fluffy ice cream."
            "The cold sensation fills your mouth and spreads throughout your body as you swallow."
        "Rolling around in a flower field at sunset":
            "You can faintly hear birds chirping in the distance as you lay on a soft field."
            "The golden rays of the sun linger on you, providing a gentle warmth to your skin."
        "Swimming in a lake as clear as glass":
            "Refreshing, serene, free."
            "That is how you feel about the glassy water rippling around you, letting you forget about all your worries."

    "It's so peaceful..."
    "You could stay like this forever-"
    # insert alarm clock sound
    "*RING!*"
    "...Or maybe not."

    scene bg bedroom_dusk with fade

    mc deadpan "Ugh..."
    mc deadpan "It's too early... I'm still recovering from jet lag..."
    mc neutral "Whatever. I need to get ready for school now."
    # if time, cutscene of alice's family surrounded by wealth
    "Growing up, you had a childhood that most people could only dream of."
    "You were fortunate enough to be born into a conglomerate family in China, Fuyu Group, and you've always gotten everything you wanted."
    "...Well, almost everything you've wanted."
    "Previously, you attended a private academy in Beijing your entire life. However, your family's company wanted to expand its international influence..."
    "...And you were forced to transfer to a high school in the west."
    # if time, cutscene of alice in front of school
    "Milkyway Academy, a large private high school in New York City known for its rigorous learning environment focused on math, science, and technology."
    "Surprisingly, even though this school holds a large and diverse student population, you are the only new exchange student this year."
    # cs of alice penthouse
    "And unlike typical exchange students who live with a host family, your family rented out a penthouse for you."
    "Pretty cool, right?"
    # black screen again
    "Your one goal is to successfully focus on your academics to properly represent your family in the United States."
    "Surely, nothing will go wrong."
    "Right?"
    "..."
    "...Right?"

    mc deadpan "It's only nine months until I can go back home. What could happen in such little time?"

    "That's right."
    "Besides, even if you did run into trouble..."
    "...what problem can't be solved with money in this day and age?"
    "It's time to get ready for the day."
    "This will be your first official day at school. Hopefully, it'll will go well, and the next nine months starting today will go smoothly."
    
    jump intro
    return

label intro:

    scene bg school_street with fade

    "Thursday, 7:00 AM."
    "After getting ready and eating a light breakfast, your chauffeur picked you up from your penthouse and brought you to school."

    mc neutral "(Finally arrived at school... I'm so thirsty...)"
    mc neutral "(It's 7:00, I still have an hour until my first class.)"
    mc neutral "(I should try to find a drink somewhere.)"
    
    scene bg cafe_outside with fade

    "After walking around for a bit, you find yourself in front of a cafe directly next to the school."

    mc happy "(I never realized the school had a cafe next to it. That's really convenient.)"
    mc neutral "(I'll go check it out. Hopefully they have something good.)"

    scene bg cafe with fade

    "The inside of the cafe feels minimalist, carrying a strong smell of roasted coffee beans and baked goods."
    "Surveying the interior, you squint your eyes as the fluorescent light above shines into your retinas."
    "The sound of quiet music and hushed conversations echo across the wooden floorboards as you make your way towards the front counter."
    "However, you notice increasing voices as you continue walking."
    "\"Hold on, look! Is that...\""
    "\"That's her! The Fuyu Group kid!\""
    "\"Why is she here and not at some luxury coffee shop instead?\""

    mc deadpan "(None of you are good at whispering.)"

    "Ignoring the murmuring voices and glaring eyes, you stop in front of the cashier and examine the menu on the wall."

    mc neutral "(Americans really do like coffee...)"
    mc deadpan "(Is there really no hot tea here? Only iced?)"
    
    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Welcome! What can I get for you today?"
    mc neutral "(I should get a...)"

    menu:
        "Matcha latte":
            $ choice = "matchalatte"
        "Frappuccino":
            $ choice = "frappuccino"

    if choice == "matchalatte":
        mc neutral "Could I get a matcha latte?"
        cashier "Good choice!"
        cashier "Our matcha is the drink of the day for only $5.25!"
    elif choice == "frappuccino":
        mc neutral "Could I get a frappuccino?"
        cashier "Are you sure? Our matcha lattes are the drink of the day for only $5.25!"
        mc deadpan "Um..."
        menu:
            "Order the matcha latte":
                mc deadpan "Um... sure."
                mc neutral "(Doesn't hurt to give it a try...)"
                $ p_aura += 1
                "+1 Aura!"
            "Order the frappuccino":
                mc deadpan "...No, I'll take the frappuccino'."

    $ playername = renpy.input("Alright then, can I get a name for your order?", length=32) # length=32 is optional
    $ playername = playername.strip() # remove leading/trailing whitespace
    # Set a default name if the player leaves it blank
    if not playername:
        $ playername = "You"

    # use character to say their name
    mc neutral "[playername]."
    cashier "Okay, I'll have it ready soon."

    hide cashier_neutral #with dissolve
    # current style is show w/ dissolve but no transition when hiding

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

label episode_1:

    scene bg cafe_2 with fade

    "You take a sip as you walk towards the closest empty table."
    "As the drink makes contact with your tongue, the taste of artificial sweetness floods your mouth."

    mc neutral "(This tastes pretty cheap compared to what I usually get back home... How many strange chemicals are in this thing?)"
    mc happy "(It's fine. It's not that bad.)"

    "You sit down at an empty table and begin to take your laptop out of your backpack when your elbow accidentally tips over your drink."
    "Thankfully, you have fast reflexes, and you were able to catch the drink before it completely fell."
    "...However, a splash still managed to escape from the cup and onto the table."

    mc angry "(...Are you kidding me?)"
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
    p happy "Of course. Mind if I take a seat?"
    mc neutral "...Go ahead."
    p neutral "Thank you."

    "The strange boy takes a seat directly across from you, but not before you notice a strange keychain dangling from his belt loop."
    "He sets a book down on the table that reads \"Feminist Literature by Cyx Sehvyn\" and hangs his tote bag on his chair."
    "But it seems that you've drawn the attention of other students in the cafe."
    "Muttered voices suddenly flood the room as the boy wearing a quarter zip-up smiles at you."
    "\"Do you see Kyren Miller over there? He's going after another girl?!\""
    "\"Wait... he's tryna go for [playername]? The nepo baby exchange student?\""
    "\"Is Kyren for real? He's really going to try this on HER of all people?!\""
    "\"Does he realize he's cooked if he offends her or something?\""
    "\"Oh nah... What if she gets his parents fired from their job?\""

    mc deadpan "(Do all people here talk so loud?)"

    p neutral "You're [playername], right?"

    $ performative = "Kyren"

    p neutral "I'm Kyren, nice to meet you."
    p neutral "I've heard great things about you and Fuyu Group!"
    p neutral "Today's your first day, right? How have you been adjusting so far?"
    mc neutral "Well..."

    menu:
        "It's been well":
            mc neutral "I've been adjusting well."
            p happy "That's great to hear!"
        "It's been okay":
            mc neutral "It's been alright."
            p neutral "That's good!"
        "It's been bad":
            mc neutral "I haven't been adjusting very well."
            p sad "Sorry to hear that, hopefully it gets better."

    p neutral "I saw you deciding between matcha and a frappuccino when I was waiting in line earlier."
    p happy "Which one do you like more? Personally, I like matcha."
    p neutral "I've been drinking it for years, way before it became mainstream."
    mc deadpan "(...Thanks for sharing?)"
    mc neutral "They're both fine."
    p neutral "What do you usually drink, then?"

    menu:
        "Pearl milk tea":
            mc neutral "Where I'm from, most people prefer pearl milk tea."
            p sad "Oh, boba?"
            mc deadpan "...Yes?"
            p happy "I love boba! We should go get some together sometime."
            p neutral "I also read this one feminist literature book where the author had a famous boba recipe."
        "Green tea":
            mc neutral "I prefer green tea."
            p neutral "I read in a feminist literature book that green tea helps a lot with being open-minded."
            p happy "I made pretty good green tea as well, if you ever wanna come over to try some."
        "Water":
            mc neutral "Just water is fine."
            p happy "I love water too!"
            p neutral "It doesn't have any toxic chemicals like what people usually drink these days."
            p neutral "I read about it once in a feminist literature book, by the way."

    mc neutral "...Feminist literature?"
    p neutral "Yes, I'd say I'm a pretty avid reader."
    p neutral "I just love women, you know? They've worked so hard and are so underappreciated."
    p neutral "And the way they have to suffer every month with period cramps..."
    p neutral "If I could choose a superpower, I would choose the ability to get rid of period cramps forever!"
    mc deadpan "..."
    mc deadpan "(What is this guy talking about?)"

    "This guy is..."
    "Interesting, to say the least."

    mc neutral "What's your favorite piece of feminist literature?"
    p shocked "..."
    p shocked "Oh, uh..."
    p neutral "They're all so good, I can't choose."

    "...I don't think that counts as an answer."

    p happy "Anyways! You're from China, right? I've always wanted to visit. I'd say I'm pretty familiar with your culture."
    mc happy "Really? I have always been proud of my culture and-"
    p neutral "I'm such a fan of \"The Drawing of War\" by Moon Tzu. It's such a beautiful and philosophical piece."
    mc deadpan "...What?" 
    p neutral "And Chinese food is so delicious, I go to Tiandilao every week. But obviously authentic Chinese food is way better."
    p neutral "Chinese music is also incredible, I like pretty niche artists. You know... like Wackson Jang."
    p neutral "I can put you on, if you want."

    p happy "Oh, and I can't forget to mention that mahjong just happens to be one of my favorite games."
    mc shocked "..." 
    
    "You can't believe what you're hearing right now."
    "This guy just doesn't stop talking!"
    "You wonder if this guy even knows what he's talking about. Does he realize he just called the Wackson Jang \"niche\"?"

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
    p neutral "Can I get your WheeChat?"
    mc neutral "Since when do Americans use WheeChat?"
    p neutral "Heh, I'm pretty cultured and open-minded."
    p happy "I've been like this because of all the feminist literature I've read since I was young."

    # im gonna make this part longer

    menu:
        "Give him your WheeChat":
            mc neutral "...Alright, scan my QR code."
            p happy "Thanks! Or, should I say, xiexie!"
        "Don't give him your WheeChat":
            p shocked "Huh? I'm not like other guys who ask for your socials, promise."
            p neutral "I just want to be friends with someone with common interests."
            mc deadpan "...Alright, scan my QR code."

    "Quickly opening WheeChat, Kyren scans your QR code and sends you a friend request. You reluctantly accept the friend request before throwing your bag over your shoulders."

    mc neutral "...I'll get going then."
    p shocked "Wait!"
    mc deadpan "...?"
    p neutral "What class do you have first?"

    "You dig into your skirt pocket to take out a small slip of paper with your class schedule attached."
    
    mc deadpan "...PE."
    p sad "Aw, that's rough."
    p neutral "You want me to show you how to get there?"
    p sad "The school's huge. I'm worried you'll get lost."
    mc deadpan "(The school is half the size of my house...)"
    
    menu:
        "Let Kyren take you to class":
            mc neutral "(I was already given a tour of the school over the weekend...)"
            mc neutral "(Whatever, I don't have anything to do until class actually starts anyways.)"
            mc neutral "Okay."
            p happy "Great! Follow me."
            jump episode_1_tour
        "Don't let Kyren take you to class":
            mc neutral "That won't be necessary. I was given a tour of the school over the weekend."
            p sad "...You sure?"
            p neutral "It's way easier to get lost on an actual school day."
            p neutral "People don't know how to walk, and they're always crowding the hallways."
            p happy "Let me take you there, I insist."
            menu:
                "Let Kyren take you to class":
                    mc neutral "(I was already given a tour of the school over the weekend...)"
                    mc neutral "(Whatever, I don't have anything to do until class actually starts anyways.)"
                    mc neutral "Okay."
                    p happy "Great! Follow me."
                    jump episode_1_tour

    return

label episode_1_tour:

    scene bg school_hallway_1 with fade

    show kyren neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0

    "You follow Kyren out of the cafe and into the school."
    "Students already crowd the halls, loudly chatting with their friends."
    "And of course, the second you enter the building, you feel a change in atmosphere among the other students."
    "\"Oh oh oh! Look!! There she is!\""
    "\"Is that actually [playername]? She looks rich, but not like, billionaire rich, y'know?\""
    "\"To think her family has control over a quarter of the world... I'm kind of scared. Why would she come here?\""
    "\"She seems so normal. I really thought she would show up wearing all luxury brand clothes.\""
    "\"Wait... Is she walking with... Kyren Miller?!\""

    p neutral "Seems you're pretty popular already."
    mc deadpan "...Didn't notice."
    p happy "Hahahaha!"
    p neutral "What other classes do you have today?"

    "You reach into your pocket to take out the slip of paper again."

    mc neutral "After PE, I have...Linear Algebra, English, Quantum Physics, Ethnic Studies, and Discrete Math."
    p neutral "Wow, two math classes and Quantum Physics?"
    p neutral "You're so smart. I could never do something like that..."
    p neutral "I'm just soooo average..."
    p happy "Could you tutor me sometime?"
    mc deadpan "(...I just met you.)"
    mc neutral "The school offers tutoring services."
    p neutral "Yeah but most of them are guys..."
    p neutral "And women are just way smarter than guys."
    mc deadpan "...This is the way to PE?"
    p shocked "Huh?"
    p neutral "Oh, haha! Yeah, but this is just a longer way with less people."
    p neutral "The flight here must've been so difficult. I'm just looking out for you, y'know?"
    mc deadpan "..."
    p neutral "Anyways, I noticed that you're a bit reserved."
    p sad "Are you alright? Did you have to go through anything when you were a kid?"
    p sad "Being closed off is a sign of vulnerability. You can tell me."
    mc deadpan "(We JUST met, and you want me to tell you about my trauma?)"
    mc neutral "What are you talking about?"
    p neutral "It's alright, I understand it can be difficult to open up to people."
    p neutral "I'm an empath."
    mc deadpan "...What?"
    
    "Thankfully, you notice the gym doors down the hallway before Kyren can continue spouting nonsense."
    "You've been saved!"

    mc neutral "...The gym is right there. Bye."
    p shocked "Huh? W-wait! Do you wanna get boba together for lunch?!"

    jump episode_2
    return

# NARCISSIST SCENE

label episode_2:
    
    $ met_narcissist = False

    scene bg school_track with fade

    "You follow a few students out the gym and onto the field while thinking about your interactions with Kyren."

    mc deadpan "(That guy was odd... Whatever)"
    mc neutral "(Okay... now it's time for first period. That man over there should be the teacher.)"

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
        n "THE DISRESPECT! Just wait until I tell my father about this insolence!"
        mc deadpan "(...Is everyone at this school this weird?)"
        n "And since you're uneducated, I'll show some mercy and inform you about WHO I am exactly."
        $ narcissist = "Ronan"
        n "I am Ronan, Ronan X.Y. Sinclair! The first in line to inherit the reputable Sinclair X.Y. Industries!"
        mc neutral "(Sinclair X.Y. Industries... kind of rings a bell. I think they source parts from dad's company?)"
        n "So, you-"
        n "..."
        n "Why do you look familiar?"
        n "Have you ever worked for my family, peasant?"
        mc deadpan "...You've probably seen me on the news before."
        n "..."
        n "Hahahahahahhahahahahahahahaha!!"
        n "What, are you a little social media influencer? Do you really think you have any power compared to ME?"
        mc deadpan "Fuyu Group."
        n "..."
        n "...What?"
        mc neutral "My father is the CEO of Fuyu Group."
        n "..."
        mc happy "(Exactly.)"
        n "*muttering* Father told me someone from a conglomerate was transferring here or something... I wasn't listening to him..."
        n "*muttering* ...So it was this girl."

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

    b1 "That's the new student! [playername] from Fuyu Group!"

    hide b1_neutral

    mc deadpan "(Am I some kind of zoo animal? (-_-;))"

    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0

    b2 "For real? I thought she would look, y'know, more classy. Isn't her family full of CEOs or whatever?"

    # still debating whether to put this before or after the ball hit/nurse's office thing
    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
        
    b1 "Oh, really? Why would she would move here? Away from her luxurious mansion?"

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0

    b2 "Her family is trying to sell in America, I think. I heard she rented a penthouse here and has a chauffeur."

    hide b2_neutral

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
        mc deadpan "(But is this a normal occurrence?)"
    else:
        mc deadpan "(Is this a normal occurrence?)"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    b1 "Hey, watch out-"
    hide b1_neutral
    "You watch in awe as one of the peasants is struck down by an incoming tackle."
    # maybe replace with cutscene?

    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    b2 "Oof!"
    hide b2_neutral
    "Right, you all are still playing football."
    "Excusing themselves, the two peasants leave just as quickly as how you met them."

    show narcissist_neutral with dissolve
    n "Hmph! That's more like it."
    
    "Then, Ronan and you make eye contact."
    n "I bet you were wondering if this happens often. And yes, it does. It's natural that people are always stunned by presence!"

    # 2do: update character n so we can use the emotion shorthand thingies
    show narcissist_neutral with dissolve
    if met_narcissist:
        n "Oh. It's that insolent brat."
        menu:
            "Excuse me?":
                n "You're excused!"
                mc deadpan "..."
                mc "(He's not supposed to be in elementary school, right...?)"
            "(Pretend like you didn't hear anything.)":
                $ n_aura += 1
                "+1 Aura!"
                pass
        "Ronan slicks his hair back. It's, like, the equivalent of a cool girl's hair flip."
        n "Hmph! I forgive you for your transgressions."
        n "After all, I'm young, rich, tall, handsome, AND nice."
        n "I recognize my kind when I see one."
        "He sent you a wink~☆ but unfortunately, you blinked right then, so you didn't notice."
        mc deadpan "..."
        n "Dear me. You're quite slow. Be grateful for this opportunity to network with me, that is, RONAN X.Y. SINCLAIR!"
    else:
        mc neutral "...I don't believe we've met before."
        n "What, have you been living under a rock all your life? Or do you really not know who I am?"
        $ narcissist = "Ronan"
        n "I am Ronan, Ronan X.Y. Sinclair! The first in line to inherit the reputable Sinclair X.Y. Industries!"
        mc neutral "(Sinclair X.Y. Industries... kind of rings a bell. I think they source parts from dad's company?)"
        n "So, you-"
        n "..."
        n "Why do you look familiar?"
        n "Have you ever worked for my family, peasant?"
        mc deadpan "...You've probably seen me on the news before."
        n "..."
        n "Hahahahahahhahahahahahahahaha!!"
        n "What, are you a little social media influencer? Do you really think you have any power compared to ME?"
        mc deadpan "Fuyu Group."
        n "..."
        n "...What?"
        mc neutral "My father is the CEO of Fuyu Group."
        n "..."
        mc happy "(Exactly.)"
        n "*muttering* Father told me someone from a conglomerate was transferring here or something... I wasn't listening to him..."
        n "*muttering* ...So it was this girl."

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
    b2 "Hey, look!"

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
    
    mc neutral "You're fine."

    # menu:
    #     "What are miracle. You're totally fine."
    #         mc happy "What a miracle. You're totally fine."
    #     "Just go back to sleep."
    #         mc deadpan "Just go back to sleep."

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

    menu:
        "(Leave.)":
            mc deadpan "It's great to see you're already feeling back to normal again."
            mc neutral "I'm leaving now."
            n "H-huh? You're leaving already? So soon?"
            "Ronan suddenly dropping his posh tone catches you off guard. But, anyways, you've got places to be."
            mc neutral "Yep. Need to go. Bye."
            jump episode_3
        "Don't worry about it.":
            #LOWKEYYYYYYYYYYYYYYYYYY i feel like this scene is not in character?! might remove/move to later episode
            mc happy "Don't worry about it."
            $ n_aura += 1
            "+1 Aura!"
            n "Hm...Hmph. You're quite down to earth."
            mc happy "Thank you."
            n "..."
            "Ronan goes quiet for a moment, pondering intently while staring at the floor."
            n "I just don't get why you're being so nice to me."
            n "...Whatever. Could you stay here with me until your next class starts?"
            menu:
                "You're just like an elementary school student.":
                    mc neutral "You're just like an elementary school student."
                    n "Excuse me? How dare you! If I'm an elementary school student, then you're an old hag!"
                    "*slink* Ronan pulls out the curtains, obscuring you from view. He just leaves a tiny enough opening to stick out his hand and motion you to scram."
                    mc happy "LOL."
                    "*silence*"
                    mc happy "Okay, okay. I'm going now."
                    jump episode_3
                "(Apologize and leave.)":
                    #ik i could use another jump but i'm lazyyy
                    n "H-huh? You're leaving already? So soon?"
                    "Ronan suddenly dropping his posh tone catches you off guard. But, anyways, you've got places to be."
                    mc neutral "Yep. Need to go. Bye."
                    jump episode_3
            
        # "Do I get a reward?":
        #     n "Of course! Just name anything, and I'll give it to you. *COOL HAIR FLIP*"
            
        #     jump episode_3



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

    b2 "Our turf-"

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

    jump episode_3_savior
    return

# choosing to ignore, seeing lucien running away
label episode_3_meeting_2:

    scene bg school_hallway_2 with fade

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
    # cutscene start
    "And before you could repeat yourself, you can't help but notice the guy is..."
    "...oddly good looking for someone so disheveled?"
    # cutscene end

    mc deadpan "Um, I said, are you alright?"
    w "..."
    mc angry "Can't you hear me? I asked if-"
    w "Suzuki Haruka?!"
    mc deadpan "...What?"
    w "Y-y-y-you... y-y-y-you're a carbon copy!! She's... she's real!!! I knew it!!"
    mc angry "What are you talking about? Are you alright or not?"
    w "Oh my god, oh my god, oh my god..."

    hide weeb_neutral

    "Before you could question what on earth this guy was talking about, a rowdy yell interrupts:"
    "\"Ugh, where did that kid go?!\""

    mc neutral "(Huh? That voice sounds a bit familiar.)"

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "Hey punk! Where are you running off to?!"
    b1 "Huh?"
    b1 "Nepo baby! Why are you here?"

    hide b1_neutral
    show weeb_neutral with dissolve

    w "G-G-GAH!!!"

    "In the blink of an eye, the disheveled guy gets up from the floor and runs to hide behind you."

    w "P-p-p-please save meeeeeeeeeeeeee!!!!!!"
    mc deadpan "...What's going on?"
    
    hide weeb_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    
    b2 "Hey, you run way too fast-"
    b2 "...Huh?"
    b2 "Why the heck are you here?"

    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "That's what I'm saying!"
    b1 "Ahem, we, uh, weren't doing anything."
    b1 "We were just hanging out with our little friend over here."
    b1 "Right?"

    hide b1_neutral
    show weeb_neutral

    w "...*Hic*"

    hide weeb_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0
    
    b1 "I said, RIGHT?"
    mc deadpan "Then could you explain why he's so scared right now?"
    b1 "...Tch."

    hide b1_neutral
    show b2_neutral with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 1.0
    
    b2 "We weren't getting into trouble or anything! We just wanted to ask him about a misunderstanding."

    hide b2_neutral
    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "It was NOT a misunderstanding, bruh."
    b1 "This kid was clearly trying to hit on my girl!"
    
    jump episode_3_savior
    return

label episode_3_savior:

    scene bg school_hallway_2

    hide b1_neutral
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

    b2 "What is this kid talking about?"

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

    b2 "Then why were you looking so intensely?!"

    hide b2_neutral
    show weeb_neutral with dissolve

    w "..."
    w "The poster on the wall above her had my waifu-"

    hide weeb_neutral

    window hide

    show manga with dissolve:
        zoom 0.3
        xalign 0.5
        yalign 0.5
    
    pause

    hide manga with dissolve
    window show

    show b1_neutral with dissolve:
        zoom 0.25
        xalign 0.5
        yalign 0.0

    b1 "I'm sick of this kid! And you smell horrible! Trying to act crazy as an excuse or what?!"
    
    "You stare in confusion as the rowdy bully suddenly lifts a leg, about to kick the poor kid."

    mc deadpan "(Maybe I should intervene...)"

    menu:
        "Try to resolve the conflict with words":
            mc neutral "Shouldn't you two be in class still?"
            b1 "...Tch, you think you're a goody two shoes?"
            b1 "Stay out of this! Go complain to your dad if you want! I don't care!"
            mc deadpan "(...Words aren't going to get through this guy.)"
        "Run away with the disheveled guy":
            mc deadpan "(...Words aren't going to get through this guy.)"

    "In the blink of an eye, you reach over and grab the disheveled guy's hand and bolt down the hallway, dragging him with you."
    b1 "Wha- Hey!"

    hide b1_neutral
    show weeb_neutral with dissolve

    w "*Hic* S-S-S-Suzuki Harukaaaaaaaa!!!! M-m-m-my savior!!!!"

    hide weeb_neutral

    window hide

    show manga_run with dissolve:
        zoom 0.5
        xalign 0.5
        yalign 0.5
    
    pause

    window show

    mc angry "If you call me that one more time, I'm going to beat you up myself."

    hide manga_run with dissolve

    show weeb_neutral with dissolve
    w "B-b-b-b-but you really are her!!!"

    hide weeb_neutral

    "...Maybe you should've just let this guy get beat."
    "After a few more minutes of running through the halls, you slow down to glance at a nearby clock."
    "15 seconds until the bell rings."

    mc happy "(Phew, that should make up for missing PE today.)"
    mc neutral "Hey, are you good now-"
    mc shocked "..."

    show weeb_neutral with dissolve

    w "*Huff* Y-you,"
    w "Ugh... *gasp*"
    w "Can't... run... anym... *wheeze*"

    "You thought you were already on the lower end of athleticism..."
    "...but this guy just created a new bar below you!"

    w "S-S-Suzu.. ki... I can't... brea- *puff*"
    mc deadpan "(...Are you serious?)"
    mc neutral "What's your name?"
    mc neutral "(So I can make sure to avoid you in the future.)"
    w "Y-y-y-you... w-w-want to know MY name!?!?!?"
    w "Suzuki Haruka... it's an honor!!!"
    $ weeb = "Lucien"
    w "I-I-I-I am Lucien Kim!!! At your service, always!!!!"
    mc deadpan "...Okay."

    "*RING!*"
    "Fortunately, the bell saved you! As students fill the halls, you turn to go to your next class."

    $ w_aura += 1
    "+1 Aura!"

    mc neutral "Well... bye."
    w "W-w-w-wait!! Suzuki Harukaaaaaaa!!!!"

    jump episode_4

    return

# lunch + meet gymbro (CURRENTLY UNFINISHED)
# MAKE SURE THAT OLIVIA ENCOUNTER IS IN EACH ROUTE
label episode_4:
    scene bg classroom_04 with fade
    "One long lecture later..."
    "*RING!*"
    mc happy "(It's finally time for lunch! English class can be so boring.)"
    # mc neutral "(Milkyway High School really is full of interesting characters.)"
    "Some students stay behind in the classroom, some students rush to leave, and some students come to eat with their friends."
    "Hopefully, you can get along with everyone, too. But first, where do you want to eat?"
    menu:
        "(Eat lunch in the classroom.)":
            # results in encounter with mean gurlz (olivia/sophia?)
            
            $ meangirl = "Some Girl In Your Class"
            $ gymbro = "Tough-Looking Guy"
            
            mc neutral "(Yep, I won't bother getting up right now.)"
            "You reach into your bag and take out your bento, which was prepared by your home cook before you woke up for school this morning."
            # fun cutscene idea: show the bento! WITH DELICIOUS SPARKLES like in genshin!!
            "Taking off the lid, you are delighted with a tender, butter-poached lobster (caught in the state of Maine) accompanied by a juicy, premium steak (only grass-fed, of course)."

            mc happy "A truly beautiful surf and turf. Home-cooked food is always the best!"
            mc neutral "*om nom nom nom nom*"

            # other fun idea: change mc sprite to a dining bib
            "The enticing aroma of your lunch draws attention to your table. It seems that everyone can smell the butter-poached lobster especially, which you admit has been pan-seared a {i}little{/i} too well."
            
            show olivia neutral with dissolve:
                zoom 0.25
                xcenter 0.5
                yalign 1.0
            o neutral "OMG. Who brings an entire lobster to school?"

            hide olivia neutral

            # idk, show sophia too?

            show king disgusted with dissolve:
                zoom 0.25
                xcenter 0.5
                yalign 1.0
            g "Women get jealous over every little thing."
            g neutral "If anything, this is a meal packed with protein!"
            
            "Suddenly, this tough-looking guy throws a straight punch. With that scowl, you'd think he was gonna start shadowboxing."
            "But then, he unfurls his index finger to point at your lunch."

            # replace with happy sprite
            g neutral "Yo, female! Could you cook me up some lobster and steak too?"
            mc neutral "(Yeah, I'll cook YOU up.)"
            mc angry "Don't call me \"female.\" My name is [playername]."
            mc angry "So uncouth. Where are your manners?"
            "The tough-looking guy retracts his pointer finger and relaxes his muscles, although still scowling."
            $ gymbro = "King"
            g neutral "Well pardon me, then. The name's King."
            "King's eyes dart around the classroom before they return to freeze at yours."
            g neutral "[playername]... you seem different from most women."
            mc deadpan "(What's his deal?)"

            hide king neutral

            menu:
                "Buy his silence.":

                    show king neutral:
                        zoom 0.25
                        xcenter 0.5
                        yalign 1.0

                    mc neutral "Will you be quiet if I give you $100?"

                    show king neutral at move_left

                    show olivia neutral:
                        zoom 0.25
                        xalign 0.9
                        yalign 1.0
                    show olivia shocked at olivia_move_left

                    o "Hey! [playername], are you naive or what?"
                    mc neutral "Excuse me... who are you?"
                    $ meangirl = "Olivia"
                    o "Olivia Johnson."
                    o neutral "But anyways, why would you give him a hundred bucks-"
                    g angry "Don't interrupt me, female. I don't need it anyways."
                    g neutral "As a real man, I make my own money."
                    # g neutral "I even have a podcast and drive a Wamborghini."
                    g neutral "Wealth and success are merely byproducts of discipline."
                    g disgusted "Besides, you're no better. You know you're only after Ronan for his money."
                    o angry "You take that back right now."
                    mc neutral "(Should I get involved?)"

                    menu:
                        # maybe i'll do this route at a later time lol
                        # "Stand up for Olivia.":
                        #     $ olivia_ticked_off = False
                        #     mc angry "Too far, King."
                        "Interrogate Olivia.":
                            $ olivia_ticked_off = True
                            show king neutral
                            mc neutral "Olivia... do you have feelings for Ronan?"
                            o shocked "That's...that's none of your business!"
                            o angry "We just met, [playername]. You don't even know me. Who are you to judge?"
                            mc deadpan "(I could say the same thing, though.)"
                            mc neutral "Then doesn't that make you a hypocrite?"
                            mc neutral "First, I heard you making comments on my lunch. And now, to my face, you're telling me how I should spend my money."
                            o shocked "..."
                            o angry "*mumbling* So annoying."
                            "Olivia mumbles some other things you can't hear. Maybe cursing you out."
                            
                            hide olivia angry
                            with dissolve

                            "She shoves her way between you and King, storming out of the classroom."

                            show king neutral at move_back_to_middle

                            mc neutral "Huh. I didn't expect her to just leave like that."
                            g neutral "Yeah! I knew you'd win."
                            g neutral "Olivia's just a 3, but you're a solid 10."
                            mc neutral "What?"
                            g neutral "Anyways... you know Ronan Sinclair?"
                            mc neutral "He's in my PE class."
                            g neutral "Ronan's taking PE? That's good. He should work out more. Like I do."

                            "King goes on to talk about the importance of maintaining appearances, and he explains how it all starts with a healthy lifestyle."
                            "He uses funny words like \"looksmaxxing\" and offers you plenty of tips for your next gym session."
                            "You decide to just let him keep talking while you finish eating your lunch."

                            g neutral "Hey [playername], you're a pretty good listener-"
                            "*RING!*"
                            g angry "...since I hate being interrupted."
                            "The bell rings, signaling that lunch is over. You need to get going to Quantum Physics, which is all the way on the other side of campus!"
                            "You frantically pack up your things and make a beeline for the door."
                            mc neutral "Sorry, I gotta run."
                            g neutral "Yeah, okay then."
                            g neutral "Join me at the gym sometime. I'll be your personal trainer."

                            # scrapped lines
                            
                            # g disgusted "This is why I don't get involved in female drama..."
                            # g neutral "Though you seem to have cooled down quick."
                            
                            # "What you thought would be a relaxing lunch ended up creating tension."
                            # "Tension in the air, and tension between you and your new classmates."
                            # mc shocked "(Did I...make the wrong decision?)"
                            # mc shocked "(Will my high school life only go downhill from here?)"
                            # "You keep your head down and finish eating your lunch. When lunch is over, you drag your feet to your next class."
                            # g neutral "Women can be scary sometimes."
                            # g neutral "Hmm...it's probably better that I don't get involved with [playername]."

                            hide king with dissolve
                            show bg classroom_04 at blur_screen
                            with dissolve

                            pass

                        "Remain neutral.":

                            hide olivia
                            hide king 
                            with dissolve

                            show bg classroom_04 at blur_screen
                            with dissolve

                            "While Olivia and King bicker with each other, you remain silent and focus on your meal."
                            "Before you know it, lunch is over, and your tummy is full."

                            mc happy "(Life is good.)"
                            mc happy "(Just gotta stay away from all the drama.)"

                            pass

                    pass

                "Offer him food.":
                    # mc neutral "(Well...I've heard Americans say that you're not you when you're hungry.)"
                    mc deadpan "I have no idea what you mean by that."
                    mc neutral "(Though... I've heard Americans say that you're not you when you're hungry.)"

                    mc happy "King, would you like a lobster tail?"
                    show king disgusted:
                        zoom 0.25
                        xcenter 0.5
                        yalign 1.0
                    g "...?"
                    g neutral "You know what? Sure, okay."
                    g neutral "Protein is protein."

                    "You serve King a lobster tail on a clean napkin."

                    show king neutral at move_left

                    show olivia happy:
                        zoom 0.25
                        xalign 0.9
                        yalign 1.0
                    show olivia happy at olivia_move_left

                    o happy "Hey [playername]! Could I try a lobster tail too?"
                    mc neutral "Sorry, but who are you?"

                    $ meangirl = "Olivia"
                    o neutral "I'm Olivia. Olivia JOHNSON, next in line to take over the Johnson Big Law Firm."
                    o happy "I've heard all about you, [playername]. Let's be friends, okay?"
                    mc neutral "(She could either become an ally or an enemy...let's just try to stay on her good side.)"
                    mc happy "Okay."
                    "Olivia brings her own napkin, and you serve her a lobster tail too."
                    g disgusted "..."
                    o angry "What are you looking at?"
                    g neutral "Hm? I was just thinking about how women can be so two-faced."
                    o angry "Excuse me?"
                    g neutral "Woah, calm down. I'm not just targeting you."
                    mc deadpan "(What is going on?)"
                    mc neutral "Not cool, King. I'm not sure what you have against women, but making comments like that say more about YOU than they do about us."
                    o happy "YES!!! YOU TELL HIM SIS!!!"
                    g neutral "..."
                    "*RING*"
                    "King doesn't say anything else before the bell rings, signaling that lunch has ended. You get up and pack your things."
                    mc neutral "Let's go, Olivia."
                    $ olivia_ticked_off = False
                    # next scene can be gymbro apologizing!!

                    hide olivia
                    hide king 
                    with dissolve

                    show bg classroom_04 at blur_screen
                    with dissolve

                    pass

            "The rest of your day is unremarkable."
            "Time goes by slowly. You find your new classes easy because your teachers only walk through slideshows today."
            "After dismissal, you find no reason to stick around at school, so your chauffeur drives you back to your penthouse."
            
            jump episode_5

            # g neutral "That made you angry? ...Women are so emotional."

            g neutral "LOLOL!!! end!!!"
            g neutral "bookmark!!!"

        "(Eat lunch outside.)":
            jump episode_4_outside

    jump episode_5
    return

# CURRENTLY UNFINISHED: sayhi, walkpast
label episode_4_outside:

    scene bg quad_outside_arts_building with fade

    # "When you exit the classroom, you're greeted by the smell of coffee."
    # "Exiting the classroom, you smell the scent of coffee, carried by a soft breeze."

    "As you leave the classroom, you get a strong whiff of coffee and cologne, but the cologne is so strong that it almost overpowers the coffee scent."
    mc neutral "*lowkey choking*"
    
    show king neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0
    
    g disgusted "Females... *sigh*"
    
    "That smell of coffee is probably coming from this tough-looking guy, who's leaving the classroom at the same time you are."

    menu:
        "Say hi.":
            
            $ playername_length = len(playername)

            if playername_length >= 4:
                $ playername_twisted = playername[0:3]
                mc happy "Hello! My name is [playername_twisted]-"
            else:
                mc happy "Hello-"
            
            # OKAY PURRRR so if u wanna have 2 transitions instead of 3, set the after transition to None
            define moveoutleft_plus_fade = ComposeTransition(dissolve, before=moveoutleft, after=None)

            hide king disgusted with moveoutleft_plus_fade
            "The tough-looking guy turns around and goes back into the classroom."

            #minus 500 aura
            $ g_aura -= 1
            "-1 Aura!"

            mc neutral "..."
            mc deadpan "(What the?)"
            mc deadpan "(So rude.)"
            mc neutral "(Whatever.)"
            mc happy "(All that matters is that I get to eat lunch now!)"

            "Finding an empty bench, you place down your bag and take out your bento."
            mc happy "Home-cooked food is always the best! *om nom nom nom nom*"

            # plan: olivia comes by and IS the one who spills the food hohoho...

            $ olivia_temperament_counter = 0

            o "Soooo...YOU'RE [playername]?"
            "Mid-chew, you look up and see..."
            show olivia neutral with dissolve:
                zoom 0.25
                xcenter 0.5
                yalign 1.0
            "...an unfamiliar face."

            menu:
                "Yes, I'm [playername].":
                    o "*gasp* It's SO great to meet you, [playername]!"
                "Who are you?":
                    o "Oh GIRL, don't be so on edge!"
                    $ olivia_temperament_counter += 1
                    mc deadpan "(How am I being on edge?)"

            $ meangirl = "Olivia"
            o "My NAME is Olivia. And I'm a total girls' girl."
            "Olivia reaches into her bag, and you hear the clink-clacking sounds of her rummaging through her items."
            o "Um...HAHAHA...one moment please...where is it..."
            mc neutral "No, please. Take your time."
            "As if you gave a magician's command, Olivia instantly pulls a small card out of her bag with a slightly embarrassed smile."


            o "You're SO sweet, [playername]. I was looking for this—thanks for being patient."
            # inventory idea? collectible trophy/memento system? it can be the same menu as a cutscene gallery
            # display business card cutscene here
            menu:
                "I didn't do anything.":
                    o "Aw, you're SUCH a humble queen."
                    mc deadpan "Uhh...thank you."
                    # $ g_aura += 1
                    # "+1 Aura!"
                "No problem.":
                    $ olivia_temperament_counter += 1

            "Flashing a pretty corporate smile, Olivia presents the small card to you, which you recognize to be a business card. You accept the card and glance at the printed text."
            # "Olivia smoothly takes your hand and curls your fingers over her business card."
            mc neutral "(Olivia Johnson...)"
            mc deadpan "(...on WinkedIn.)"

            # o "Oh my gosh, you don't know how EXCITED I've been to meet you!"
            o "*giggle* When I heard the heiress to Fuyu Group was coming to OUR school..."
            o "I didn't think you'd be so pretty AND kind!"
            menu:
                "Thank you.":
                    mc neutral "Thank you."
                    # $ g_aura += 1
                    # "+1 Aura!"
                "So you thought I was ugly and mean?":
                    mc angry "So you thought I was ugly and mean?"
                    $ olivia_temperament_counter += 1
                    o "WOAH, girl, way to put words into my mouth."
                    o "I guess the rumors WERE right, then."

                    menu:
                        "(Scoff.)":
                            $ olivia_temperament_counter += 3
                            # mc angry "..."
                            mc neutral "You're not really a \"girl's girl\" if you believe rumors and mindless gossip so easily."
                            mc neutral "You're just a hypocrite."
                            # olivia angry
                            o "You...you're one to talk!"
                            # o "You act all high and mighty just because your parents are loaded."
                            o "You act all high and mighty just because your family owns a huge company."
                            o "But listen carefully, [playername]. You're NOT special."
                            "Olivia Johnson's blood is boiling now. Her voice goes up a couple decibels, and you notice some students staring at you two from a distance."
                            o "Take another good look at that business card I gave you."
                            
                            "In small print at the bottom of the card, you read: \"Johnson Big Law Firm\"."
                            o "I was trying to be humble, but you SHOULD know that I'm also Olivia JOHNSON, next in line to take over the Johnson Big Law Firm!"
                            mc happy "(She kind of reminds me of someone...)"
                            mc neutral "Ahem. I see. Noted."
                            $ n_aura += 1
                            "+1 Aura!"

                        "(Say you were just kidding.)":
                            mc neutral "I was just kidding."
                            o "Oh, good. I HATE it when people can't take a joke."
                            o "But you seem like a nice girl. I think we'll get along QUITE well."
                            $ olivia_temperament_counter -= 2

            # "Olivia looks away into the distance as her voice trails off..."

            "*RING RING RING*"
            "It's Olivia's phone, and she once again rummages through her bag to find it."

            if (olivia_temperament_counter < 3):
                o "Oh my, would you look at the time. Sorry our meeting was so short. I have an IMPORTANT call to take right now."
                o "ANYWAYS, I just gave you my business card, with my WinkedIn on the back side. We're friends now, 'kay?"
                mc neutral "Uh-"
                o "[playername], don't hesitate to say hello when you see me in the halls. Bye now!"
                hide olivia neutral
                mc neutral "(...What a character.)"
            else:
                
                $ olivia_ticked_off = True

                o "See, this is an IMPORTANT call I have to take right now."
                o "Bye, [playername]."

                hide olivia neutral

                "Olivia runs past you in a jiffy, and you watch as she wears her corporate smile, answering her phone with her happy corporate voice."
                "As if you two weren't just on the verge of pulling each other's hair."

                mc neutral "(Finally, some peace and quiet.)"
                
            mc neutral "(I get the feeling that it won't be long before I run into her again.)"
            "Sluggishly, you take out your phone to check the time. As you thought, lunch is ending soon."
            mc neutral "(Better head to my next class, Quantum Physics.)"

            menu:
                "Head to your next class.":
                    scene bg classroom_04 with fade
                    "The rest of your day is unremarkable."
                    "Time goes by slowly. You find your new classes easy because your teachers only walk through slideshows today."
                    "After dismissal, you find no reason to stick around at school, so your chauffeur drives you back to your penthouse."

            jump episode_5

        "Walk past him.":
            "You stare straight ahead and walk just a little faster than usual, because you've got places to be and lunch to eat."
            g neutral "..."
            hide king disgusted

            # maybe cutscene of the bento
            "Finding an empty bench, you place down your bag and take out your bento."
            mc happy "Home-cooked food is always the best! *om nom nom nom nom*"
            
            "As you eat by yourself, you're left with your own thoughts. You think about all the new people you've met today."
            mc neutral "(Kyren, Mr. Teacher, Ronan and the two peasants...Lucien...)"
            # mc neutral "(I wonder what they're all doing during lunch.)"
            "And that tough-looking guy just now..."
            with hpunch
            mc neutral "*shudder*"
            mc shocked "Ack! One of my chopsticks fell..."

            "You reach down to grab your chopstick, which has left a sticky residue on the ground."
            mc neutral "(Good thing I'm always prepared with napkins and spare utensils.)"

            menu:
                "(Use napkins to clean up after yourself.)":
                    # olivia: "wowww ur cleaning urself? ur not having ur little housemaids do it for u?" (pretentious, fake tone)
                    mc happy "All clean. Time to throw this napkin in the trash can."
                    "You throw away your trash, and once again smell the pungent cologne and coffee combination from before."
                    show king neutral with dissolve:
                        zoom 0.25
                        xcenter 0.5
                        yalign 1.0
                    g "In a world of 3s, you are a 10."
                    # gym bro sees olivia, is like "you women are so emotional. at least this girl has potential"
                    mc deadpan "(What's his deal?)"

                    # bookmark
                    "Go back?"

                    # menu:
                    #     "Throwing away trash is the bare minimum.":
                    #         # idk yet
                    #     "Not cool bro."
                    #         mc neutral "Not cool bro. You shouldn't say things like that."
                    #     "(Walk away.)":
                    #         # idk yet

                    # |COME BACK!!!!!|
                    # ---------------
                    #   __  __
                    #  | |_| |
                    # |   _ _|
                    # (    ^ )
                    # different route...

    jump episode_5
    return

# date w/ performative (athena)
label episode_5:
    scene bg black_background with fade

    "The next day..."
    # maybe a quick cutscene of mc going through her day

    "Friday, 3:00 PM."
    "Thankfully, your day was less... eventful compared to your first day of school."
    "However, you were quickly reminded that you are now a student at THE Milkyway High School..."
    "...meaning you have a mountain of homework and assignments to complete before Monday."
    "Let's lock in!"

    scene bg bedroom_afternoon with fade

    mc neutral "Nothing looks that difficult..."
    mc deadpan "Just tedious."
    mc neutral "What should I start with?"

    menu:
        "English presentation":
            mc happy "The English presentation will take a bit. I should get it over with."
            "You open the assignment on your laptop to read the instructions for the presentation:"
            "\"Students must prepare an extensive, 5-7 minute presentation about an author of their choice.\""
            mc neutral "An author of my choice?"
            mc neutral "Maybe I should head to the library to get ideas."
            jump episode_5_english
        "Math homework":
            mc happy "The math homework is pretty simple. I'll start with it first."
            mc neutral "Maybe I should head to the library so I can concentrate."
            jump episode_5_math

    return

# performative guy helps mc with presentation
label episode_5_english:

    scene bg library_1 with fade

    "You called your chauffeur to drive you to a nearby library so you could work on your presentation."
    "Thankfully, the library wasn't too packed, and your presence was mostly unnoticed."

    mc neutral "(Since I'm in New York City, I should probably make my presentation about an author that grew up here.)"

    "You find an empty table to set your belongings down before roaming the shelves."
    "As you walk around and brush your fingers on the spines of displayed books, you catch a lingering scent in the air."
    "The library smelled of dusty books and heavy coffee. You notice a faint, musky sweetness exuding from every corner."
    "But you soon realize there's a new aroma slowly getting stronger, and you can't help but find this scent... familiar."
    "It's fresh and grassy, yet sweet and creamy."
    "Almost like..."

    mc neutral "(...Matcha?)"

    "Eh, whatever."
    "You continue looking through the shelves labeled with a \"NYC-Born Authors\" sign until one book catches your eye."

    mc neutral "(Hm? What's this?)"
    mc happy "(This looks interesting.)"

    "You reach a hand out to grab the book from the shelf..."
    "But instead, you make contact with another hand."
    "Looking up, you meet a familiar face."
    
    # cutscene?

    "Only inches away from you stands Kyren Miller, one of the people you met yesterday."
    "Once again in his quarter zip-up and baggy jeans, Kyren had a cup of matcha in his grip with a book tucked under his arm."
    "His eyes widened once you made contact, and his lips parted ever so slightly."
    
    # end cutscene

    show kyren neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0

    p neutral "Oh, [playername], I didn't expect to see you here."
    p happy "I was looking for you at school and didn't see you."
    mc deadpan "(It's this guy.)" 
    mc neutral "(Why is he here?)"
    p neutral "What are you doing here?"
    mc neutral "I'm..."

    menu:
        "Working on a presentation":
            mc neutral "I'm working on a presentation for English."
            p neutral "Really? What kind of presentation?"
        "None of your business":
            mc neutral "It's none of your business."
            p sad "Well... it wouldn't hurt to tell me, would it?"
            mc deadpan "..."
            mc neutral "(I guess I'll tell him.)"
    
    mc neutral "I have to research an author."
    p neutral "An author? Like, any author?"
    mc neutral "Yes, I'm trying to find one who was born in New York City."
    
    "Noticing that Kyren moved his hand away from the book you were both looking at, you wonder if you should take it first."

    menu:
        # -1 point
        "Take it":
            "You quickly extend your hand to grab the book."
            mc neutral "...I'll take this."
            p neutral "Huh? Oh, feel free!"
            $ p_aura -= 1
            "-1 Aura!"
        # +1 point
        "Let Kyren take it":
            "Your eyes glance over to the book before making their way back to Kyren."
            mc neutral "You can have the book."
            p neutral "Huh? Oh, don't worry. You can have it."
            $ p_aura += 1
            "+1 Aura!"

    p neutral "It's only natural that I let women choose first."
    p neutral "Are you going to make your presentation about this author?"
    # x = placeholder, will think of name later
    "Taking a closer look at the book in your hand, you open the front cover to read the short biography of the author, x"

    mc neutral "(The presentation has to be 5-7 minutes. I should make sure the author went through a lot of events so I can extend the presentation.)"

    "According to the biography, the author transferred schools frequently and used his constantly changing youth as inspiration for his work."

    p neutral "This is a good author too."

    "Kyren reached into his tote bag and took out a book, handing it to you with a gentle smile."
    # y = also palceholder
    "\"Awesome Book\" by y"
    "The book seemed old; the pages were slightly ripped and clear tape held the spine together."

    mc neutral "What's this?"
    p neutral "Heh."
    p neutral "Feminist literature."
    mc deadpan "..."

    "Which author will you choose?"

    menu:
        # -1 point
        "Choose x":
            mc neutral "I'll use this one."
            p sad "Oh, alright then."
            "You watch as Kyren returns the book to his bag, almost looking disappointed that you didn't choose it."
            $ p_aura -= 1
            "-1 Aura!"
        # +1 point
        "Choose y":
            mc neutral "I'll use that one."
            p happy "Of course! You can keep it too."
            p neutral "It's a signed copy, by the way."
            $ p_aura += 1
            "+1 Aura!"
    
    p neutral "Are you going to work on your presentation here?"
    p neutral "If so, do you mind if I accompany you?"

    menu:
        # +1 point
        "Let Kyren accompany you":
            $ p_aura += 1
            "+1 Aura!"
            mc neutral "That's fine."
            p happy "Thanks!"
            p neutral "I won't disturb you, I promise!"
        # -1 point
        "Don't let Kyren accompany you":
            mc deadpan "No thank you."
            p sad "...Oh, that's okay."
            $ p_aura -= 1
            "-1 Aura!"
            p neutral "I'll get going now then."
            p neutral "See you at school, [playername]."
            jump episode_6

    "You lead Kyren to the table where you set your belongings at before turning on your laptop..."
    "...but you soon realize that it's out of battery."

    mc deadpan "(That's unfortunate.)"
    mc neutral "(Good thing I brought my charger-)"
    mc shocked "(...)"
    p neutral "Hm? What's the matter?"
    mc neutral "...My laptop died and I forgot my charger."
    p neutral "Oh, you can use my charger if you want."
    
    menu:
        # +1
        "Accept Kyren's laptop charger":
            mc neutral "Thank you."
            p happy "Of course!"
            $ p_aura += 1
            "+1 Aura!"
        # -1
        "Reject Kyren's laptop charger":
            mc neutral "I'll just work on it at home."
            p sad "Huh? Oh, that's fine..."
            $ p_aura -= 1
            "-1 Aura!"
            p neutral "See you at school then, [playername]."
            jump episode_6

    scene bg black_background with fade

    "You diligently work on your presentation as Kyren reads across from you."
    "No words are said, but the silence isn't disturbing."
    "Rather, it's peaceful."

    scene bg library_1 with fade

    "Friday, 7:00 PM."
    "You were able to finish your entire presentation!"
    "It's time to call your chauffer to bring you home now."
    mc neutral "I'll get going now."
    p shocked "Wait!"
    p neutral "Are you going on the train? I'll bring you home."
    
    menu:
        # +1
        "Let Kyren take you home":
            mc neutral "(I could just call my chauffeur...)"
            mc deadpan "(Eh, whatever.)"
            mc neutral "Sure."
            $ p_aura += 1
            "+1 Aura!"
            p happy "Okay!"
        "Don't let Kyren take you home":
            mc neutral "No, I'll have someone drive me home."
            p sad "Aw, okay."
            p neutral "See you at school then, [playername]."
            jump episode_6

    scene bg black_background with fade

    "Kyren led you into the correct train and sat next to you before digging into his pockets for his wired earbuds."
    "Plugging the cord into his phone, he looks over at you and smiles before offering one end of the earbuds."
    "Will you accept?"

    menu:
        # +1
        "Accept":
            "You reach out to accept the earbud and insert it in your ear."
            $ p_aura += 1
            "+1 Aura!"
            "What plays in your ear is a popular RnB song you've heard being played in the school cafe several times."
            "Glancing over to you again, Kyren softly whispers, only inches away from your face."
            p neutral "Do you know this song?"
            mc neutral "Yes, I've heard it before."
        # -1
        "Reject":
            mc neutral "...No thank you."
            "With an apologetic look, Kyren retracts his hand and inserts the earbud into his ear."
            $ p_aura -= 1
            "-1 Aura!"
            "However, you realize that the earbuds must be of low quality, as you can hear his music spilling out."
            "It's not too noticeable, but you identify a popular RnB song you've heard being played in the school cafe several times."
    
    "Surprisingly, there's not too many people on the train."
    "The soft rumble of the train tracks and the shuffling of feet numb your mind, and you feel your eyelids growing heavy."
    "Thankfully, you reached your stop."

    p neutral "Oh, we're here."
    p sad "Will you be okay walking home from here?"
    mc neutral "It's fine. The sun hasn't set yet."
    p neutral "Alright then."
    p happy "See you at school, [playername]."
    mc neutral "(I think I got a little closer to Kyren today.)"

    jump episode_6
    return

# mc tutors performative guy
label episode_5_math:

    scene bg library_1 with fade

    "You called your chauffeur to drive you to a nearby library so you could work on your presentation."
    "Thankfully, the library wasn't too packed, and your presence was mostly unnoticed."

    mc neutral "(I should find an empty table near a window for natural light.)"

    "As you walk around and brush your fingers on the spines of displayed books, you catch a lingering scent in the air."
    "The library smelled of dusty books and heavy coffee. You notice a faint, musky sweetness exuding from every corner."
    "But you soon realize there's a new aroma slowly getting stronger, and you can't help but find this scent... familiar."
    "It's fresh and grassy, yet sweet and creamy."
    "Almost like..."

    mc neutral "(...Matcha?)"

    "Eh, whatever."
    "You find an empty table to set your belongings down before taking out several worksheets."
    "But before you could begin working, you hear a series of footsteps making their way towards you."
    "You turn to look in the direction of the footsteps, and you find a familiar figure."

    show kyren neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0

    p neutral "Oh, [playername], I didn't expect to see you here."
    p happy "I was looking for you at school and didn't see you."
    mc deadpan "(It's this guy.)"
    mc neutral "(Why is he here?)"
    p neutral "What are you doing here?"
    mc neutral "I'm..."

    menu:
        "Doing math homework":
            mc neutral "I'm doing math homework."
            p neutral "Really? What kind of math is it?"
        "None of your business":
            mc neutral "It's none of your business."
            p sad "Well... it wouldn't hurt to tell me, would it?"
            mc deadpan "..."
            mc neutral "(I guess I'll tell him.)"

    mc neutral "I have some linear algebra worksheets to complete."
    p neutral "Wow... linear algebra..."
    p neutral "That seems hard."
    p happy "You're such a genius, you know."
    p neutral "I'm just taking statistics this year, thankfully."
    p neutral "I'm soooo average and soooo dumb unlike you..."
    p neutral "I could never be smart enough to take those advanced math courses."
    p neutral "How many worksheets do you have to do?"

    
    jump episode_6
    return

# date w/ narcissist (kaylee)
label episode_6:

    jump episode_7
    return

# date w/ weeb (athena)
label episode_7:
    
    jump episode_8
    return

# date w/ looksmaxxer (kaylee)
label episode_8:

    jump episode_9
    return

# confessions
label episode_9:

    # if u see this, after u finish ep 4 im gonna tweak the beginning of this ep so it flows nicely
    scene bg black_background with fade

    "After an... interesting first day of school, you decided to go to bed early to relax."
    "However, ever since you woke up this morning, you feel as if there's been signs telling you that today won't be so typical either."
    "Let's take a look, shall we?"

    scene bg bedroom_dusk with fade

    "Friday, 5:00 AM."
    "*RING!*"
    "..."
    "*RING!* *RING!*"

    mc deadpan "...Ugh, I'm awake..."

    "The ringing of your phone's alarm burned through your ears."
    "Reaching an arm over with your eyes barely open, you try to find your phone to turn off the alarm."

    mc neutral "Where is it..."
    mc happy "Oh, here it is-"
    
    "*CRASH!*"

    mc shocked "..."

    "*RING!*"
    "Once you found your phone on your nightstand, you lazily dragged it across the marble surface..."
    "...But in doing so, you knocked over a mini mirror that happened to be sitting on the table."
    "Sitting up, you lean over the side of your bed, just to meet face-to-face with broken shards across the floor."

    mc deadpan "...Oops."
    mc neutral "Unfortunate... That's the mirror I got when I was a kid, too."
    mc deadpan "What a great start to the day..."

    "And unfortunately, this was definitely not the only strange thing to happen."

    scene bg living_room with fade

    "Friday, 6:00 AM."
    mc neutral "Cleaning up the glass was annoying."
    mc happy "It's fine. Nothing's better than starting the day with a fulfilling meal!"
    mc happy "And at least the weather's nice today."

    "After putting your plate in the sink for the housekeeper to wash while you're at school, you make your way towards the giant window in your living room."
    "From all the way up in your penthouse, all the pedestrians look like tiny ants, and cars look like pebbles."
    "However, before you can appreciate the view further, a black blob covered in feathers flew towards you and slammed against the window!"
    "*THUD!*"

    mc shocked "Ah!"
    mc shocked "Was that a bird?!"

    "Getting closer to the window, you notice that same feathered blob unelegantly falling to the streets."

    mc neutral "That scared me... It just came out of nowhere."

    "It's only 6 in the morning, and you already experienced two bad omens!"
    "Too bad for you, because that's not it!"

    scene bg school_street with fade

    "Friday, 7:30 AM."
    "After those two unfortunate events, you still managed to get yourself together and go to school."
    "Once your chauffeur dropped you off, you decided to explore the shops near the school until class started."

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Good luck charms, only sold today! Only $20 per charm! Protect yourself with these charms!!"
    mc neutral "(Hm? What's this?)"
    cashier "Young lady! Good morning! Would you like to purchase a good luck charm? Only sold today!"
    mc neutral "Why are they only being sold today?"
    cashier "Hoho! Look at a calendar! What day is it today?"
    mc deadpan "It's Friday, but so what?"

    "Taking out your phone, you quickly glance at the top of the screen where it shows the date."

    mc neutral "It's the 13th...?"
    cashier "Exactly! Friday the 13th! The unluckiest day of the year!"
    cashier "Young lady, with such a beautiful face and a heart of gold like yours, you can't take any risks on such an unlucky day!"
    mc neutral "(Isn't this just a superstition? What could possibly happen today out of all days?)"
    mc neutral "(Whatever. Twenty dollars is just twenty dollars.)"
    mc neutral "Here you go."
    cashier "Hehehe... Thank you for your purchase!! A lucky charm for a lucky girl! Have a good day!"
    
    "Isn't this just a placebo effect?"
    "Still, why not?"
    
    mc neutral "Thank you, you as well."
    
    hide cashier_neutral with dissolve

    "After making the purchase, you head over to the school entrance with the charm in your hand."

    mc neutral "(Ah, I have to remember to talk to my counselors about applying to American universities as an international stude-)"

    "*CRACK!*"
    mc shocked "...?!"

    "...Not even ten minutes after buying it, the wooden charm in your hand snapped in half!"

    mc deadpan "That... probably isn't a good sign."

    "If the mirror shattering wasn't already a signal that something won't go well today, this just confirmed it!"
    "But superstitions are just superstitions, right?"
    "..."
    "...Right?"

    # mmight do some interactive stuff with the morning classes, like how going to class in persona5 works
    scene bg cafe_outside with fade 

    "Friday, 12:00 PM."
    "Thankfully, your morning classes went smoothly, and nothing was out of the ordinary. After all, superstitions are just superstitions."
    "More importantly, it's time for lunch!"
    "You head over to the same cafe from the day before to get something to eat."

    mc happy "(I'm starving...)"
    mc neutral "(I didn't look too closely at the menu yesterday, hopefuly they have something filling.)"

    scene bg cafe with fade

    "Entering the cafe, you immediately notice that the place is packed with students."
    "Laughter and chit-chat flood every corner, and you can feel the vibrations of footsteps ripple across the floorboards."

    mc neutral "(The line's not too long, thankfully.)"
    mc happy "(It'd be unfortunate if I had to wait a long time just to order.)"

    scene bg cafe with fade

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Welcome! What can I get for you?"
    mc neutral "Can I get a..."
    
    menu:
        "Egg and ham sandwich":
            mc neutral "Egg and ham sandwich, please?"
        "Caesar salad":
            mc neutral "Caesar salad, please?"
        "Vegetable wrap":
            mc neutral "Vegetable wrap, please?"
    
    cashier "Yep, anything else?"
    mc neutral "(I should probably get a drink too.)"
    mc neutral "Can I also have a..."

    menu: 
        "Milk tea":
            mc neutral "Milk tea, please?"
            cashier "Of course!"
        "Water":
            mc neutral "Water, please?"
            cashier "Of course!"
        "Energy drink":
            mc neutral "Energy drink, please?"
            cashier "Of course!"
    
    cashier "Can I get a name for the order?"
    mc neutral "[playername]."
    cashier "That'll be $15.25."

    hide cashier_neutral with dissolve

    "After swiping your card, you find an empty seat to wait under your order is ready."

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Order for [playername]!"
    mc neutral "Thank you."
    cashier "Have a good day!"
    
    hide cashier_neutral with dissolve

    "After getting your order, you leave the cafe to find a quieter place to eat."

    mc neutral "(I heard they open the door to the rooftop during lunch hours.)"
    mc neutral "(I'll go check it out.)"

    scene bg rooftop_afternoon with fade

    "Heading over to the rooftop, you realize that nobody's there besides you."

    mc neutral "Huh... Maybe people just prefer to be near air conditioning."
    mc happy "Oh well. More room for me."

    "Settling down on a bench, you peacefully eat your meal while watching videos on your phone, until you hear a series of footsteps making their way towards you."

    mc neutral "(Did someone come up here?)"
    mc neutral "(Who is it-)"
    mc deadpan "(...Oh. It's this guy.)"

    "Lo and behold, the figure that appeared in front of you turned out to be..."

    show kyren neutral with dissolve:
        zoom 0.25
        xcenter 0.5
        yalign 1.0
    
    "Kyren Miller, the guy you met yesterday morning."

    p neutral "Hey, [playername], what a coincidence!"
    p happy "I didn't think you would be up here as well."
    p neutral "How has your day been?"
    mc neutral "It's been..."

    menu:
        "Good":
            mc neutral "It's been good."
            p happy "I'm happy to hear that!"
            p neutral "Hopefully I can continue that with what I want to say."
        "Alright":
            mc neutral "It's been alright."
            p neutral "That's good."
            p neutral "Hopefully I can make your day better with what I want to say."
        "Bad":
            mc neutral "It's hasn't been great."
            p sad "Aw, I'm sorry to hear that."
            p neutral "Hopefully I can make your day better with what I want to say."

    mc deadpan "(Why do I have a bad feeling about this...)"
    p neutral "The truth is..."
    p neutral "I'm in love with you, [playername]."
    mc shocked "...?!"

    "Wow."
    "Not to brag, but you were already used to abrupt love confessions from people you barely knew, but this guy just set a new record!"

    mc deadpan "I've known you for a day."
    p sad "Yes, but for me, it was love at first sight!"
    p neutral "You remember, right? We have so much in common!"
    p sad "I'm only into niche things, so it was so surprising that someone else had similar interests!"
    p neutral "It's okay, you don't have to say anything, I know."
    mc neutral "(You know that you sound crazy right now? That's great to hear.)"
    p neutral "I know that growing up, someone like you probably struggled to open up, so you can't help but act reserved."
    p neutral "Oh, you're wondering how I know? I read about it in a feminist literature book."
    mc deadpan "..."

    "Again, this guy just doesn't know when to stop talking nonsense."
    "What will you do?"


    return