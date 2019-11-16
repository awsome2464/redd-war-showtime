##################################################################################################################################
## Welcome to the code of REDD War: Showtime! Please use this information for learning and inspiration rather than just blindly ##
## copying and pasting. If you have any questions about the specifics of this code, feel free to check out the Ren'Py online    ##
## documentation at https://renpy.org/doc/html/ or contact Good Tales via Twitter or Discord.         © 2019 Good Tales         ##
##################################################################################################################################

## Keymap Changes ################################################################################################################

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['help'].remove('meta_shift_/')
    config.keymap['help'].remove('K_F1')

## Toggling Splash Screen upon Launch ############################################################################################

init python:
    persistent.splash = True

## Vibrates Phone When Vibration is Turned On (Android Port Only) ################################################################

init python:
    def vibrate():
        renpy.vibrate(0.25)

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

## Characters

# Dakota
layeredimage dakota:
    group body:
        pos (-50,100)
        attribute crossed:
            "Characters/Dakota/[clothing]_crossed.png"
        attribute hips:
            "Characters/Dakota/[clothing]_hips.png"
        attribute side:
            "Characters/Dakota/[clothing]_side.png"
    group head:
        pos (-50,100)
        attribute bawl:
            "Characters/Dakota/bawl.png"
        attribute confident:
            "Characters/Dakota/confident.png"
        attribute confused:
            "Characters/Dakota/confused.png"
        attribute crying:
            "Characters/Dakota/crying.png"
        attribute determined:
            "Characters/Dakota/determined.png"
        attribute mad:
            "Characters/Dakota/mad.png"
        attribute neutral:
            "Characters/Dakota/neutral.png"
        attribute sad:
            "Characters/Dakota/sad.png"
        attribute small_smile:
            "Characters/Dakota/small_smile.png"
        attribute smirk:
            "Characters/Dakota/smirk.png"

# Jangle
image jangle = Placeholder("boy")

# Jessica
image jessica_base:
    "Characters/Jessica/torture_base_r.png"
    pause 0.5
    "Characters/Jessica/torture_base_l.png"
    pause 0.5
    repeat
image jessica_tears:
    "Characters/Jessica/torture_tears_r.png"
    pause 0.5
    "Characters/Jessica/torture_tears_l.png"
    pause 0.5
    repeat
image jessica_terror:
    "Characters/Jessica/torture_terror[persistent.gore]_r.png"
    pause 0.5
    "Characters/Jessica/torture_terror[persistent.gore]_l.png"
    pause 0.5
    repeat
layeredimage jessica:
    group full:
        attribute stand_hip:
            zoom 0.9
            ypos 100
            "Characters/Jessica/standing_hip.png"
        attribute stand_up:
            zoom 0.9
            ypos 100
            "Characters/Jessica/standing_up.png"
        attribute wheelchair:
            "Characters/Jessica/wheelchair[persistent.gore].png"
    group chair:
        attribute bothknees:
            "Characters/Jessica/chair_bothknees.png"
        attribute full:
            "Characters/Jessica/chair_full[persistent.gore].png"
        attribute oneknee:
            "Characters/Jessica/chair_oneknee.png"
        attribute chair:
            "Characters/Jessica/chair.png"
    group face:
        attribute base:
            "jessica_base"
        attribute blank:
            "Characters/Jessica/torture_blank[persistent.gore].png"
        attribute left:
            "Characters/Jessica/torture_base_l.png"
        attribute left_oneeye:
            "Characters/Jessica/torture_oneeye[persistent.gore]_l.png"
        attribute left_tears:
            "Characters/Jessica/torture_tears_l.png"
        attribute left_terror:
            "Characters/Jessica/torture_terror[persistent.gore]_l.png"
        attribute terror:
            "jessica_terror"
        attribute right:
            "Characters/Jessica/torture_base_r.png"
        attribute right_tears:
            "Characters/Jessica/torture_tears_r.png"
        attribute screaming:
            "Characters/Jessica/torture_screaming.png"
        attribute tears:
            "jessica_tears"

# Jingle
image jingle = Placeholder("girl")

