﻿## Keymap Changes ###############################################################################################################

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['help'].remove('meta_shift_/')
    config.keymap['help'].remove('K_F1')
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['hide_windows'].remove('h')


## Toggling Splash Screen upon Launch ###########################################################################################

init python:
    persistent.splash = True


## Characters ###################################################################################################################

define narrate = nvl_narrator
define a = Character("Anchor", what_prefix='"', what_suffix='"')
define d = Character("Dakota", image="dakota", what_prefix='"', what_suffix='"')
define j = Character("Jessica", image="jessica", what_prefix='"', what_suffix='"')
define ja = Character("Jangle", image="jangle", what_prefix='"', what_suffix='"')
define ji = Character("Jingle", image="jingle", what_prefix='"', what_suffix='"')
define k = Character("Kate", image="kate", what_prefix='"', what_suffix='"')
define kr = Character("Krag", color="#d00000", image="krag", what_prefix='"', what_suffix='"') # Mr. Sprinkles
define l = Character("Laura", what_prefix='"', what_suffix='"')
define m = Character("Ms. Madeline", image="madeline", what_prefix='"', what_suffix='"')
define r = Character("Richard", image="richard", what_prefix='"', what_suffix='"')
define re = Character("Reddington", color="#d00000", what_prefix='"', what_suffix='"')
define s = Character("Mr. Sprinkles", color="#d00000", image="sprinkles", what_prefix='"', what_suffix='"') # Krag Dovason


## Character Sprites ############################################################################################################

image dakota confident = "Characters/Dakota/confident.png"
image dakota confused = "Characters/Dakota/confused.png"
image dakota determined = "Characters/Dakota/determined.png"
image dakota mad = "Characters/Dakota/mad.png"
image dakota neutral = "Characters/Dakota/neutral.png"
image dakota sad = "Characters/Dakota/sad.png"
image dakota small_smile = "Characters/Dakota/small_smile.png"
image dakota smirk = "Characters/Dakota/smirk.png"

image jangle = Placeholder("boy")

image jessica = Placeholder("girl")

image jingle = Placeholder("girl")

image kate alert = "Characters/Kate/alert.png"
image kate concerned = "Characters/Kate/concerned.png"
image kate confused = "Characters/Kate/confused.png"
image kate excited = "Characters/Kate/excited.png"
image kate happy = "Characters/Kate/happy.png"
image kate mad = "Characters/Kate/mad.png"
image kate shocked = "Characters/Kate/shocked.png"

image krag concerned = "Characters/Krag/concerned.png"
image krag horrified = "Characters/Krag/horrified.png"
image krag laughing = "Characters/Krag/laughing.png"
image krag neutral = "Characters/Krag/neutral.png"
image krag smile = "Characters/Krag/smile.png"
image krag worried = "Characters/Krag/worried.png"

image laura concerned = "Characters/Laura/concerned.png"
image laura determined = "Characters/Laura/determined.png"
image laura excited = "Characters/Laura/excited.png"
image laura mad = "Characters/Laura/mad.png"
image laura neutral = "Characters/Laura/neutral.png"
image laura rage = "Characters/Laura/rage.png"
image laura sad = "Characters/Laura/sad.png"
image laura shocked = "Characters/Laura/shocked.png"
image laura smile = "Characters/Laura/smile.png"
image laura smug = "Characters/Laura/smug.png"
image laura surprised = "Characters/Laura/surprised.png"
image laura wut = "Characters/Laura/wut.png"

image madeline blank = "Characters/Madeline/blank.png"
image madeline shocked = "Characters/Madeline/shocked.png"
image madeline smile = "Characters/Madeline/smile.png"

image richard concerned = "Characters/Richard/concerned.png"
image richard glare = "Characters/Richard/glare.png"
image richard laughing = "Characters/Richard/laughing.png"
image richard rage = "Characters/Richard/rage.png"
image richard shocked = "Characters/Richard/shocked.png"
image richard smile = "Characters/Richard/smile.png"

image sprinkles evilgrin = "Characters/Sprinkles/evilgrin.png"
image sprinkles happy = "Characters/Sprinkles/happy.png"
image sprinkles hm = "Characters/Sprinkles/hm.png"
image sprinkles horror = "Characters/Sprinkles/horror.png"
image sprinkles huh = "Characters/Sprinkles/huh.png"
image sprinkles jeer = "Characters/Sprinkles/jeer.png"
image sprinkles laugh = "Characters/Sprinkles/laugh.png"
image sprinkles wut = "Characters/Sprinkles/wut.png"


