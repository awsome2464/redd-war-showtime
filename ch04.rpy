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

    I'd have to be fucking wizard to figure that shit out.
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