# Kate
layeredimage kate:
    group body:
        ypos 180
        attribute down:
            "Characters/Kate/[clothing]_down.png"
        attribute fidget:
            "Characters/Kate/[clothing]_fidget.png"
        attribute up:
            "Characters/Kate/[clothing]_up.png"
    group head:
        ypos 180
        attribute alert:
            "Characters/Kate/alert.png"
        attribute concerned:
            "Characters/Kate/concerned.png"
        attribute confused:
            "Characters/Kate/confused.png"
        attribute crying:
            "Characters/Kate/crying.png"
        attribute excited:
            "Characters/Kate/excited.png"
        attribute happy:
            "Characters/Kate/happy.png"
        attribute mad:
            "Characters/Kate/mad.png"
        attribute shocked:
            "Characters/Kate/shocked.png"
    if k_hat:
        ypos 180
        "Characters/Kate/hat.png"

# Krag
layeredimage krag:
    group body:
        yalign -0.09
        attribute down:
            "Characters/Krag/down.png"
        attribute hips:
            "Characters/Krag/hips.png"
    group head:
        yalign -0.09
        attribute concerned:
            "Characters/Krag/concerned.png"
        attribute horror:
            "Characters/Krag/horror.png"
        attribute laughing:
            "Characters/Krag/laughing.png"
        attribute neutral:
            "Characters/Krag/neutral.png"
        attribute smile:
            "Characters/Krag/smile.png"
        attribute worried:
            "Characters/Krag/worried.png"

# Laura
layeredimage laura:
    always:
        "Characters/Laura/[clothing].png"
    always:
        "Characters/Laura/[l_exp].png"

# Madeline
layeredimage madeline:
    group full:
        yalign 0.0
        xpos -100
        attribute dead:
            "Characters/Madeline/Dead[persistent.gore].png"
    group body:
        yalign -0.1
        attribute down:
            "Characters/Madeline/Down.png"
        attribute shrug:
            "Characters/Madeline/Shrug.png"
    group head:
        yalign -0.1
        attribute blank:
            "Characters/Madeline/Blank.png"
        attribute excited:
            "Characters/Madeline/Excited.png"
        attribute glare:
            "Characters/Madeline/Glare.png"
        attribute shocked:
            "Characters/Madeline/Shocked.png"
        attribute smile:
            "Characters/Madeline/Smile.png"
        attribute stabbed:
            "Characters/Madeline/Stabbed.png"

# Richard
layeredimage richard:
    group body:
        yalign 0.0
        attribute crossed:
            "Characters/Richard/[clothing]_crossed.png"
        attribute down:
            "Characters/Richard/[clothing]_down.png"
    group head:
        yalign 0.0
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

# Mr. Sprinkles
layeredimage sprinkles:
    group leftarm:
        yalign 0.0
        attribute leftdown:
            "Characters/Sprinkles/left down.png"
        attribute cane:
            "Characters/Sprinkles/Hand on cane.png"
    group head:
        yalign 0.0
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
        yalign 0.0
        attribute rightdown:
            "Characters/Sprinkles/right down.png"
        attribute hat:
            "Characters/Sprinkles/Hand on hat.png"

# Trosh
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
image helmet = "helmet.png"
image bus_window = "window.png"
image spotlight = "spotlight.png"
image blood_base = "blood[persistent.gore].png"
image blood:
    "blood_base"
    alpha 0.75
image blood2:
    "blood_base"
    xzoom -1.0
    xpos 1
    alpha 0.5
image blood3:
    "blood_base"
    yzoom -1.0
    xpos 500
    alpha 0.95
image blood4:
    "blood_base"
    xzoom -1.0 yzoom -1.0
    xpos 1000
    alpha 0.25
layeredimage tvscreen:
    always:
        "bg bar"
        xzoom -1.0
        alpha 0.05
    always:
        "tvscreen.png"
image dressingroom_blur = im.Blur("BG/dressingroom.jpg", 1.0)

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
image fire:
    "#d57500"
    alpha 0.0
    block:
        ease 0.25 alpha 0.25
        ease 0.25 alpha 0.125
        repeat

## Backgrounds ####################################################################################################################

# Solid Backgrounds
image bg fade = "#000000"
image bg flash = "#ffffff"
image bg blood = "#f00000"

