##################################################################################################################################
## Welcome to the code of REDD War: Showtime! Please use this information for learning and inspiration rather than just blindly ##
## copying and pasting. If you have any questions about the specifics of this code, feel free to check out the Ren'Py online    ##
## documentation at https://renpy.org/doc/html/ or contact Good Tales via Twitter or Discord.                                   ##
##################################################################################################################################

## Keymap Changes ################################################################################################################

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['help'].remove('meta_shift_/')
    config.keymap['help'].remove('K_F1')

## Toggling Splash Screen upon Launch ############################################################################################

init python:
    persistent.splash = True

## Characters ####################################################################################################################

define narrate = nvl_narrator
define a = Character("Anchor", what_prefix='"', what_suffix='"')
define an = Character("Announcer", what_prefix='"', what_suffix='"', what_italic=True, who_italic=True)
define b = Character("[b_name]", what_prefix='"', what_suffix='"')
define d = Character("Dakota", image="dakota", what_prefix='"', what_suffix='"')
define dt = Character("Dakota", color="#0061d9", who_italic=True, what_italic=True)
define j = Character("Jessica", image="jessica", what_prefix='"', what_suffix='"')
define ja = Character("Jangle", color="#d00000", image="jangle", what_prefix='"', what_suffix='"')
define ji = Character("Jingle", color="#d00000", image="jingle", what_prefix='"', what_suffix='"')
define k = Character("Kate", image="kate", what_prefix='"', what_suffix='"')
define kr = Character("Krag", color="#d00000", image="krag", what_prefix='"', what_suffix='"')
define l = Character("Laura", what_prefix='"', what_suffix='"')
define lt = Character("Laura", color="#00d90a", who_italic=True, what_italic=True)
define m = Character("Ms. Madeline", image="madeline", what_prefix='"', what_suffix='"')
define man = Character("Man", what_prefix='"', what_suffix='"')
define r = Character("Richard", image="richard", what_prefix='"', what_suffix='"')
define re = Character("Reddington", color="#d00000", what_prefix='"', what_suffix='"')
define redd = Character("REDD", color="#d00000", what_prefix='"', what_suffix='"')
define s = Character("[s_name]", color="#d00000", image="sprinkles", what_prefix='"', what_suffix='"')
define t = Character("[t_name]", color="#d00000", image="trosh", what_prefix='"', what_suffix='"')
define woman = Character("Woman", what_prefix='"', what_suffix='"')

## Images #######################################################################################################################

# Characters
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

layeredimage madeline:
    group full:
        attribute dead:
            "Characters/Madeline/Dead.png"
    group body:
        attribute down:
            "Characters/Madeline/Down.png"
        attribute shrug:
            "Characters/Madeline/Shrug.png"
    group head:
        attribute blank:
            "Characters/Madeline/Blank.png"
        attribute shocked:
            "Characters/Madeline/Shocked.png"
        attribute smile:
            "Characters/Madeline/Smile.png"

layeredimage richard:
    group body:
        attribute main_crossed:
            "Characters/Richard/main_crossed.png"
        attribute main_down:
            "Characters/Richard/main_down.png"
        attribute pjs_crossed:
            "Characters/Richard/pjs_crossed.png"
        attribute pjs_down:
            "Characters/Richard/pjs_down.png"
        attribute show_crossed:
            "Characters/Richard/show_crossed.png"
        attribute show_down:
            "Characters/Richard/show_down.png"
    group head:
        attribute concerned:
            "Characters/Richard/concerned.png"
        attribute glare:
            "Characters/Richard/glare.png"
        attribute laughing:
            "Characters/Richard/laughing.png"
        attribute rage:
            "Characters/Richard/rage.png"
        attribute shocked:
            "Characters/Richard/shocked.png"
        attribute smile:
            "Characters/Richard/smile.png"

