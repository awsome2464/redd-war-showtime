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
        l_exp = "crying"
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
    $l_exp = "sad"
    "Hell, for all I know, my husband's body is still lying flat in the street."
    "This is all just insane..."
    "After a while, I took out my phone."
    $l_exp = "surprised"
    "No new messages from Dakota."
    "That didn't stop me from sending another text."
    $l_exp = "crying"
    lt "I'm sorry Dakota. I'm sorry I couldn't keep your dad safe"
    lt "Please be safe okay? That's all I want"
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
    scene bg basement_hall with dissolve
    pause 0.1
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
    show bus_window at truecenter
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
                jump hijingle
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
                if not persistent.achievements["rattrap"]:
                    $persistent.achievements["rattrap"] = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievelist.append(1)
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
                I then ran until I came across another turn, this time to the left.

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
                if not persistent.achievements["rattrap"]:
                    $persistent.achievements["rattrap"] = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievelist.append(1)
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
    Though I also heard quick footsteps coming from his general location.

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
    play music escape
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
            narrate """
            I turned around and ran back the way I came.

            It was risky, but it was safer than running towards a murderer!

            After a quick backtrack, I found myself right back at the entrance where I started.
            """
            $axehit = "Jingle"
            jump stayorgo

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
        "{font=fonts/GosmickSans.ttf}Left{/font}":
            nvl clear
            jump goleft
        "{font=fonts/GosmickSans.ttf}Right{/font}":
            nvl clear
            jump goright

label goright:
    narrate """
    I turned to the right, which I believe would bring me further into the maze.

    It would also bring me closer to the middle, which is where I needed to go to win, and by extension survive, anyway.

    {nw}

    Another fork.

    Left or right?{nw}
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Left{/font}":
            nvl clear
            narrate """
            I ran to the left.

            And came across a dead end.

            Shit...

            Before I could turn around, though...
            """
            # show Jangle in reflection
            nvl hide
            window hide
            stop music
            play sound hammer
            show blood
            pause 1.5
            scene bg fade
            with Dissolve(2.0)
            pause 1.0
            if not persistent.achievements["rattrap"]:
                $persistent.achievements["rattrap"] = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover
        "{font=fonts/GosmickSans.ttf}Right{/font}":
            nvl clear
            narrate """
            I ran to the right.

            Greeting me as I did was Jangle facing me with an axe!
            """
            nvl hide
            window hide
            stop music
            play sound hammer
            show blood
            pause 1.5
            scene bg fade
            with Dissolve(2.0)
            pause 1.0
            if not persistent.achievements["rattrap"]:
                $persistent.achievements["rattrap"] = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover

label goleft:
    narrate """
    I went left, only to be instantly greeted by another corner going to the right.

    Moving on, there was yet another intersection, this time spliting in 3 directions: straight, right, and left.
    """
    label threeway: # ;)
        narrate "Where do I go from here?{nw}"
        menu(nvl=True):
            "{font=fonts/GosmickSans.ttf}Go straight{/font}":
                nvl clear
                jump goingstraight
            "{font=fonts/GosmickSans.ttf}Go right{/font}":
                nvl clear
                narrate """
                I ran to the right.

                A few feet later, I came across yet another fork in the path, one going left, and one going{nw}
                """
                #Jangle with axe slides in
                $nvl = False
                nvl hide
                window hide
                stop music
                play sound hammer
                show blood
                pause 1.5
                scene bg fade
                with Dissolve(2.0)
                pause 1.0
                if not persistent.achievements["rattrap"]:
                    $persistent.achievements["rattrap"] = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievelist.append(1)
                $renpy.end_replay()
                jump gameover
            "{font=fonts/GosmickSans.ttf}Go left{/font}" if leftdeadend == False:
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
    narrate "I ran straight ahead, which seemed to just lead to a long endless hallway."
    play sound running loop
    narrate """
    As I did, I could hear movement a fair distance behind me!

    I definitely don't think it's smart to go back now...

    {nw}

    Another fork, one to the left and one to the right.{nw}
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Go left{/font}":
            nvl clear
            stop sound fadeout(3.0)
            narrate """
            I ran to the left.

            I eventually came across a turn to the right.

            What I found at the end of the hall was...

            ...one of the entrances...!
            """
            $axehit = "Jangle"
            jump stayorgo
        "{font=fonts/GosmickSans.ttf}Go right{/font}":
            nvl clear
            narrate """
            I ran to the right.

            ...

            Dead end.

            I heard the footsetps behind me get closer!
            """
            $nvl = False
            nvl hide
            window hide
            stop music
            play sound hammer
            show blood
            pause 1.5
            scene bg fade
            with Dissolve(2.0)
            pause 1.0
            if not persistent.achievements["rattrap"]:
                $persistent.achievements["rattrap"] = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover

label stayorgo:
    nvl clear
    narrate """
    I looked ahead at the outer wall of the building and saw that the hangar doors were wide open.

    There were also two REDD guards off to the side watching the live feed of the event, which was focused on one of the other contestants.

    ...

    Do I want to risk it?

    Do I want to risk running out of both the maze and the hangar without getting shot?

    What should I do...?
    """
    menu(nvl=True):
        "{font=fonts/GosmickSans.ttf}Run back in the maze{/font}":
            nvl clear
            narrate """
            No. It's too risky.

            At least by trying to win the game, I'll have a better chance of having an outcome where I survive.

            With that, I ran back into the maze.
            """
            stop music fadeout(3.0)
            #Showing Jingle or Jangle depending on value of "axehit"
            if axehit == "Jingle":
                pass
            elif axehit == "Jangle":
                pass
            pause 3
            narrate """
            ...only to be greeted by [axehit].

            Well, shi{nw}
            """
            $nvl = False
            nvl hide
            window hide
            stop music
            play sound hammer
            show blood
            pause 1.5
            scene bg fade
            with Dissolve(2.0)
            pause 1.0
            if not persistent.achievements["rattrap"]:
                $persistent.achievements["rattrap"] = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover
        "{font=fonts/GosmickSans.ttf}Escape the building{/font}":
            nvl clear
            narrate """
            Fuck it.

            {nw}

            Using whatever energy I had left, I bolted out of the maze and straight for the wide open doors.

            I wasn't really thinking of anything else at that moment.

            All that was important to me was getting the fuck out of this godforsaken nightmare.

            {nw}

            I don't know if the guards had seen me.

            I don't know if the camera's facing me and everyone's seeing me flee.

            If I can get out of here with my life, that's all that matters to me.

            ...
            """
            $nvl = False
            nvl hide
            window hide
            stop music fadeout(3.0)
            pause 2
            show trosh at middle
            with Dissolve(1.0)
            pause 1
            window show dissolve
            pause 0.1
            redd "Shouldn't we try and stop her, Sir?"
            t "Stop a young woman with no weapons from heading towards a densely-populated area during the REDD War?"
            t "Nah. Let's let nature take its course."
            redd "Understood."
            call sceneend
            if not persistent.scenes["ch4_s1"]:
                $persistent.scenelist.append(1)
                $persistent.scenes["ch4_s1"] = True