# Image Backgrounds
image bg alley = "BG/alley.jpg"
image bg arena_hall_day = "BG/arenahall_day.jpg"
image bg arena_hall_night = "BG/arenahall_night.jpg"
image bg bar = "BG/bar.jpg"
image bg basement = "BG/basement.jpg"
image bg basement_hall = "BG/basementhall.jpg"
image bg curtain = "BG/sprinklescurtain.jpg"
image bg dakotaroom_day = "BG/dakotaroom_day.jpg"
image bg dakotaroom_night = "BG/dakotaroom_night.jpg"
image bg dressingroom = "BG/dressingroom.jpg"
image bg dressingroom_blur = im.Blur("BG/dressingroom.jpg", 2.0)
image bg dressingroom_woozy:
    "BG/dressingroom.jpg"
    "dressingroom_blur" with dissolve
    pause 0.5
    "BG/dressingroom.jpg" with dissolve
    pause 0.5
    repeat
image bg janitorcloset = "BG/janitorcloset.jpg"
image bg livestage = "BG/livestage2.jpg"
image bg livingroom_day = "BG/livingroom_day.jpg"
image bg livingroom_day_blur = im.Blur("BG/livingroom_day.jpg", 2.0)
image bg livingroom_night = "BG/livingroom_night.jpg"
image bg livingroom_night_blur = im.Blur("BG/livingroom_night.jpg", 2.0)
image bg lobby = "BG/lobby.jpg"
image bg newsroom = "BG/newsroom.jpg"
image bg parkinggarage = "BG/parkinggarage.jpg"
image bg restroom = "BG/restroom.jpg"
image bg showstage = "BG/showstage.jpg"
image bg stage = "BG/stage.jpg"
image bg stage_blur = im.Blur("BG/stage.jpg", 2.0)
image bg storage = "BG/storage.jpg"
image bg street = "BG/street.jpg"
image bg theater_ext = "BG/theaterexterior.jpg"
image bg theater_ext_blur = im.Blur("BG/theaterexterior.jpg", 2.0)
image bg warehouse = "BG/warehouse.jpg"
image bg warehouse_blur = im.Blur("BG/warehouse.jpg", 2.0)

## Audio ##########################################################################################################################

# Music
define audio.autumn_changes = "audio/music/Autumn-Changes_Looping.mp3"
define audio.bells_of_weirdness = "audio/music/Bells-of-Weirdness_Looping.mp3"
define audio.classy_ghouls = "audio/music/Classy-Ghouls-Halloween-Gathering_Looping.mp3"
define audio.creaky_country_fair = "audio/music/Creaky-Country-Fair.ogg"
define audio.escape = "audio/music/Escape_Looping.mp3"
define audio.ice_cream_truck = "audio/music/Ice-Cream-Truck_Looping.mp3"
define audio.into_battle = "audio/music/Into-Battle_v001.mp3"
define audio.into_the_haunted_forest = "audio/music/Into-the-Haunted-Forest_Looping.mp3"
define audio.neon_runner = "audio/music/Neon-Runner_Looping.mp3"
define audio.packing = "audio/music/Packing_Looping.mp3"
define audio.shattered_mind = "<to 34>audio/music/Shattered-Mind.ogg"
define audio.sprinkles_radio = "<to 64>audio/music/The Mr Sprinkles Show - Radio.mp3"
define audio.sprinkles_spooky = "<to 100.364>audio/music/Sprinkles Theme - Spooky.mp3"
define audio.sprinkles_theme = "<to 64>audio/music/The Mr Sprinkles Show.mp3"
define audio.ten_past_midnight = "audio/music/10-Past-Midnight_Looping.mp3"
define audio.the_calm = "<to 111.628 loop 11.163>audio/music/The Calm.mp3"
define audio.the_twins = "<to 68 loop 4>audio/music/The Twins.mp3"
define audio.title = "audio/music/title.ogg"
define audio.vast_places = "audio/music/Vast-Places_Looping.mp3"