layeredimage sprinkles:
    group leftarm:
        attribute leftdown:
            "Characters/Sprinkles/left down.png"
        attribute cane:
            "Characters/Sprinkles/Hand on cane.png"
    if cane_blood:
        "Characters/Sprinkles/Bloody cane.png"
    group head:
        attribute evilgrin:
            "Characters/Sprinkles/evilgrin.png"
        attribute happy:
            "Characters/Sprinkles/happy.png"
        attribute hm:
            "Characters/Sprinkles/hm.png"
        attribute horror:
            "Characters/Sprinkles/horror.png"
        attribute huh:
            "Characters/Sprinkles/huh.png"
        attribute jeer:
            "Characters/Sprinkles/jeer.png"
        attribute laugh:
            "Characters/Sprinkles/laugh.png"
        attribute wut:
            "Characters/Sprinkles/wut.png"
    group rightarm:
        attribute rightdown:
            "Characters/Sprinkles/right down.png"
        attribute hat:
            "Characters/Sprinkles/Hand on hat.png"

image trosh = Placeholder("boy")

# Main Images
image black = "#000000"
image white = "#ffffff"
image red = "#f00000"
image dark:
    "black"
    alpha 0.33
image splash = "Good Tales Transparent.png"
image logo = "gui/logo.png"
image choice_bg = "gui/choice_bg.png"
image curtain_overlay = "gui/save_curtain.png"
image sprinklelogo:
    "Ringleader Draft.png"
    size(360, 475)
image pause_bg = "gui/save_bg.jpg"
image textbox_bg:
    "gui/textbox_bg.png"
    yalign 0.99
image spotlight = "spotlight.png"
image blood:
    "blood.png"
    alpha 0.75
image blood2:
    "blood.png"
    xzoom -1.0
    xpos 1
    alpha 0.5
image blood3:
    "blood.png"
    yzoom -1.0
    xpos 500
    alpha 0.95
image blood4:
    "blood.png"
    xzoom -1.0 yzoom -1.0
    xpos 1000
    alpha 0.25

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
image extras_overlay:
    size(1280, 720)
    "gui/extras_overlay.png"
    pause 1
    "gui/extras_overlay_2.png"
    pause 1
    repeat
image ctc_arrow_1:
    xalign 0.5 yalign 0.99
    alpha 0.0
    "gui/ctc_arrow.png"
    block:
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        repeat
image ctc_arrow_nvl:
    xalign 0.95 yalign 0.99
    alpha 0.0
    "gui/ctc_arrow.png"
    block:
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        repeat

## Backgrounds ####################################################################################################################

# Solid Backgrounds
image bg fade = "#000000"
image bg flash = "#ffffff"
image bg blood = "#f00000"

# Image Backgrounds
image bg alley = "BG/alley.jpg"
image bg arena_hall = "BG/arenahall.jpg"
image bg bar = "BG/bar.jpg"
image bg basement = "BG/basement.jpg"
image bg basement_hall = "BG/basementhall.jpg"
image bg curtain = "BG/sprinklescurtain.jpg"
image bg dakotaroom = "BG/dakotaroom2.jpg"
image bg dressingroom = "BG/dressingroom.jpg"
image bg janitorcloset = "BG/janitorcloset.jpg"
image bg livestage = "BG/livestage2.jpg"
image bg livingroom = "BG/livingroom2.jpg"
image bg lobby = "BG/lobby.jpg"
image bg newsroom = "BG/newsroom.jpg"
image bg parkinggarage = "BG/parkinggarage.jpg"
image bg restroom = "BG/restroom.jpg"
image bg showstage = "BG/showstage.jpg"
image bg stage = "BG/stage.jpg"
image bg storage = "BG/storage.jpeg"
image bg street = "BG/street.jpg"
image bg theater_ext = "BG/theaterexterior.jpg"

## Custom Audio Channels ##########################################################################################################

init python:
    renpy.music.register_channel('ambience', mixer="sound", loop=True)
    renpy.music.register_channel('ambience2', mixer="sound", loop=True)
    renpy.music.register_channel('sound2', mixer="sound", loop=False)

## Audio ##########################################################################################################################

