label chapter_3:
    python:
        currenttime = "7:09 PM"
        currentdate = "March 31st"
        timeleft = "11 hours and 51 minutes"
        event = "REDD War ends"
        save_name = "Chapter 3"
        save_subtitle = "The Storm Arrives"
        l_exp = "neutral"
    stop music
    call chaptername
    call chapterstart
    pause 1
    play music classy_ghouls
    scene bg storage
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
    show screen laura
    with dissolve
    pause 0.1
    