# Sound Effects / Ambience
define audio.airhorn = "audio/se/airhorn.ogg"
define audio.applause = "audio/se/applause.ogg"
define audio.beep = "audio/se/beep.ogg"
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
define audio.fire = "<to 55 loop 5>audio/se/fire.ogg"
define audio.fire_start = "audio/se/fire start.ogg"
define audio.flicker = "audio/se/flicker.ogg"
define audio.footsteps = "audio/se/footsteps.ogg"
define audio.hammer = "audio/se/hammer.ogg"
define audio.heartbeat = "audio/se/heartbeat.ogg"
define audio.helicopter_loop = "<to 6 loop 1>audio/se/helicopter.ogg"
define audio.helicopter_finish = "<from 6>audio/se/helicopter.ogg"
define audio.impact = "audio/se/impact.ogg"
define audio.machine_gun = "audio/se/machine gun.ogg"
define audio.rapid_gunfire = "audio/se/rapid gunfire.ogg"
define audio.running = "audio/se/running.ogg"
define audio.saw = "audio/se/saw.ogg"
define audio.shotgun = "audio/se/shotgun.ogg"
define audio.siren = "audio/se/siren.ogg"
define audio.slow_footsteps = "audio/se/slow footsteps.ogg"
define audio.smack = "audio/se/smack.ogg"
define audio.snap = "audio/se/snap.ogg"
define audio.stab = "audio/se/stab.ogg"

# Custom Audio Channels
init python:
    renpy.music.register_channel('ambience', mixer="sound", loop=True, tight=True)
    renpy.music.register_channel('ambience2', mixer="sound", loop=True, tight=True)
    renpy.music.register_channel('music2', mixer="music", loop=True, tight=True)
    renpy.music.register_channel('sound2', mixer="sound", loop=False, tight=True)

## Transforms ####################################################################################################################

# Animated Transforms
transform choice_dissolve:
    alpha 0.0
    ease 1.0 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0
transform spotlight_wander:
    xalign 1.0 yalign 1.0
    linear 1.0 xalign 0.0 yalign 0.0
    linear 0.5 yalign 1.0
    linear 1.0 xalign 1.0 yalign 0.0
    linear 0.5 yalign 1.0
    repeat
transform spotlight_focus:
    linear 0.1 xalign 0.5 yalign 0.5
transform game_name_flash:
    xalign 0.5 yalign 0.1
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
    zoom 0.75
    xalign 0.5 ypos 0
transform middle_jessica:
    zoom 0.6
    xalign 0.5 ypos 0
transform middle_short:
    zoom 0.75
    xalign 0.5 ypos 100
transform middle_sprinkles:
    zoom 0.75
    xalign 0.6

transform left:
    zoom 0.75
    xalign 0.1 ypos 0
transform left_short:
    zoom 0.75
    xalign 0.1 ypos 100
transform left_sprinkles:
    zoom 0.75
    xalign 0.05

transform right:
    zoom 0.75
    xalign 0.9 ypos 0
transform right_short:
    zoom 0.75
    xalign 0.9 ypos 100
transform right_sprinkles:
    zoom 0.75
    xalign 1.3

transform two1:
    zoom 0.75
    xalign 0.25 ypos 0
transform two1_jessica:
    zoom 0.6
    xalign 0.2 ypos 0
transform two1_short:
    zoom 0.75
    xalign 0.25 ypos 100

transform two2:
    zoom 0.75
    xalign 0.8 ypos 0
transform two2_jessica:
    zoom 0.6
    xalign 0.8 ypos 0
transform two2_short:
    zoom 0.75
    xalign 0.8 ypos 100
transform two2_sprinkles:
    zoom 0.75
    xalign 0.98

transform sideimage:
    size(250, 250)
    xalign 0.05 yalign 1.026
    alpha 1.0
    on show:
        alpha 0.0
        ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0
transform sideimagequick:
    size(250, 250)
    xalign 0.05 yalign 1.026

## Transitions ####################################################################################################################

init -5:
    define explosion = ImageDissolve("explosion.png", 0.2)
    define fastslideawayup = CropMove(0.6, "slideawayup")
    define fastslidedown = CropMove(0.6, "slidedown")
    define tvoff = ImageDissolve("tvwipe.png", 0.35, reverse=True)
    define tvon = ImageDissolve("tvwipe.png", 0.35)

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
    outlines [(1.0 ,'#000000', 0.0, 0.0)]
    size 75
style chaptersub:
    font "fonts/Stanberry.ttf"
    color "#ffffff"
    text_align 0.5
    outlines [(1.0 ,'#000000', 0.0, 0.0)]
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
    color "#a39600"
    text_align 0.5
style creditscreen2:
    font "fonts/circula-medium.otf"
    color "#a39600"
    text_align 0.5
    size 50

## Custom Screens #################################################################################################################

# Overlay Screens
screen ctc():
    zorder 100
    if nvl:
        add "ctc_arrow_nvl"
    else:
        add "ctc_arrow_1"