# Music
define audio.autumn_changes = "audio/music/Autumn-Changes_Looping.mp3"
define audio.bells_of_weirdness = "audio/music/Bells-of-Weirdness_Looping.mp3"
define audio.classy_ghouls = "audio/music/Classy-Ghouls-Halloween-Gathering_Looping.mp3"
define audio.creaky_country_fair = "audio/music/Creaky-Country-Fair.ogg"
define audio.ice_cream_truck = "audio/music/Ice-Cream-Truck_Looping.mp3"
define audio.into_battle = "audio/music/Into-Battle_v001.mp3"
define audio.into_the_haunted_forest = "audio/music/Into-the-Haunted-Forest_Looping.mp3"
define audio.neon_runner = "audio/music/Neon-Runner_Looping.mp3"
define audio.sprinkles_radio = "<to 64>audio/music/The Mr Sprinkles Show - Radio.mp3"
define audio.sprinkles_spooky = "<to 100.364>audio/music/Sprinkles Theme - Spooky.mp3"
define audio.sprinkles_theme = "<to 64>audio/music/The Mr Sprinkles Show.mp3"
define audio.the_calm = "<to 111.628 loop 11.163>audio/music/The Calm.mp3"
define audio.the_twins = "<to 68 loop 4>audio/music/The Twins.mp3"
define audio.title = "audio/music/title.ogg"
define audio.vast_places = "audio/music/Vast-Places_Looping.mp3"

# Sound Effects
define audio.airhorn = "audio/se/airhorn.ogg"
define audio.applause = "audio/se/applause.ogg"
define audio.blood = "audio/se/blood.ogg"
define audio.buzzer_full = "audio/se/buzzer.ogg"
define audio.buzzer_short = "<to 0.5>audio/se/buzzer.ogg"
define audio.children_screaming = "audio/se/children_screaming.ogg"
define audio.crowd = "audio/se/crowd.ogg"
define audio.crowd_screaming = "audio/se/crowd_screaming.ogg"
define audio.doorbell = "audio/se/doorbell.ogg"
define audio.door_creak = "audio/se/door creak.ogg"
define audio.door_knock = "audio/se/doorknock.ogg"
define audio.door_open = "audio/se/door_open.ogg"
define audio.drumroll_buildup = "<to 4.9 loop 0.5>audio/se/drumroll.ogg"
define audio.drumroll_finish = "<from 4.9>audio/se/drumroll.ogg"
define audio.flicker = "audio/se/flicker.ogg"
define audio.footsteps = "audio/se/footsteps.ogg"
define audio.hammer = "audio/se/hammer.ogg"
define audio.heartbeat = "audio/se/heartbeat.ogg"
define audio.helicopter_loop = "<to 6 loop 1>audio/se/helicopter.ogg"
define audio.helicopter_finish = "<from 6>audio/se/helicopter.ogg"
define audio.machine_gun = "audio/se/machine gun.ogg"
define audio.rapid_gunfire = "audio/se/rapid gunfire.ogg"
define audio.saw = "audio/se/saw.ogg"
define audio.shotgun = "audio/se/shotgun.ogg"
define audio.siren = "audio/se/siren.ogg"
define audio.slow_footsteps = "audio/se/slow footsteps.ogg"
define audio.smack = "audio/se/smack.ogg"
define audio.snap = "audio/se/snap.ogg"
define audio.stab = "audio/se/stab.ogg"

## Transforms ####################################################################################################################

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

# Stationary Transforms
transform middle:
    xalign 0.5 yalign 0.5
transform middle_k:
    xalign 0.5 yalign -0.1
transform middle_s:
    size(675, 1125)
    xalign 0.6 yalign 0.0
transform middle_r:
    size(562, 1125)
    xalign 0.5 yalign 0.0
transform middle_m:
    size(562, 1125)
    xalign 0.5 yalign -0.15

transform left:
    xalign 0.05 yalign 0.5
transform left_s:
    size(675, 1125)
    xalign 0.05 yalign 0.0
transform left_r:
    size(562, 1125)
    xalign 0.05 yalign 0.0

transform right:
    xalign 0.95 yalign 0.5
transform right_s:
    size(675, 1125)
    xalign 1.3 yalign 0.0
transform right_r:
    size(562, 1125)
    xalign 0.95 yalign 0.0

transform two1:
    xalign 0.25 yalign 0.5
transform two1_s:
    size(675, 1125)
    xalign 0.25 yalign 0.0
transform two1_r:
    size(562, 1125)
    xalign 0.2 yalign 0.0
transform two1_m:
    size(562, 1125)
    xalign 0.2 yalign -0.15

transform two2:
    xalign 0.75 yalign 0.5
transform two2_s:
    size(675, 1125)
    xalign 0.98 yalign 0.0
transform two2_r:
    size(562, 1125)
    xalign 0.75 yalign 0.0
