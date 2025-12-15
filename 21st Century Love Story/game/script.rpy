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
define g = Character("[gymbro]", image="king")
# pnw = pacific northwest!
define teacher = Character("Mr. Teacher")
define classmate = Character("classmate")
define b1 = Character("Bully 1", image="bully1")
define b2 = Character("Bully 2", image="bully2")
# mean gurlz
define s = Character("[meangirl]")
# i'm thinking about combining Sophia and Olivia to be the same person? :p will bring it up next call

# character sprites
image player neutral = "side player neutral.png"

image kyren neutral = "kyren_neutral.png"
image kyren angry = "kyren_angry.png"
image kyren sad = "kyren_sad.png"
image kyren happy = "kyren_happy.png"
image kyren shocked = "kyren_shocked.png"

image king neutral = "gymbro_neutral.png"
image king disgusted = "gymbro_disgusted.png"

image cashier_neutral = "cashier.png"
image classmate_neutral = "billG.jpg"

image narcissist_neutral = "narcissist_neutral.png"
image weeb_neutral = "weeb_neutral.png"

# image define b1 neutral = "bully1 neutral.png"
# image define b2 neutral = "bully2 neutral.png"

image b1_neutral = "bully1 neutral.png"
image b2_neutral = "bully2 neutral.png"

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
# image bg classroom_morning = "classroom_morning.webp" it dont work its too small
image bg quad_outside_arts_building = "monele_arts_building.webp"
image bg rooftop_afternoon = "rooftop.png"
    # house backgrounds
image bg bedroom_afternoon = "room_afternoon_light_loff.jpg"
image bg bedroom_dusk = "room_dusk_light_on.jpg"
image bg bedroom_morning = "room_morning_light_off.jpg"
image bg bedroom_night = "room_night_light_off.jpg"
image bg dining_room = "condo_Day 03.jpg"
image bg living_room = "condo_Day 05.jpg"

# The game starts here.

label start:

    scene bg black_background

    $ playername = "You"
    $ performative = "???"
    $ narcissist = "Guy Sitting By Himself"
    $ weeb = "Guy With Disheveled Hair"
    $ gymbro = "Tough Looking Guy"
    $ meangirl = "???"

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
    # if time, cutscene of alice during her rich childhood
    "Growing up, you had a childhood that most people could only dream of."
    "You were fortunate enough to be born into a conglomerate family in China, Fuyu Group, and you've always gotten everything you wanted."
    "...Well, almost everything you've wanted."
    "Previously, you attended a private academy in Beijing your entire life. However, your family's company wanted to expand its international influence..."
    "...And you were forced to transfer to a high school in the west."
    # if time, cutscene of alice in front of school
    "Milkyway Academy, a large private high school in New York City known for its rigorous learning environment focused on math, science, and technology."
    "Surprisingly, even though this school holds a large and diverse student population, you are the only new exchange student this year."
    "And unlike typical exchange students who live with a host family, your family rented out a penthouse for you."
    "Pretty cool, right?"
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

    mc happy "(I never realized the school had a cafe next to it. That works out really well.)"
    mc neutral "(I'll go check it out. Hopefully they have something good.)"

    scene bg cafe with fade

    show cashier_neutral with dissolve:
        zoom 1.5
        xcenter 0.5
        yalign 1.0

    cashier "Welcome! What can I get for you today?"

    menu:
        "Can I get a matcha latte?":
            $ choice = "matchalatte"
        "Can I get a frappuccino?":
            $ choice = "frappuccino"

    if choice == "matchalatte":
        cashier "Good choice!"
        cashier "Our matcha is the best of the best!"
    elif choice == "frappuccino":
        cashier "Are you sure? I think I'll give you a matcha latte instead."
        mc deadpan "Um..."
        menu:
            "That's fine.":
                mc deadpan "Um... okay."
            "No, I said what I said.":
                mc deadpan "...No, I said I wanted a frappuccino."

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
    mc neutral "...Go ahead."
    p neutral "Thank you."

    "The strange boy takes a seat directly across from you, but not before you notice a strange keychain dangling from his belt loop."
    "He sets a book down on the table that reads \"Feminist Literature by Cyx Sehvyn\" and hangs his tote bag on his chair."
    "But it seems that you've drawn the attention of other students in the cafe."
    "Muttered voices suddenly flood the room as the boy wearing a quarter zip-up smiles at you."
    "\"Do you see that? He's going after another girl?!\""
    "\"Wait... Isn't that [playername]? The nepo baby exchange student?\""
    "\"Is Kyren serious? He's really going to try this on HER of all people?!\""
    "\"Does he realize his life is over if he offends her or something?\""

    mc deadpan "(Do all people here talk so loud?)"

    p neutral "You're [playername], right?"

    $ performative = "Kyren"

    p neutral "I'm Kyren, it's nice to meet you."
    p neutral "I've heard great things about you and Fuyu Group! How have you been adjusting so far?"
    mc neutral "Well..."

    menu:
        "It's been well":
            mc neutral "I've been adjusting well."
            p happy "That's great to hear!"
        "It's been okay":
            mc neutral "It's been alright."
            p neutral "That's good!"
        "It's been bad":
            me neutral "I haven't been adjusting very well."
            p sad "Sorry to hear that, hopefully it gets better."

    p neutral "I saw you deciding between matcha and a frappuccino when I was waiting in line earlier."
    p happy "Which one do you like more? Personally, I'm team matcha."
    p neutral "I've been drinking it for years, way before it became popular."
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

    "You take out your phone and notice that it's 7:25. Your first class starts in only five minutes!"
    "Quickly opening WheeChat, Kyren scans your QR code and sends you a friend request. You reluctantly accept the friend request before throwing your bag over your shoulders."

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
        "(Approach them.)":
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
                mc neutral "..."
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
    mc angry "If you call me that one more time, I'm going to beat you up myself."
    w "B-b-b-b-but you really are her!!!"

    hide weeb_neutral

    "...Maybe you should've let this guy to get beat."
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

    mc neutral "Well... bye."
    w "W-w-w-wait!! Suzuki Harukaaaaaaa!!!!"

    jump episode_4

    return