## Images ####################################################################################################################

# Solid Backgrounds
image black = "#000000"
image white = "#ffffff"
image choice_bg:
    "#000000"
    alpha 0.35

# Main Images
image splash = "Good Tales Transparent.png"
image logo = "gui/logo.png"
image sprinklelogo:
    "Ringleader Draft.png"
    size(360, 475)
image pause_bg = "gui/save_bg.jpg"
image textbox_bg:
    "gui/textbox_bg.png"
    yalign 0.99
image spotlight = "spotlight.png"

# Text Images
image announcetext = ParameterizedText(style='announce')
image ctc = ParameterizedText(style='ctc')

# Animated Images
image ctc_arrow_1:
    xalign 0.5 yalign 0.99
    "gui/ctc_arrow.png"
    block:
        ease 0.15 xalign 0.45
        ease 0.15 xalign 0.5
        repeat
image ctc_arrow_nvl:
    xalign 0.95 yalign 0.99
    "gui/ctc_arrow.png"
    block:
        ease 0.15 xalign 1.0
        ease 0.15 xalign 0.95
        repeat

# Main Menu Images
image dust = SnowBlossom("dust_alpha", count=5, xspeed=(10, 40), yspeed=(3, 6), start=5, fast=True, horizontal=True)
image dust2 = SnowBlossom("dust particle 2.png", count=10, xspeed=(10, 40), yspeed=(3, 6), start=5, fast=True, horizontal=True)
image dust3 = SnowBlossom("dust_alpha", count=5, xspeed=(-40, -10), yspeed=(3, 6), start=5, fast=True, horizontal=True)
image dust4 = SnowBlossom("dust particle 2.png", count=10, xspeed=(-40, -10), yspeed=(3, 6), start=5, fast=True, horizontal=True)
image dust_alpha:
    "dust particle.png"
    choice:
        alpha 0.25
    choice:
        alpha 0.5
    choice:
        alpha 0.75
    choice:
        alpha 1.0
image fade_into_menu:
    "#000000"
    block:
        ease 0.05 alpha 0.5
        ease 0.05 alpha 1.0
        repeat 3
    ease 1.0 alpha 0.0


## Backgrounds ###################################################################################################################

image bg fade = "#000000"
image bg flash = "#ffffff"
image bg stage = "BG/stage.jpg"
image bg curtain = "BG/sprinklescurtain.jpg"
image bg showstage = "BG/showstage.jpg"
image bg livingroom = "BG/livingroom.jpg"
image bg dakotaroom = "BG/dakotaroom.jpg"
image bg newsroom = "BG/newsroom.jpg"
image bg arena_ext = "BG/arenaexterior.jpg"


## Custom Audio Channels #########################################################################################################

init python:
    renpy.music.register_channel('ambience', mixer="sound", loop=True)


## Audio #########################################################################################################################

# Music
define audio.title = "audio/music/title.ogg"
define audio.arcade_madness = "audio/music/Arcade-Madness.mp3"
define audio.autumn_changes = "audio/music/Autumn-Changes_Looping.mp3"
define audio.techno_celebration = "audio/music/Techno-Celebration-Looping.mp3"
define audio.neon_runner = "audio/music/Neon-Runner_Looping.mp3"
define audio.after_the_invasion = "audio/music/After-the-Invasion_Looping.mp3"
define audio.bells_of_weirdness = "audio/music/Bells-of-Weirdness_Looping.mp3"
define audio.vast_places = "audio/music/Vast-Places_Looping.mp3"
define audio.classy_ghouls = "audio/music/Classy-Ghouls-Halloween-Gathering_Looping.mp3"
define audio.the_calm = "<to 111.628 loop 11.163>audio/music/The Calm.mp3"

# Sound Effects
define audio.flicker = "audio/se/flicker.ogg"
define audio.drumroll_buildup = "<to 4.9 loop 0.5>audio/se/drumroll.ogg"
define audio.drumroll_finish = "<from 4.9>audio/se/drumroll.ogg"
define audio.applause = "audio/se/applause.ogg"
define audio.doorbell = "audio/se/doorbell.ogg"
define audio.door_open = "audio/se/door_open.ogg"
define audio.helicopter_loop = "<to 6 loop 1>audio/se/helicopter.ogg"
define audio.helicopter_finish = "<from 6>audio/se/helicopter.ogg"
define audio.siren = "audio/se/siren.ogg"