transform two2_m:
    size(562, 1125)
    xalign 0.8 yalign -0.15

transform sideimage:
    size(225, 225)
    xalign 0.0575 yalign 1.0
    alpha 0.0
    on show:
        ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0
transform sideimagequick:
    size(225, 225)
    xalign 0.0575 yalign 1.0

## Transitions ####################################################################################################################

init -5:
    define fastslidedown = CropMove(0.6, "slidedown")
    define fastslideawayup = CropMove(0.6, "slideawayup")
    define explosion = ImageDissolve("gui/explosion.png", 0.15)

## Styles #########################################################################################################################

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
style replay_desc:
    size 25
    xalign 0.5
    text_align 0.5
    justify True
style creditscreen:
    font "fonts/circula-medium.otf"
    color "#ffffff"
    outlines [(1.0, '#a39600', 0.0, 0.0)]
    text_align 0.5

## Custom Screens #################################################################################################################

# Overlay Screens
screen ctc():
    zorder 100
    if nvl == True:
        add "ctc_arrow_nvl"
    else:
        add "ctc_arrow_1"
screen laura():
    zorder 100
    if not quickhide:
        add "laura [l_exp]" at sideimage
    else:
        add "laura [l_exp]" at sideimagequick
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

# Menu Screens
screen extras():
    tag title
    modal True
    add "extras_overlay"
    imagebutton auto "gui/chapter_%s.png" action ShowMenu('chapterselect') xalign 0.13 yalign 0.33
    imagebutton auto "gui/achievements_%s.png" action ShowMenu('achievements') xalign 0.87 yalign 0.33
    imagebutton auto "gui/follow_%s.png" action ShowMenu('socials') xalign 0.25 yalign 0.57
    imagebutton auto "gui/credits_%s.png" action ShowMenu('credits') xalign 0.75 yalign 0.57
    imagebutton auto "gui/return_%s.png" action [ToggleVariable("title", True), Hide('extras', transition=dissolve)] xalign 0.5 yalign 0.99
