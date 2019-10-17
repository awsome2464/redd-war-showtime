label chapter_4:
    python:
        save_name = "Chapter 4"
        save_subtitle = "Fleeing the Storm"
    call chaptername
label mirrormadness:
    python:
        currenttime = "12:32 AM"
        timeleft = "6 hours and 28 minutes"
        nvl = True
        l_exp = "surprised"
    call chapterstart
    pause 2
    nvl clear
    nvl show dissolve
    narrate """
    It had been a little over an hour since Richard lost the game.

    Honestly, it didn't really feel like it's been that long, but ever since it happened, it's all I could really think about.

    I had seen other adults that were in the room with us die on that screen, but Richard wasn't supposed to be one of them.

    He was supposed to make it to the end of the night with me so we could see Kate and Dakota again.

    Then we'd all go home as one happy family.

    ...

    {nw}

    I guess I was pretty fucking stupid to think that would ever happen.
    """
    nvl clear
    play music vast_places
    narrate """
    I tried to be positive about our situation.

    I tried to assume that we'd be okay.

    I tried to believe that the deaths we saw on the screen couldn't happen to us.

    But in the end, I just made a damn fool of myself.

    {clear}

    Despite everything, though, I couldn't stop apologizing.

    I apologized to Richard for not leaving Atlanta.

    I apologized to Kate and Dakota for bringing them to this horror show.

    I apologized to every innocent person in the theater for all the terror they have gone or will go through tonight.

    {nw}

    Although maybe I shouldn't be blaming myself for all this.

    After all, how was I supposed to know that a REDD would use the REDD War to kill innocent people?

    I'd have to be a fucking wizard to figure that shit out.
    """
    $nvl = False
    window show
    nvl hide
    with dissolve
    pause 1.0
    scene bg storage
    with Dissolve(2.0)
    pause 0.1
    show screen laura
    pause 0.6
    "In the hour since Richard's death, there have been more."
    "The room is slowly but surely getting emptier as hostages are either going back to their seats or having their bodies tossed who-knows-where."
    $l_exp = "concerned"
    "Hell, for all I know, my husband's body is still lying flat in the street."
    $l_exp = "sad"
    "This is all just insane..."
    stop music fadeout(3.0)
    play sound door_open
    pause 1.5
    show trosh at middle with dissolve
    pause 0.1
    $l_exp = "neutral"
    t "Alright! We're gonna need 4 contestants for this one."
    t "Let's start with you."
    "He then pointed to a nearby woman near the front of the room."
    "A guard then grabbed her and held her by the doorway as Trosh moved deeper into the room."
    t "You."
    "A middle-aged man, probably about 10 years older than me."
    $l_exp = "surprised"
    "Trosh then moved closer and closer."
    "Closer to me."
    t "Heh..."
    t "Looks like you don't have anyone to volunteer as tribute this time."
    $l_exp = "mad"
    l "..."
    "A guard then grabbed me by the arm as Trosh moved to the very back of the room to pick the final contestant."
    $l_exp = "concerned"
    "Trosh really wants me dead, doesn't he?"
    "I suppose he could have just shot me himself by now."
    $l_exp = "mad"
    "But I'm sure he'd be more entertained by watching me fail miserably at the games."
    "With no other choice, I, along with the other contestants, made our way out of the room."
    "I was expecting us to be going towards the stage."
    $l_exp = "concerned"
    "Instead, we were going towards a door that led outside."
    "Guess we're playing another 'big and exciting' game in a separate location."
    "Should have expected as much from Trosh."
    $renpy.music.set_volume(0.75, channel="ambience")
    play music into_the_haunted_forest
    play ambience rapid_gunfire
    scene bg alley with dissolve
    pause 0.1
    $l_exp = "neutral"
    "We were all brought outside to an alley that wasn't too far from the main street."
    show trosh at middle with dissolve
    pause 0.1
    t "Sit tight; our ride will be here shortly."
    man "R-Ride? Where are you taking us??"
    t "To the game, dumbass!"
    t "This one's farther away than the parking garage we used last time."
    t "So just sit there and wait patiently or I'll kill ya and grab another contestant to fill your spot. Capiche?"
    man "...yes."
    hide trosh with dissolve
    pause 0.1
    "With that, Trosh walked closer to the edge of the alley, looking down the road for the expected transportation."
    $l_exp = "concerned"
    "It truly does make me wonder how far away we're going for this."
    "And why this game would require this particular space."
    $l_exp = "neutral"
    "I can only think of a handful of {i}Mr. Sprinkles{/i} games that are truly big."
    play sound "audio/se/whistle.ogg"
    $l_exp = "surprised"
    "Suddenly, I heard a whistle come down the alley."
    "Trosh was facing us, pointing towards the road with his thumb."
    "The other guards then started dragging us towards him."
    $l_exp = "concerned"
    "Almost on cue, a large vehicle pulled up in front of us."
    "It looked like a city bus, but was covered in coal-black metal armor, making it look more like a tank."
    t "Let's go! Move it!"
    $l_exp = "neutral"
    "One by one, we were moved into the vehicle and were sat down."
    "Unsurprisingly, we were the only ones in there."
    "The 4 humans were sat towards the front while the guards sat behind us, never seeming to break eye contact with us."
    t "Alright, let's go! We've got a deadline here!"
    "The REDD driver gave a nod and started driving towards our destination."
    $l_exp = "concerned"
    "Wherever that may be."
    hide screen laura
    window hide dissolve
    pause 1.5
    scene bg street
    show bus_window at middle
    with Fade(1.0, 0.5, 1.0)
    pause 1.0
    $l_exp = "neutral"
    show screen laura
    window show dissolve
    pause 0.6
    "After about 10 minutes, we were still driving."
    $l_exp = "concerned"
    "I guess we truly were a decent distance away from the theater."
    $l_exp = "surprised"
    "As I looked out the window, I could see REDD out there, smashing store windows, chasing after panicked humans with weapons, and so much more."
    $l_exp = "sad"
    "You'd think they would've ran out of stuff to kill and destroy by now."
    $l_exp = "surprised"
    "I quickly decided to stop looking out the window and instead look around the vehicle we were in."
    "It was very clean and professional, like it wasn't just a makeshift vehicle made during the War."
    $l_exp = "concerned"
    "So I suppose that begs the question of where it came from."
    "If I didn't know any better, I'd say it was from the REDD Base in Antarctica."
    $l_exp = "surprised"
    "..."
    "Actually, now that I think about it, how the hell did Krag manage to afford all these REDD guards?"
    $l_exp = "concerned"
    "I mean, yeah, one of them is his brother, but there's no way they're all doing this for free."
    "The only thing I can think of is--{nw}"
    stop ambience fadeout(3.0)
    $l_exp = "surprised"
    t "Alright, assholes! We're here!"
    t "Let's move it!"
    "Before we could do anything else, the guards grabbed us and pulled us out of the vehicle."
    scene bg fade with dissolve
    pause 0.1
    $l_exp = "concerned"
    "I was a bit disoriented, but it looked like we were approaching a warehouse or air hangar of some sort."
    "Whatever it was, there were lights on inside, so they were clearly expecting company."
    scene bg warehouse with dissolve
    pause 0.1
    $l_exp = "neutral"
    "The building was devoid of life save for us, though it was far from empty."
    $l_exp = "concerned"
    "Towards the middle of the building was what looked like a tall wall."
    "A door on each side could be seen, it seeming to enter a hallway of some sort."
    $l_exp = "surprised"
    "!!!"
    "Or a maze."
    show trosh at middle with dissolve
    pause 0.1
    t "Alright, everyone get to one of the corners!"
    t "Move it! Come on!"
    $l_exp = "rage"
    l "Alright! Hold your damn horses!"
    "He glared at me for a second before walking towards a table near the entrance, leaving the remaining guards to drag each of us to one of the openings of the maze."
    hide trosh with dissolve
    pause 0.1
    $l_exp = "neutral"
    "He then turned on a radio near the warehouse entrance, where we could hear live audio from back at the theater."
    play music sprinkles_radio
    s "Alright, ladies and gentlemen! Our contestants are live and ready at the {i}Mirror Madness{/i} maze~!"
    s "Who will make it to the middle first?"
    s "Will any of them be able to avoid our added twist?"
    $l_exp = "surprised"
    l "{i}'Added twist?'{/i}"
    l "What twist?"
    "The guards just laughed among each other, choosing to ignore my question."
    s "Let's find out, shall we~?"
    s "Are you ready, contestants?"
    $l_exp = "mad"
    "Of course not."
    stop music fadeout(3.0)
    s "On your marks..."
    $l_exp = "surprised"
    "I guess I don't have much of a choice here."
    s "Get set..."
    "I took a deep breath and looked ahead at the hallway in front of me."
    "It's just a giant maze of mirrors that I have to navigate while avoiding an 'added twist'."
    $l_exp = "concerned"
    "What could go wrong?"
    s "{b}GO!{/b}"
    play sound airhorn
    play music into_battle
    $l_exp = "sad"
    "Well, here goes!"
    $nvl = True
    nvl clear
    hide screen laura
    nvl show dissolve
    narrate """
    I bolted into the maze, not really knowing where I was going.

    I had seen the game being played on TV many times, and I always found it a bit trippy and disorienting.

    Being inside the maze itself, though, is a million times worse than I could have imagined.

    The context of this whole night's events might be adding to it, though.

    {nw}

    I soon came to my first fork in the path, one way going to the right and one continuing straight.

    Which way should I go?{nw}
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Straight{/font}":
            $direction = "straight"
            nvl clear
            narrate "I kept going straight."
        "{font=fonts/GosmickSans.ttf}Right{/font}":
            $direction = "right"
            nvl clear
            narrate "I turned to the right."
    narrate """
    As I ran, I couldn't help but see the infinite reflections from the mirrors in my peripheral vision.

    It was truly messing with my head, especially when I could see a dead end coming up ahead.
    """
    if direction == "straight":
        jump wentstraight
    elif direction == "right":
        jump wentright

label wentstraight:
    narrate """
    I reached the end and saw the only way to go was right.

    I turned that direction...
    only to be met with a proper dead end.

    Shit...

    With no other option, I turned around and ran back the way I had come.

    After reaching the first path again, I went to the right.

    Or, rather, techincally the left this time.
    """
    nvl clear

label wentright:
    narrate """
    There were only two ways to go: right or left.

    Which way should I go?{nw}
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Left{/font}":
            nvl clear
            narrate "I went to the left."
            if direction == "straight":
                narrate "Shit. Another dead end."
                narrate "With no other choice, I ran back the other way."
                jump nojingle
            elif direction == "right":
                narrate "Shit. A dead end."
                stop music fadeout (3.0)
                play sound running loop
                narrate """
                That's when I heard something behind me.

                I looked at the reflection in front of me and saw the culprit:

                A REDD mime with long hair running towards me with an axe in her hand!

                Before I could react in any way...!
                """
                $nvl = False
                nvl hide
                window hide
                play sound hammer
                show blood
                pause 1.5
                scene bg fade
                with Dissolve(2.0)
                pause 1.0
                if not persistent.achievement_rattrap:
                    $persistent.achievement_rattrap = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $renpy.end_replay()
                jump gameover
        "{font=fonts/GosmickSans.ttf}Right{/font}":
            nvl clear
            narrate "I went to the right."
            if direction == "straight":
                jump hijingle
            elif direction == "right":
                nvl clear
                narrate """
                I then ran ran until I came across another turn, this time to the left.

                Once I turned...
                """
                # Slide in Jingle with axe
                nvl hide
                window hide
                play sound hammer
                show blood
                pause 1.5
                scene bg fade
                with Dissolve(2.0)
                pause 1.0
                if not persistent.achievement_rattrap:
                    $persistent.achievement_rattrap = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $renpy.end_replay()
                jump gameover