# lunch + meet gymbro (CURRENTLY UNFINISHED)
label episode_4:
    scene bg classroom_04 with fade
    "One long lecture later..."
    "*RING!*"
    mc happy "(It's finally time for lunch! What a day it's been...)"
    # mc neutral "(Milkyway High School really is full of interesting characters.)"
    "Some students stay behind in the classroom, some students rush to leave, and some students come to eat with their friends."
    "Hopefully, you can get along with everyone, too. But first, where do you want to eat?"
    menu:
        "(Eat lunch in the classroom.)":
            # results in encounter with mean gurlz (olivia/sophia?)
            mc neutral "(Yep, I won't bother getting up right now.)"
            "You reach into your bag and take out the bento you made this morning."
        "(Eat lunch outside.)":
            # just encounter with gymbro
            jump episode_4_outside
        "(Grab something from the cafe.)":
            # another encounter with performative maybe?
            jump episode_4_cafe
    
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
        "(Say hi.)":
            
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

            mc neutral "..."
            mc deadpan "(What the?)"
            mc deadpan "(So rude.)"
            mc neutral "(Whatever.)"
            mc happy "(All that matters is that I get to eat lunch now!)"

            "Finding an empty bench, you place down your bag and take out your bento."
            mc happy "Home-cooked food is always the best! *om nom nom nom nom*"

            s "Soooo...YOU'RE [playername]?"
            "Mid=chew, you look up and see..."
            # show s neutral
            "...an unfamiliar face."

            # olivia (nepo baby) likes narcissist, confronts mc
                # pretending to befriend her, "i have connections too, you're not special"
            # gym bro comes back



            # gym bro and twin secret twin brothers
            # also results in encounter with mean girl?
            #  _______________
            # |COME BACK!!!!!|
            # ---------------
            #   __  __
            #  | |_| |
            # |   _ _|
            # (    ^ )
            # different route...
            

            "This is a bookmark for testing purposes."

        "(Walk past him.)":
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

    jump episode_5
    return

label episode_4_cafe:
    scene bg quad_outside_arts_building with fade
    mc neutral "(Hmm...I think the cafe should be this way.)"

    show kyren neutral with dissolve
    p happy "[playername]? What a coincidence! You're going to the cafe too?"
    p neutral "Wanna go together?"

    # menu:
    #     "Yes":
    #         mc neutral "Sure, why not."
    #         jump episode_4_in_cafe
    #     "No":
    #         mc neutral "No, thank you.":
    #         #idk

    scene bg cafe_memoria_outside_04_afternoon with dissolve
    jump episode_5
    return

# conflict/climax, all characters confess
label episode_5:
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
    p neutral "I like you, [playername]."
    mc shocked "...?!"

    "Wow."
    "Not to brag, but you were already used to abrupt love confessions from people you barely knew, but this guy just set a new record!"

    mc deadpan "I've known you for a day."
    p sad "Yes, but for me, it was love at first sight!"
    p neutral "You remember, right? We have so much in common!"
    p sad "I'm only into niche things, so it was so surprising that someone else had similar interests!"
    p neutral "It's okay, you don't have to say anything, I know."
    mc neutral "(You know that you sound crazy right now? That's great to hear.)"
    p neutral "I know that someone like you growing up."

    jump episode_6
    return

# date w/ performative (athena)
label episode_6:

    return

# date w/ narcissist (kaylee)
label episode_7:
    
    return

# date w/ weeb (athena)
label episode_8:

    return

# date w/ gym bro (kaylee)
label episode_9:

    return