screen chapterselect():
    tag title
    add "dark"
    add "curtain_overlay"
    frame:
        xysize(250, 550)
        xalign 0.1 yalign 0.5
        xpadding 25 ypadding 15
        viewport id "vp":
            child_size(250, 500)
            mousewheel True
            draggable True
            scrollbars "vertical"
            vbox:
                text "Chapter 1" xalign 0.5
                if persistent.chapter1_scene1:
                    textbutton "Meet the Farrs" xalign 0.5:
                        hovered SetVariable("replay_num", 1)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("chapter_1")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter1_scene2:
                    textbutton "Unfortunate News" xalign 0.5:
                        hovered SetVariable("replay_num", 2)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("kragonnews")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 20
                text "Chapter 2" xalign 0.5
                if persistent.chapter2_scene1:
                    textbutton "Evening Plans" xalign 0.5:
                        hovered SetVariable("replay_num", 3)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("chapter_2")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter2_scene2:
                    textbutton "Backstage Drama" xalign 0.5:
                        hovered SetVariable("replay_num", 4)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("backstagedrama", scope={"currentdate": "March 31st", "event": "REDD War begins"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter2_scene3:
                    textbutton "Packed Parking" xalign 0.5:
                        hovered SetVariable("replay_num", 5)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("arriveatshow", scope={"currentdate": "March 31st", "event": "REDD War begins"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter2_scene4:
                    textbutton "Meet and Greet" xalign 0.5:
                        hovered SetVariable("replay_num", 6)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("meetandgreet", scope={"currentdate": "March 31st", "event": "REDD War begins"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter2_scene5:
                    textbutton "Showtime!" xalign 0.5:
                        hovered SetVariable("replay_num", 7)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("showbegins", scope={"currentdate": "March 31st", "event": "REDD War begins"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 20
                text "Chapter 3" xalign 0.5
                if persistent.chapter3_scene1:
                    textbutton "The First Game" xalign 0.5:
                        hovered SetVariable("replay_num", 8)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("firstgame", scope={"currentdate": "March 31st", "nvl": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene2:
                    textbutton "When You Gotta Go..." xalign 0.5:
                        hovered SetVariable("replay_num", 9)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("gottago", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene3:
                    textbutton "Laughs and Cracks" xalign 0.5:
                        hovered SetVariable("replay_num", 10)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("secondbeating", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene4:
                    textbutton "Toilet Escape" xalign 0.5:
                        hovered SetVariable("replay_num", 11)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("girlsescape", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene5:
                    textbutton "Standing Up" xalign 0.5:
                        hovered SetVariable("replay_num", 12)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("showmustgoon", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene6:
                    textbutton "Hiding in the Closet" xalign 0.5:
                        hovered SetVariable("replay_num", 13)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("kidshiding", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene7:
                    textbutton "A Special Game" xalign 0.5:
                        hovered SetVariable("replay_num", 14)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("deadlygame", scope={"currentdate": "March 31st", "event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.chapter3_scene8:
                    textbutton "Eyesore" xalign 0.5:
                        hovered SetVariable("replay_num", 15)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("jessicaseye", scope={"event": "REDD War ends"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
    frame:
        xalign 0.75 yalign 0.5
        xysize (700, 250)
        vbox:
            xalign 0.5 yalign 0.5
            if replay_num == -1:
                text "???" style "replay_desc" xalign 0.5
            elif replay_num == 1:
                text "The Farr family enjoys a normal day at home before their lives change forever." style "replay_desc" xalign 0.5
            elif replay_num == 2:
                text "The TV brings both good and bad news." style "replay_desc" xalign 0.5
            elif replay_num == 3:
                text "The Farrs decide whether or not to stay in Atlanta upon hearing new information." style "replay_desc" xalign 0.5
            elif replay_num == 4:
                text "Krag and Madeline have a brief conversation before the show starts." style "replay_desc" xalign 0.5
            elif replay_num == 5:
                text "The Farrs are on their way to the theater." style "replay_desc" xalign 0.5
            elif replay_num == 6:
                text "Kate and Dakota get to meet their television idol." style "replay_desc" xalign 0.5
            elif replay_num == 7:
                text "The show begins, but it's not what everyone expected it to be." style "replay_desc" xalign 0.5
            elif replay_num == 8:
                text "Two contestants play the first game of the evening." style "replay_desc" xalign 0.5
            elif replay_num == 9:
                text "Dakota tries to get her and her sister out of the audience." style "replay_desc" xalign 0.5
            elif replay_num == 10:
                text "After telling some jokes, Mr. Sprinkles has more fun with Jessica." style "replay_desc" xalign 0.5
            elif replay_num == 11:
                text "A typical restroom break. At least, it {b}was{/b}." style "replay_desc" xalign 0.5
            elif replay_num == 12:
                text "Laura has choice words for a REDD after learning about her daughters' potential endangerment." style "replay_desc" xalign 0.5
            elif replay_num == 13:
                text "Kate and Dakota, along with other children, hide from the REDD Guards." style "replay_desc" xalign 0.5
            elif replay_num == 14:
                text "Trosh has a special contestant in mind for an upcoming game." style "replay_desc" xalign 0.5
            elif replay_num == 15:
                text "Kate and Dakota build tension between them while Jessica has a close encounter with a power tool." style "replay_desc" xalign 0.5
    imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.5 yalign 0.95
screen achievements():
    tag title
    frame:
        xysize(1240, 670)
        xalign 0.5 yalign 0.4
        vbox:
            xalign 0.25 yalign 0.5
            if persistent.achievement_toosafe:
                text "{i}Playing it TOO Safe{/i}" xalign 0.5
                text "Escape Atlanta" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievement_futurecorpses:
                text "{i}Future Corpses{/i}" xalign 0.5
                text "Fulfill Your Destiny" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievement_epicfail:
                text "{i}Schadenfreude{/i}" xalign 0.5
                text "Embarrass Yourself on Live Television" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
    null height 10
    textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.9
screen credits():
    tag title
    frame:
        xysize(1240, 670)
        xalign 0.5 yalign 0.4
        vbox:
            xalign 0.15 yalign 0.5
            text "Writing and Development" style "creditscreen" xalign 0.5
            text "Cole Goodrich" xalign 0.5
            null height 20
            text "Story" style "creditscreen" xalign 0.5
            text "Cole Goodrich" xalign 0.5
            text "SlightlySimple" xalign 0.5
            null height 20
            text "Character Art" style "creditscreen" xalign 0.5
            text "HazardSquare" xalign 0.5
            null height 20
            text "Background Art" style "creditscreen" xalign 0.5
            text "Mattyd (MacDaddyMatty.com)" xalign 0.5
        vbox:
            xalign 0.5 yalign 0.5
            text "Music" style "creditscreen" xalign 0.5
            null height 10
            text "{i}Autumn Changes{/i}" xalign 0.5
            text "{i}Bells of Weirdness{/i}" xalign 0.5
            text "{i}Classy Ghouls Halloween Gathering{i}" xalign 0.5
            text "{i}Creaky Country Fair{/i}" xalign 0.5
            text "{i}Ice Cream Truck{/i}" xalign 0.5
            text "{i}Into Battle v001{/i}" xalign 0.5
            text "{i}Into the Haunted Forest{/i}" xalign 0.5
            text "{i}Neon Runner{/i}" xalign 0.5
            text "{i}Vast Places{/i}" xalign 0.5
            null height 10
            text "by Eric Matyas (soundimage.org)" xalign 0.5
            null height 20
            text "{i}Rotten Sprinkles{/i}" xalign 0.5
            text "{i}Showtime!{/i}" xalign 0.5
            text "{i}The Calm{/i}" xalign 0.5 
            text "{i}The Mr. Sprinkles Show{/i}" xalign 0.5
            text "{i}The Twins{/i}" xalign 0.5
            null height 10
            text "by Cole Goodrich" xalign 0.5
        vbox:
            xalign 0.85 yalign 0.5
            text "Sound Effects" style "creditscreen" xalign 0.5
            text "freesound.org" xalign 0.5
            null height 20
            text "Made with Ren'Py 7.3.3" style "creditscreen" xalign 0.5
    imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.9 yalign 0.9
screen socials():
    tag title
    frame:
        xysize(800, 600)
        xalign 0.5 yalign 0.5
        textbutton "Twitter" action OpenURL("https://twitter.com/goodtalesvn") xalign 0.1 yalign 0.1
        textbutton "Instagram" action OpenURL("https://instagram.com/goodtalesvn") xalign 0.9 yalign 0.1
        textbutton "Discord Server" action OpenURL("https://discord.gg/zZhPrkC") xalign 0.5 yalign 0.9
    imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.5 yalign 0.99

## Variable Defaults ##############################################################################################################

default persistent.gore = True
default preferences.fullscreen = False
define config.replay_scope = {"_game_menu_screen": "pause"}
default title = True
default _game_menu_screen = "pause"
default save_subtitle = ""
default replay_num = 0
default l_exp = "neutral"
default quickhide = False
default nvl = False
default currenttime = "4:12 PM"
default currentdate = "March 30th"
default timeleft = "2 hours and 48 minutes"
default event = "War Zones are revealed"
default clickortap = "Click"
default badcredits = False
default b_name = "???"
default s_name = "Mr. Sprinkles"
default t_name = "REDD"
default cane_blood = False

## Labels #########################################################################################################################

# Splash Screen/Main Menu Intro
label before_main_menu:
    scene bg fade
    if not persistent.gorewarning:
        "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){nw}"
        menu:
            "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){fast}"
            "Yes, disable them":
                $persistent.gore = False
                "Graphic images disabled."
            "No, enable them":
                $persistent.gore = True
                "Graphic images enabled."
        window hide dissolve
        pause 2
        $persistent.gorewarning = True
    play music title noloop
    if persistent.splash:
        pause 1.0
        show announcetext "This story contains graphic violence and strong language and is intended for mature audiences" at truecenter
        with Dissolve(1.0)
        pause 2.0
        hide announcetext
        with Dissolve(1.0)
        show splash at truecenter
        with Dissolve(1.0)
        pause 2.0
        hide splash
        with Dissolve(1.0)
        pause 0.1
        $ persistent.splash = False
    play sound flicker
    show logo zorder 2:
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
    stop sound2
    stop ambience
    stop ambience2
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
        $renpy.pause(delay=5)
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
    $quick_menu = False
    $save_name = "Chapter 1"
    $save_subtitle = "The Calm Before the Storm"
    play sound "audio/se/gong.ogg"
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(1.0)
    pause 3
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
