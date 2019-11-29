label chapter_5:
    python:
        save_name = "Chapter 5"
        save_subtitle = "Stopping the Storm"
    call chaptername
label backattheater:
    python:
        currenttime = "3:12 AM"
        timeleft = "3 hours and 48 minutes"
        l_exp = "determined"
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
    $l_exp = "sad"
    "I have really got to find a way inside."
    "..."
    $l_exp = "surprised"
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
    play sound door_locked
    pause 0.75
    $l_exp = "concerned"
    extend " and discovered it was locked."
    $l_exp = "neutral"
    "I guess I figured it couldn't have been that easy."
    play sound footsteps
    $l_exp = "surprised"
    "That's when I heard footsteps approach the door from the inside!"
    $l_exp = "sad"
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
    $l_exp = "shocked"
    l "{b}OH MY GOD!!{/b}"
    "The guard quickly turned around and pointed his gun at the alley entrance."
    $l_exp = "mad"
    "I quickly grabbed a wooden plank and swung it at his head!"
    play sound impact
    "He let out a grunt before collapsing onto the ground."
    $l_exp = "neutral"
    extend " And didn't move."
    "..."
    $l_exp = "smug"
    "Well, I guess that's one problem solved."
    $l_exp = "concerned"
    play music into_the_haunted_forest
    "So now back to the original problem of how I'm going to get in..."
    "I don't think I can just sit and wait for another guard to come out."
    $l_exp = "surprised"
    "Although, he had to have had a way to get back in, himself, right...?"
    "I approached the REDD and searched around for anything that might be of use."
    $l_exp = "excited"
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
    pause 0.5
    scene bg basement_hall
    show helmet zorder 3
    with Fade(1.0, 1.0, 1.0)
    pause 0.5
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

    Alright, my first priority is to find Jessica.

    But where would she be, I wonder...

    In hindsight, this is very much one of those plans where every step should have been decided ahead of time.

    Then again, even the best plans can be affected by REDD War shenanigans.


    The back of this theater is pretty big and maze-like, and I can't just ask someone where she is.

    Unless they're stupid enough to think a REDD has the voice of a human.
    """
    $nvl = False
    nvl hide
    window show
    redd "C'mon, pick up the pace!"
    show screen laura
    pause 0.6
    "I turned around, only to see a REDD walking towards me."
    "Specifically, Jangle."
    $l_exp = "concerned"
    "He didn't appear to be talking to me, though; he was looking behind him, where Jingle could be seen."
    $l_exp = "sad"
    "Together, they were both carrying a dead body down the hall."
    show jangle down stern at two1
    show jingle down confused at two2
    with dissolve
    pause 0.1
    ji "Hey, maybe you shouldn't have given me the heavy side!"
    ja angry "Oh, boo-hoo! Suck it up, will ya?"
    $l_exp = "shocked"
    "I can't tell what's more surprising: the fact that they're talking or the fact that they're arguing."
    "..."
    $l_exp = "concerned"
    "Yeah, hearing them talk is weirding me out more."
    $l_exp = "neutral"
    "They then approached me, but neither seemed to pay me any mind."
    "They just carried the body past me, grumbling and complaining to each other as they did."
    hide jingle
    hide jangle
    with dissolve
    pause 0.1
    s "Ahaha! I hope to see you all back here in 15 minutes!"
    $l_exp = "shocked"
    "I wasn't even aware I was that close to the stage."
    $l_exp = "neutral"
    show sprinkles jeer rightdown cane at two1 with dissolve
    pause 0.1
    "Mr. Sprinkles then appeared in view and walked by me."
    "Didn't even bat an eye."
    $l_exp = "concerned"
    "Am I really that invisible?"
    hide sprinkles with dissolve
    pause 0.1
    $l_exp = "neutral"
    "He entered a nearby room and closed the door most of the way."
    $l_exp = "concerned"
    "He appeared to be taking out a phone as he did."
    "Well, at least he's not a threat right now."
    "This seems like a good chance to try and find Jessica."
    $l_exp = "neutral"
    "I then started to walk away."
    s "Hello, Mr. Reddington!"
    $l_exp = "surprised"
    "I froze."
    "Did he just say...?"
    s "A-Ah, yes, of course. {b}Lord{/b} Reddington. My apologies."
    $l_exp = "concerned"
    "Why is Krag Dovason talking to the leader of the REDD?"
    "Curious, I approached the door and listened in."
    $s_name = "Krag"
    hide screen laura
    scene bg dressingroom
    show sprinkles jeer rightdown leftdown at middle_sprinkles
    with dissolve
    pause 0.1
    play music sprinkles_spooky
    s "I assume you're satisfied with what I've presented so far?"
    "..."
    s laugh "Ahaha! I'm glad to hear it!"
    "..."
    s jeer "Bad? Why would I feel bad?"
    s evilgrin "I'm a REDD, after all!"
    "..."
    s laugh hat "Oh, good! I wasn't sure how well that would go over with audiences."
    s evilgrin "But I guess even the REDD love a good pun every now and then~"
    "..."
    s jeer rightdown "Oh, I assure you that the grand finale will be the most exciting part of all."
    s "I don't wanna spoil anything specific for ya, but I will say this:"
    s "That whole 'earn your freedom' concept is a sham."
    s evilgrin "Win or lose, the only way these parents will leave this theater is in a body bag."
    "..."
    s happy "Well, I wouldn't want to do anything less!"
    s jeer hat "After all, not pleasing the event's biggest backer would be foolish!"
    "..."
    s wut "Aha... Well, you see..."
    s hm rightdown "I actually don't plan to kill her."
    s horror "N-Now hold on! Let me explain!"
    s wut "Killing her after everything that I've put her through tonight would feel like an act of mercy, wouldn't you agree?"
    s "She's got two obliterated knees, a shattered hand, a missing eye, a charred husband, and cuts and bruises throughout her whole body."
    s jeer "All toppled with the fact she's been trapped alone in a dark basement when not on stage."
    s laugh "That sort of solitude in this context would drive anyone mad!"
    s jeer hat "The way I see it, leaving her alive to deal with that trauma, as well as the knowledge that she's the reason I decided to kill all these innocent people..."
    s evilgrin "Well, that feels like a fate worse than death."
    "..."
    s jeer "Of course, Sir."
    s happy "I need to get back to preparing for the next scene, but I am so glad to hear all the positive feedback!"
    s jeer "Perhaps once the War ends, we can get to work discussing the full-time opportunity?"
    "..."
    s laugh "Wonderful! Enjoy your evening, my lord!"
    $l_exp = "surprised"
    stop music fadeout(3.0)
    pause 1
    show screen laura
    show helmet zorder 3
    scene bg basement_hall
    show helmet zorder 3
    with dissolve
    pause 0.1
    "He then walked towards the door."
    "I moved out of the way as to not seem like I was doing what I was doing."
    show sprinkles happy rightdown leftdown at middle_sprinkles with easeinleft
    pause 0.1
    "As he opened the door, he started walking back towards the stage."
    "Once again completely not noticing me."
    hide sprinkles with easeoutright
    pause 0.1
    $s_name = "Mr. Sprinkles"
    $l_exp = "sad"
    "Alright, my next objective is clear."
    "I walked down further into the back of the theater."
    $l_exp = "surprised"
    "I eventually came to a dead end that had only a single door on the wall."
    "It was labeled {i}'Basement'{/i}."
    $l_exp = "determined"
    "Bingo."
    play sound door_creak
    "I slowly opened the door, discovering a staircase leading to a pitch-black hall."
    $l_exp = "concerned"
    "After flipping on a light switch nearby, I could make a better sense of when the stairs ended."
    "I then walked down."
    show bg basement with dissolve
    pause 0.1
    "It was still dark down here, but I could make a better sense of where I was going."
    $l_exp = "surprised"
    "And as I approached the bottom, I could see, sitting only a few feet from the stairs..."
    pause 1
    show jessica full blank at middle_jessica with dissolve
    pause 1
    "She didn't seem to pay mind to my presence."
    "Her blank stare ahead really made me question if she was actually still alive."
    "Though a quick blink proved otherwise."
    show helmet:
        ease 0.5 alpha 0.0
    pause 0.6
    hide helmet
    "I took my helmet off and set in on the ground."
    l "Jessica?"
    "Nothing."
    "I slowly approached her and bent down to her level."
    "Still nothing."
    "The blood on her face was dried out, but recent tear stains could be seen along the bottom of her eyes."
    $l_exp = "excited"
    l "I'm gonna get you out of here, okay?"
    j "..."
    $l_exp = "concerned"
    "I guess expecting a verbal response from a gagged woman was kinda stupid."
    $l_exp = "surprised"
    "Still, not even a movement to indicate a response or acknowledgment."
    "I sighed and rested my hand on her hand."
    "The good one, not the broken one."
    play music vast_places
    $l_exp = "neutral"
    l "I'm sorry that you had to go through everything you went through."
    l "And I'm really sorry that your husband was dragged into it."
    $l_exp = "surprised"
    "I was actually taken aback a bit when her eye slowly turned towards me."
    $l_exp = "smile"
    "But I regained myself and continued."
    l "I watched my husband die tonight, too."
    l "I get it. It sucks."
    $l_exp = "sad"
    l "It makes you feel powerless knowing there's nothing you can do to stop the man you love from going through that."
    "Even though she was looking at me now, she still had that blank look in her face."
    "I couldn't tell how she was feeling or if I was even completely getting through to her at all."
    $l_exp = "mad"
    l "Believe me, I'm just as pissed at Krag Dovason as you are."
    $l_exp = "neutral"
    "..."
    "Did I really just say that?"
    $l_exp = "smug"
    "I then couldn't help but give a small chuckle."
    l "Wow. If someone had told me 24 hours ago that I would be in agreement with you on something..."
    "Sighing and getting back on track, I turned to Jessica and spoke quietly."
    $l_exp = "concerned"
    l "Listen, Jessica. The best way to get revenge on Krag is to ruin this show."
    l "It may be almost over, but if that means we can save some lives in the process, it'll be worth it."
    "She stared at me for a few more seconds before turning back to where she was before."
    $l_exp = "concerned"
    "Curious, I looked in the general direction she was looking."
    "It was dark, but I could actually see something, though faint."
    "I looked around for a light switch or something similar, but couldn't see one."
    "Desperate, I quickly took off the armor and reached into my pocket to pull out my phone."
    $l_exp = "smug"
    "I'm actually a bit relieved; that shit was heavy."
    $l_exp = "neutral"
    "I then turned the flashlight of my phone on and pointed it towards the other side of the basement."
    $l_exp = "shocked"
    "When I did, I almost dropped the phone in fear."
    play music shattered_mind
    scene bg fade with dissolve # CG of body pile
    pause 0.1
    "On the other side of the basement was a pile of bodies."
    "They weren't just any bodies, though; I recognized plenty of them."
    "They were the contestants who lost the games."
    $l_exp = "surprised"
    "Well, I guess that's one mystery solved..."
    "But did they throw them down here to add to Jessica's torture?"
    "Was it a way to go {i}\"You did this!\"{/i}?"
    $l_exp = "sad"
    "Either way, just looking along the back wall and seeing the corpses just thrown aside like they were literal garbage is just..."
    "..."
    "I guess when you actually see all the casualties thrown together like this, you get a sense of just how crazy this night has been."
    "All of these people..."
    "They were just innocent parents who wanted to protect their children from the REDD War."
    "They didn't deserve this."
    "Especially not--"
    $l_exp = "shocked"
    stop music fadeout(3.0)
    "!!!"
    "As I looked at the far end of the pile, I saw something."
    "Or rather, some{b}one{/b}."
    "Someone too familiar."
    # Fades and focuses on Richard
    "Richard..."
    play music packing
    "I approached my husband and felt my throat tighten."
    "His body was so broken, I almost couldn't tell it was him."
    $l_exp = "sad"
    "But that face..."
    "That build..."
    "I'd recognize it anywhere."
    "The shaky breathing commenced as I tried to hold back the tears."
    "I then got next to him and grabbed onto his hand."
    "It was cold."
    $l_exp = "crying"
    l "Richard..."
    l "I..."
    "I couldn't hold it back."
    "The tears flowed and the sobs emerged as I collapsed, never letting go of his hand."
    l "I'm sorry, Richard!"
    l "We should have left Atlanta like you said!"
    l "But I was stupid and made us stay!"
    l "I'm so sorry!!"
    $nvl = True
    nvl clear
    hide screen laura
    nvl show dissolve
    narrate """
    I held on tightly to his frigid hand as I sat there and bawled my eyes out.

    I had been so calm about it up to this point.

    Dare I say I sort of forgot about it.

    It's not that I didn't care about him; it's very much the opposite!

    But if I didn't think about anything else, I would've become like Jessica: wallowing in my pain to the point where I become a mindless zombie.

    {nw}

    I honestly thought I had gotten over it enough to where I could get through the rest of the night.

    But seeing him right now, looking like this...

    I just couldn't help myself.

    What else was I supposed to do upon seeing the love of my life in a state like this?

    ...

    {clear}

    No.

    No, I need to be strong.

    I can do this.

    My desire to stay in the city may have caused this, but the least I can do is honor his final request to me.

    {i}\"Stay alive for them...\"{/i}

    I suppose this grand scheme of mine will heavily risk that promise being broken.

    But if I can pull this off, I'll have an awesome story to tell him when I see him again.

    The thought of how he would react to that brought a smile across my face.
    """
    $nvl = False
    $l_exp = "smile"
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    "I finally let go of his hand and stood up, continuing to stare at him with a motivated grin."
    $l_exp = "determined"
    l "Don't worry, Richard."
    l "We'll get through the night."
    l "And so will everyone else."
    "I looked at him for a few more seconds before turning around and walking back to Jessica."
    stop music fadeout(3)
    scene bg basement
    show jessica full blank at middle_jessica
    with dissolve
    pause 0.1
    l "Come on."
    l "Let's get you out of here."
    call sceneend
    if not persistent.scenes["ch5_s1"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch5_s1"] = True


label deadchild:
    python:
        currenttime = "3:43 AM"
        timeleft = "3 hours and 17 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    play music classy_ghouls
    scene bg basement_hall
    show jessica wheelchair at middle_jessica zorder 1
    show helmet zorder 3
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    l "Alright, I think you should be good..."
    "It was a bit of a hassle to get her up here."
    $l_exp = "concerned"
    "I just wish we found this wheelchair sooner; it would've been much easier to move her around."
    "Of course, her legs are a bit useless at the moment, so getting her up the stairs was gonna be a chore whether she was in the wheelchair or the torture chair."
    "The heavy-ass armor wasn't helping, either."
    $l_exp = "neutral"
    "Though I guess the nature of the torture chair made it a bit easier, as she was less likely to fall out as she went up."
    $l_exp = "sad"
    "But she was wincing and groaning in pain with each bump up the step the chair made."
    $l_exp = "smile"
    "Well, at the very least, she was showing some kind of emotion."
    "Fortunately, when we got up, we were able to find a small closet that housed the wheelchair."
    "I guess it's for emergencies and/or theater guests who are unable to walk."
    $l_exp = "smug"
    "Well, I can't think of a more relevant use than this."
    $l_exp = "neutral"
    "After transferring her to the wheelchair, I put both her and the torture chair in the closet."
    $l_exp = "concerned"
    "It's not the most ideal safe haven, but it's not where they last left her, so it's something."
    $l_exp = "excited"
    l "I'll check up on you later. For now, I gotta find a way to stop Krag."
    j "..."
    $l_exp = "surprised"
    "Despite no longer being gagged, she's still not talking."
    "I don't know whether she's just too out of it or if she's just got nothing to say."
    $l_exp = "excited"
    l "It'll be alright, Jessica."
    l "I'll be back."
    l "And if the worst-case scenario happens, there's the handle inside the door you can use to get yourself out."
    $l_exp = "neutral"
    hide jessica with dissolve
    pause 0.1
    "With that, I slowly closed the door."
    "Okay. On to the next step of my improvised plan."
    $l_exp = "surprised"
    "So, how exactly am I gonna stop this show without getting myself killed?"
    "I can't just go onto the stage. The guards would stop me for sure."
    $l_exp = "concerned"
    "I guess if I'm gonna do this proper, I'll need to sabotage the show from behind the scenes."
    $l_exp = "smug"
    "Hiding Jessica is a good start, but I'll need to do more than that."
    $l_exp = "concerned"
    "I suppose the best way to avoid playing games is having no contestants to play them."
    "But how in the hell am I going to free all of the remaining hostages?"
    "There's only so far wearing this guard outfit will go before questions are asked."
    $l_exp = "surprised"
    "It's already bad enough that Krag seems suspicious of my presence near his location."
    "..."
    $l_exp = "concerned"
    "Well, at the very least, let's see if I can find the room and go from there."
    "The break should be ending quickly, which means they'll need another contestant."
    "Following the guards seems like the best option to find the hostages."
    $l_exp = "smug"
    "Who knows? Maybe I can stop them from bringing the hostage out onto the stage."
    stop music fadeout(3)
    $l_exp = "surprised"
    redd "Let's go! Don't make this difficult!"
    "A bit ahead of me, I could see a woman being dragged to one of the stage entrances."
    $l_exp = "sad"
    "Well, there goes that plan..."
    $l_exp = "concerned"
    "Still, seeing where they came from, I'll just have to follow that path."
    "I'm sure once I do, my memory will be refreshed on where the location is."
    s "Alright, everyone~! Welcome back to the show!"
    $l_exp = "neutral"
    "As I walked past, I could see a live feed of the stage above each stage entrance."
    play music sprinkles_theme
    hide screen laura
    scene bg stage
    show sprinkles laugh hat cane at middle_sprinkles
    with dissolve
    pause 0.1
    s "We're in the home stretch now, ladies and gentlemen~!"
    s jeer "And soon, we'll experience our grand finale!"
    s evilgrin "I simply can't wait to share it with you all!"
    s rightdown happy "In the meantime, let's play our next game, shall we?"
    s jeer "And the Wacky Dartboard has landed on..."
    s "..."
    s laugh cane "{i}Magic Mic!{/i}"
    show game_name "Magic Mic" at game_name_flash
    $l_exp = "concerned"
    show screen laura
    pause 0.6
    "I've always found that game name to be in poor taste, especially for a children's show."
    "Then again, this version of the show isn't exactly what you'd call {i}'family-friendly'{/i}."
    hide game_name
    s jeer "Let's meet our lucky contestant!"
    "The woman from earlier was then dragged onto the stage, looking as frightened as you'd expect."
    $l_exp = "surprised"
    "Good luck, lady."
    $l_exp = "neutral"
    "I was about to walk away from the screen to find the hostages, but..."
    $b_name = "Kid"
    b "MOM!!"
    $l_exp = "surprised"
    stop music fadeout(3)
    "I heard a child's voice through the speaker."
    scene bg livestage with dissolve
    pause 0.1
    "Turning back to the screen revealed the camera pointed to a little boy  around Dakota's age in the audience."
    "He was standing up and staring at the stage with tears in his eyes."
    woman "Rodney!"
    "The contestant was looking back at her son with terror on her face."
    $b_name = "Rodney"
    b "Let her go!!"
    $l_exp = "sad"
    "Rodney then ran into the aisle and towards the stage!"
    woman "Rodney, go back! Please!"
    b "No!"
    "A REDD guard stepped in front of him."
    redd "Back to your seat {b}now{/b}!"
    b "Let my mom go!"
    "The guard pointed his gun at him."
    redd "Last chance!"
    b "..."
    $l_exp = "surprised"
    "Rodney slowly turned around and walked towards his seat, with the camera panning back towards the stage."
    $l_exp = "neutral"
    scene bg stage
    show sprinkles wut rightdown cane at middle_sprinkles
    with dissolve
    pause 0.1
    s "Alright, then."
    play music sprinkles_theme
    s jeer hat "Without any further interruptions, let's--"
    redd "{b}HEY!!{/b}"
    show sprinkles hm
    $l_exp = "surprised"
    "The camera panned back to where Rodney and the guard just were, only to show Rodney on the stage!"
    woman "Rodney!!"
    b "MO--"
    $renpy.music.set_volume(1.0, channel="ambience")
    stop music
    play sound machine_gun
    show blood2 zorder 3
    call gunflash
    $l_exp = "shocked"
    show sprinkles horror
    pause 0.1
    play sound2 children_screaming
    play ambience crowd_screaming
    pause 1
    "I just stared at the screen and covered my mouth in shock."
    "The mother shrieked with pain."
    "Even Mr. Sprinkles couldn't hide how he was feeling as he stared at the dead boy with a horrified look."
    s "...!"
    s rightdown wut "Uh..."
    s jeer "I-It looks like we've got a bit of an unexpected mess to clean up here, folks."
    s hat "H-Hang tight while we clean it up, ahaha..."
    show sprinkles rightdown hm
    "He then waved his hand in front of his throat, signaling the camera operators to cut the broadcast."
    stop sound2 fadeout(3)
    stop ambience fadeout(3)
    scene bg basement_hall
    show helmet zorder 3
    with dissolve
    pause 0.1
    "I still can't believe that just happened."
    "A lot of adults died here tonight, but never a child."
    "I could feel myself on the verge of crying again."
    "It wasn't my child who died, but it was still {b}a{/b} child."
    "That's just--"
    $l_exp = "surprised"
    "Suddenly, Mr. Sprinkles, Trosh, and the guard who shot Rodney entered the backstage area and stormed around the corner."
    "Sprinkles did not look happy."
    "They didn't appear to see me, but I ducked away from their sight just to be safe."
    play music sprinkles_spooky
    s "What the hell was that??"
    redd "What? The kid was warned!"
    s "I thought I made it perfectly clear at the beginning of the night that children are {b}off limits!!{/b}"
    redd "I didn't have much of a choice, man! Cut me some slack!"
    s "I will do no such thing!"
    redd "What, would you have preferred he go up and ruin the game?"
    redd "If I had let him get away with that, what would stop another kid from running onto the stage when their parent was up there?"
    redd "Or from all the kids running up to ambush you for the hell of it??"
    redd "The audience needed to realize that if they disobey orders and/or go where they're not supposed to, they receive negative consequences!"
    redd "C'mon, Trosh! Back me up here!"
    $l_exp = "concerned"
    "After a few seconds of silence, Trosh sighed and spoke."
    $t_name = "Trosh"
    $l_exp = "neutral"
    t "If something like that happens again, you fire at the ceiling or grab the child by the arm."
    t "You do {b}not{/b} shoot them."
    t "Do I make myself perfectly clear?"
    redd "Trosh!"
    t "{b}DO!{w=0.5} I MAKE MYSELF!{w=0.5} {i}CLEAR?!{w=0.5}{/i}{/b}"
    redd "..."
    t "Fine."
    play sound beep
    $l_exp = "surprised"
    "I heard some light shuffling before a strange beeping noise."
    redd "Yo, what the fuck did you just--??"
    t "Your weapon will be inactive for the next 30 minutes."
    t "Maybe when it reactivates, you'll have learned something."
    $l_exp = "neutral"
    "The guard scoffed with annoyance and anger."
    redd "I don't know why you two are getting so pissy about this. I'm sure the REDD at the Base are loving the fact that a human kid died!"
    redd "That certainly won't damage your ratings."
    redd "Hell, Reddington might even increase the budget if the night ended by killing all the kids!"
    s "Stop talking right now."
    s "No more dead children. End of discussion."
    redd "Whatever, man."
    stop music fadeout(3)
    "The guard then walked back into view and towards the stage while it sounded like the other two headed further down the hall, possibly towards the dressing room Sprinkles was in earlier."
    $l_exp = "surprised"
    "Wow. Krag really is upset by this."
    "..."
    $l_exp = "wut"
    "A REDD is upset by a child being murdered."
    "..."
    $l_exp = "concerned"
    "Huh."
    "After all he's done tonight, after all the people he's killed and had killed, {b}this{/b} is what's too far?"
    "If this were a human, that would be more understandable to an extent, but this is a REDD we're talking about here."
    "And why is Trosh seemingly in Krag's defense?"
    "He hates kids! Him killing kids is what started this whole mess in the first place!"
    $l_exp = "neutral"
    "I guess his mindset is 'orders are orders', but--"
    $l_exp = "surprised"
    t "There you are, Ranigan!"
    play music classy_ghouls
    show trosh gun concerned at two2 with dissolve
    pause 0.1
    "I turned and saw Trosh next to me."
    $l_exp = "wut"
    "Oh, sure. {b}Now{/b} someone notices my presence."
    t angry "We've been looking for you for half an hour!"
    t "I need you to head back to your station."
    $l_exp = "shocked"
    "..."
    "Well, I feel kinda screwed right now."
    t concerned "You {b}do{/b} remember where it is, right?"
    $l_exp = "surprised"
    "I just stared ahead."
    "Speaking would totally blow my cover, but not knowing where to go would also get me in hot water."
    $l_exp = "neutral"
    "Finally, he sighed."
    t "Fine. I'll show you back to your post."
    t "Follow me."
    "..."
    $l_exp = "concerned"
    "Well, he's acting a bit too calm about this."
    $l_exp = "surprised"
    "But I don't think I have much of a choice."
    $l_exp = "sad"
    "With that, I followed him down the hall."
    hide trosh with dissolve
    pause 0.5
    show bg dressingroom with dissolve
    pause 0.1
    $l_exp = "surprised"
    "I was a bit confused that I wound up in the dressing room."
    $l_exp = "concerned"
    "Why would a guard be--"
    stop music
    $quickhide = True
    hide screen laura
    window hide
    play sound smack
    call gunflash
    show bg dressingroom_woozy
    pause 1
    $l_exp = "wut"
    $quickhide = False
    show screen laura
    window show dissolve
    pause 0.1
    "The next thing I knew, I was smacked in the back of the head and I collapsed to the floor."
    t "Oh, did I fail to mention that Ranigan was found unconscious outside the building and without his armor??"
    t "My bad!"
    $l_exp = "shocked"
    "Fuck!"
    "He then picked me up and pinned me against the wall!"
    show bg dressingroom
    show trosh hips angry at middle
    with dissolve
    pause 0.1
    t "No more fucking around!"
    "In one quick motion, he reached behind my head and yanked the helmet off."
    $l_exp = "surprised"
    show helmet:
        ease 0.25 alpha 0.0
    pause 1.25
    hide helmet
    t fear "..."
    "He backed up a bit, still sporting a shocked expression."
    t "..."
    t concerned "Heh. Ahaha."
    t laugh "Ahahahaha!!!"
    t "Oh my fucking...!"
    t "I... I've seen a lot of humans in my time on this planet."
    t "But {b}you{/b}? Oh, you are {b}easily{/b} the stupidest of them all!"
    t "After escaping the hellhole where you're destined for death, you decided to {b}come back{/b}???"
    t angry "If you wanted to die here so badly, you should have just said so!"
    $l_exp = "shocked"
    show trosh gun
    "He then raised his gun at my head."
    l "{b}{i}WAIT!!{/i}{/b}"
    show trosh concerned
    "He froze, but still had the gun pointed at me, finger never leaving the trigger."
    $l_exp = "sad"
    l "L-Let's just talk for a second!"
    t angry "Talk? Pft. No, thanks."
    l "If you're gonna kill me no matter what, the least you can do is hear what I have to say."
    t "I've got better things to do with my time."
    l "What if I have information that could save Krag's life?"
    t concerned "..."
    $l_exp = "surprised"
    "He then held the gun with one hand while using the other to slip off his helmet."
    $helmet = ""
    with dissolve
    pause 0.1
    t "What the fuck are you talking about?"
    "Well, I'm not dead yet."
    "This could be my one and only chance to talk some sense into him."
    $l_exp = "sad"
    "I'm taking a huge gamble here, especially since REDD minds are different than human ones, but I'm very, {b}very{/b} low on options here."
    play music vast_places
    l "Craig Tate, from earlier? He wasn't wrong."
    l "Legally, Krag won't be punished for the stuff that happened in this show."
    $l_exp = "shocked"
    l "But there are so many people who are furious at Krag and want him punished!"
    l "And if the law won't punish him, then they'll resort to vigilantism, and who knows how bad that'll turn out?"
    $l_exp = "sad"
    l "No amount of laws still stop people from harming or even killing him as a result of what he's done tonight!"
    t "Heh. You really think so?"
    $l_exp = "mad"
    l "Want proof?"
    l "Look at Jessica.{w} Look at what she did because of the shit that happened last year."
    show trosh angry
    "He got a more furious look on his face, but still seemed to be focused on what I had to say."
    l "You received no legal trouble for killing those people, yet she attacked you and your brother nonstop. And that was just because of several households!"
    l "You take that established hatred of Krag mixed with the {b}many{/b} innocent parents he's killed tonight, and you've got a ticking time bomb!"
    t yelling "Oh, so what?"
    t "That's life. Fight, kill, repeat."
    $l_exp = "concerned"
    l "And you don't see anything wrong with that?"
    show trosh smile
    "He then gave a light chuckle."
    t "See, that's the problem with you humans."
    t "It's always gotta be about 'right' and 'wrong' with you."
    t concerned "Who truly decides what's 'right' and 'wrong', huh? What's right to me could be wrong to you and vice versa."
    t angry "And that's why REDD are superior. We don't worry about pathetic morals. We just do what we do because we can."
    $l_exp = "neutral"
    l "Alright, fair enough. I'm human, you're REDD. We're different."
    l "But maybe we're not completely different."
    l "Maybe we have some things in common."
    t smile "Heh. Such as?"
    l "We both care about what's going to happen to Krag."
    t angry "What are you talking about? Why would I care?"
    $l_exp = "mad"
    l "Because he's your brother."
    t "And?"
    $l_exp = "neutral"
    l "So you're not bothered in any way, shape, or form that Krag might die as a result of his actions?"
    t concerned "This was his idea. What happens to him as a result of that is beyond my control."
    $l_exp = "concerned"
    "He looks a bit nervous."
    "I may be on to something."
    l "Alright, so tell me this:"
    l "If you truly don't care about him, why bother funding his TV show?"
    l "It's everything that goes against what the REDD stand for. It's everything that goes against what {b}you{/b} stand for!"
    t angry "..."
    l "Stop me if I'm wrong..."
    $l_exp = "smug"
    l "...but I think it's because you wanted him to be happy."
    l "REDD may be biological killers, but they're not heartless."
    t "..."
    $l_exp = "neutral"
    "His trigger finger was shaking."
    "I'm getting somewhere, but I better make sure I don't push it."
    $l_exp = "concerned"
    l "Let's put it this way: if you were really as heartless as you make yourself out to be, I would be dead right now. We wouldn't be having this discussion."
    t concerned "..."
    l "But as soon as I mentioned saving Krag's life, you actually listened to what I had to say."
    $l_exp = "sad"
    l "And that's nothing to be ashamed about, I assure you."
    "He continued to stare at me for a few seconds."
    $l_exp = "surprised"
    show trosh hips with dissolve
    pause 0.1
    "Finally, he lowered his weapon."
    t "Alright, answer me this:"
    t "Why do {b}you{/b} care what happens to Krag?"
    $l_exp = "shocked"
    l "I'm sorry?"
    t "Why would you give a shit about a guy who's responsible for the deaths of so many innocent people?"
    t yelling "One of which was your husband!"
    $l_exp = "sad"
    l "..."
    t "Because of Krag, you'll never see your husband again."
    t "Because of Krag, your daughters will grow up without a father."
    $l_exp = "crying"
    l "..."
    t angry "You seem exactly like the kind of person who would want to see Krag get punished."
    t "So why should I believe you when you say you care about keeping him safe?"
    $l_exp = "sad"
    l "..."
    l "Well..."
    l "You're right. I have every reason to want to see him get what he deserves."
    l "The things he's done tonight are awful."
    l "Torturing Jessica, killing parents who were here to enjoy their night and protect themselves from the War..."
    $l_exp = "surprised"
    l "But at the same time, I can't really place all the blame on the guy."
    t intrigued "..."
    $l_exp = "sad"
    l "I truly believe that he would have never even thought of doing these things if it wasn't for Jessica fighting against him and having her little army threatening him."
    l "As terrible as it is seeing him get off the hook, hurting a guy who did all this because he felt like he had no other choice would just make me feel even more terrible."
    t concerned "..."
    l "I know that doesn't make sense, but not everything does."
    $l_exp = "smug"
    l "You know, such as a human asking a REDD for help."
    t angry "And how exactly do you expect me to help you? Do you somehow think we'll be able to convince the whole world to not attack him?"
    $l_exp = "shocked"
    l "Oh, hell no. That's impossible."
    $l_exp = "sad"
    l "But if we can stop this live show and get him to come to his senses about the situation he's created, we might be able to help him form a way to go into hiding until this dies down."
    $l_exp = "surprised"
    l "If he thinks he'll be completely off the hook at 7, he'll be a dead man walking. We need to get him to realize what he's gotten himself into."
    t "..."
    $l_exp = "sad"
    l "Look, you don't have to like me. I'm not even asking you to."
    l "But if you really do care about Krag as much as I think you do, then please help me."
    t intrigued "..."
    l "..."
    "He finally let out a deep sigh."
    t "I'll help you on one condition."
    $l_exp = "concerned"
    l "Which is?"
    t concerned "Nobody, not even Krag, must know that I had a part in this."
    t "If word gets out that I helped a human, my career and livelihood are finished."
    $l_exp = "neutral"
    l "..."
    l "Deal."
    "I extended my hand, which he stared at for a second before shaking."
    t "So what exactly is your plan?"
    $l_exp = "smug"
    "Something tells me I shouldn't tell him that I've been making this up as I go."
    $l_exp = "concerned"
    l "Well, you pretending like you're not involved will admittedly complicate things."
    $l_exp = "determined"
    l "I've got some ideas, but if we're gonna pull this off, we'll need to work together on a proper plan."
    call sceneend
    if not persistent.scenes["ch5_s2"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch5_s2"] = True


label escapeplan:
    python:
        currenttime = "4:02 AM"
        timeleft = "2 hours and 58 minutes"
        l_exp = "rage"
        helmet = "_helmet"
    call chapterstart
    pause 2
    scene bg storage
    with Dissolve(2.0)
    pause 0.1
    show trosh gun angry at middle with dissolve
    pause 0.5
    t "Get in!"
    play sound smack
    pause 1
    show screen laura
    window show dissolve
    pause 0.1
    l "Geez, you don't have to be so--"
    t "Shut up, bitch!"
    redd "Wait a second; isn't that--?"
    $l_exp = "mad"
    t laugh "Heh. Yep."
    t "The dumb cunt actually came back after her grand escape."
    redd "Hahaha! God, what a fuckin' retard!"
    t "Tell me about it!"
    t concerned "Anyway, don't let her get too comfortable here; I'm sure Krag would love to see her out on stage for another game."
    t "Only this time, let's make sure she doesn't run away."
    redd "Understood, sir."
    t "Oh, and one more thing:"
    t "Since the number of prisoners has shrunken incredibly low, we don't need 4 of you in here anymore."
    t "One should suffice."
    redd "Understood, sir."
    $l_exp = "neutral"
    "Trosh then looked at me with a smirk before walking closer to me."
    t laugh "Have fun."
    "He then gave a quick laugh before turning around and walking out of the room."
    "Three of the REDD guards followed him out, leaving only a single one behind."
    hide trosh
    with Dissolve(2.0)
    pause 0.5
    "The guard then got back into position in front of the door."
    "A few people huddled closer to me."
    man "Why the hell would you come back?"
    "He whispered quietly."
    woman "For real! Why would you?"
    l "It's complicated."
    "I replied as I slipped off my shoe."
    redd "What the hell are you doing?"
    "He asked as he pointed his gun at me."
    $l_exp = "mad"
    l "I've got a rock in my shoe, maybe in my sock."
    "I then slipped off my sock and shook it a few times, with the guard never lowering his weapon."
    $l_exp = "concerned"
    l "Hm. I {b}thought{/b} there was..."
    "The guard sighed, lowered the gun, and backed up against the door."
    "When he did, I leaned in towards the people around me and made my voice as low as it could."
    $l_exp = "mad"
    l "Listen, I need you all to pay attention."
    l "When I say 'Now', I need you to help me jump the guard."
    man "I'm sorry...?"
    l "Trust me."
    $l_exp = "surprised"
    redd "What are you yapping about over there?"
    "He then approached us."
    $l_exp = "mad"
    "I then smacked the outside of my pocket."
    play sound beep
    "A beep rang through the room."
    $l_exp = "rage"
    l "{b}{i}NOW!!!{/i}{/b}"
    play music escape
    "I sprinted towards the guard, who pulled up his weapon in retaliation and squeezed the trigger."
    "..."
    "Only for nothing to happen."
    redd "What the fuck??"
    $l_exp = "mad"
    "Taking advantage of his confusion, I smacked his gun out of his hands and punched him in the head!"
    play sound smack
    pause 0.5
    $l_exp = "concerned"
    "The helmet he was wearing certainly hurt my fist a bit."
    $l_exp = "determined"
    "But it still distracted him long enough for some of the male hostages nearby to fully tackle him to the ground!"
    "He struggled to break free, but more hostages came forward and helped hold him down."
    redd "Help! I need help!! Ple--!"
    "Before he could finish, I yanked his helmet off and jammed my sock into his mouth."
    "All that was left to do was plug his nose."
    "He struggled even harder."
    "But, finally, he slowed down as his eyes closed and head turned."
    "I unplugged his nose and backed up a bit."
    stop music fadeout(3.0)
    l "Alright, that should be good."
    "Everyone slowly got off of him and backed up."
    "As they did, I walked over to the door and locked it."
    "After confirming that the guard was unconscious, everyone turned to me."
    play music vast_places
    woman "What the hell just happened?"
    $l_exp = "smug"
    "I reached into my pocket and pulled out a small remote with a big button on it."
    l "It's a device that disables all REDD weapons within range."
    l "I swiped it from Big Bad Trosh on my way over here."
    l "After seeing him use it on the guard who shot that kid, I knew I had to use it to save you guys."
    man "That's why you came back? To free us?"
    $l_exp = "neutral"
    l "Kinda."
    $l_exp = "sad"
    l "But why I came back doesn't matter. What's important is stopping this show."
    man "Don't you think you're a bit late for something like that, lady?"
    $l_exp = "mad"
    l "Better late than never."
    l "Besides, even if you, by some miracle, win the game, you're still fucked unless we do something!"
    woman "What are you talking about?"
    l "Mr. Sprinkles isn't planning on letting any of the parents live!"
    l "I overhead him say that the only way they're leaving is in a body bag!  Those were his exact words!"
    $l_exp = "concerned"
    l "I don't know what exactly he has planned to pull that off, but if we can stop this show, then it won't matter."
    man "And how exactly do you plan to do this?"
    $l_exp = "determined"
    l "Locking you all in here is a start. You can't play a game if you can't get to your players, right?"
    man "Yeah, but how long until the other guards get suspicious and busts the door down? Then what??"
    l "Then it's just a repeat of what we did to that poor sap over there."
    woman "You expect us to just start tackling and fighting the guards?? There are so many of them!"
    $l_exp = "mad"
    l "And the number of us in this room alone can at least match their numbers."
    man "Lady, taking out one guard when we catch him by surprise is one thing."
    man "Taking out an entire fucking {b}army{/b} is another!"
    man "Even if you used that little doodad to stop their guns, they could easily pin us down first and snap our fucking necks or something!"
    $l_exp = "concerned"
    l "They could. They're still highly-trained killers on top of being biological sociopaths."
    $l_exp = "mad"
    l "But if you sit here and do nothing, it's guaranteed death. At least fighting back will give you a chance."
    l "A chance to survive the REDD War! A chance to see your children again!"
    l "Don't you all want that?"
    $l_exp = "neutral"
    "A lot of the parents looked at each other, waiting for anyone to give a response."
    l "Okay, look."
    l "If you don't want to fight, then that's your choice."
    $l_exp = "mad"
    l "But if you want to help me stop this mess..."
    $l_exp = "sad"
    l "And I really am begging that you do..."
    $l_exp = "mad"
    l "Then let's--"
    stop music
    play sound door_locked
    $l_exp = "surprised"
    "I was caught off-guard as the door to the room shook a bit as someone tried to open it."
    s "Trosh? Trosh, what's going on?? Where's the next contestant??"
    "Everyone in the room went silent."
    play sound door_pound loop
    "Mr. Sprinkles then began pounding rapidly on the door."
    s "Hey! Open the door!! Trosh?? {b}Anyone?!{/b}"
    "Silence on our end."
    s "This isn't funny!! I can't afford another delay or slip-up!! {b}OPEN THE DOOR!!{/b}"
    "..."
    stop sound
    s "..."
    "Finally, he growled and stomped away."
    $l_exp = "concerned"
    "It sounded like he threw something as he did."
    l "..."
    woman "Do you think he'll come back?"
    $l_exp = "neutral"
    l "Eventually. For now, I think you're safe."
    woman "{i}'You\'re'?{/i}"
    $l_exp = "determined"
    l "I'm heading out to free the audience and cut the broadcast."
    l "With no contestants and nobody to watch him, Sprinkles will have nothing left."
    $l_exp = "neutral"
    "I then slipped the deactivation device into her hand."
    l "If a guard comes in here, {b}please{/b} use this!"
    woman "What about you? You'll get yourself killed out there!"
    l "Better me than you guys."
    "I then placed my ear against the door."
    "..."
    "Nothing."
    $l_exp = "mad"
    l "Alright. Good luck, guys."
    man "Heh. You need it more than us."
    $l_exp = "smug"
    l "Touché."
    $l_exp = "neutral"
    "I gently opened the door."
    play music classy_ghouls
    scene bg basement_hall with dissolve
    pause 0.1
    $l_exp = "surprised"
    "The first thing I noticed was something lying on the floor right in front of my feet."
    "It was Mr. Sprinkles's cane."
    $l_exp = "neutral"
    "I picked it up and began walking."
    "Having any weapon is better than none."
    $l_exp = "surprised"
    "..."
    $l_exp = "sad"
    "..."
    "I then made a quick detour back to the closet near the basement."
    $l_exp = "neutral"
    "The door was still closed, which is a good sign."
    "I opened it up, sighing with relief at what I saw."
    show jessica wheelchair at middle_jessica with dissolve
    pause 0.1
    $l_exp = "smile"
    "Jessica was still in the closet, just how I left her."
    $l_exp = "concerned"
    "...{b}exactly{/b} how I left her."
    $l_exp = "shocked"
    "Not even any movement when I opened the door."
    $l_exp = "surprised"
    "A quick blink from her startled me, but prevented me from assuming the worst."
    $l_exp = "concerned"
    "Still, what if a REDD had opened the door?"
    "I guess it's a good thing I checked up on her."
    l "Here."
    "I placed the cane on her lap."
    l "If anyone other than me opens the door, use this on them. Okay?"
    j "..."
    $l_exp = "sad"
    l "..."
    "Well, I'm not sure what else I can do."
    "I then closed the door."
    hide jessica with dissolve
    pause 0.1
    l "Poor woman..."
    play sound footsteps
    $l_exp = "shocked"
    "I then heard footsteps approach from the side!"
    "I turned my head towards where they were coming from."
    $l_exp = "smile"
    "And was so relieved that it was the one REDD I wanted to see."
    $helmet = ""
    show trosh angry hips at middle with dissolve
    pause 0.1
    t "What are you doing over here? You were supposed to meet me by the curtain."
    $l_exp = "sad"
    l "Sorry. Had to make a quick stop."
    "I replied as I lightly tapped the closet door."
    t concerned "Well, if you wanna stop Krag, we need to hurry."
    t "He's running out of jokes to tell Madeline."
    $l_exp = "neutral"
    l "Alright. You got the goods?"
    "He then pulled the book of matches out of his pocket and handed them to me."
    l "And you're sure no guards will find me?"
    t "As long as you stay in this area, you'll be fine."
    $l_exp = "determined"
    l "Alright, then. Here goes!"
    stop music fadeout(3.0)
    hide trosh with dissolve
    pause 0.1
    $l_exp = "neutral"
    "Trosh walked down the hall that led towards the front of the theater, leaving me all alone."
    "No REDD guards in sight, so at least Trosh is staying true to his word."
    $l_exp = "sad"
    "That doesn't mean he'll come through with the entire plan, though."
    "Trusting a REDD hasn't exactly proven to be in my benefit, but I've got no other choice."
    $l_exp = "concerned"
    "I watched the screen."
    play music sprinkles_theme
    scene bg stage
    show sprinkles leftdown rightdown happy at two2_sprinkles
    show madeline dead at two1
    with dissolve
    pause 0.1
    s "How do prisoners call each other?"
    s jeer "{i}Beats me, Mr. Sprinkles!{/i}"
    s laugh hat "On {b}cell phones!{/b} Ahaha!"
    $l_exp = "surprised"
    redd "Hey!!"
    scene bg basement_hall with dissolve
    pause 0.1
    "I turned around and saw two REDD staring at me."
    show jingle down angry at two1
    show jangle down yell at two2
    with dissolve
    pause 0.1
    ja "What the hell are you doing here??"
    $l_exp = "shocked"
    "Shit! I didn't take these two into account!"
    "And they don't look like they'll cooperate as well as Trosh."
    ji yell "We're gonna have to call security on you!"
    ja confused "...are you serious?"
    ji happy_grin "Of course not! It's the REDD War!"
    ji evil_grin "Let's take care of this the way any REDD should!"
    ja happy_grin "That's more like it!"
    $l_exp = "mad"
    "Alright, no turning back now."
    "Let's do this."
    play music escape
    "I pulled the matchbook out and lit one of the matches."
    $l_exp = "surprised"
    show jingle angry
    show jangle yell
    "I could also see Jingle and Jangle turn towards me once I did."
    play sound fire_start
    "Being quick, I lit the rest of the matches in the book on fire, creating one large burst of flames."
    $l_exp = "surprised"
    "..."
    "The original plan involved me throwing it at the curtain, but..."
    $l_exp = "concerned"
    "...maybe throwing it at them will work in my favor."
    $renpy.music.set_volume(0.5, delay=1, channel="music")
    menu:
        "What should I do?"
        "Throw it at the curtain":
            $renpy.music.set_volume(1.0, delay=1, channel="music")
            $l_exp = "mad"
            "No. I gotta stick to the plan."
            scene bg basement_hall with dissolve
            pause 0.1
            "I threw the burning matchbook at the curtain."
            "As soon as I did, the fire spread up the fabric."
            $l_exp = "shocked"
            "And I felt myself being shoved towards it!"
            "By the time I realized what had happened, it was too late to stop myself."
            "I landed face-first into the flame."
            play sound fire loop
            show fire
            pause 1
            "The next thing I knew, my shirt sleeve was on fire!"
            stop music fadeout(5.0)
            $l_exp = "crying"
            "I tried getting down and rolling so I could try and get it out, but the second I got down, it seemed to spread around me even quicker!"
            "I cried out in pain as I rolled, but it just kept getting worse and worse."
            $l_exp = "angry"
            "It truly figures."
            "Even after all this planning and thought..."
            "...the REDD War finds a way to fuck it up."
            hide screen laura
            window hide dissolve
            stop sound fadeout(3.0)
            pause 1
            scene bg fade
            with Dissolve(2.0)
            pause 1
            if not persistent.achievements["sickburn"]:
                $persistent.achievements["sickburn"] = True
                $renpy.notify("Achievement Unlocked: {i}Sick Burn{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover
        "Throw it at the mimes":
            $renpy.music.set_volume(1.0, delay=1, channel="music")
    $l_exp = "mad"
    "Well, here goes."
    "I tossed the matchbook towards Jingle and Jangle."
    scene bg basement_hall with dissolve
    pause 0.1
    "I wasn't necessarily trying to throw it {b}on{/b} one of them, just something to potentially scare them."
    $l_exp = "shocked"
    play sound fire_start
    queue sound fire loop
    show fire
    "That didn't stop the matches from landing on Jangle and igniting his shirt!"
    "He cried out in pain as the fire spread across him, with Jingle being too distracted by it to go after me!"
    ja "{b}{i}GET IT OFF!! GET IT OFF!!{/i}{/b}"
    $l_exp = "surprised"
    "Jingle looked like she wanted to help, but didn't know how, especially as Jangle ran around like a chicken without a head."
    $l_exp = "shocked"
    "And then stumbled onto the curtain!"
    "Which then burst up into flames!"
    $l_exp = "concerned"
    "Well, I guess that worked out well for the plan...?"
    hide screen laura
    $renpy.music.set_volume(0.5, delay=0.5, channel="sound")
    scene bg stage
    show madeline dead at two1
    show sprinkles leftdown rightdown wut at two2_sprinkles
    with dissolve
    pause 0.1
    s "What in the...?"
    s horror "Oh my goodness!!"
    $renpy.music.set_volume(1.0, delay=0.5, channel="sound")
    show fire
    pause 0.5
    play sound2 children_screaming fadein(1.0)
    play ambience crowd_screaming fadein(1.0)
    pause 1
    play ambience2 "audio/se/fire alarm.ogg"
    pause 3
    scene bg livestage with dissolve
    pause 0.1
    show dakota side sad at two1
    show kate fidget shocked at two2
    with dissolve
    pause 0.1
    k "K-Kota, what's happening??"
    d "The stage is on fire!"
    k crying down "!!!"
    show kate concerned
    show dakota neutral
    play audio "audio/se/Door Open.ogg"
    "Suddenly, the door at the back of the room slammed open."
    "One of the REDD guards came in, looked at the stage, and stomped over to one of the other guards nearby."
    scene bg livestage with dissolve
    $helmet = "_helmet"
    $t_name = "Guard"
    show trosh gun concerned at middle with dissolve
    pause 0.1
    t "What the hell is going on??"
    redd "I-I don't know, Sir! The stage just caught fire!"
    t angry "Well don't just fuckin' stand there! Put it out!"
    t "All of you! Let's go! Find extinguishers and get this shit out!"
    "The rest of the guards looked around the room, trying to find a fire extinguisher or anything that can put the fire out."
    stop ambience fadeout(1.0)
    $l_exp = "surprised"
    show screen laura
    scene bg basement_hall
    show fire
    with dissolve
    pause 0.1
    "Jingle wrapped her brother up in an unburned curtain to try and extinguish him."
    "After he seemed to be out, she unwrapped him."
    $l_exp = "shocked"
    "Only to reveal his whole body was burned to a crisp."
    "And he wasn't moving."
    $l_exp = "surprised"
    "While she was distracted with that, I ran towards the front of the theater for the next step in the plan."
    scene bg lobby with dissolve
    pause 0.1
    "The doors were open, which made this next part easy."
    $l_exp = "rage"
    l "{b}EVERYONE GET INTO THE LOBBY!! LET'S GO!!{/b}"
    hide screen laura
    scene bg livestage
    show dakota side neutral at two1
    show kate down shocked at two2
    with dissolve
    pause 0.1
    "Kate and Dakota turned towards the opened doorway with shock and confusion."
    k "M...Mommy??"
    d sad "!!!"
    l "{b}LET'S GO, LET'S GO!! MOVE IT!!{/b}"
    hide kate
    hide dakota
    show trosh hips concerned at middle
    with dissolve
    pause 0.1
    redd "What the hell??"
    $t_name = "Trosh"
    t angry "Hey! Focus on the fire!"
    redd "The audience is getting away!"
    t "They won't be able to escape the building; we'll collect them after the fire's out!"
    redd "And further delay this damn show??"
    t "The show will be delayed indefinitely if the building burns to the fucking ground with us all in it!!"
    redd "But--"
    t "Put the damn fire out and worry about the damn audience later! I'm not gonna tell you again!"
    redd "..."
    redd "Understood."
    hide trosh with dissolve
    pause 0.5
    scene bg stage
    show fire zorder 3
    with dissolve
    pause 0.5
    show sprinkles horror rightdown leftdown at two1 with dissolve
    show trosh hips concerned at two2 with easeinright
    pause 0.1
    t "Krag, get to your dressing room until we can get this fire out!"
    $s_name = "Krag"
    s "B-But..."
    t "Come on! We'll fix this for you! Just get to your dressing room!"
    s "I... This can't be...!"
    show sprinkles:
        ease 0.5 two1_short
    "Krag was starting to hyperventilate as he fell to his knees."
    t fear "Krag!"
    show trosh:
        ease 0.5 two2_short
    pause 1
    $helmet = ""
    with dissolve
    pause 0.1
    t "Krag, don't you do this to me! Get up!"
    pause 1
    show sprinkles:
        ease 1.0 two1
    show trosh:
        ease 1.0 two2
    pause 1.5
    t intrigued "Come on. Let's get you to safety."
    pause 0.5
    hide trosh
    hide sprinkles
    with Dissolve(1.0)
    pause 1
    $l_exp = "mad"
    show screen laura
    scene bg lobby with dissolve
    pause 0.1
    l "Let's go, let's go! Move it!"
    "More and more people ran into the lobby in a panic."
    l "Get somewhere safe! Hide wherever you can! Go, go, go!"
    "As people ran down hallways, went into bathrooms, and just went anywhere that wasn't the main theater, I could see the fire being extinguished and Mr. Sprinkles nowhere on the stage."
    $l_exp = "concerned"
    "I could also see a half-burned body standing upright on a pole."
    "Well, I hope Madeline's family planned on a cremation."
    stop music fadeout(5.0)
    stop sound fadeout(5.0)
    stop ambience2 fadeout(5.0)
    $l_exp = "mad"
    "Alright. All that's left is the final step in the plan."
    "Making my way through the crowd, I walked back towards the backstage area."
    "Time to end this once and for all."
    hide screen laura
    pause 2
    show dakota sad crossed at two1
    show kate fidget concerned at two2
    with Dissolve(1.0)
    pause 0.5
    k "Mommy?? Mommy!!"
    d "Mom, where are you?? Mom!!!"
    call sceneend
    if not persistent.scenes["ch5_s3"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch5_s3"] = True


label finalconfrontation:
    python:
        currenttime = "4:32 AM"
        timeleft = "2 hours and 28 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    scene bg basement_hall
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    "I approached the dressing room, where a familiar ally could be spotted."
    show trosh hips intrigued at middle with dissolve
    pause 0.1
    t "You actually pulled it off."
    $l_exp = "smug"
    l "{b}We{/b} pulled it off."
    t concerned "Hm."
    t "You really think you'll be able to get him to listen to reason?"
    $l_exp = "concerned"
    l "It's a little late to think otherwise, don't you think?"
    t "Perhaps."
    l "And we're good with the guards?"
    t smile "Any sane REDD who's told that Lord Reddington is disappointed in their failure knows to get a hundred miles away from their last-known location."
    $l_exp = "smug"
    l "And they actually believed you?"
    t "I'm their boss. They have to whether they want to or not."
    $l_exp = "smile"
    l "Okay, then. I guess this is it."
    t concerned "Good luck."
    $l_exp = "neutral"
    l "Thanks."
    hide trosh with dissolve
    pause 1
    "Taking a deep breath, I opened up the dressing room door."
    play sound door_open
    scene bg dressingroom with dissolve
    pause 0.1
    "Opposite of me, staring blankly into the mirror, was Krag Dovason."
    show sprinkles rightdown leftdown hm at middle_sprinkles with dissolve
    pause 0.1
    "He didn't seem to react when I opened the door."
    "He just continued to stare forward with his hands in his lap and his phone on the desk."
    l "Hello, Krag."
    s "..."
    "He then readjusted himself in his seat a bit before sighing."
    play music vast_places
    s "I just received a call from Lord Reddington."
    s "He informed me that he saw that little stunt you pulled."
    s "Of course, explaining to him that it wasn't me, but rather a human, led to him asking how a human was given the chance to do it in the first place."
    s "Needless to say, the most powerful REDD on the planet is very disappointed in me."
    s "Very, {b}very{/b} disappointed."
    $l_exp = "surprised"
    l "..."
    "He said all that in a deadpan tone while not looking away from his reflection."
    $l_exp = "sad"
    "I don't think he even blinked once."
    s "Any chance I had at saving my show..."
    s "Gone."
    s "Down the drain."
    "He took another deep breath before slowly standing up from his seat and turning towards me."
    $l_exp = "shocked"
    "And revealing that he had a pistol in his hand!"
    l "Krag!"
    "It wasn't being pointed at me, but the fact that he had it made the situation problematic."
    s "I don't know who you are."
    s "I don't know how you managed to do this."
    s "But..."
    $l_exp = "surprised"
    s jeer "Congratulations."
    s "You stopped me from performing my big, grand performance."
    s "And now I am left with nothing."
    s "No show, no audience, no fans, no support."
    s "All I have left is the joy that this night brought me."
    s "I haven't felt this alive in years."
    s "So at least now, despite it not ending the way I had planned, I can rest knowing that, if only for one night, I was happy."
    $l_exp = "shocked"
    "He then held onto the gun's barrel and pointed it towards me handle-first."
    s "Here. You deserve this."
    $l_exp = "surprised"
    l "..."
    "I was hesitant, but I slowly took the weapon from his hands."
    s "You win, my dear."
    s "You may now claim your prize."
    stop music fadeout(5.0)
    show sprinkles hat
    "He then tipped his hat to me before turning back around."
    hide sprinkles with dissolve
    pause 0.1
    "Through the mirror, I could see him close his eyes and give a large grin."
    "..."
    $l_exp = "concerned"
    "..."
    hide screen laura
    window hide dissolve
    pause 1
    $finalchoice = True
    menu:
        "Claim Your Prize":
            jump claimprize
        "Decline Your Prize":
            jump declineprize

label claimprize:
    pause 1
    play sound gunshot
    call gunflash
    show blood2
    pause 2
    $l_exp = "crying"
    show screen laura
    window show dissolve
    pause 0.1
    "..."
    "I..."
    "I can't believe I just..."
    pause 1
    show trosh gun intrigued at middle with dissolve
    pause 0.1
    t "What just--"
    t fear "{b}Krag!!{b}"
    show trosh:
        ease 0.5 middle_short
    "He ran to his brother and dropped to his knees."
    t "Krag! Oh God!! {b}KRAG!!{/b}"
    "He then turned to me."
    show trosh intrigued
    $l_exp = "surprised"
    "And noticed the gun still in my hand."
    t "..."
    show trosh:
        ease 1.0 middle
    pause 2
    t "You mean to tell me..."
    t "After all that talk about you wanting him safe..."
    t "About how watching him get hurt despite everything he's done felt wrong..."
    $l_exp = "sad"
    l "T-Trosh, let me explain!"
    "He slowly walked towards me."
    t "After all of that..."
    $l_exp = "crying"
    l "Trosh, I--!"
    t "I trusted you."
    t "I trusted a human for the first time in my life."
    t "Well, I guess now I know better."
    t concerned "And I assure you that's a mistake I'll never make again."
    l "Trosh, please!"
    t "Now, if you'll excuse me..."
    t angry "...I have a right to exercise."
    l "{b}TRO--!!{/b}"
    $quickhide = True
    hide screen laura
    window hide
    play sound machine_gun
    call gunflash
    pause 1
    scene bg blood
    with Dissolve(3.0)
    pause 3
    scene bg fade
    with Dissolve(3.0)
    pause 1
    if not persistent.achievements["grandprize"]:
        $persistent.achievements["grandprize"] = True
        $renpy.notify("Achievement Unlocked: {i}Grand Prize{/i}")
        $persistent.achievelist.append(1)
    $renpy.end_replay()
    jump gameover

label declineprize:
    pause 1
    $l_exp = "mad"
    show screen laura
    window show dissolve
    pause 0.1
    l "No."
    l "I won't do it."
    s "..."
    "His eyes remained closed, but his smile went away."
    s "Is that right?"
    l "That's right."
    s "..."
    $l_exp = "neutral"
    "He opened his eyes and turned towards me."
    show sprinkles hm rightdown leftdown at middle_sprinkles with dissolve
    pause 0.1
    s "Very well."
    s jeer "I suppose I'll take that back, then."
    "He extended his hand towards me."
    $l_exp = "mad"
    l "Why? So you can use it on yourself?"
    s @ wut "..."
    s "Heh. That's funny."
    s "Most people would think that if you gave a REDD a gun, he'd use it to kill {b}you{/b}, not himself."
    $l_exp = "concerned"
    l "Well, I'm not most people."
    l "And you're not most REDD."
    s wut "Ma'am, with all due respect..."
    s hm "...you are very, {b}very{/b} foolish if you believe that after everything I've done tonight."
    l "Look, Krag, I'm not gonna turn a blind eye to everything you've done tonight."
    l "You've done things that might be arguably worse than things other REDD have done."
    $l_exp = "sad"
    l "But..."
    l "I really gotta know: {w}Why?"
    l "Why would you do all of this?"
    s wut "..."
    l "If this was all a way to get back at Jessica, then why bring innocent parents into this?"
    l "Why kill the people who came here because they respected and trusted you?"
    s hm "It's like I said at the beginning of the night: I'm a REDD. I can't and shouldn't be trusted."
    $l_exp = "mad"
    l "Bullshit."
    l "If you wanted humans dead, you wouldn't have waited 7 years to do it."
    s "..."
    $l_exp = "sad"
    l "Come on, Krag. The least you can do is be honest about this."
    s wut "..."
    "He sighed and looked down."
    play music autumn_changes
    s "Do you know what it's like to be one step away from losing everything you've worked so hard to achieve?"
    $l_exp = "neutral"
    l "I can't say that I do."
    s jeer "Well, I can honestly say it's not a fun feeling."
    s "At all."
    s wut "As plain old Krag Dovason, I'm just... a REDD."
    s "Nothing special. Nothing unique."
    s jeer "But... as Mr. Sprinkles..."
    s @ laugh "I... I'm loved."
    s hat "I know the other REDD don't really get it."
    s "Even my own brother doesn't fully get it."
    s rightdown happy "But when I put on this suit and hat..."
    s laugh "Ahaha... It just makes me feel like who I was always meant to be."
    s hm "So to have that all taken away..."
    s wut "Because of something that wasn't even my fault!!"
    $l_exp = "sad"
    l "I get that, Krag. Believe me, I've been vocal about how unfair you were treated, as well."
    s hm "Well, it didn't matter. Everyone's minds were already made up."
    s "And I just felt so..."
    s "..."
    s wut "Well, 'angry' doesn't do it justice."
    s "It's like in that period of time, I finally 'became a REDD'."
    s "I just couldn't stop picturing what it was like to see all of those protesters flattened on the street or set ablaze."
    s jeer hat "How their screams of pain and begs for mercy would sound so pleasant to my ears."
    s "It just felt so..."
    s evilgrin "{i}Wonderful.{/i}"
    $l_exp = "shocked"
    "He was actually starting to scare me."
    $l_exp = "concerned"
    "But I have to stay calm and in control."
    l "So you decided to put on a show where you'd get to kill people?"
    s rightdown jeer "It was only fitting; the REDD War was just around the corner."
    s huh "The biggest issue was location."
    s "If the War wasn't going to be local, then there would be no point."
    $l_exp = "mad"
    l "And that's when Reddington got involved?"
    s hat laugh "My, my. You certainly have quite the brain in there."
    s rightdown jeer "You see, my brother is a very well-respected member in the REDD military."
    s "He's one of the few REDD who have close connections with Lord Reddington."
    s laugh "So having him set up a meeting between us wasn't as difficult as you'd think."
    s wut "Though the guy is just as intimidating as you'd expect him to be, if not more so."
    $l_exp = "wut"
    l "...I see."
    s jeer "Anyway, I spoke with Reddington about my situation and how I wanted one of the War Zones to be located in Atlanta."
    s laugh hat "It felt like a natural pick, anyway. A large city that's never been picked while in an area of the country that REDD War activity is seldom seen in was bound to be chosen eventually."
    $l_exp = "concerned"
    l "But why would Reddington make Atlanta one of the five War Zones just because you wanted him to? I'm sure he gets requests all the time from REDD with more tendency to take advantage of the REDD War."
    s wut rightdown "Oh, absolutely. He even told me as much."
    s huh "I'm not sure whether it was because I was Trosh's brother or if he truly wanted to see if I would go through with it or whatever."
    s jeer hat "But he accepted my offer. He even offered to fund the entire show from his own pocket!"
    s "And not only that, but he told... no, {b}promised{/b}! That if this 12-hour extravaganza went well..."
    s laugh "He'd be the main producer for the main TV series, no matter how low the ratings!"
    s "I'd be free to continue making episodes of Mr. Sprinkles forever!"
    s hm "But, well..."
    s "A certain someone had to go and spoil the fun."
    $l_exp = "wut"
    l "So, you did all this just so you could keep making your show?"
    l "Even if it was just an audience of no one?"
    l "Even if the entire world literally wanted your head on a pike?"
    s rightdown wut "You just don't get it, do you?"
    s "Having an audience doesn't matter to me."
    s hat "What matters is I was able to continue doing what I love."
    $l_exp = "mad"
    l "But at what cost, Krag?"
    l "Is it really worth being hated by those who loved you?"
    s hm "Believe me, I would've loved the circumstances to be different."
    s jeer "Having more fans means having more money."
    $l_exp = "wut"
    l "...really?"
    $l_exp = "mad"
    l "I don't believe for a second that you only loved having fans for the money."
    s wut "..."
    $l_exp = "concerned"
    l "You said it, yourself: being Mr. Sprinkles made you loved."
    l "But now, after this live show, you'll be lucky if anyone who used to be a fan of yours will continue to love you."
    l "That has to be eating at you."
    s "..."
    l "It's like I told you: you're not most REDD."
    $l_exp = "sad"
    l "You actually care about humans."
    l "Not many REDD seem to care about anyone, much less a human."
    l "But you..."
    $l_exp = "surprised"
    l "..."
    $l_exp = "smile"
    l "Here. Let me show you something."
    "I reached into my pocket and pulled out my phone."
    "After opening my gallery, I pointed the screen at him."
    show cg photo zorder 3 with dissolve
    pause 0.5
    l "Do you remember these girls?"
    s "..."
    "He slowly approached the phone to get a better look at the picture."
    s "..."
    s "Yeah... I do, actually."
    s "I pretended the girl on the left was my reflection."
    l "That's right."
    l "Those are my daughters. Before this show started, they were as happy and excited as any child would be."
    $l_exp = "surprised"
    l "But now?"
    $l_exp = "sad"
    l "Now they don't have a father."
    l "Now they must be worried sick about whether or not they'll see their mother again."
    l "Now they must be so scared and horrified by what you've done."
    s "..."
    show sprinkles hm rightdown
    hide cg photo with dissolve
    pause 0.1
    "I put my phone away."
    l "Krag, you need to see the bigger picture of what you've done tonight."
    l "You may have been trying to save your show, but at what cost, man?"
    l "Ruining the lives of all these children? Children who didn't do anything to hurt you?"
    s @ wut "..."
    s "Well... does it really matter now, anyway?"
    s "What's done is done."
    s "Those people are still dead. My show is still ruined."
    s wut "And Reddington is still going to kill me."
    $l_exp = "surprised"
    l "Well, you're right about what's done being done."
    $l_exp = "sad"
    l "But your future doesn't have to be so grim."
    l "You can still find ways to get through this."
    s hm "Ha. Such as?"
    l "You'll need to hide. Stay off the grid. Go somewhere where nobody will find you."
    s wut "No such place exists."
    s "Reddington will find me no matter where I go."
    l "It's still something, Krag."
    l "If you play your cards right and hide until this situation is forgotten about, or at least out of the public mind, you can have a chance to start over."
    s hm "..."
    s "You truly don't understand."
    s wut "I don't {b}want{/b} to start over. I {b}can't{/b} start over!"
    $l_exp = "mad"
    l "Well, there are a lot of things I want right now, but I just can't have them."
    $l_exp = "concerned"
    l "But if you want to have any chance of living--"
    $l_exp = "surprised"
    s huh "Why do you even care so much, anyway?"
    s "Why are you pushing me so hard to try and fix this when I don't deserve it?"
    $l_exp = "mad"
    l "Because you're wrong, Krag."
    l "You {b}do{/b} deserve it! {b}Everyone{/b} deserves a second chance!"
    l "The question is are you willing to accept one."
    s hm "..."
    $l_exp = "sad"
    l "Krag..."
    l "I can't promise what the future holds."
    l "I don't know how many people will forgive you."
    $l_exp = "smile"
    l "But that's the biggest difference between humans and REDD:"
    l "Humans have compassion and empathy. We can look at things objectively and see things from other perspectives."
    l "Look at me, for example. I didn't shoot you despite everything you've done."
    l "That's because I see what you're going through. I can understand why you did what you did."
    $l_exp = "wut"
    l "Do I agree with why you did it? Not really."
    $l_exp = "surprised"
    l "But I can at least see it from your eyes and figure out why you did it."
    $l_exp = "smile"
    l "And if I can do it, so can any other human."
    l "If you go into hiding for a bit, come back and explain your side of the story..."
    $l_exp = "excited"
    l "Well, you never know who will understand you, too."
    s wut "..."
    $l_exp = "determined"
    l "What do you say, Krag?"
    s "I..."
    $l_exp = "surprised"
    "He covered his mouth and looked up, as if he was on the verge of tears."
    s "I don't know."
    s hm "The truth is, your compassion and forgiveness is something I've never understood about you humans."
    s "With REDD, it's 'if you mess up, kiss your ass goodbye'."
    s wut "But humans..."
    s "You... you're so..."
    "He took another deep breath and wiped his eyes."
    s jeer "Alright. We'll go with your plan."
    $l_exp = "smile"
    l "I'm glad to hear it."
    s "Thank you. Really."
    $l_exp = "determined"
    l "Any time."
    s hat happy "If you don't mind, I'd, uh... like some time alone."
    s jeer "I'm gonna need to think of a hiding spot, after all."
    l "Fair enough."
    s rightdown "Thanks again. I truly do mean it."
    $l_exp = "smile"
    l "Just take it easy, okay?"
    s laugh "Will do."
    stop music fadeout(5.0)
    $quickhide = True
    hide screen laura
    window hide
    pause 1
    scene bg basement_hall
    with Dissolve(3.0)
    pause 1
    $l_exp = "neutral"
    $quickhide = False
    show screen laura
    window show dissolve
    pause 0.1
    "I sat by one of the stage curtains (the one that wasn't burned up) and let out a huge sigh."
    "That truly was more difficult than I had expected."
    $l_exp = "surprised"
    play sound footsteps
    "I heard footsteps approaching."
    show trosh hips intrigued at middle with dissolve
    pause 0.1
    t "Well?"
    $l_exp = "smug"
    l "We're all good to go."
    l "He's agreed to go into hiding until more people are willing to forgive him."
    t concerned "Wow. I'm actually impressed."
    l "Never underestimate the power of humans."
    t "Hm..."
    $l_exp = "neutral"
    l "Speaking of which, where are all the audience members?"
    t "Scattered across the theater."
    t "None are in this backstage area, at least that I've found."
    t "Well, outside of the hostages who never got the chance to play the games."
    $l_exp = "smile"
    l "But they're all safe?"
    t "I haven't been walking around the place, since I don't wanna spook them and cause a frenzy."
    t smile "But yeah. It seems like they're safe."
    l "That's good to hear."
    t "..."
    t "You know, I never thought I'd say this to a human, but..."
    t "You did good."
    $l_exp = "smug"
    l "{b}We{/b} did good, Trosh."
    t "Heh. Yeah, I guess {b}we{/b} did."
    t concerned "But it's like I told you--"
    $l_exp = "determined"
    l "Don't worry. I won't tell anyone that you helped."
    l "And if someone were to ever find out, we can just say that I blackmailed you or some shit."
    t laugh "Hahaha! Not sure how many REDD would believe that."
    l "Hey, I'm just trying to help here!"
    $l_exp = "smile"
    "We both then let out a laugh."
    t intrigued "Hey, uh..."
    t "Does Krag know that I'm still here?"
    $l_exp = "surprised"
    l "I'm not sure, actually."
    t smile "I guess the least I can do is check up on him and see how he's doing."
    $l_exp = "excited"
    l "Great idea! I really feel like he needs that right now."
    hide trosh with dissolve
    pause 0.1
    $l_exp = "smile"
    "Trosh then went around the corner and out of sight as he went towards the dressing room."
    "Well, all things considered, everything turned out okay."
    $l_exp = "sad"
    "It sucks that so many people still died here, but..."
    $l_exp = "smile"
    "At least a good amount were still saved."
    "At least some children could return home with both of their parents."
    "At least most of the children could return home with at least one parent."
    "..."
    $l_exp = "neutral"
    "I then felt my eyelids get heavy."
    "Geez, I've had way too long of a night."
    "I guess now's a good time to try and get some rest."
    "I then slowly started to close my eyes."
    $l_exp = "shocked"
    t "{b}OH MY GOD!!!{/b}"
    "My eyes sprung open as I turned towards the hall Trosh went down."
    "What happened? What's wrong??"
    "I quickly got up and ran towards Trosh's voice."
    $l_exp = "surprised"
    "The hallway was empty, but the dressing room door was wide open."
    "I ran inside to see what the problem was."
    $l_exp = "shocked"
    "When I did..."
    l "Oh..."
    l "My..."
    l "God..."
    hide screen laura
    window hide dissolve
    scene bg flash
    with Dissolve(1.0)
    pause 1
    play audio dramatic
    scene bg floor
    show cg deadsprinkles1
    pause 2
    show white zorder 2
    pause 0.1
    show cg deadsprinkles2
    play audio dramatic
    hide white
    pause 2
    show white zorder 2
    pause 0.5
    play audio dramatic
    show cg deadsprinkles3
    hide white
    pause 3
    show screen laura
    window show dissolve
    "..."
    "I couldn't believe what I was looking at."
    "This... can't be real."
    "It just... can't!"
    "Trosh was crouched next to Krag, staring in shock and awe."
    "He then slowly turned towards Jessica, who was facing down towards her lap, not moving a muscle."
    t "How the... how did..."
    $l_exp = "surprised"
    "I slowly walked over to Jessica."
    hide cg deadsprinkles3
    show bg dressingroom_blur:
        xalign 0.5 yalign 0.5
        zoom 1.15
    with dissolve
    pause 0.5
    show cg jessicainsane1
    with Dissolve(1.0)
    pause 0.5
    "I tried to look at her face, but it was covered by her hair."
    l "J... Jessica?"
    l "W-What happened?"
    play sound "audio/voice/jessica_giggle.ogg" loop
    "I could then hear some soft giggling come from her."
    "It's the most I've heard out of her in hours."
    l "Jessica?"
    $l_exp = "sad"
    l "Jessica!"
    hide screen laura
    window hide dissolve
    $giggle_timer = renpy.random.randint(1, 3)
    if giggle_timer == 1:
        pause 2
    elif giggle_timer == 2:
        pause 2.5
    else:
        pause 3
    play music shattered_mind
    show cg jessicainsane2
    with Dissolve(0.2)
    play sound "audio/voice/jessica_laugh.ogg" loop
    show cg jessicainsane2:
        linear 45.0 zoom 1.15
    show bg dressingroom_blur:
        linear 45.0 zoom 1.0
    pause 2
    $l_exp = "shocked"
    show screen laura
    window show dissolve
    pause 0.1
    "She wouldn't stop laughing."
    "She just stared blankly ahead and laughed like a maniac."
    "..."
    $l_exp = "sad"
    "..."
    "She's officially lost it."
    "All the torture..."
    "All the pain..."
    "It's all destroyed her brain."
    "And it's brought her to this."
    "To murder."
    "And seemingly no understanding of the consequences."
    "..."
    "I looked back down at Krag."
    "No signs of breathing."
    $l_exp = "crying"
    "Damn it."
    "Damn it!!"
    $l_exp = "angry"
    l "{b}{i}DAMN IT!!!{/i}{/b}"
    scene bg dressingroom
    "I stood up and slammed my fist against the counter."
    "It fucking hurt, but I didn't care."
    l "This wasn't how this was supposed to go!!"
    l "This wasn't supposed to happen!!"
    "I slammed my fist against the counter 3 times in a row, giving a loud {b}'FUCK!!'{/b} with each one."
    $l_exp = "crying"
    "I took a deep breath and turned towards Trosh, who was still staring at his dead brother."
    l "T-Trosh, I--"
    t "Please..."
    t "Just... leave me alone with him."
    l "..."
    $l_exp = "sad"
    l "..."
    l "...okay..."
    "I said in a near-whisper."
    stop sound fadeout(5.0)
    stop music fadeout(5.0)
    $quickhide = True
    hide screen laura
    window hide
    pause 1
    scene bg basement_hall
    with Fade(1.0, 1.0, 1.0)
    pause 1
    play music vast_places
    $quickhide = False
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    I put Jessica back in the closet.

    I made sure to face her towards the back this time so she couldn't reach the handle.

    Even then, she still wouldn't stop laughing.

    After that, I slowly walked back towards the stage.

    {clear}

    All that effort...

    All that work...

    All that hope...

    For nothing.

    {nw}

    Krag is dead.

    Jessica killed him.

    I gave her the weapon she used to kill him.

    That can't possibly be my fault, though, right?

    I gave her that cane to defend herself.

    ...

    {clear}

    That... wasn't self-defense.

    She techincally broke REDD War rules...!

    It's not like Krag threatened her as soon as she came in!

    ...

    ...right?

    ...
    """
    $nvl = False
    $l_exp = "angry"
    show screen laura
    window show
    nvl hide
    with dissolve
    pause 0.1
    "I screamed as loud as I could into the open hallway."
    l "{b}FUCK YOU, REDD WAR!!!{/b}"
    l "{b}FUCK!!! {i}YOOOUUUUU!!!!!{/i}{/b}"
    $l_exp = "crying"
    "I then leaned my head back and starting crying."
    l "Please..."
    l "Just let this goddamn piece of shit night be over already!"
    "I then tightly closed my eyes and continued to cry."
    "There are only about 2 more hours left until this fucking War ends."
    "And they can't get here soon enough."
    hide screen laura
    window hide dissolve
    stop music fadeout(3.0)
    pause 1
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 1.75
    stop music
    hide black
    window show
    d "Mom??"
    $l_exp = "shocked"
    show screen laura
    pause 0.6
    "That voice...!"
    l "Dakota??"
    d "MOM!!"
    $l_exp = "crying"
    l "DAKOTA!!"
    "I bolted towards that voice. It was coming from the hall that led to the lobby."
    scene bg lobby with dissolve
    pause 0.1
    "When I got into the doorway that led to the lobby, I saw nobody in the room."
    "At least, at first."
    "Towards the main entrance was--"
    l "Dakota! Kate!"
    show dakota bawl side at two1
    show kate crying fidget at two2
    with dissolve
    pause 0.1
    k "Mommy!!"
    "Both girls ran towards me, and I towards them."
    "I can't believe it! They're alive!"
    "They're safe! They're--!"
    $l_exp = "concerned"
    show dakota sad
    show kate shocked
    "...they're stopping and pointing at me."
    d "{b}MOM, BEHIND YOU!!{/b}"
    $l_exp = "surprised"
    "I stopped and turned around."
    hide dakota
    hide kate
    with easeoutleft
    show jingle yell axe at middle zorder 2 with easeinright
    play music shattered_mind
    $l_exp = "shocked"
    "Oh, fuck!!"
    "She then swung the axe down at me, but I was barely able to dodge it by jumping to the side!"
    show jingle evil_grin
    "She then turned to me with a psychotic smile."
    ji "You may have stopped the show..."
    ji angry "...but the War's not over yet, bitch!!"
    "She then swung again, with me barely dodging it before falling down on my ass."
    $l_exp = "crying"
    "No. It can't end like this."
    "After everything..."
    "Not like this!"
    "Not in front of my little girls!"
    show jingle evil_grin
    "She then raised her axe again."
    ji "Thanks for playing~!"
    show jingle yell up:
        linear 0.1 xalign 0.55
        linear 0.1 xalign 0.5
    $l_exp = "surprised"
    ji "Gah!!"
    "Her head suddenly jerked back as her axe fell out of her hands."
    "I was quick to get out of the way before it hit me."
    "After that, I crawled back and away from her."
    $l_exp = "shocked"
    "And I was surprised at what I saw:"
    show kate down mad at two2_short zorder 1 with dissolve
    pause 0.1
    "Kate was pulling on one of Jingle's twin tails!"
    k "{b}LEAVE MY MOMMY ALONE!!!{b}"
    show jingle:
        linear 0.1 xalign 0.55
        linear 0.1 xalign 0.5
    show kate:
        linear 0.1 xalign 0.85
        linear 0.1 xalign 0.8
    "Kate then yanked hard, which seemed to disorient Jingle even more!"
    ji angry down "Get off me, you fucking brat!!"
    $l_exp = "surprised"
    d "She's not a brat, you idiot!!"
    show dakota side mad at two1_short with dissolve
    pause 0.1
    "Dakota then ran over and yanked on the other twin tail!"
    show jingle:
        linear 0.1 xalign 0.45
        linear 0.1 xalign 0.5
    show dakota:
        linear 0.1 xalign 0.2
        linear 0.1 xalign 0.25
    ji "Gah!!"
    show jingle:
        linear 0.1 xalign 0.55
        linear 0.1 xalign 0.5
    show kate:
        linear 0.1 xalign 0.85
        linear 0.1 xalign 0.8
    ji "Argh!!"
    ji "You goddamn {b}cunts{/b}!!"
    show jingle up
    show kate concerned
    show dakota sad
    "Jingle then reached and grabbed each of my daughters by the arm."
    $l_exp = "shocked"
    show dakota bawl
    show kate crying
    "And seemingly squeezed them as tight as she could!"
    "It seemed to do the trick, as they let go of her hair."
    show dakota:
        ease 0.25 left_short
    show kate down:
        ease 0.25 two1_short
    show jingle down:
        ease 0.25 right
    "With that, Jingle quickly turned around and threw them to the ground!"
    ji yell"{b}YOU'RE FUCKING DEAD!! BOTH OF YOU!!!{b}"
    $l_exp = "rage"
    "Not on my fucking watch!!"
    "Without any hesitation, I picked up the axe and sprinted at her!"
    "Before I realized what I was doing...!"
    stop music
    play sound hammer
    call gunflash
    show blood zorder 5
    show dakota neutral
    show kate shocked
    hide jingle
    pause 2
    $l_exp = "surprised"
    show dakota bawl:
        ease 1.0 two1
    show kate fidget crying:
        ease 1.0 two2
    show blood:
        ease 1.0 alpha 0.0
    pause 2
    k "M... Mommy...?"
    $l_exp = "crying"
    l "..."
    "I dropped down to my knees and extended my arms to the side."
    "On cue, my daughters bolted towards me and hugged me as tight as they could, with me wrapping my arms around both of them like a boa constrictor."
    play music packing
    "Loud sobs from all three of us could be heard echoing through the lobby."
    d "I love you, Mom!! I love you!!"
    k "I love you, too, Mommy!!"
    l "I love both of you so much! God, I really do!!"
    "I gave each of them a long, hard kiss on the top of the head before going back to placing my head between them."
    "Yes, I was covered in blood."
    "Yes, they've witnessed me kill someone."
    "Yes, they've witnessed a lot of people being killed tonight, including their father."
    "But none of that mattered right now."
    "My babies were alive and in my arms."
    "At this point in time, literally not a single other thing matters."
    k "M... Mommy?"
    l "Yes, Kate?"
    k "I liked her better... when she didn't talk."
    d "Or use props!"
    "I couldn't help but start laughing through my tears."
    l "Me, too, girls. Me, too."
    hide screen laura
    window hide dissolve
    pause 1
    scene bg fade
    with Dissolve(2.0)
    pause 2
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    After we finally let go of each other, we walked around the theater to try and find anyone else.

    There were a lot of them in a spare janitor's closet that the girls said they hid in earlier.

    After getting settled in, we huddled together.

    We didn't really say much; after everything that's happened, what {b}could{/b} we say?

    The other families in there with us seemed to have the same idea.

    {nw}

    But to everyone's surprise, time was moving faster than expected.

    Because before we knew it...
    """
    nvl hide
    pause 0.5
    play sound siren
    pause 8
    if not persistent.scenes["ch5_s4"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch5_s4"] = True


label epilogue:
    if not renpy.music.get_playing() == audio.packing:
        play music packing
    python:
        currenttime = "6:09 PM"
        currentdate = "June 7th"
        clothing = "main"
        l_exp = "neutral"
        b_name = "Bartender"
        nvl = False
    play sound2 flicker
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
    $renpy.pause(delay=5)
    hide screen dateandtime
    with Dissolve(2.0)
    pause 2
    play ambience crowd fadein(2.0)
    scene bg bar
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    "I sat down at the stool."
    stop sound
    b "Hey, there she is!"
    $l_exp = "smug"
    "I gave a small chuckle and wave."
    b "What can I get ya?"
    $l_exp = "determined"
    l "Ginger ale, please."
    b "Heh. You're probably the only regular we've got at this bar that doesn't order alcohol."
    $l_exp = "smug"
    l "I have my reasons, you know."
    b "Yeah, I know. It's just funny, that's all."
    $l_exp = "neutral"
    "He then grabbed a can of ginger ale from behind the counter and poured it into a glass of ice."
    "After accepting it and thanking him, he nodded and walked away."
    "As I took a sip, I could hear the news on the bar's TV."
    a "Prosecutors say they're confident the jury will choose the 'correct' verdict in the trial of Jessica Tate."
    $l_exp = "concerned"
    "Curious, I turned towards the TV."
    $renpy.music.set_volume(0.25, delay=0.5, channel="ambience")
    hide screen laura
    scene bg newsroom with dissolve
    pause 0.1
    a "The insanity plea the defense has been fighting for has certainly been in their favor, and the responses from protesters outside the courthouse and social media are in favor of Tate."
    a "However, the prosecution is convinced that their evidence and logic of how the murder of Krag Dovason felt too planned-out to be executed by an insane person will be enough to get Tate a 'guilty' verdict."
    a "With the final day of trial taking place next week, the world sits in anticipation on whether or not 38-year-old Jessica Tate will find herself in a mental institution or a prison."
    $renpy.music.set_volume(1.0, delay=0.5, channel="ambience")
    show screen laura
    scene bg bar with dissolve
    pause 0.1
    "I sighed and took another sip."
    "Admittedly, I haven't been following the updates of the trial as much as I probably should have."
    $l_exp = "sad"
    "But as someone who was there..."
    "The look in her eyes..."
    "That wasn't the look of a premeditated murderer."
    $l_exp = "concerned"
    "I'm sure the jury will be in favor of her, but I guess time will tell."
    $l_exp = "surprised"
    woman "Excuse me."
    "I turned around and saw a woman staring at me."
    woman "Y-You're that woman from the Sprinkles show during the REDD War, right?"
    $l_exp = "concerned"
    l "...I was there, yes."
    woman "You... saved everyone, right?"
    l "..."
    l "Yeah, you could say that."
    $l_exp = "surprised"
    "She then came closer and hugged me."
    woman "Thank you!"
    $l_exp = "concerned"
    l "You're, uh... welcome."
    "She broke from the hug, wiping some tears as she did."
    woman "Heh. I'm sorry. It's just..."
    $l_exp = "sad"
    "She wiped her eyes again."
    woman "That night was just..."
    woman "I-I really thought I was going to die."
    woman "In fact, from what I understand, I {b}was{/b} going to die."
    woman "So the fact that I'm still here because of your bravery..."
    woman "It means a lot. To me and so many others."
    woman "You're a hero."
    $l_exp = "smile"
    l "I appreciate all that; thanks."
    woman "Can I get you a drink or something?"
    $l_exp = "smug"
    l "That's not necessary, I promise."
    woman "Are you sure?"
    l "Positive. But I appreciate the gesture."
    woman "Still, you deserve some sort of reward or recognition!"
    $l_exp = "neutral"
    l "Probably, but if it's all the same to you..."
    $l_exp = "sad"
    l "...I just wanna put that night behind me and focus on my life going forward."
    woman "I understand."
    woman "Well, it was nice to meet you."
    $l_exp = "smile"
    l "Same here."
    woman "I'm truly grateful for what you've done. Thanks again!"
    $l_exp = "determined"
    l "Any time."
    "With that, she walked away and I turned back towards the bar."
    $l_exp = "neutral"
    "She's not the first person I've had approach me because of my actions from that night."
    "I've had a lot of hostages thank me for everything, one of whom was the mother of Rodney, the child who was killed on stage."
    $l_exp = "sad"
    "That one in particular was an emotional one, but she was still thankful that her daughter and other son made it through the night, as well."
    "It really made me happy that I got through the night with both of my children in one piece."
    $l_exp = "concerned"
    "Physically, at least."
    $l_exp = "neutral"
    "I gulped the rest of my ginger ale and asked the bartender for another."
    "As he poured it, he struck up a conversation."
    b "So, how's the house remodeling going?"
    $l_exp = "concerned"
    l "About as well as you'd expect."
    l "I'm just glad REDD insurance is covering the damages."
    b "Hey, that's what it's there for, after all."
    $l_exp = "smug"
    l "Yeah, I know."
    "He then handed me my refill."
    $l_exp = "concerned"
    l "Though it makes paying for everything else less of a financial headache."
    l "The bills, the groceries..."
    $l_exp = "sad"
    l "...the therapy sessions..."
    b "Yeah, I can only imagine."
    b "Your girls getting better?"
    $l_exp = "concerned"
    l "Well, my youngest can finally start to look at a picture of Mr. Sprinkles without covering her face and crying, so there's progress, I suppose."
    l "Though she's still way too reclusive for my liking."
    l "And my oldest..."
    $l_exp = "sad"
    l "I just get this feeling that she blames herself for everything that happened."
    l "As if her being a dick to her dad is the reason he's... you know..."
    b "Sure."
    b "What about you? You went through more hell than them, it seems."
    $l_exp = "concerned"
    l "Heh."
    l "I guess I'm getting there."
    l "Sleeping in a one-person bed at the in-laws' place has helped me get over the mindset of waking up next to him, but..."
    $l_exp = "sad"
    l "The nightmares still come and go."
    b "The in-laws still mad at you for what happened to your husband?"
    $l_exp = "concerned"
    l "If they are, they're not showing it as much as they did."
    l "I still remember Buck claiming that he'd rather see me on the streets than house the woman who convinced his son to stay in Atlanta during the REDD War."
    $l_exp = "smug"
    l "Fortunately, though, they love their granddaughters more than they hate me."
    $l_exp = "neutral"
    "I took another drink and sighed."
    l "So, yeah. Could be a hell of a lot better, but a hell of a lot worse."
    b "Well, if nothing else, you survived the REDD War."
    b "That's not something a lot of people in Atlanta can say."
    $l_exp = "smug"
    l "Kinda hard for a dead person to say anything, wouldn't you agree?"
    "He rolled his eyes and draped his rag on his shoulder."
    b "Hey, uh, if you don't mind me asking..."
    $l_exp = "neutral"
    l "Look, you're a nice guy, but I'm not ready to start dating again."
    "He just closed his eyes and gave a soft chuckle."
    b "That's not at all where I was going, but good to know."
    $l_exp = "surprised"
    l "Oh."
    $l_exp = "sad"
    l "S-Sorry."
    b "You're good."
    b "What I was {b}going{/b} to ask was..."
    b "...how did you manage to pull that big show-stopper of yours?"
    $l_exp = "neutral"
    l "..."
    b "I know you said you wanna put that night behind you, but I'm curious how you pulled that off without the guards getting ya."
    "I shrugged and took another sip."
    l "Doesn't matter. What matters is the show was stopped and lives were saved."
    "He grinned at me before slowly nodding."
    b "Yeah, you're right."
    man "Excuse me, bartender?"
    "He looked towards the patron for confirmation before giving me a quick nod and walking over to him."
    $l_exp = "sad"
    "I gave a small sigh and looked into my drink."
    "I haven't seen or spoken to Trosh since I left him with his brother's body."
    "To be fair, I have no way to contact him, but I'm curious as how he's feeling."
    "Is he still mourning his death? Has his REDD mind gotten past it already?"
    "It truly does make me wonder..."
    $nvl = True
    hide screen laura
    nvl clear
    nvl show dissolve
    narrate """
    With that, I sat in mostly silence while I continued to drink.

    I caught some more stuff from the news, such an interview with Madeline's parents and how what Jessica did was something everyone would've done if they had the chance.

    I gave a small scoff at that.

    There was even a quoted tweet from Lord Reddington about how on one hand, she did technically break REDD War rules, but on the other hand, he can't be too angry at her for killing someone, as the hypocrisy would be astounding if he did.

    Well, that wasn't his exact reason for not being too angry, but reading between the lines wasn't hard to do.

    {clear}

    A while later, a live interview with Georgia senator Peter Carson was broadcast.

    He wasn't necessarily angry towards Jessica or Krag, but rather the concept of the REDD War, as a whole, saying things like \"This would have never happened if the REDD War didn't exist.\" and \"There are children who are now orphaned because of what the REDD War allowed.\"

    He was careful with his words, but it was clear that he was throwing shade at Lord Reddington.

    Politics, I tell ya...
    """
    $l_exp = "neutral"
    $nvl = False
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    "Finally, I was ready to head home for the night."
    "I reached into my purse to grab my credit card."
    $l_exp = "shocked"
    "..."
    "I felt something smooth and waxy."
    "I slowly took it out."
    $l_exp = "concerned"
    "...as I thought."
    "It was the playing card that Jangle pulled out of Dakota's ear."
    "..."
    "I put it back into my purse and dug around for the card I needed."
    "After paying my tab, I left the bar and returned to my vehicle."
    stop ambience fadeout(1.0)
    scene bg fade with dissolve
    pause 0.1
    "..."
    "I sat in the driver's seat and stared out the windshield for what felt like several minutes."
    "Finally, I took out my phone and scrolled through my gallery."
    "Eventually, I found it."
    hide screen laura
    window hide dissolve
    show white:
        alpha 0.0
        ease 1.0 alpha 1.0
    pause 2
    scene cg photo
    with Dissolve(3.0)
    pause 2
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    I feel like most people would've erased any ties and connections to that night.

    Honestly, part of me feels like I should.

    But...

    When I look at this picture, my mind doesn't jump to the bad things that happened that night.

    Instead, I look at how happy my little girls are.

    How this was the last photo I ever got of them when they were still happy.

    When they were just innocent kids who didn't have firsthand experience of the horrors the REDD War brings.

    They may never fully recover from that night.

    They may spend the rest of their lives bitter and upset at the the things that happened.

    But when I look at this picture, I can assure myself that that night wasn't all bad.

    That some joy and happiness was found from the Farr family on March 31st, 2030.
    """
    nvl hide
    pause 3
    nvl clear
    nvl show dissolve
    narrate """
    I don't think the REDD War is going anywhere.

    Even after the whole Mr. Sprinkles fiasco, something people are already calling 'the biggest tragedy in REDD War history', I don't think it's gonna stop.

    If anything, the REDD are just gonna protest to add more things in their favor.

    Fortunately, now that the REDD War has happened in Atlanta, it shouldn't take place here again.

    ...at least, I hope it doesn't...

    Regardless, we've survived the worst event in modern human history.

    Like the bartender said, not everyone was so lucky.

    I'm reminded of that every time I glance down at my wedding ring.

    But if my girls and I can get through the REDD War, then what can stop us?

    {clear}

    No matter what happens now, all 3 of us will be together.

    As long as that's true, nothing will stand in our way.
    """
    nvl hide
    pause 2
    show cg photo_blur
    with Dissolve(3.0)
    $goodcredits = True
    jump gameover