## Transforms ###################################################################################################################

# Animated Transforms
transform logo_rotate:
    size(336, 337)
    xanchor 0.5 yanchor 0.5
    xalign -0.088
    ycenter 0.235
    ease 1.0 rotate 5
    block:
        ease 2.0 rotate -10
        ease 2.0 rotate 10
        repeat
transform choice_dissolve:
    alpha 0.0
    ease 1.0 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0
transform menu_lower:
    xanchor 0.5 yanchor 1.0
    xalign 0.5 yalign 0.0
    ease 0.5 yalign 1.0
transform scrollup:
    xalign 0.5 yalign 1.05
    ease 15.0 yalign -0.05
transform spotlight_wander:
    xalign 1.0 yalign 1.0
    block:
        linear 1.0 xalign 0.0 yalign 0.0
        linear 0.5 yalign 1.0
        linear 1.0 xalign 1.0 yalign 0.0
        linear 0.5 yalign 1.0
        repeat
transform spotlight_focus:
    linear 0.1 xalign 0.57 yalign 0.35

# Character Transforms
transform middle:
    xalign 0.5 yalign 0.5
transform middle_s:
    xalign 0.5 yalign 0.0
transform middle_r:
    xalign 0.5 yalign -0.1
transform middle_m:
    xalign 0.5 yalign -0.2

transform left:
    xalign 0.05 yalign 0.5
transform left_s:
    xalign 0.05 yalign 0.0
transform left_r:
    xalign 0.05 yalign -0.1
transform left_m:
    xalign 0.05 yalign -0.2

transform right:
    xalign 0.95 yalign 0.5
transform right_s:
    xalign 0.95 yalign 0.0
transform right_r:
    xalign 0.95 yalign -0.1
transform right_m:
    xalign 0.95 yalign -0.2

transform two1:
    xalign 0.25 yalign 0.5
transform two1_s:
    xalign 0.25 yalign 0.0
transform two1_r:
    xalign 0.25 yalign -0.1
transform two1_m:
    xalign 0.25 yalign -0.2

transform two2:
    xalign 0.75 yalign 0.5
transform two2_s:
    xalign 0.75 yalign 0.0
transform two2_r:
    xalign 0.75 yalign -0.1
transform two2_m:
    xalign 0.75 yalign -0.2

transform sideimage:
    size(225, 225)
    xalign 0.0575 yalign 1.0


## Styles ########################################################################################################################

style announce:
    font "fonts/circula-medium.otf"
    color "#ffffff"
    text_align 0.5
    size 50
style dateandtime:
    font "fonts/NEON GLOW.otf"
    color "#d00000"
    text_align 0.5
    size 100
style remaining:
    font "fonts/circula-medium.otf"
    color "#d00000"
    xmaximum 1200
    text_align 0.5
    size 65
style ctc:
    font "fonts/circula-medium.otf"
    color "#d00000"
    text_align 0.5
    size 25
style creditheader:
    font "fonts/circula-medium.otf"
    color "#b00000"
    text_align 0.5
    size 50
style credittext:
    font "fonts/Stanberry.ttf"
    color "#ffffff"
    text_align 0.5
    size 25
style chaptertext:
    font "fonts/circula-medium.otf"
    color "#d00000"
    text_align 0.5
    size 75
style chaptersub:
    font "fonts/Stanberry.ttf"
    color "#ffffff"
    text_align 0.5
    size 50


## Custom Screens ################################################################################################################

# Overlay Screens
screen ctc():
    zorder 100
    if nvl == True:
        add "ctc_arrow_nvl"
    else:
        add "ctc_arrow_1"
