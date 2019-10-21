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
    "After a while, I took out my phone."
    $l_exp = "surprised"
    "No new messages from Dakota."
    "That didn't stop me from sending another text."
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
                if not persistent.achievement_rattrap:
                    $persistent.achievement_rattrap = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievetotal += 1
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
                if not persistent.achievement_rattrap:
                    $persistent.achievement_rattrap = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievetotal += 1
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
                if not persistent.achievement_rattrap:
                    $persistent.achievement_rattrap = True
                    $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                    $persistent.achievetotal += 1
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
            if not persistent.achievement_rattrap:
                $persistent.achievement_rattrap = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievetotal += 1
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
            if not persistent.achievement_rattrap:
                $persistent.achievement_rattrap = True
                $renpy.notify("Achievement Unlocked: {i}Rat Trap{/i}")
                $persistent.achievetotal += 1
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
            window hide dissolve
            pause 1
            scene bg fade
            with Dissolve(2.0)
            pause 4
            $renpy.end_replay()
            if not persistent.chapter4_scene1:
                $persistent.scenetotal += 1
            $persistent.chapter4_scene1 = True


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
    play sound "se/woman scream.ogg"
    pause 2
    show screen laura
    window show dissolve
    pause 0.1
    "A woman's scream could be heard around the corner, as well as laughter from multiple people."
    "A second later, I could see her sprint across the alley entrance, with 3 or 4 REDD coming after her with bat, machetes, and other weapons of the sort."
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
    $renpy.pause() # Car crash SE
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
