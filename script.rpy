## Keymap Changes ###############################################################################################################

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
define an = Character("Announcer", what_prefix='"', what_suffix='"', what_italic=True, who_italic=True)
define d = Character("Dakota", image="dakota", what_prefix='"', what_suffix='"')
define j = Character("Jessica", image="jessica", what_prefix='"', what_suffix='"')
define ja = Character("Jangle", color="#d00000", image="jangle", what_prefix='"', what_suffix='"')
define ji = Character("Jingle", color="#d00000", image="jingle", what_prefix='"', what_suffix='"')
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
image commencement_overlay = "Commencement_Overlay.png"

# Text Images
image announcetext = ParameterizedText(style='announce')
image ctc = ParameterizedText(style='ctc')
image game_name = ParameterizedText(style='game')
image credit_1 = ParameterizedText(style='creditheader')
image credit_2 = ParameterizedText(style='creditheader')
image credit_3 = ParameterizedText(style='creditheader')

# Animated Images
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
image logo_light:
    size(336, 337)
    "gui/logo_light01.png"
    pause 1
    "gui/logo_light02.png"
    pause 1
    repeat
image fade_into_menu:
    "#000000"
    block:
        ease 0.05 alpha 0.5
        ease 0.05 alpha 1.0
        repeat 3
    ease 1.0 alpha 0.0
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
image bg dressingroom = "BG/dressingroom.jpg"
image bg livestage = "BG/livestage.jpg"
image bg arena_hall = "BG/arenahall.jpeg"
image bg commencement = "BG/commencement.png"


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
define audio.the_twins = "<to 68 loop 4>audio/music/The Twins.mp3"
define audio.sprinkles_theme = "<to 64>audio/music/The Mr Sprinkles Show.mp3"
define audio.creaky_country_fair = "audio/music/Creaky-Country-Fair.ogg"

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
define audio.door_knock = "audio/se/doorknock.ogg"
define audio.crowd = "audio/se/crowd.ogg"


## Transforms ###################################################################################################################

# Animated Transforms
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
transform game_name_flash:
    xalign 0.5 yalign 0.1
    block:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat
transform credit_scroll_1:
    xalign 0.25 yalign 1.5
    linear 15 yalign -0.5
transform credit_scroll_2:
    xalign 0.75 yalign 1.5
    linear 15 yalign -0.5
transform credit_scroll_3:
    xalign 0.75 yalign 2.0
    linear 13 yalign -1.0
transform notify_transform:
    xalign 0.95 yalign -0.1
    on show:
        ease 1.0 yalign 0.1
    on hide:
        ease 1.0 yalign -0.1

# Stationary Transforms
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

transform commencement:



## Styles ########################################################################################################################

style announce:
    font "fonts/circula-medium.otf"
    color "#ffffff"
    layout "subtitle"
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
    size 50
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
style game:
    font "fonts/Stanberry.ttf"
    color "#14ff00"
    text_align 0.5
    outlines [(1.0 ,'#ffffff', 0.0, 0.0)]
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
        add "laura excited" at sideimage
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
        text "[currentdate], 2030" style "dateandtime" xalign 0.5
screen timeremaining():
    text "[timeleft] until the [event]" style "remaining" xalign 0.5 yalign 0.6
screen gameover():
    vbox:
        xalign 0.5 yalign 0.5
        if badcredits:
            text "THE END...?" style "dateandtime"
        else:
            text "YOU DIED" style "dateandtime"
screen loadorquit():
    vbox:
        xalign 0.5 yalign 0.85
        spacing 10
        textbutton "Load Game" action ShowMenu('load') xalign 0.5
        textbutton "Main Menu" action MainMenu() xalign 0.5
        textbutton "Quit" action Quit() xalign 0.5
screen notify(message):
    zorder 100
    text message at notify_transform
    timer 5.0 action Hide('notify')

# Menu Screens
screen extras():
    tag menu
    add gui.main_menu_background
    vbox:
        xalign 0.5 yalign 0.5
        spacing 10
        textbutton "Chapter Select" action ShowMenu('chapterselect')
        textbutton "Achievements" action ShowMenu('achievements')
        textbutton "Credits" action [ToggleVariable('persistent.credits', True), Jump('credits')]
        textbutton "Follow Good Tales!" action NullAction()
        null height 10
        textbutton "Return" action ShowMenu('main_menu')
screen chapterselect():
    tag menu
    add gui.main_menu_background
    vbox:
        xalign 0.25 yalign 0.15
        spacing 10
        text "Chapter 1" xalign 0.5
        if persistent.chapter1_scene1:
            textbutton "Meet the Farrs" action Replay("chapter_1") xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
        if persistent.chapter1_scene2:
            textbutton "Unfortunate News" action Replay("kragonnews") xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
    vbox:
        xalign 0.75 yalign 0.15
        spacing 10
        text "Chapter 2" xalign 0.5
        if persistent.chapter2_scene1:
            textbutton "Evening Plans" action Replay("chapter_2", scope={"currenttime": "5:23 AM", "currentdate": "March 31st", "timeleft": "13 hours and 37 minutes", "event": "REDD War begins"}) xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
        if persistent.chapter2_scene2:
            textbutton "Backstage Drama" action Replay("backstagedrama", scope={"currentdate": "March 31st", "event": "REDD War begins"}) xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
        if persistent.chapter2_scene3:
            textbutton "Packed Parking" action Replay("arriveatshow", scope={"currentdate": "March 31st", "event": "REDD War begins"}) xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
        if persistent.chapter2_scene4:
            textbutton "Meet and Greet" action Replay("meetandgreet", scope={"currentdate": "March 31st", "event": "REDD War begins"}) xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
        if persistent.chapter2_scene5:
            textbutton "Showtime!" action Replay("showbegins", scope={"currentdate": "March 31st", "event": "REDD War begins"}) xalign 0.5
        else:
            textbutton "LOCKED" action NullAction() xalign 0.5
    textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.95