screen laura():
    zorder 100
    if l_exp == "concerned":
        add "laura concerned" at sideimage
    elif l_exp == "determined":
        add "laura determined" at sideimage
    elif l_exp == "excited":
        add "laura determined" at sideimage
    elif l_exp == "mad":
        add "laura mad" at sideimage
    elif l_exp == "neutral":
        add "laura neutral" at sideimage
    elif l_exp == "rage":
        add "laura rage" at sideimage
    elif l_exp == "sad":
        add "laura sad" at sideimage
    elif l_exp == "shocked":
        add "laura shocked" at sideimage
    elif l_exp == "smile":
        add "laura smile" at sideimage
    elif l_exp == "smug":
        add "laura smug" at sideimage
    elif l_exp == "surprised":
        add "laura surprised" at sideimage
    elif l_exp == "wut":
        add "laura wut" at sideimage
screen chaptername():
    vbox:
        xalign 0.5 yalign 0.5
        text "[save_name]" style "chaptertext" xalign 0.5
        text "[save_subtitle]" style "chaptersub" xalign 0.5
screen dateandtime():
    vbox:
        xalign 0.5 yalign 0.25
        text "[currenttime]" style "dateandtime" xalign 0.5
        text "[currentdate]" style "dateandtime" xalign 0.5
screen timeremaining():
    text "[timeleft] until the [event]" style "remaining" xalign 0.5 yalign 0.6
screen credits():
    if creditpos == 1:
        vbox:
            xalign 0.5 yalign 0.5
            spacing 10
            text "[credit_header]" style "creditheader" xalign 0.5
            text "[credit_text]" style "credittext" xalign 0.5
    elif creditpos == 2:
        vbox:
            xalign 0.25 yalign 0.25
            spacing 10
            text "[credit_header]" style "creditheader" xalign 0.5
            text "[credit_text]" style "credittext" xalign 0.5
    elif creditpos == 3:
        vbox:
            xalign 0.75 yalign 0.25
            spacing 10
            text "[credit_header]" style "creditheader" xalign 0.5
            text "[credit_text]" style "credittext" xalign 0.5
    elif creditpos == 4:
        vbox:
            xalign 0.25 yalign 0.75
            spacing 10
            text "[credit_header]" style "creditheader" xalign 0.5
            text "[credit_text]" style "credittext" xalign 0.5
    elif creditpos == 5:
        vbox:
            xalign 0.75 yalign 0.75
            spacing 10
            text "[credit_header]" style "creditheader" xalign 0.5
            text "[credit_text]" style "credittext" xalign 0.5

# Menu Screens
screen extras():
    tag menu
    add gui.main_menu_background
    vbox:
        xalign 0.5 yalign 0.5
        spacing 10
        textbutton "Chapter Select" action ShowMenu('chapterselect')
        textbutton "Achievements" action NullAction()
        textbutton "Credits" action Jump('credits')
        textbutton "Follow Good Tales!" action NullAction()
        null height 10
        textbutton "Return" action ShowMenu('main_menu')
screen chapterselect():
    tag menu
    add gui.main_menu_background
    vbox:
        xalign 0.5 yalign 0.5
        spacing 10
        if persistent.chapter1:
            textbutton "Chapter 1" action Replay("chapter_1") xalign 0.0
        else:
            textbutton "LOCKED" action NullAction() xalign 0.0
        if persistent.chapter2:
            textbutton "Chapter 2" action Replay("chapter_2", scope={"currenttime": "5:23 AM", "currentdate": "March 31st, 2030", "timeleft": "13 hours and 37 minutes", "event": "REDD War begins"}) xalign 1.0
        else:
            textbutton "LOCKED" action NullAction() xalign 1.0
        null height 10
        textbutton "Return" action ShowMenu("extras") xalign 0.5


## Variable Defaults #############################################################################################################

default persistent.gore = True
default version = 0.0
default l_exp = ""
default nvl = False
default currenttime = "4:12 PM"
default currentdate = "March 30th, 2030"
default timeleft = "2 hours and 48 minutes"
default event = "War Zones are revealed"
default clickortap = "Click"
default creditpos = 0
default credit_header = "Writing and Development"
default credit_text = "Cole Goodrich"

## Labels ########################################################################################################################

