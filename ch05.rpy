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
    extend "...and never be out of sight and first up in the next game."
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
