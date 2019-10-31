label chapter_5:
    python:
        save_name = "Chapter 5"
        save_subtitle = "Facing the Storm"
    call chaptername
label backattheater:
    python:
        currenttime = "3:12 AM"
        timeleft = "3 hours and 48 minutes"
        l_exp = "mad"
    call chapterstart
    pause 2
    play music into_the_haunted_forest
    scene bg theater_ext
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    "I finally made my way back to the theater."
    $l_exp = "concerned"
    "Admittedly, I'm a bit surprised, given my recent drinking endeavors."
    $l_exp = "mad"
    "Regardless, I'm back and ready to get in and stop this."
    "..."
    $l_exp = "concerned"
    "..."
    "Although I suppose answering the question of \"How?\" would be a good idea."
    $l_exp = "neutral"
    "I stared out the truck's windshield in thought."
    "They're not just gonna let me waltz right in the front door, I wouldn't think."
    $l_exp = "surprised"
    "I suppose if they didn't shoot me, they could just take me back to the back room where I was before..."
    $l_exp = "neutral"
    extend " and never be out of sight and first up in the next game."
    "Yeah, that's out."
    $l_exp = "surprised"
    "That's when I could see a large vehicle similar to the one that took me to the Mirror Madness maze."
    "It was headed towards the theater, and by extension, me!"
    "I quickly pulled my seat back and laid as flat as I could."
    "A second or so passed before I could hear it drive past me."
    $l_exp = "concerned"
    "After slowly lifting the seat back up, I saw the vehicle pull around to the back of the theater and stop."
    "Was it taking more people out to a game?"
    $l_exp = "neutral"
    "I sat there and waited for a minute before the vehicle pulled away."
    $l_exp = "surprised"
    "There certainly seemed to be a good amount of people in there..."
    "I have really got to find a way inside."
    "..."
    $l_exp = "concerned"
    "Wait a minute...! The back door!"
    $l_exp = "determined"
    "I took a deep breath before exiting the pickup and making my way to the back of the theater."
    scene bg alley with dissolve
    pause 0.1
    "Thankfully, there weren't any REDD guards back here."
    $l_exp = "surprised"
    "Though the other side of the door may be another thing entirely."
    "I tried remembering that time I left this way to go to the maze, if there were any REDD guards by the door that {b}weren't{/b} the ones dragging us away."
    "But try as I might, I couldn't remember. That whole situation was a blur."
    $l_exp = "mad"
    "Well, here goes..."
    "I reached for the handle..."
    play sound "audio/se/locked door.ogg"
    pause 0.75
    $l_exp = "concerned"
    extend " and discovered it was locked."
    $l_exp = "neutral"
    "I guess I figured it couldn't have been that easy."
    play sound footsteps
    $l_exp = "surprised"
    "That's when I heard footsteps approach the door from the inside!"
    "Shit! They must've heard me try to open it!"
    "I ducked a bit to the side so I was right against the back corner of the alley."
    play sound door_open
    "The door opened with a REDD guard in full body armor walking out of the building and towards the opening of the alley, not turning back at all towards me."
    $l_exp = "neutral"
    "He then took off his helmet and pulled out what seemed to be a pack of cigarettes."
    $l_exp = "concerned"
    "As he walked, the door slowly shut behind him."
    $l_exp = "excited"
    "This could be my chance!"
    "I slowly approached the door, making sure to make as little noise as I could."
    $l_exp = "surprised"
    redd "Shit..."
    "He was patting his side pocket, clearly looking for something."
    "He was also turning around to head back into the alley!"
    $l_exp = "sad"
    "I quickly picked up the pace to try and make it in."
    extend ".. but the door fully shut by the time I could get to it!"
    redd "Hey!!"
    stop music fadeout(3.0)
    $l_exp = "surprised"
    "Fuck!"
    "He had his gun pulled out and pointed at me."
    redd "Stay right where you are! Move a muscle and I shoot!"
    "I obeyed his commands as he slowly approached me."
    redd "And just what do you think you're doing?"
    "I just stared at him, trying to think of any way to get out of this."
    $l_exp = "concerned"
    "Out of the corner of my eye, I saw some wooden planks leaning against a dumpster."
    "They looked pretty thick, but I couldn't tell without turning my head."
    $l_exp = "surprised"
    redd "I asked you a question, bitch!"
    "He told me as he moved his gun closer to me."
    $l_exp = "concerned"
    "This might be the oldest and stupidest trick in the book, but I'm low on options."
    $l_exp = "surprised"
    "I looked past his shoulder towards the alley entrance for a quick moment before widening my eyes."
    l "{b}OH MY GOD!!{/b}"
    "The guard quickly turned around and pointed his gun at the alley entrance."
    $l_exp = "determined"
    "I quickly grabbed a wooden plank and swung it at his head!"
    play sound impact
    "He let out a grunt before collapsing onto the ground."
    $l_exp = "neutral"
    extend " And didn't move."
    "..."
    $l_exp = "excited"
    "Well, I guess that's one problem solved."
    $l_exp = "concerned"
    play music into_the_haunted_forest
    "So now back to the original problem of how I'm going to get in..."
    "I don't think I can just sit and wait for another guard to come out."
    $l_exp = "surprised"
    "Although, he had to have had a way to get back in, himself, right...?"
    "I approached the REDD and searched around for anything that might be of use."
    $l_exp = "smug"
    "After feeling inside his pockets, I found a key!"
    "I approached the back door and was about to unlock it."
    $l_exp = "surprised"
    "But then I realized something."
    $l_exp = "concerned"
    "If a human waltzed right in and another REDD guard was there..."
    "..."
    $l_exp = "surprised"
    "I turned towards the unconscious REDD guard."
    "Surely it can't be this simple."
    stop music fadeout(3.0)
    hide screen laura
    window hide dissolve
    pause 0.1
    scene bg basement_hall
    with Fade(0.5, 1.0, 0.5)
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    As I looked through the mask and saw a REDD guard walk past me without even turning to face me, I gave a small smile to myself.

    It really was that simple.
    """
    play music classy_ghouls
    narrate """
    {nw}

    Now that I'm in, I must admit I'm a bit stuck on where to go from here.

    Or what to even do.

    In hindsight, this is very much one of those plans where every step should have been decided ahead of time.

    Then again, even the best plans can be affected by REDD War shenanigans.
    """