screen laura():
    zorder 100
    if not quickhide:
        add "laura" at sideimage
    else:
        add "laura" at sideimagequick
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
            text "THE END" style "dateandtime"
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
screen pause():
    tag menu
    add "bg curtain"
    frame:
        xalign 0.5 yalign 0.5
        xpadding 50 ypadding 25
        if not nicetry:
            vbox:
                xalign 0.5 yalign 0.5
                spacing 10
                textbutton "Save" action ShowMenu('save') xalign 0.5
                textbutton "Load" action ShowMenu('load') xalign 0.5
                textbutton "Options" action ShowMenu('preferences') xalign 0.5
                textbutton "Main Menu" action MainMenu() xalign 0.5
                textbutton "Quit" action Quit() xalign 0.5
                null height 10
                textbutton "Return" action Return() xalign 0.5
        else:
            vbox:
                xalign 0.5 yalign 0.5
                text "Nice try, cheater ;)" xalign 0.5
                null height 10
                textbutton "Return" action Return() xalign 0.5
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
                null height 10
                text "Chapter 1" xalign 0.5
                if persistent.scenes["ch1_s1"]:
                    textbutton "Meet the Farrs" xalign 0.5:
                        hovered SetVariable("replay_num", 1)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("meetthefarrs")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch1_s2"]:
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
                if persistent.scenes["ch2_s1"]:
                    textbutton "Evening Plans" xalign 0.5:
                        hovered SetVariable("replay_num", 3)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("eveningplans")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch2_s2"]:
                    textbutton "Backstage Drama" xalign 0.5:
                        hovered SetVariable("replay_num", 4)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("backstagedrama", scope={"currentdate": "March 31st", "event": "REDD War begins"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch2_s3"]:
                    textbutton "Packed Parking" xalign 0.5:
                        hovered SetVariable("replay_num", 5)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("arriveatshow", scope={"currentdate": "March 31st", "event": "REDD War begins", "k_hat": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch2_s4"]:
                    textbutton "Meet and Greet" xalign 0.5:
                        hovered SetVariable("replay_num", 6)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("meetandgreet", scope={"currentdate": "March 31st", "event": "REDD War begins", "clothing": "show", "k_hat": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch2_s5"]:
                    textbutton "Showtime!" xalign 0.5:
                        hovered SetVariable("replay_num", 7)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("showbegins", scope={"currentdate": "March 31st", "event": "REDD War begins", "clothing": "show", "k_hat": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 20
                text "Chapter 3" xalign 0.5
                if persistent.scenes["ch3_s1"]:
                    textbutton "The First Game" xalign 0.5:
                        hovered SetVariable("replay_num", 8)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("firstgame", scope={"currentdate": "March 31st", "nvl": True, "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s2"]:
                    textbutton "When You Gotta Go..." xalign 0.5:
                        hovered SetVariable("replay_num", 9)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("gottago", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show", "k_hat": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s3"]:
                    textbutton "Laughs and Cracks" xalign 0.5:
                        hovered SetVariable("replay_num", 10)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("secondbeating", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s4"]:
                    textbutton "Toilet Escape" xalign 0.5:
                        hovered SetVariable("replay_num", 11)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("girlsescape", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show", "k_hat": True})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s5"]:
                    textbutton "Standing Up" xalign 0.5:
                        hovered SetVariable("replay_num", 12)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("showmustgoon", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s6"]:
                    textbutton "Hiding in the Closet" xalign 0.5:
                        hovered SetVariable("replay_num", 13)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("kidshiding", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s7"]:
                    textbutton "A Special Game" xalign 0.5:
                        hovered SetVariable("replay_num", 14)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("deadlygame", scope={"currentdate": "March 31st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch3_s8"]:
                    textbutton "Eyesore" xalign 0.5:
                        hovered SetVariable("replay_num", 15)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("jessicaseye", scope={"event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 20
                text "Chapter 4" xalign 0.5
                if persistent.scenes["ch4_s1"]:
                    textbutton "Mirror Madness" xalign 0.5:
                        hovered SetVariable("replay_num", 16)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("mirrormadness", scope={"currentdate": "April 1st", "event": "REDD War ends", "clothing": "show", "t_name": "Trosh"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch4_s2"]:
                    textbutton "Safe Haven" xalign 0.5:
                        hovered SetVariable("replay_num", 17)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("citychase", scope={"currentdate": "April 1st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch4_s3"]:
                    textbutton "Going Back" xalign 0.5:
                        hovered SetVariable("replay_num", 18)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("goingback", scope={"currentdate": "April 1st", "event": "REDD War ends", "b_name": "Bartender", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 20
                text "Chapter 5" xalign 0.5
                if persistent.scenes["ch5_s1"]:
                    textbutton "Sneaking In" xalign 0.5:
                        hovered SetVariable("replay_num", 19)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("backattheater", scope={"currentdate": "April 1st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch5_s2"]:
                    textbutton "Unexpected Events" xalign 0.5:
                        hovered SetVariable("replay_num", 20)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("deadchild", scope={"currentdate": "April 1st", "event": "REDD War ends", "clothing": "show"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch5_s3"]:
                    textbutton "Fight for Freedom" xalign 0.5:
                        hovered SetVariable("replay_num", 21)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("escapeplan", scope={"curentdate": "April 1st", "event": "REDD War ends", "clothing": "show", "t_name": "Trosh"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch5_s4"]:
                    textbutton "Final Confrontation" xalign 0.5:
                        hovered SetVariable("replay_num", 22)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("finalconfrontation", scope={"currentdate": "April 1st", "event": "REDD War ends", "clothing": "show", "t_name": "Trosh"})]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                if persistent.scenes["ch5_s5"]:
                    textbutton "Epilogue" xalign 0.5:
                        hovered SetVariable("replay_num", 23)
                        unhovered SetVariable("replay_num", 0)
                        action [SetVariable("replay_num", 0), Replay("epilogue")]
                else:
                    textbutton "LOCKED" xalign 0.5:
                        hovered SetVariable("replay_num", -1)
                        unhovered SetVariable("replay_num", 0)
                        action NullAction()
                null height 10

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
            elif replay_num == 16:
                text "Laura, along with some other parents, are brought out for yet another special game." style "replay_desc" xalign 0.5
            elif replay_num == 17:
                text "Laura finds herself on the streets of Atlanta." style "replay_desc" xalign 0.5
            elif replay_num == 18:
                text "After watching more of Mr. Sprinkles's show, Laura decides to return to the theater." style "replay_desc" xalign 0.5
            elif replay_num == 19:
                text "Laura sneaks her way back into the theater to try and stop Mr. Sprinkles." style "replay_desc" xalign 0.5
            elif replay_num == 20:
                text "Things don't go according to Mr. Sprinkles's plan when an unexpected casualty occurs." style "replay_desc" xalign 0.5
            elif replay_num == 21:
                text "A battle within the War commences as the hostages fight back against their captors." style "replay_desc" xalign 0.5
            elif replay_num == 22:
                text "A confrontation between Laura and Krag that might spell the end of this show." style "replay_desc" xalign 0.5
            elif replay_num == 23:
                text "A few months later, Laura returns to her safe haven." style "replay_desc" xalign 0.5
    frame:
        xalign 0.13 yalign 0.95
        xpadding 20 ypadding 5
        text "[scene_percent]% Completed" xalign 0.5 yalign 0.5
    imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.65 yalign 0.95
screen achievements():
    tag title
    frame:
        xysize(1240, 670)
        xalign 0.5 yalign 0.4
        vbox:
            xalign 0.25 yalign 0.5
            if persistent.achievements["toosafe"]:
                text "{i}Playing it TOO Safe{/i}" xalign 0.5
                text "Escape Atlanta" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievements["futurecorpses"]:
                text "{i}Future Corpses{/i}" xalign 0.5
                text "Fulfill Your Destiny" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievements["epicfail"]:
                text "{i}Schadenfreude{/i}" xalign 0.5
                text "Embarrass Yourself on Live Television" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievements["rattrap"]:
                text "{i}Rat Trap{/i}" xalign 0.5
                text "Fall Victim to the {i}Mirror Madness{/i} Maze" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
            null height 25
            if persistent.achievements["memoryloss"]:
                text "{i}Memory Loss{/i}" xalign 0.5
                text "Forget the password to Frank's Bar" xalign 0.5
            else:
                text "LOCKED" xalign 0.5
        text "[achieve_percent]% Completed" xalign 0.95 yalign 0.95
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
            text "{i}10 Past Midnight{/i}" xalign 0.5
            text "{i}Autumn Changes{/i}" xalign 0.5
            text "{i}Bells of Weirdness{/i}" xalign 0.5
            text "{i}Classy Ghouls Halloween Gathering{i}" xalign 0.5
            text "{i}Creaky Country Fair{/i}" xalign 0.5
            text "{i}Escape{/i}" xalign 0.5
            text "{i}Ice Cream Truck{/i}" xalign 0.5
            text "{i}Into Battle v001{/i}" xalign 0.5
            text "{i}Into the Haunted Forest{/i}" xalign 0.5
            text "{i}Neon Runner{/i}" xalign 0.5
            text "{i}Packing{/i}" xalign 0.5
            text "{i}Shattered Mind{/i}" xalign 0.5
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
            text "Made with Ren'Py 7.3.5" style "creditscreen" xalign 0.5
    vbox:
        xalign 0.9 yalign 0.9
        textbutton "Next >" action ShowMenu("credits2") xalign 1.0
        imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.5
screen credits2():
    tag title
    frame:
        xysize(1240, 670)
        xalign 0.5 yalign 0.4
        vbox:
            xalign 0.5 yalign 0.25
            text "Special Thanks" style "creditscreen2" xalign 0.5
            null height 20
            text "God" style "creditscreen" xalign 0.5
            text "For all the gifts and abilities He has given me" xalign 0.5
            null height 20
            text "Tom 'PyTom' Rothamel" style "creditscreen" xalign 0.5
            text "For creating the Ren'Py visual novel engine" xalign 0.5
            null height 20
            text "James DeMonaco" style "creditscreen" xalign 0.5
            text "For creating the concept that the REDD War was based on" xalign 0.5
            null height 20
            text "Jed Elinoff and Scott Thomas" style "creditscreen" xalign 0.5
            text "For writing the film that inspired this story" xalign 0.5
            null height 20
            text "SlightlySimple, Mattyd, Thugzilla, Xeno, and many other friends on Discord" style "creditscreen" xalign 0.5
            text "For being so supportive of this project's development" xalign 0.5
            null height 20
            text "You" style "creditscreen" xalign 0.5
            text "For reading this story" xalign 0.5
    vbox:
        xalign 0.9 yalign 0.9
        textbutton "< Previous" action ShowMenu("credits") xalign 0.0
        imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.5
screen socials():
    tag title
    frame:
        xysize(400, 300)
        xalign 0.5 yalign 0.5
        imagebutton auto "gui/twitter_%s.png" action OpenURL("https://twitter.com/goodtalesvn") xalign 0.15 yalign 0.1
        imagebutton auto "gui/instagram_%s.png" action OpenURL("https://instagram.com/goodtalesvn") xalign 0.85 yalign 0.1
        imagebutton auto "gui/discord_%s.png" action OpenURL("https://discord.gg/zZhPrkC") xalign 0.5 yalign 0.9
    imagebutton auto "gui/return_%s.png" action ShowMenu("extras") xalign 0.5 yalign 0.99

## Variables ######################################################################################################################

## Definitions
define _game_menu_screen = "pause"
define alpha = "ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
init python:
    if not renpy.variant('mobile'):
        clickortap = "Click"
    else:
        clickortap = "Tap"
define config.hard_rollback_limit = 1000000
define config.replay_scope = {"_game_menu_screen": "pause"}

## Persistents and Preferences

# Lists
default persistent.achievelist = []
default persistent.scenelist = []

# Dictionaries
default persistent.achievements = {"toosafe": False, "futurecorpses": False, "epicfail": False, "rattrap": False, "memoryloss": False}
default persistent.scenes = {
"ch1_s1": False, "ch1_s2": False,
 "ch2_s1": False, "ch2_s2": False, "ch2_s3": False, "ch2_s4": False, "ch2_s5": False,
 "ch3_s1": False, "ch3_s2": False, "ch3_s3": False, "ch3_s4": False, "ch3_s5": False, "ch3_s6": False, "ch3_s7": False, "ch3_s8": False, 
 "ch4_s1": False, "ch4_s2": False, "ch4_s3": False,
 "ch5_s1": False, "ch5_s2": False, "ch5_s3": False, "ch5_s4": False, "ch5_s5": False}

# Booleans
default preferences.fullscreen = False

## Defaults

# Strings
default axehit = ""
default b_name = "???"
default clothing = "main"
default currentdate = "March 30th"
default currenttime = "4:12 PM"
default direction = ""
default event = "War Zones are revealed"
default l_exp = "neutral"
default password = ""
default s_name = "Mr. Sprinkles"
default save_name = "Chapter 1"
default save_subtitle = "The Calm Before the Storm"
default t_name = "REDD"
default timeleft = "2 hours and 48 minutes"

# Booleans
default badcredits = False
default gotdrink = False
default k_hat = False
default leftdeadend = False
default nicetry = False
default nvl = False
default quickhide = False
default title = True

# Integers
default achieve_percent = 100 * len(persistent.achievelist) / len(persistent.achievements)
default replay_num = 0
default scene_percent = 100 * len(persistent.scenelist) / len(persistent.scenes)

## Labels #########################################################################################################################

# Splash Screen/Main Menu Intro
label before_main_menu:
    scene bg fade
    if not persistent.gorewarning:
        $quick_menu = False
        "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){nw}"
        menu:
            "This visual novel contains graphic violence and has visuals to accommodate it. Would you like to disable the graphic images? (This can be changed later in the options menu){fast}"
            "Yes, disable them":
                $persistent.gore = "_sfw"
                "Graphic images disabled."
            "No, enable them":
                $persistent.gore = ""
                "Graphic images enabled."
        "There are also brief moments of the screen flashing a bright light quickly when weapons are fired. Would you like to disable flashing lights? (This can also be changed later in the options menu){nw}"
        menu:
            "There are also brief moments of the screen flashing a bright light quickly when weapons are fired. Would you like to disable flashing lights? (This can also be changed later in the options menu){fast}"
            "Yes, disable them":
                $persistent.flash = False
                "Screen flashes disabled."
            "No, enable them":
                $persistent.flash = True
                "Screen flashes enabled."
        "Thank you. Enjoy the story."
        window hide dissolve
        pause 2
        $persistent.gorewarning = True
        $quick_menu = True
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
    if save_name == "Chapter 1":
        scene bg livingroom_day_blur
    elif save_name == "Chapter 2":
        scene bg theater_ext_blur
    elif save_name == "Chapter 3":
        scene bg stage_blur
    elif save_name == "Chapter 4":
        scene bg warehouse_blur
    elif save_name == "Chapter 5":
        scene bg dressingroom_blur
    with Dissolve(2.0)
    show screen chaptername
    with dissolve
    $renpy.pause(delay=3)
    hide screen chaptername
    scene bg fade
    with Dissolve(2.0)
    pause 2
    return

# Shows Time, Date, and Time Remaining
label chapterstart:
    stop music
    stop sound
    stop sound2
    stop ambience
    stop ambience2
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
        ease 1.0 alpha 1.0
    $renpy.pause()
    hide screen dateandtime
    hide screen timeremaining
    hide ctc
    with dissolve
    return

# End of Scene
label sceneend:
    if nvl:
        $nvl = False
        nvl hide
        with dissolve
    else:
        hide screen laura
    window hide dissolve
    stop music fadeout(3.0)
    stop sound fadeout(3.0)
    stop sound2 fadeout(3.0)
    stop ambience fadeout(3.0)
    stop ambience2 fadeout(3.0)
    pause 1
    if not renpy.showing("bg fade"):
        scene bg fade
        with Dissolve(2.0)
        pause 3
    else:
        pause 1
    $renpy.end_replay()
    return

# Game Over Screen
label gameover:
    python:
        renpy.block_rollback()
        config.skipping = False
        config.allow_skipping = False
    if not badcredits:
        play music creaky_country_fair
    pause 0.75
    show screen gameover
    with Dissolve(2)
    if badcredits:
        $renpy.pause(delay=5)
        hide screen gameover
        with Dissolve(2)
        pause 1
        scene bg fade
        with Dissolve(1.0)
        pause 1
        return
    else:
        pause 1
        show screen loadorquit
        with Dissolve(1)
        $renpy.pause(hard=True)
        return
label after_load:
    $config.allow_skipping = True
    return

# Shows Flash of Gun/Vibrates Phone
label gunflash:
    if persistent.vibrate:
        $renpy.vibrate(0.25)
    if persistent.flash:
        show white zorder 5
        pause 0.05
        hide white
    else:
        pause 0.05
    return

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