# Splash Screen/Main Menu Intro
label before_main_menu:
    scene bg fade
    play music title noloop
    if persistent.splash == True:
        pause 1.0
        show announcetext "This story contains graphic violence and strong language and is\nintended for mature audiences" at truecenter
        with Dissolve(1.0)
        pause 2.0
        hide announcetext
        with Dissolve(1.0)
        show splash at truecenter
        with Dissolve(1.0)
        hide circustext
        pause 2.0
        hide splash
        with Dissolve(1.0)
        pause 0.1
        $ persistent.splash = False
    play sound flicker
    show logo:
        xalign 0.5 yalign 0.5
        alpha 0.0
        pause 0.1
        block:
            ease 0.05 alpha 0.5
            ease 0.05 alpha 0.0
            repeat 4
        pause 0.2
        ease 0.2 alpha 0.5
        ease 0.2 alpha 0.0
        pause 0.4
        ease 0.2 alpha 1.0
    pause 2.1
    show logo:
        alpha 1.0
        size(672, 674)
        parallel:
            linear 1.0 xalign 0.0 yalign 0.0
        parallel:
            linear 1.0 size(336, 337)
    pause 1.0
    return

# Shows Chapter Name and Subtitle
label chaptername:
    show screen chaptername
    with dissolve
    $renpy.pause(delay=3)
    hide screen chaptername
    with dissolve
    pause 2
    return

# Shows Time, Date, and Time Remaining
label chapterstart:
    stop music
    stop sound
    if renpy.variant('mobile'):
        $clickortap = "Tap"
    play sound flicker
    show screen dateandtime
    with Dissolve(0.05)
    hide screen dateandtime
    with Dissolve(0.05)
    show screen dateandtime
    with Dissolve(0.05)
    hide screen dateandtime
    with Dissolve(0.05)
    show screen dateandtime
    with Dissolve(0.05)
    hide screen dateandtime
    with Dissolve(0.05)
    show screen dateandtime
    with Dissolve(0.05)
    hide screen dateandtime
    with Dissolve(0.05)
    pause 0.5
    show screen dateandtime
    with dissolve
    pause 2
    show screen timeremaining
    with dissolve
    show ctc "[clickortap] anywhere to continue":
        alpha 0.0
        xalign 0.5 yalign 0.9
        pause 3
        block:
            alpha 1.0
            pause 1
            alpha 0.0
            pause 1
            repeat
    $renpy.pause()
    hide screen dateandtime
    hide screen timeremaining
    hide ctc
    with dissolve
    return

# Start of Story
label start:
    play sound "audio/se/gong.ogg"
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(1.0)
    pause 3
    $save_name = "Chapter 1"
    $save_subtitle = "The Calm Before the Storm"
    if not persistent.gorewarning:
        "This visual novel contains graphic violence and has visuals to accomodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){nw}"
        menu:
            "This visual novel contains graphic violence and has visuals to accomodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){fast}"
            "Yes":
                $persistent.gore = False
                "Graphic images disabled."
            "No":
                $persistent.gore = True
                "Graphic images enabled."
        window hide dissolve
        pause 2
        $persistent.gorewarning = True
    jump chapter_1

# Credits
label credits:
    scene bg fade
    play music title
    show logo:
        xalign 0.5 yalign 0.5
        alpha 0.0
        pause 0.1
        block:
            ease 0.05 alpha 0.5
            ease 0.05 alpha 0.0
            repeat 4
        pause 0.2
        ease 0.2 alpha 0.5
        ease 0.2 alpha 0.0
        pause 0.4
        ease 0.2 alpha 1.0
        pause 3.0
        ease 1.0 alpha 0.0
    pause 6.6
    scene bg stage
    with Dissolve(1)
    $creditpos = renpy.random.randint(1, 5)
    show screen credits
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "Story"
        credit_text = "Cole Goodrich\nSlightlySimple"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "Character Art"
        credit_text = "HazardSquare"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "Background Art"
        credit_text = "Mattyd\n(MacDaddyMatty.com)"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "Sound Effects"
        credit_text = "freesound.org\nCole Goodrich"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "{image=renpy.png}"
        credit_text = "Made with Ren'Py 7.3"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=5)
    python:
        credit_header = "Special Thanks"
        credit_text = "God\nTom \"PyTom\" Rothamel\nJames DeMonaco\nSlightlySimple\nDems\nYou"
        creditpos = renpy.random.randint(1, 5)
    with dissolve
    $renpy.pause(delay=7)
    hide screen credits
    with Dissolve(1.5)
    pause 2.0
    scene bg fade
    with Dissolve(3)
    pause 2
    show announcetext "The End" at truecenter
    with Dissolve(3)
    pause 3
    hide announcetext
    stop music fadeout(6.0)
    with Dissolve(3)
    pause 5
    return