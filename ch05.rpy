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
    play sound "audio/se/locked door.ogg"
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
    s "Ahaha! I hope to see you all back here in 15 minutes!"
    show screen laura
    pause 0.6
    "I wasn't even aware I was that close to the stage."
    $l_exp = "neutral"
    show sprinkles jeer rightdown cane at middle_sprinkles with dissolve
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
    s "I don't wanna spoil anything big for ya, but I will say this:"
    s evilgrin "The only way those hostages will leave this theater is in a body bag."
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
    show sprinkles happy rightdown leftdown at middle_sprinkles with dissolve
    pause 0.1
    "As he opened the door, he started walking back towards the stage."
    show sprinkles wut
    "He paused when he noticed me."
    s "..."
    l "..."
    s hm "..."
    "He then continued walking forward, but still had that suspicious look on his face."
    hide sprinkles with dissolve
    pause 0.1
    $s_name = "Mr. Sprinkles"
    $l_exp = "sad"
    "I better get out of here fast."
    "I walked down further into the back, just looking for anywhere to hide."
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
    show jessica at middle with dissolve
    pause 1
    "She didn't seem to pay mind to my presence."
    "Her blank stare ahead really made me question if she was actually still alive."
    "Though a quick blink proved otherwise."
    show helmet:
        ease 0.5 alpha 0.0
    "I took my helmet off and set in on the ground."
    hide helmet
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
    show jessica at middle
    with dissolve
    pause 0.1
    l "Come on."
    l "Let's get you out of here."
    hide screen laura
    window hide dissolve
    pause 1.5
    scene bg fade
    with Dissolve(2.0)
    pause 4
    $renpy.end_replay()
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
    show jessica at middle zorder 1
    show helmet zorder 3
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    l "Alright, I think you should be good..."
    "It was a bit of a hassle to get her up here."
    $l_exp = "concerned"
    "After getting the armor back on, I thought about how we were going to do this."
    "With her legs being a bit useless at the moment, there was no way she would be able to move on her own."
    $l_exp = "sad"
    "And she was wincing and groaning in pain with each bump up the step the chair made."
    $l_exp = "excited"
    "Well, at the very least, she was showing some kind of emotion."
    $l_exp = "neutral"
    "The nature of the chair she was in certainly made it a bit easier, though, as she was less likely to fall out as she went up."
    "Fortunately, when we got up, we were able to find a small closet that housed a wheelchair."
    "I guess it's for emergencies and/or theater guests who are unable to walk."
    $l_exp = "smug"
    "Well, I can't think of a more relevant use than this."
    $l_exp = "neutral"
    "After transferring her to the wheelchair, I put both her and the torture chair in the closet."
    $l_exp = "excited"
    l "Alright, you should be safe in here for now."
    l "I'll check up on you later. For now, I gotta find a way to stop Krag."
    j "..."
    $l_exp = "surprised"
    "Despite no longer being gagged, she's still not talking."
    "I don't know whether she's just too out of it or if she's just got nothing to say."
    $l_exp = "excited"
    l "It'll be alright, Jessica."
    l "I'll be back."
    hide jessica with dissolve
    pause 0.1
    $l_exp = "neutral"
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
    if persistent.gore:
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
    "Suddenly, Mr. Sprinkles and the guard entered the backstage area and stormed around the corner."
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
    $l_exp = "concerned"
    "Sprinkles then made a light growl."
    "After a few seconds of silence, he sighed and spoke."
    $l_exp = "neutral"
    s "If something like that happens again, you fire at the ceiling or grab the child by the arm."
    s "You do {b}not{/b} shoot them."
    s "Do I make myself perfectly clear?"
    redd "Yeah, I guess so."
    redd "Don't know why you're getting so pissy about this. I'm sure the REDD at the REDD Base are loving the fact that a human kid died!"
    redd "That certainly won't damage your ratings."
    redd "Hell, Reddington might even increase your budget if you ended the night by killing all the kids!"
    s "Stop talking right now."
    s "No more dead children. End of discussion."
    redd "Whatever, man."
    stop music fadeout(3)
    "The guard then walked back into view and towards the stage while it sounded like Sprinkles was headed further down the hall, possibly towards the dressing room he was in earlier."
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
    "..."