screen achievements():
    tag menu
    add gui.main_menu_background
    if persistent.achievement_toosafe:
        text "{i}Playing it TOO Safe{/i}\nEscape Atlanta" xalign 0.5 yalign 0.5
    else:
        text "LOCKED" xalign 0.5 yalign 0.5
    null height 10
    textbutton "Return" action ShowMenu("extras") xalign 0.25 yalign 0.9


## Variable Defaults #############################################################################################################

default persistent.gore = True
default preferences.fullscreen = True
define config.replay_scope = {"replay": True, "_game_menu_screen": "pause"}
default _game_menu_screen = "pause"
default version = 0.0
default replay = False
default gameover = False
default save_subtitle = ""
default l_exp = ""
default nvl = False
default currenttime = "4:12 PM"
default currentdate = "March 30th"
default timeleft = "2 hours and 48 minutes"
default event = "War Zones are revealed"
default clickortap = "Click"
default badcredits = False


## Labels ########################################################################################################################

# Splash Screen/Main Menu Intro
label before_main_menu:
    scene bg fade
    if not persistent.gorewarning:
        "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){nw}"
        menu:
            "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){fast}"
            "Yes":
                $persistent.gore = False
                "Graphic images disabled."
            "No":
                $persistent.gore = True
                "Graphic images enabled."
        window hide dissolve
        pause 2
        $persistent.gorewarning = True
    play music title noloop
    if persistent.splash:
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
            linear 1.0 xalign 0.5 yalign 0.1
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
    $renpy.block_rollback()
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
            ease 1.0 alpha 1.0
    $renpy.pause()
    hide screen dateandtime
    hide screen timeremaining
    hide ctc
    with dissolve
    return

# Game Over Screen
label gameover:
    $renpy.block_rollback()
    if not badcredits:
        play music creaky_country_fair
    show screen gameover
    with Dissolve(2)
    if badcredits:
        $renpy.pause()
        hide screen gameover
        with Dissolve(2)
        pause 1
        return
    else:
        pause 1
        show screen loadorquit
        with Dissolve(1)
        $renpy.pause(hard=True)

# Start of Story
label start:
    if persistent.credits:
        $persistent.credits = False
        return
    play sound "audio/se/gong.ogg"
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(1.0)
    pause 3
    $save_name = "Chapter 1"
    $save_subtitle = "The Calm Before the Storm"
    jump chapter_1

# Credits
label credits:
    scene bg fade
    if not badcredits:
        play music title
    else:
        stop music
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
        pause 3.0
        ease 1.0 alpha 0.0
    pause 6.6
    if not badcredits:
        scene bg stage
        with Dissolve(1)
    show credit_1 "Writing and Development\n{font=fonts/Stanberry.ttf}{color=#ffffff}Cole Goodrich{/color}{/font}" at credit_scroll_1
    pause 5
    show credit_2 "Story\n{font=fonts/Stanberry.ttf}{color=#ffffff}Cole Goodrich\nSlightlySimple{/color}{/font}" at credit_scroll_2
    pause 5
    show credit_3 "Character Art\n{font=fonts/Stanberry.ttf}{color=#ffffff}HazardSquare{/color}{/font}" at credit_scroll_1
    pause 5
    show credit_1 "Background Art\n{font=fonts/Stanberry.ttf}{color=#ffffff}Mattyd (MacDaddyMatty.com){/color}{/font}" at credit_scroll_2
    pause 5
    show credit_2 "Music\n{font=fonts/Stanberry.ttf}{color=#ffffff}Eric Matyas\nCole Goodrich{/color}{/font}" at credit_scroll_1
    pause 5
    show credit_3 "Sound Effects\n{font=fonts/Stanberry.ttf}{color=#ffffff}freesound.org{/color}{/font}" at credit_scroll_2
    pause 3
    show credit_1 "Made with Ren'Py 7.3.2" at credit_scroll_1
    pause 5
    show credit_2 "Special Thanks\n{font=fonts/Stanberry.ttf}{color=#ffffff}God\nTom \"PyTom\" Rothamel\nJames DeMonaco\nSlightlySimple\nDems\nYou{/color}{/font}" at credit_scroll_3
    pause 13
    scene bg fade
    with Dissolve(3.0)
    pause 1
    if badcredits:
        show announcetext "The End?" at truecenter
    else:
        show announcetext "The End" at truecenter
    with Dissolve(3)
    pause 3
    hide announcetext
    with Dissolve(3)
    pause 2
    show splash at truecenter
    with Dissolve(3)
    pause 3
    stop music fadeout(6.0)
    hide splash
    with Dissolve(3)
    pause 3
    return