label citychase:
    python:
        currenttime = "1:15 AM"
        timeleft = "5 hours and 45 minutes"
        l_exp = "concerned"
    call chapterstart
    pause 2
    $renpy.music.set_volume(0.75, channel="ambience")
    play music into_the_haunted_forest
    play ambience rapid_gunfire
    scene bg street
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    "After hiding in an alley for a few minutes, I poked my head out and looked around."
    "No visuals of any REDD, but I could hear them nearby."
    $l_exp = "neutral"
    "I moved back into the alley and hid behind the trash."
    $l_exp = "sad"
    extend ".. and corpses."
    "At least, what was left of some of them."
    $l_exp = "surprised"
    "Thank God none of them appeared to be people I knew or else this would be more traumatizing than this night has already been."
    nvl clear
    $nvl = True
    hide screen laura
    nvl show dissolve
    narrate """
    The fact that the REDD are still not showing signs of slowing down despite the War being halfway over really boggles my mind.

    Do they really show no remorse?

    Homes destroyed, family members' lives lost...

    Do they really not care that they're causing so much damage to innocent people?

    Heh.{w=0.5} What am I saying?

    They're REDD. Of course they don't.

    {clear}

    I don't know why I ever tried to be neutral about them.

    Krag Dovason really seemed like my best proof that maybe, just maybe, a good REDD exists.

    Richard was always quick to point out how the REDD War in London had a moment where pro-REDD humans who were trying to make peace were mowed down like they were nothing.

    He said that it showed that they don't like any humans, period. Even the ones who kiss their asses.

    \"But that was one of the earlier REDD Wars,\" I always replied. \"Things {b}had{/b} to have changed since then!\"

    Well, as I look back at tonight's events, I guess I can see that they didn't.
    """
    $nvl = False
    nvl hide
    window hide
    play sound "audio/se/woman scream.ogg"
    pause 2
    show screen laura
    window show dissolve
    pause 0.1
    "A woman's scream could be heard around the corner, as well as laughter from multiple people."
    "A second later, I could see her sprint across the alley entrance, with 3 or 4 REDD coming after her with bats, machetes, and other weapons of the sort."
    woman "P-Please leave me aloooone!!!"
    $l_exp = "sad"
    "I could hear the sobs mixed in with that plea."
    $l_exp = "surprised"
    "But the REDD only replied with howls of laughter."
    $l_exp = "mad"
    "I just can't believe it..."
    "I can't believe I let myself believe that these things were able to show any form of empathy towards us."
    $l_exp = "neutral"
    "But that also means that I need to be extra careful to not get caught."
    "Even if that means I have to hide next to dismembered body parts for the next 6 hours."
    "..."
    $l_exp = "concerned"
    "I suppose it's not the most desired outcome, but it's better than being dead."
    $l_exp = "sad"
    "...like Richard..."
    $l_exp = "concerned"
    woman "{b}AIIIIEEEE!!!{/b}"
    "More REDD laughter."
    redd "Nowhere to run now, you little--!"
    $l_exp = "surprised"
    stop ambience
    stop music
    play sound "audio/se/car crash.ogg"
    pause 3.5
    $t_name = "REDD 1"
    t "Are you fucking serious?!"
    $t_name = "REDD 2"
    t "God {b}DAMN IT!!!{/b}"
    "..."
    "It sounded like she got hit by a car."
    $l_exp = "sad"
    "That poor girl..."
    t "{b}FUCK!!{/b}"
    t "That was supposed to be {b}OUR{/b} kill!!!"
    $t_name = "REDD 3"
    t "Who the fuck was driving that?? I say we hunt that shithead down!!"
    $t_name = "REDD 1"
    t "Forget it; it's a waste of time. We'll find someone else to kill."
    $t_name = "REDD 3"
    t "Where??"
    $t_name = "REDD 1"
    t "It's a big city; we'll find someone even if we've gotta break into every building!"
    t "Now c'mon!"
    $l_exp = "surprised"
    "I made sure I was as hidden as I could be; maybe they'll just glance right over me."
    "Maybe they won't even go down the alley."
    $l_exp = "neutral"
    play sound footsteps
    "..."
    "...or maybe they will."
    "I took a look around, looking for anything I could use to defend myself."
    $l_exp = "concerned"
    "Not sure how much a trash bag or a human head will do, though."
    "Then again, I suppose anyone, REDD or human, would be confused by a head being thrown at them, right?"
    $l_exp = "surprised"
    $t_name = "REDD 2"
    t "Well, hello there~"
    "I looked up and saw one of the REDD staring at me with a hideous grin."
    t "You look a bit bored back here. What do you say I spice up your night a bit?"
    $l_exp = "mad"
    l "My night has had too much excitement already, thank you very much."
    $l_exp = "neutral"
    "I probably shouldn't have been snippy, but this night is just bringing out the worst in me."
    t "Is that right?"
    t "Then allow me to add even more excitement to your night!"
    "He then turned towards the alley entrance."
    t "Hey, fellas! I've got someone who wants to play a game of tag with us!"
    $l_exp = "mad"
    "...{w}no."
    $l_exp = "rage"
    "I am sick and fucking tired of games."
    "While he was looking away, I quickly kicked straight up at him!"
    t "Ach!"
    "When my foot made contact with his crotch and he fell to the ground, I quickly stood up and ran out of the alley!"
    $l_exp = "mad"
    "Once out on the street, I looked and saw movement coming from my peripheral vision."
    $l_exp = "concerned"
    "The other REDD in the group were chasing after me!"
    $l_exp = "mad"
    "With no other option, I bolted in the opposite direction."
    play music escape
    "I could hear them behind me, their footsteps and laughter a fair distance away, but still close enough to where one slip-up can fuck me over."
    "I took a quick turn around the block, showing more empty streets, unless you count burning bodies on the sidewalks."
    $l_exp = "concerned"
    "A quick glance behind me showed they were still on my trail."
    "It's not gonna be easy to get away from them."
    $l_exp = "mad"
    "But I didn't come this far just to die now!"
    "I made another turn on the block, which was still very empty and devoid of life."
    $l_exp = "concerned"
    "But I did see one building up ahead that looked untouched."
    "The lights were even on and there seemed to be a good amount of people inside."
    $l_exp = "surprised"
    "As I ran closer, I could make out the sign on the building:"
    "{i}Frank's Bar{/i}"
    $l_exp = "excited"
    "Oh, my God! A Safehouse!!"
    "I felt myself sprint even faster as I thought about getting into a {b}proper{/b} Government Safehouse!"
    "I finally reached the front door and tried to open it."
    $l_exp = "surprised"
    extend " Only to reveal that it's locked."
    $l_exp = "concerned"
    "I guess that would make sense."
    $l_exp = "sad"
    play sound "audio/se/door pound.ogg" loop
    "I then knocked on the door as hard as I could."
    l "{b}PLEASE LET ME IN!!!{/b}"
    stop sound
    $l_exp = "surprised"
    "I stopped knocking when I could see a section along the top slide away, revealing a pair of eyes looking back at me."
    man "What's the password?"
    l "Password...?"
    man "The password to get in. What is it?"
    $l_exp = "shocked"
    "Oh, God... I read what it was earlier..."
    "What was it??{nw}"
    python:
        renpy.block_rollback()
        nicetry = True
        password = renpy.input("What was it??", allow=alpha, length=10)
    if not password:
        l "I-I don't know!"
    else:
        $password = password[0].upper() + password[1:len(password)].lower()
        l "[password]?"
        if password == "Martini":
            jump rightcode
        elif password == "Martinis":
            man "Eh. Close enough."
            jump rightcode