label hijingle:
    nvl clear
    narrate """
    I kept on running.

    I soon came across another turn, this time to the left.

    Once I turned, I saw one of the other contestants in the distance!
    """
    stop music fadeout(3.0)
    $renpy.music.set_volume(0.5, channel="sound")
    play sound running loop
    narrate """
    Though I also heard quick footsteps coming from his general loction.

    He turned to where the footsteps were coming from and screamed!

    A split second later...
    """
    nvl hide
    window hide
    $renpy.music.set_volume(1.0, channel="sound")
    play sound hammer
    pause 1.5
    window show
    nvl show
    narrate """
    ...an axe lodged itself into his forehead!

    {clear}

    As I screamed and he dropped to the ground, a figure came from around the corner.

    A short figure with long tied-up hair, a black dress, and pale white face makeup.

    After she yanked the axe out of the man's head, she then turned towards me with a grin.

    Not even a threatening grin that showed any ill intent; just a casual grin you'd expect her to make on the TV show.

    Somehow, that makes this situation even scarier.

    Especially when she then ran towards me with the axe!
    """
    play music theyre_closing_in
    nvl clear
    narrate """
    I looked and saw a hallway just a few feet ahead of me that led further into the maze.

    But that would also mean getting closer to Jingle to get there!

    My only other option would be to run back the way I came.

    What should I do??{nw}
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Run further into the maze{/font}":
            nvl clear
            jump runfurther
        "{font=fonts/GosmickSans.ttf}Run away{/font}":
            nvl clear
            jump runaway

label runfurther:
    narrate """
    I decided to try my luck and run further into the maze.

    Dashing as fast as I could, I went around the corner before Jingle had a chance to catch up with me.

    I had no idea where I was going from here, but anywhere that didn't have a REDD mime with an axe was good enough for me.
    """
    play sound hammer
    narrate"""
    {nw}

    As I got further down the hall, I heard another scream and impact of the axe.

    Only it wasn't from behind me, but in front...!

    Not necessarily directly around the corner, but very much in that general area.

    Of course, even if I wanted to go back, a quick look in the mirrors showed Jingle was on her way towards me!

    Hoping for the best, I kept moving forward.

    {nw}

    Another fork, left or right.

    Where to?{nw}
    """
    menu(nvl=True):
        "Left":
            nvl clear
            jump goleft
        "Right":
            nvl clear
            jump goright

label goleft:
    narrate """
    I went left, only to be instantly greeted by another corner going to the right.

    Moving on, there was yet another intersection, this time spliting in 3 directions: straight, right, and left.
    """
label threeway: # ;)
    narrate "Where do I go from here?{nw}"
    menu(nvl=True):
        "Go straight":
            nvl clear
            $direction = "straight"
            jump goingstraight
        "Go right":
            nvl clear
        "Go left" if leftdeadend == False:
            nvl clear
            narrate """
            I turned left only to find...

            ...a dead end.

            Groaning, I turned back to the intersection and got myself reoriented to how I was before.
            """
            nvl clear
            $leftdeadend = True
            jump threeway

label goingstraight:

