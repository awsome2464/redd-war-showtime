label chapter_3:
    python:
        currenttime = "7:14 PM"
        timeleft = "11 hours and 46 minutes"
        event = "REDD War ends"
        save_name = "Chapter 3"
        save_subtitle = "The Storm Arrives"
        l_exp = "excited"
    stop music
    call chaptername
    call chapterstart
    pause 1
    play music classy_ghouls
    scene bg storage
    with Dissolve(2.0)
    pause 0.5
    nvl clear
    nvl show dissolve
    narrate """
    We were led to a back area behind the stage.

    Fortunately, nobody was shot on the way over.
    
    Well, at least in the building.

    We could hear gunshots and rioting outside of the building, all unrelated REDD War activities.
    
    Ironic. We came here to {b}avoid{/b} being treated like the humans out there.

    I guess the REDD War truly is unpredictable.

    {clear}

    There were several hundred of us total, so we were divided up into different rooms.
    
    They weren't really basing it on anything specific; it was just filling up a room until it got full, then going to the next one.

    Or maybe there are specifics and we just can't see them.

    Then again, the REDD aren't really known for having specific biases.

    If you're a human, you may as well be an ant under their magnifying glass.

    Though despite all this, I'm grateful for one thing:
    """
    $nvl = False
    window show
    nvl hide
    show screen laura
    with dissolve
    pause 0.1
    show richard concerned at middle_r with dissolve
    pause 0.1
    "Richard and I were together."
    "Despite everything, at least we had each other."
    $l_exp = "sad"
    "At least, for now..."
    redd "Alright, everybody pay attention! And no funny business!"
    $l_exp = "neutral"
    "We get the idea, tough guy."
    stop music fadeout(3)
    play sound door_open
    "The door opened up, revealing the REDD himself."
    hide richard with dissolve
    play music sprinkles_spooky
    show sprinkles laugh at middle_s with dissolve
    pause 0.1
    s "Well, hello, everyone~!"
    s jeer "First off, I do wish to apologize."
    s "As you've probably figured out by now, we are, in fact, {b}not{/b} in an officially recognized Government Safehouse."
    s "I know I told you, as well as the whole world, that it was, but..."
    s evilgrin "...I don't believe anyone in their right mind would willingly come here if they knew the truth."
    s laugh "So do forgive me for this little fib."
    man "\'Little fib?!\'"
    $l_exp = "surprised"
    "One of the guards then raised their guns."
    "That seemed to shut the man up."
    show sprinkles hm
    "Mr. Sprinkles then raised his hand towards the guard."
    s "Easy there."
    s evilgrin "We wanna make sure we have enough volunteers to last us the whole night."
    $l_exp = "mad"
    "{i}\'Volunteers\'{/i} isn't the word I'd use."
    s happy "It's safe to assume you all have a basic understanding of how my show works, so I'll spare you the rundown."
    s "Instead, I'll cut right to the point:"
    s jeer "Whether or not you live to see your children again is entirely up to you."
    $l_exp = "sad"
    s laugh "If you cooperate and be a good sport, you'll be given the chance to participate in one of the many games we have planned tonight!"
    s happy "Although compared to the games from the television show, these games are a lot less..."
    s evilgrin "...safe."
    s laugh "But they're not impossible, I assure you~"
    s "You just have to play the games to the best of your abilities."
    s "If you win, you keep your life!"
    s "If you lose..."
    s jeer "Well, I'm sure you can finish that sentence."
    s happy "But don't forget that this is still a show~!"
    s "A show that the entire world is watching!"
    s jeer "Not to put you under any unneeded stress, of course...~"
    s happy "So just remember to have fun!"
    s laugh "Ooo, this is just going to be a fantastic night, I can tell~!"
    s @ jeer "Anyway, just sit back and behave yourselves; we'll get you when we're ready for you."
    s "In the meantime, you can watch the show from the screen we have set up here!"
    "As he said that, he gestured towards a flat-screen TV along the back wall, which was currently displaying a \'We\'ll Be Right Back!\' message."
    s happy "Well, that's it for now!"
    s evilgrin "Enjoy your night~"
    "He then turned around and started walking towards the door."
    woman "Why are you doing this??"
    show sprinkles wut
    "He stopped in his tracks."
    "Everyone looked towards the woman, who tried to look confident, but mostly just looked scared."
    woman "Why would you do all this to those who trusted you?!"
    s "..."
    show sprinkles jeer
    "He then turned his head back towards her with a sly grin."
    s "Because I can."
    stop music fadeout(3)
    hide sprinkles
    with Dissolve(2)
    $l_exp = "neutral"
    "He then exited the room and closed the door behind him."
    "The guards looking over us then got back in position, with one in front of the door and the other 4 in one of the room's corners."
    $l_exp = "sad"
    "The room was uncomfortably silent."
    "Everyone just looked at each other with terror in their faces."
    "What else could we do?"
    "You know, that wouldn't end with getting killed?"
    $l_exp = "concerned"
    "Suddenly, the TV changed to a live feed of the stage."
    play music sprinkles_theme
    hide screen laura
    scene bg stage
    show sprinkles laugh at middle_s
    with dissolve
    pause 0.1
    s "Thank you for your patience, everyone!"
    s happy "To start this show properly, I would like to bring out a special guest who will be joining us throughout the evening!"
    s "Please give a big round of applause to our guest..."
    s laugh "...Jessica Tate!"
    hide sprinkles with dissolve
    pause 0.5
    show jessica:
        offscreenright
        ease 1.5 middle
    # She's strapped to a chair, her arms and legs tied the chair's arms and legs and her head tied across her forehead so she's looking forward. She's also had her mouth gagged.
    pause 2
    $l_exp = "surprised"
    show screen laura
    "Oh, my God!"
    "She looked just as terrified as the rest of us, but given her current situation, I'm sure she's even more so."
    hide screen laura
    show jessica zorder 2:
        ease 0.5 two2
    show sprinkles happy at two1_s zorder 1 with dissolve
    pause 0.1
    s "I must say it's finally nice to meet you, Mrs. Tate!"
    show sprinkles jeer
    "{color=#d00000}Mr. Sprinkles{/color}" "\"I do wish it was under different circumstances,{nw}"
    s laugh "I do wish it was under different circumstances,{fast} but better late than never, I always say~!"
    "He then wrapped his arm around her shoulder and leaned in towards her as he grinned at the camera."
    s happy "Now, there's a chance that some of you might not have heard of Jessica Tate, so allow me to explain:"
    s "You see, Jessica here..."
    s hm "...doesn't like me very much."
    s laugh "But that's okay! It really is!"
    s happy "After all, everyone feels different ways about different people, and there's nothing you can do to change that."
    s "So, tonight, I brought Jessica onto the show to teach you all an important lesson:"
    s "While it's okay to dislike someone for a reason only you can understand..."
    s hm "...it's never okay to use that disliking to harm that person. If you do..."
    s evilgrin "...you might just have some very bad things happen to you in return."
    s laugh "Here, Jessica. Why don't we show the folks at home what I mean?"
    "Jessica then started giving some screams through her gag, and her eyes started darting side to side, almost as if she were trying to shake her head."
    s happy "Don't worry. I won't be too harsh."
    s evilgrin "...yet."
    "On cue, Jingle skipped onto the stage and handed Mr. Sprinkles an aluminum baseball bat."
    "After he accepted the gift, she gave a small curtsy and skipped back off."
    $l_exp = "concerned"
    show screen laura
    "...so, Jingle and presumably Jangle are in on this?"
    $l_exp = "neutral"
    "I mean, they're REDD, as well, so I guess I shouldn't be too surprised, given the circumstances..."
    hide screen laura
    s hm "Now, Jessica, despite everything that's happened tonight, I'm not going to lie to you."
    s "What's about to happen right now..."
    s evilgrin "...if gonna hurt a lot."
    "He then wound up the bat..."
    play sound smack
    "And smacked Jessica right in the face with it!"
    "She cried out in pain, but her gag muffled the noise."