label wrongcode:
    man "Sorry, Miss."
    $l_exp = "sad"
    "He then slid the door hole shut!"
    play sound "audio/se/door pound.ogg" loop
    l "Wait!! Please!!"
    l "Let me--!!"
    $l_exp = "surprised"
    show blood4
    stop music
    play sound stab
    pause 2
    "I looked down and saw a blade sticking out of my gut."
    $l_exp = "shocked"
    "I then felt my head yanked back as a voice whispered in my ear:"
    $t_name = "REDD 1"
    t "You're it~"
    "The machete was then removed from my gut and placed along my neck."
    "Where they proceeded to slide it across."
    $quickhide = True
    hide screen laura
    window hide
    play sound blood
    if persistent.gore == '':
        show blood3
        with None
        scene bg blood
        with Dissolve(2.5)
        pause 0.5
    else:
        pause 3
    scene bg fade
    with Dissolve(2.0)
    pause 1.0
    if not persistent.achievements["memoryloss"]:
        $persistent.achievements["memoryloss"] = True
        $renpy.notify("Achievement Unlocked: {i}Memory Loss{/i}")
        $persistent.achievelist.append(1)
    $renpy.end_replay()
    jump gameover

label rightcode:
    $nicetry = False
    stop music fadeout(3.0)
    $l_exp = "excited"
    "I then heard the door unlock and it opened up!"
    l "Thank you, thank you, thank you!!!"
    "I almost knocked the guy over as I ran inside the bar."
    "As soon as I was in, he shut and locked the door behind me."
    $renpy.music.set_volume(0.5, channel="ambience")
    play ambience crowd fadein(0.5)
    scene bg bar with dissolve
    pause 0.1
    play music ten_past_midnight
    $l_exp = "neutral"
    "The bar was pretty packed, as to be expected, but it wasn't very claustrophobic."
    $l_exp = "surprised"
    "Especially compared to the back room in the theater."
    $l_exp = "concerned"
    "But what really surprised me was how calm everyone was, even after a random woman just rushed in here."
    "If I didn't know any better, I'd say this was just a normal night at a bar."
    $l_exp = "smile"
    "Though given my night so far, any sense of normalcy is good enough for me."
    "I found my way over to the counter area, where I found an empty stool to sit on."
    "Once I sat down, I felt so much pressure, physical and mental, release from my body."
    "I'm safe."
    "I'm alive."
    $l_exp = "neutral"
    "I'm {b}very{/b} tired."
    "I then rubbed my eyes and let out a giant yawn."
    $b_name = "Bartender"
    b "Long night?"
    $l_exp = "concerned"
    "I looked behind the counter to see a young bartender looking at me with a sly grin."
    $l_exp = "smug"
    l "You have no idea."
    b "Oh, given tonight's events, I'm sure I've got {b}some{/b} idea."
    b "What can I get ya?"
    "I then gave a small chuckle."
    l "No, thanks."
    b "You sure? We're having a REDD War special; everything's 75%% off."
    $l_exp = "surprised"
    l "Seriously? That sounds a bit excessive, don't you think?"
    b "Hey, it was Frank's idea, not mine. The way he sees it, if he's opening up his place to protect people from the chaos outside, the least he can do is offer them a fair amount for a drink."
    $l_exp = "concerned"
    l "Well, I guess that makes sense..."
    l "I think."
    menu:
        b "So? You want anything?"
        "\"Sure.\"":
            $gotdrink = True
            $l_exp = "smug"
            l "Eh, what the hell. Sure."
            "I'm not much of a drinker, but after this night, what have I got to lose?"
            "After I ordered and received my rum, the bartender walked towards another patron."
        "\"I'm fine.\"":
            $l_exp = "smug"
            l "Thanks, but I'm fine, really."
            b "Alright, then. But if you change your mind..."
            l "I got it."
            "He gave a friendly nod and walked towards another patron."
    $l_exp = "neutral"
    "I gave another yawn and felt my eyes get heavier."
    "I guess I've had a really long night so far."
    "A long, tiring, emotional night."
    "The REDD War is halfway over, and what have I got to show for it?"
    "A sore body, a dead husband, and two traumatized children."
    $l_exp = "surprised"
    stop ambience fadeout(3.0)
    stop music fadeout(3.0)
    "!!!"
    if gotdrink:
        "I nearly dropped my glass in shock!"
    $l_exp = "shocked"
    l "MY CHILDREN!!!"
    "Nearly every head in the bar turned towards me."
    $l_exp = "crying"
    play sound heartbeat loop
    l "O-Oh my God!!"
    l "I-I was so focused on escaping that I--!!"
    l "I can't believe I just--!!"
    "My breathing became heavier and heavier."
    "The bartender rushed over to me with a worried look."
    stop sound fadeout(3.0)
    b "Ma'am, are you okay?"
    l "My kids! I abandoned my kids!!"
    l "They're still trapped and alone!!"
    b "O-Okay, okay! Just breathe! Deep breaths!"
    b "Where are they at?"
    l "Th-The theater! Downtown!"
    "The bartender got a look of shock on his face. I even saw and heard a few people nearby talking among themselves."
    b "You mean the theater Mr. Sprinkles is killing people at?"
    $l_exp = "shocked"
    l "!!"
    l "Y-Yeah! How did--?"
    b "You kidding? It's all anyone's talking about!"
    "He then pulled out a TV remote from behind the counter and aimed it at the screen along the wall."
    scene bg fade
    show tvscreen
    with dissolve
    pause 0.1
    play sound "audio/se/tv.ogg"
    show bg flash with tvon
    show bg newsroom
    with Dissolve(0.1)
    pause 0.5
    "The first thing that appeared when it turned on was a live local news report where a photo of Mr. Sprinkles could be seen above the headline of {i}MR. SPRINKLES' MURDER SHOW SHOWS NO SIGNS OF STOPPING{/i}"
    hide screen laura
    hide tvscreen with dissolve
    pause 0.1
    play music neon_runner
    a "As the 2030 REDD War continues, we're seeing television icon Krag Dovason, more commonly known as Mr. Sprinkles, continuing his live television special."
    a "A special whose true intentions were kept a secret until it was too late for the audience members inside."
    a "As the body count rises to over one hundred, leaving many children witnessing many murders, some of which could have been their parents, it seems that Dovason shows no remorse for his actions nor signs that his show will stop before 7 AM."
    a "Many across the globe are wondering what would prompt the previously saint-like REDD to turn to these actions. Some speculate it was the mass protests and boycotts of his program, while others believe his kindness was all an act."
    a "Whatever the reason may be, you can view his live broadcast on the channel listed in your TV guide if you so wish."
    stop music fadeout(0.5)
    scene bg bar
    show screen laura
    with dissolve
    pause 0.1
    play music ten_past_midnight
    l "My God..."
    b "So you were really at the show the entire time?"
    l "Y-Yeah..."
    b "Then how the heck did you wind up here?"
    $l_exp = "sad"
    l "I-I escaped one of the games we were playing a little out of the way from here. {i}Mirror Madness{/i}."
    man "Holy shit!"
    "A man next to me stared at me with wide eyes."
    man "{b}You{/b} were the contestant who escaped that game?"
    l "Yeah. I was."
    "More murmurs from the bar."
    b "Well, you are one lucky lady, you know that?"
    $l_exp = "concerned"
    l "I don't feel lucky."
    b "You're alive after being caught in the REDD War, aren't ya?"
    $l_exp = "mad"
    l "Yeah, but does that really mean anything when you aren't protecting your family?"
    stop music fadeout(3.0)
    "I then got up off my stool."
    b "Where you going?"
    l "To save my daughters."
    "I then started walking away."
    b "Hold on a second!"
    $l_exp = "neutral"
    "I turned back to him."
    play music vast_places
    b "Look, I'm not gonna tell you what you can and can't do, but I am gonna make sure you're thinking logically about this."
    b "How old are your daughters? Really young, I take it?"
    l "...yeah. Both are younger than 10."
    b "None of the people that died there tonight are children, only adults. Which means for them, it's just as much of a Safehouse as this bar."
    b "And now you're here in a proper Safehouse, where you won't be hurt."
    b "Your daughters are safe. You're safe."
    b "Why would you wanna risk your life to save them from a danger that doesn't exist for them?"
    $l_exp = "rage"
    l "Because I don't want them to be there!"
    b "And what, you think they're just gonna let you take your girls right out the front door with no problems?"
    $l_exp = "mad"
    l "..."
    b "Believe me, as a parent, myself, I get it."
    b "You don't want them to be hurt. You don't want them to feel alone. If these were normal circumstances, I'd fully agree that you're making a great decision."
    b "But these aren't normal circumstances. You really think you can survive a trip back to the theater while the REDD War is going on?"
    $l_exp = "surprised"
    l "..."
    b "And believe me, at this point, any trauma and shock they're experiencing is fully cemented in them; there's nothing you can do about it now."
    $l_exp = "sad"
    "I could feel the tears coming up as I covered my mouth."
    b "I'm sorry, but my advice is to just stay here for the rest of the War."
    b "I think it's the best way for both you and your kids to survive. Understand?"
    "I took a deep breath before nodding."
    l "Yeah... I understand."
    "I slowly walked back to my barstool and stared at the counter."
    "He was right."
    "After watching many innocent people die right in front of them, including their own father, what more can I really protect them from?"
    if gotdrink:
        "I took my glass and gulped down the rest of my rum."
        l "Can I have another, please?"
    else:
        l "Can I have a rum, please?"
    b "Sure."
    hide screen laura
    window hide dissolve
    pause 1
    scene black
    with Dissolve(2.0)
    pause 1
    window show dissolve
    lt "Dakota, please know that you and Kate will see me again"
    lt "I know you have to wait longer than you want"
    lt "Believe me, I'd love to be right beside you right now"
    lt "But once this is all over, I'll be back for you"
    lt "I promise"
    window hide dissolve
    pause 1
    scene bg livestage
    show dakota sad hips at two1 zorder 2
    show kate mad fidget at two2 zorder 1
    with Dissolve(2.0)
    pause 1
    window show dissolve
    pause 0.1
    d "...Kate?"
    k "..."
    d "Kate, please don't ignore me."
    k "..."
    d mad crossed "What do you want from me, Kate?"
    d "Do you want me to say that you were right?"
    d "That Mom is never coming back?"
    k alert "..."
    d "Huh? Is that want you want??"
    k mad "..."
    d "Fine, then. You were right."
    d "Mom and Dad are both gone and they're never coming back."
    d "It's just us now."
    k alert "..."
    d sad hips "We only have each other left Kate."
    k mad "How do you know Mr. Sprinkles won't take you away from me, too?"
    d "..."
    d crossed "I guess I don't, but--"
    "Kate then crossed her arms and turned away from her sister."
    k "I hate Mr. Sprinkles."
    k "I hate how he took Mommy and Daddy away."
    k "I hate how you keep lying about how we'll be okay!"
    show dakota mad side
    "Dakota then grabbed her sister's shoulder and faced her towards her."
    d crying "Kate, listen."
    d "I'm the only person here who can feel what you're feeling about what happened to Mom and Dad."
    d "Believe me, I'm mad that Mr. Sprinkles did all of this, too!"
    d "I want Mom and Dad to come back just as much as you do!"
    d "But they're not going to, Kate! That much I know for sure!"
    d "I'm all you've got right now! So please don't act this way to me!"
    d "You can hate Mr. Sprinkles all you want, but please don't hate me!"
    k "..."
    d neutral "..."
    "Kate broke from Dakota's grip and turned back away from her."
    d bawl "..."
    show dakota:
        ease 0.5 middle
    hide kate with dissolve
    pause 0.1
    "Dakota felt even more tears fall down her face."
    d "Mom..."
    d "Dad..."
    d "I'm sorry I was such a jerk to you guys."
    d "This must be my punishment for acting that way."
    d "I don't know what I'm gonna do without you!"
    d "I wish you were here with me!"
    d "I don't want you to be gone!"
    d "I really don't..."
    call sceneend
    if not persistent.scenes["ch4_s2"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch4_s2"] = True


label goingback:
    python:
        currenttime = "2:34 AM"
        timeleft = "4 hours and 26 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    play music ten_past_midnight
    play ambience crowd
    scene bg bar
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    l "So that explosion really was just a coincidence?"
    b "Yep."
    b "The REDD who caused it even posted their view of the fall."
    b "Even said a while later that he was happy to add some 'excitement' to the show."
    b "If you want, I can show--"
    $l_exp = "mad"
    l "No. Seeing it once is enough."
    "I commented before taking another drink."
    b "Fair enough."
    $l_exp = "neutral"
    "I sighed and leaned back a bit."
    "I could certainly feel myself getting a bit woozy, but I at least had enough mental capability to think rationally."
    $l_exp = "concerned"
    "I think."
    b "You really do sound like you've had a bad night, Laura."
    $l_exp = "smile"
    l "Heh. Understatement of the fuckin' year."
    b "Well, at least your children are still alive, right?"
    b "And that they still have at least one of their parents around."
    $l_exp = "mad"
    l "Buddy, I know you're trying to be helpful, but can you please shut up?"
    b "...sure. My bad."
    $l_exp = "concerned"
    "Okay, so maybe the booze is affecting my behavior more than I thought."
    $l_exp = "mad"
    "But the last thing I need to be reminded about right now is my dead husband and abandoned children."
    $l_exp = "smug"
    "Which is why I need to do things like drink or talk about politics or dance topless on the karaoke stage."
    "..."
    $l_exp = "shocked"
    "...Geez, I {b}have{/b} had too much."
    $l_exp = "neutral"
    "I gave a soft groan and rested my head on the counter."
    l "I just want this night to be over."
    man "Don't we all, Lady."
    woman "Yeah, especially the people who are still trapped in the theater."
    woman "I wonder how many parents are left...?"
    man "Well, if Sprinkles really wants the show to last all night, he'll need enough to last 4 more hours."
    $l_exp = "mad"
    l "You sound like you're rooting for the bastard."
    man "I ain't. Just pointing out a fact."
    $l_exp = "concerned"
    l "Hm..."
    man "Actually, I wonder what the maniac's up to."
    man "Hey, bartender! Could you turn the TV to Mr. Sprinkles' broadcast?"
    $l_exp = "neutral"
    "The bartender paused before taking a quick glance at me, as if asking for my permission."
    "I just gave a small shrug in response."
    "With that, he pointed the remote at the TV and turned it on."
    stop music fadeout(1.0)
    scene bg fade
    show tvscreen zorder 3
    with dissolve
    pause 0.1
    play sound "audio/se/tv.ogg"
    show bg flash with tvon
    $renpy.music.set_volume(0.0, channel="music")
    $renpy.music.set_volume(1.0, channel="music2")
    stop ambience fadeout(0.75)
    play music2 sprinkles_radio fadein(0.75)
    play music sprinkles_theme fadein(0.75)
    show bg stage
    show sprinkles happy hat cane at two2_sprinkles zorder 2
    show madeline dead at two1 zorder 1
    with Dissolve(0.1)
    pause 0.1
    s "Where do writing utensils go for vacation?"
    s jeer "{i}I don't know!{/i}"
    s laugh "They go to {b}Pencil-vania{/b}!!"
    $l_exp = "concerned"
    "So nothing's changed, it seems."
    $renpy.music.set_volume(0.0, delay=0.5, channel="music2")
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    hide screen laura
    hide tvscreen with dissolve
    pause 0.1
    s jeer "What do you get when you mix a vampire with a snowman?"
    s "{i}Beats me, Mr. Sprinkles!{/i}"
    s laugh "You get {b}frostbite{/b}!"
    s @ jeer "{i}Golly, Mr. Sprinkles! You'd have to be really smart to figure that out, and I'm not smart in any way!{/i}"
    s "At least you're honest~!"
    s rightdown happy "Alright, we'll give you another break, Ms. Madeline."
    s laugh "Maybe you'll get them next time~!"
    s jeer hat "Though I seriously doubt it."
    hide madeline
    show sprinkles at middle_sprinkles
    with easeoutleft
    pause 0.1
    s rightdown happy "And if you've got a good memory, you may remember what comes after our jokes with Ms. Madeline!"
    s hat laugh "Let's give a big round of applause for Jessica~!"
    show sprinkles at two1 zorder 3 with easeinright
    show jessica full left_oneeye zorder 2:
        zoom 0.6
        xalign 1.75
        ease 1.5 two2_jessica
    pause 2
    $l_exp = "surprised"
    show screen laura
    pause 0.6
    "Jessica's certainly seen better days."
    $l_exp = "concerned"
    "I suppose we all have, but..."
    $l_exp = "sad"
    "She just looks like a wreck."
    s rightdown happy "Now, Jessica, I can tell you've had a bit of an eventful evening."
    s laugh "So I thought I'd give you a bit of a break from the fun and bring out {b}another{/b} guest!"
    s jeer hat "You can just sit and watch the fun."
    $l_exp = "concerned"
    "Another guest...?"
    $l_exp = "surprised"
    "My confusion didn't last too long; in a similar fashion to how Ms. Madeline's corpse was revealed hours ago, a large curtain was rolled onto the stage."
    $l_exp = "concerned"
    "Though I could see movement going on inside it, so at least it wasn't a dead body."
    show sprinkles:
        ease 0.5 left_sprinkles
    $l_exp = "surprised"
    "Mr. Sprinkles then walked over to the curtain and gave a small chuckle."
    s laugh "Ladies and gentlemen, let's meet our new special guest!"
    "He then yanked off the curtain, revealing the person inside."
    show jessica left_terror
    "It was a middle-aged man who was gagged and tied in a fashion similar to Jessica."
    $l_exp = "concerned"
    "Only instead of looking terrified, he looked pissed."
    $l_exp = "sad"
    "Though when Jessica looked at him, she looked even more scared than usual."
    "If that was even possible."
    $l_exp = "surprised"
    "Mr. Sprinkles then took the gag off the man."
    s rightdown happy "Can you please tell the audience your name?"
    man "Fuck you!"
    s jeer "Ahaha..."
    show sprinkles hm
    play sound snap
    "He then snapped his fingers and nodded offstage."
    "Almost instantly, Jingle and Jangle entered the stage with bats in their hands."
    show jingle zorder 1:
        offscreenright
        yalign 0.5
        linear 1.0 offscreenleft
    pause 0.1
    show jangle zorder 1:
        offscreenright
        yalign 0.5
        linear 1.0 offscreenleft
    pause 1
    play sound smack loop
    $l_exp = "sad"
    "And proceeded to start beating the shit out of the man!"
    "Cries of pain and some swears escaped his mouth as the mimes did their duty, with Jessica continuing to cry and to look terrified."
    s jeer hat "Alright, that should do it, fellas."
    stop sound
    "Jingle and Jangle stopped attacking the man and backed up a bit, but certainly looked ready to get back into the action if necessary."
    hide screen laura
    pause 0.6
    s rightdown "Let's try this again, Sir:"
    s "Can you please state your name?"
    "The man stared at Mr. Sprinkles with pure hatred before replying:"
    man "...Craig. Craig Tate."
    s huh "{i}Tate{/i}? As in Jessica Tate?"
    $b_name = "Craig"
    b "Yes... I'm her husband."
    $l_exp = "sad"
    s jeer hat "Well, well..."
    s evilgrin "What a small world we live in~!"
    $l_exp = "shocked"
    show screen laura
    $renpy.music.set_volume(1.0, delay=0.5, channel="music2")
    $renpy.music.set_volume(0.0, delay=0.5, channel="music")
    show tvscreen zorder 3 with dissolve
    pause 0.1
    "Holy shit...!"
    "I couldn't help but stare at the screen in disbelief."
    "It's one thing to take out your anger and frustrations on the one who wronged you."
    $l_exp = "surprised"
    "But to take it out on someone close to them for the sake of getting even?"
    $l_exp = "mad"
    "That's just..."
    $l_exp = "concerned"
    "Hypocritical, actually."
    $l_exp = "neutral"
    "Unless this is some sort of 'using your methods against you' shtick."
    $l_exp = "mad"
    "Still, this is wrong on so many levels."
    $l_exp = "neutral"
    "Well, I guess this whole event is, to be fair..."
    $renpy.music.set_volume(0.0, delay=0.5, channel="music2")
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    hide tvscreen with dissolve
    pause 0.1
    s jeer rightdown "Jessica, do you have any comments to make?"
    $l_exp = "surprised"
    show jessica screaming
    "She tried her best to speak through her gag, but it was all mumbled nonsense."
    "The screams and cries were pretty easy to understand, though."
    s @ hm "Hm. I guess not."
    "He then nodded to the twins, who dropped their bats and went offstage."
    show jangle:
        linear 1.0 offscreenright
    pause 0.1
    show jingle zorder 1:
        linear 1.0 offscreenright
    pause 1
    hide screen laura
    pause 0.6
    show jessica left_oneeye
    b "You're a goddamn monster, you know that??"
    b "You're evil! Pure evil!! All you fucking REDD are!!"
    s wut "Sir, with all due respect, can you please watch your language?"
    s jeer hat "There are children present, after all~"
    b "Like you give a fucking shit about children, you cocksucking--!"
    s wut "Ah-ah-ah! That's the sort of thing I'm talking about!"
    s hm rightdown "Dear me, and they say {b}children{/b} are the ones who have no respect..."
    s hat jeer "Oh, well. I suppose this can be a good thing."
    s evilgrin "It'll make what's to come a lot more enjoyable."
    s laugh "After all, everyone loves to see the bad guy get their comeuppance~!"
    b "Bad guy?? Comeuppance?? What are you talking about?!"
    b "I didn't do shit!!"
    s rightdown hm "I beg to differ, Mr. Tate."
    s "Your prejudice towards my species was perfectly demonstrated less than a minute ago."
    s hat jeer "The truth is I've met my fair share of REDD who are kind, loving individuals."
    s @ laugh "In fact, I used to be such a REDD, myself!"
    s "But I believe there's a saying you humans have: Anyone can change."
    s evilgrin "For better {b}or{/b} worse."
    stop music fadeout(3.0)
    stop music2 fadeout(3.0)
    show screen laura
    pause 0.6
    "Jingle and Jangle then entered the stage again, only instead of holding bats..."
    $l_exp = "sad"
    "...Jingle was holding a gas can and Jangle was holding a book of matches!"
    play music sprinkles_spooky
    s rightdown happy "Alright, then; let's have ourselves a grand ol' time, shall we?"
    s "And what better way to celebrate tonight than a good old-fashioned bonfire?"
    s huh "Though I seem to have misplaced my firewood..."
    s hat evilgrin "I suppose I'll just have to improvise a bit~!"
    "Jingle then began pouring gasoline all over Craig!"
    "She seemed careful as to not spread it around too much to where the whole stage is coated in it, but Craig's flailing didn't seem to be doing her any favors."
    $l_exp = "surprised"
    show jessica terror:
        linear 0.1 xalign 0.805
        block:
            linear 0.2 xalign 0.795
            linear 0.2 xalign 0.805
            repeat
    "As she did, Jessica continued to scream and cry, doing her best to move and jiggle around her chair in an attempt to escape, but it was no use."
    "Finally, Jingle stopped pouring the gas and backed up far to the other side of the stage."
    "Jangle handed Mr. Sprinkles the box of matches and went on to join his twin."
    show jessica left_oneeye:
        linear 0.1 two2_jessica
    hide screen laura
    pause 0.6
    s jeer leftdown "I should warn you now that the room might just get a little toasty for everyone in the front row."
    s evilgrin "And especially a certain someone on stage!"
    b "You really think you're gonna get away with this??"
    stop music fadeout(3.0)
    s wut "..."
    s jeer "My, my, my. I do believe my helpers have beaten you a little {b}too{/b} hard!"
    s rightdown laugh "For I'm afraid you seem to have forgotten what day it is!"
    s jeer "If this were any other situation, then no. I would never get away with this."
    s "But you see, Mr. Tate..."
    extend hat evilgrin " this is the exact time, day, and location where I {b}will{/b} get away with this!"
    b "Heh. L-Lucky you, then."
    $l_exp = "surprised"
    show screen laura
    pause 0.6
    "Craig looked his damned best to not let Sprinkles see how scared he was."
    s jeer "Yes, I suppose you could say that."
    b "And what the fuck are you going to get out of this?? Huh?? Nobody is going to love you afterwards! Millions of people hate you right now!!"
    b "When the REDD War is over, your show will be finished! Your career will be finished! Nobody will ever love you again!"
    s rightdown hm "You know, I'm not one to throw around insults."
    s jeer "But if you're really going to insult the REDD who literally has the fate of your life in his hands..."
    extend evilgrin " then you're the biggest moron on the face of the planet!"
    $l_exp = "sad"
    "He then lit a match and threw it at Craig."
    $l_exp = "shocked"
    play sound fire_start
    queue sound fire loop
    show fire zorder 3
    pause 0.2
    play sound2 children_screaming
    play ambience crowd_screaming
    show sprinkles laugh
    show jessica left_oneeye
    pause 1
    "Almost instantly, the room went into chaos as the audience, Craig, and Jessica all screamed in horror while Mr. Sprinkles laughed."
    "Craig flailed around, the camera not being shy from zooming in on his burning body."
    show jessica screaming
    "It then panned to Jessica, who looked just absolutely hurt in every way possible, screaming as loud as she could through her gag, the tears seeming to flow down her eye, all while seemingly trying to reach out and grab her husband."
    $l_exp = "crying"
    "As I stared at the poor woman, I could feel my own eyes starting to well up."
    "At least when I watched Richard die, it was a quick and painless death."
    "But this... being burned alive..."
    $l_exp = "surprised"
    stop ambience
    stop sound2
    play sound "audio/se/tv.ogg"
    scene bg flash
    with Dissolve(0.1)
    scene bg fade with tvoff
    pause 1
    scene bg bar with dissolve
    pause 0.1
    "Everyone seemed to unanimously turn towards the bartender, who was pointing the remote at the now-off TV."
    $b_name = "Bartender"
    b "If anyone wants to keep watching the show, do it on your phone."
    "With that, he put the remote back behind the counter and the general chatter commenced."
    $l_exp = "sad"
    play music ten_past_midnight fadein(1.0)
    play ambience crowd fadein(1.0)
    "I wiped my eyes and slowly shook my head."
    b "You okay?"
    "I gave a weak shrug."
    l "I'm just sick and tired of watching people get hurt."
    man "Ah, it's not so bad. That bitch Jessica deserves it, after all!"
    $l_exp = "mad"
    "My face jolted towards the man next to me."
    l "How do you figure?"
    man "That bitch wouldn't shut the fuck up about how bad the REDD are. You mess with the bull, you'll eventually get the horns."
    $l_exp = "rage"
    l "That doesn't fucking matter! You shouldn't torture someone because you don't like what the fuck they're saying!"
    stop music fadeout(3.0)
    $renpy.music.set_volume(0.5, delay=3, channel="ambience")
    "Even I could notice how loud I was getting, but I couldn't control myself."
    man "Okay, easy there, Tiger. No need to get snippy."
    $l_exp = "mad"
    l "Oh, I'm not snippy! I'm just pointing out how you're a fucking monster!"
    man "Me? A monster?"
    man "Okay, I think someone's had a bit too much~"
    "A few people nearby laughed at his comment."
    $l_exp = "rage"
    "I then got off my stool and leaned in closer to his big ugly face."
    l "I don't care who she is or what she's done! She's just as human as you and me!"
    $l_exp = "angry"
    l "And {b}nobody{/b}, not even her, deserves to go through what she's going through!"
    l "We, as a species, are better than that!"
    l "And if you can't see that, if you really think it's funny that another person is being mutilated and tortured, then you are literally no better than a goddamn REDD!"
    stop ambience fadeout(1)
    "Some collective 'Oooo!'s could be heard."
    "The man just stared at me with what looked like anger and fear."
    $l_exp = "mad"
    "I then backed up and sat back on my stool."
    "When I did, the man got off his stool and walked away."
    play music ten_past_midnight fadein(3.0)
    $l_exp = "surprised"
    "I groaned and covered my face with my hands."
    l "I really have had too much, haven't I...?"
    "I asked to nobody in particular."
    b "You weren't wrong, though."
    $l_exp = "concerned"
    "I looked and saw the bartender looking at me with a smirk."
    b "It's why Frank turned the place into a Safehouse: he feels that nobody should have to be hurt in this city tonight."
    $l_exp = "neutral"
    l "Well, good on him, I suppose."
    "I looked down at my empty glass and sighed."
    $l_exp = "surprised"
    "The REDD War has done nothing but make the lives of all the humans in Atlanta worse."
    $l_exp = "concerned"
    "But in a fucked-up way, it's also brought us closer together as a species."
    "After all, nothing seems to make humans bond more than pointing out how much something sucks ass."
    $l_exp = "neutral"
    "But what can I do about it?"
    "I'm just one person against hundreds, if not thousands, of REDD."
    "..."
    stop music fadeout(3.0)
    $l_exp = "mad"
    "You know what?"
    "If I don't do it, who will?"
    $l_exp = "concerned"
    l "Excuse me?"
    "I asked as I waved at the bartender, who turned to and approached me."
    b "Yes?"
    l "I'd like to pay my tab."
    b "Hey, if you're done for the night because of what you said--"
    $l_exp = "neutral"
    l "That's not it. I'm leaving."
    b "I beg your pardon?"
    l "I'm leaving the bar and going back out there."
    "He stared at me for a second before sighing."
    b "Well, like I said, I'm not gonna tell you what you can and can't do."
    b "But can I least ask why you wanna leave?"
    $l_exp = "concerned"
    l "Because someone needs to stop Mr. Sprinkles."
    "He gave a small smile, trying to hold back his laughter, but he quickly regained his composure."
    b "And you, uh, are gonna do that how, exactly? Just walk right up to him and tell him to stop?"
    $l_exp = "mad"
    l "If you're going to mock me, I'll happily walk out of here without paying."
    b "Ah, sorry."
    $l_exp = "neutral"
    "He then gave me my total, which I then paid."
    "With that, I got off my stool."
    b "Hey, Laura?"
    $l_exp = "concerned"
    "I turned towards him."
    play music autumn_changes
    b "I'm not fully sure I know why you're doing this or if you'll succeed..."
    b "But just know that I'm rooting for ya."
    l "Is that right?"
    b "Oh, don't get me wrong: I think going back out there with no weapons while intoxicated is the stupidest thing one can do."
    b "But you've got guts, Laura. I can see that."
    b "Plus, if you actually put an end to the show, I can be known as the bartender that served the great Laura..."
    b "Uh..."
    $l_exp = "smug"
    l "Farr."
    b "The great Laura Farr!"
    "I rolled my eyes and crossed my arms."
    l "You done?"
    b "..."
    b "Not exactly."
    $l_exp = "concerned"
    "He then reached into his pocket and pulled out a set of keys."
    b "Here. There's a pickup parked at the back of the bar. Take it to the theater."
    $l_exp = "wut"
    l "...!"
    l "You're seriously giving me your vehicle?"
    b "Do you not want it?"
    $l_exp = "concerned"
    l "Well, it's just..."
    l "Why would you do that?"
    b "It's like I said: I'm rooting for ya."
    b "I'm just giving you a little help, that's all."
    $l_exp = "neutral"
    "..."
    $l_exp = "smile"
    "I walked back over to him and took the keys."
    l "Thank you. I mean it."
    b "Don't worry about it. I hope you succeed."
    b "Or at the very least, don't die."
    $l_exp = "smug"
    l "I'll do my best."
    $l_exp = "surprised"
    l "But aren't you worried about your truck getting destroyed or something?"
    b "It's insured. To be frank, I've actually been praying that it {b}does{/b} get destroyed so I can be rid of it and get a new one!"
    $l_exp = "excited"
    "I couldn't help but let out a snicker."
    "That must be the alcohol reacting."
    b "But if it's still working by the time the War ends, it's yours."
    $l_exp = "smile"
    l "Oh, you don't need to go that far; I've got no need for it after sunrise."
    b "Then you can leave it wherever."
    l "Alright, if you say so..."
    $l_exp = "excited"
    l "Well, thanks again; I really appreciate it!"
    b "Take care of yourself, Laura."
    $l_exp = "determined"
    "I nodded and walked towards the back exit of the bar."
    scene bg street with dissolve
    pause 0.1
    "After finding the pickup and getting in, I locked the doors and took a deep breath."
    $l_exp = "surprised"
    "Am I really about to do this?"
    "Am I really about to head back to the theater where I was held prisoner most of the night?"
    "Just to try and stop a madman and save innocent lives?"
    "..."
    $l_exp = "determined"
    "Of course I am."
    play sound "audio/se/truck start.ogg"
    call sceneend
    if not persistent.scenes["ch4_s3"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch4_s3"] = True
    jump chapter_5
