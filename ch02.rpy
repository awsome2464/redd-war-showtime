label chapter_2:
    python:
        save_name = "Chapter 2"
        save_subtitle = "The Storm Approaches"
    call chaptername
label eveningplans:
    python:
        currenttime = "5:23 AM"
        currentdate = "March 31st"
        timeleft = "13 hours and 37 minutes"
        event = "REDD War begins"
        clothing = "pjs"
    stop music
    call chapterstart
    pause 1
    scene bg livingroom_night
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
    pause 0.1
    "I had made my way downstairs, where I found my husband watching the news on TV."
    $l_exp = "neutral"
    show screen laura
    show richard down concerned at middle
    with dissolve
    pause 0.1
    l "Has anything happened?"
    r crossed glare "Yes. A lot, actually."
    "He pointed to the screen."
    "The main headline along the bottom was {i}'MR. SPRINKLES' STAR KRAG DOVASON SPEAKS OUT AGAINST ATLANTA WAR ZONE ANNOUNCEMENT{/i}."
    $l_exp = "surprised"
    "This ought to be good."
    "I sat down and tuned in."
    play music autumn_changes
    scene bg newsroom
    hide screen laura
    with dissolve
    pause 0.1
    a "The actor took to Twitter last night, shortly after the War Zone announcement, to express his feelings about the news, saying, quote:"
    a "{i}I'm very heartbroken about the announcement {color=#00aced}@lordreddington{/color} made regarding {color=#00aced}#REDDWar2030{/color}. For those who were planning to go to the Mr. Sprinkles live show, I'll look into a solution.{/i}"
    a "A few hours later, Dovason made these Tweets:"
    a "{i}If you wish to not attend the live show tomorrow, I completely understand. Simply request a refund on the official site and it will be provided to you.{/i}"
    a "{i}However, for those who still wish to attend, first of all, thank you! {image=reddsmile.png} And secondly, I have been talking with Reddington, and he has agreed to recognize the theater as an official Government Safehouse.{/i}"
    a "{i}No matter which choice you make, I wish you, as well as everyone else, good luck. The next few days are going to be crazy. {color=#00aced}#REDDWar2030{/color}{/i}"
    $l_exp = "excited"
    scene bg livingroom_night
    show richard crossed glare at middle
    show screen laura
    with dissolve
    pause 0.1
    l "Wow. A Government Safehouse?"
    l "I wonder how many strings he had to pull to make that happen."
    r "..."
    $l_exp = "shocked"
    l "What's wrong?"
    r concerned "..."
    r "Nothing's 'wrong'..."
    $l_exp = "smug"
    "I stared at him for a second before giving a smirk and crossing my arms."
    l "You're debating whether or not to stay, aren't you?"
    r @ rage "..."
    r "..."
    r down smile "Alright. You've got me."
    $l_exp = "smile"
    l "See?"
    "I asked as I playfully pushed him away with a grin."
    l "I told you you just needed to wait and see what happens."
    r laughing "Yeah, yeah. You were right, as usual."
    "We could then hear footsteps coming down the stairs."
    show richard at two1 with easeinright
    pause 0.5
    show dakota neutral hips at two2_short with dissolve
    pause 0.1
    r smile "Good morning, Dakota."
    d "..."
    d "Are we staying in Atlanta tonight?"
    $l_exp = "neutral"
    l "Well, we haven't decided yet."
    $l_exp = "smile"
    l "But we just learned that Mr. Sprinkles's show is in one of the buildings that the REDD aren't allowed to attack."
    d confused "Really?"
    l "That's what the news says, at least."
    d "..."
    r crossed concerned "But like your mother said, we haven't decided yet."
    r "We still need to talk this over as a family."
    d "..."
    d neutral side "We'd really be safe?"
    d "Like, no REDD would kill us?"
    r "Yes, that's what was said."
    d "...{w}then..."
    d small_smile crossed "...maybe we could go see Mr. Sprinkles after all?"
    r glare "Dakota, that doesn't mean we can just go to the show."
    $l_exp = "neutral"
    d sad side "But Mom said it's at one of the safe places!"
    r "I know, but..."
    d mad "You just don't wanna go because you hate Mr. Sprinkles!"
    r down "That has nothing to do with this, Dakota!"
    stop music fadeout(3.0)
    d hips "You know what? You're right!"
    d "It's not because of Mr. Sprinkles!{w} It's because of me!"
    $l_exp = "concerned"
    r concerned "What are you talking about?"
    d "If Kate told you she wanted to stay, you'd say we could stay!"
    d side "But because {b}I{/b} want to stay, it's wrong!"
    r rage "That's not true at all!"
    d crying "Yes, it is!!"
    d "I never get what I want! It's always about Kate!"
    d "I wish she was never born so you would actually care about me!!"
    $l_exp = "shocked"
    r concerned "..."
    "The atmosphere was bone-chilling."
    "I wanted to scream at her for saying that, but..."
    "...I was in too much shock."
    "Richard seemed the same way."
    show dakota neutral
    "Even Dakota seemed to finally realize what she said in her fit of anger."
    "Before anyone could say anything else..."
    "...we heard what sounded like someone running up the stairs."
    "We all turned to see a quick blur go around the corner."
    "A blur the height of a 6-year-old."
    "Richard quickly bolted up the stairs after her."
    hide richard with easeoutleft
    pause 2.0
    show dakota sad:
        ease 1.0 middle
    pause 3.0
    d "I..."
    d "I didn't..."
    $l_exp = "surprised"
    l "Hey..."
    "I gave Dakota a hug of comfort and took a deep breath."
    l "You shouldn't have said that, but you seem to know that."
    menu:
        d "...are you mad at me...?"
        "\"Yes, a little.\"":
            $l_exp = "mad"
            l "Yes, a little."
            $l_exp = "neutral"
            l "But I won't ground you or anything over it."
            d crossed "...okay..."
            jump dakotaissorry
        "\"No, I'm not.\"":
            l "No, I'm not, sweetie."
            d "...you promise?"
            l "I promise."
            d crossed "..."
label dakotaissorry:
    "She then sighed and rubbed her eyes."
    play music vast_places
    d "I really am sorry, Mom."
    $l_exp = "sad"
    l "I know you are, Dakota."
    d side "Not just for what I said about Kate."
    d "I'm sorry for being so mad at Dad."
    d "I don't know why I got so mad at him like that."
    $l_exp = "neutral"
    l "Hey, this time of the year just brings out the worst in people."
    l "We're all scared and upset, Dakota."
    d neutral "...even you?"
    $l_exp = "sad"
    l "Are you kidding? I'm terrified!"
    l "There's no point in trying to sugarcoat it: people are going to be hurt, and much worse, once it's 7."
    l "They call it a REDD {b}War{/b} for a reason, after all."
    show dakota sad crossed
    "Dakota grabbed on me to even tighter."
    $l_exp = "concerned"
    "I guess telling that to an already-horrified 9-year-old wasn't the smartest idea."
    $l_exp = "surprised"
    l "But I can't stress enough how much I care about making sure we're all safe."
    d mad "So then why don't we just go to the show tonight?! We were gonna go there, anyway!"
    $l_exp = "neutral"
    l "I know."
    d hips "Dad doesn't seem to."
    $l_exp = "concerned"
    l "Well..."
    l "Your father wants to keep us all safe, as well; he just has a different way of doing it."
    l "He would just feel safer if we were outside of the War Zone, not inside of it."
    d sad "But..."
    $l_exp = "smug"
    "I gave a small chuckle and looked down at my little girl."
    l "You really wanna go see this show, don't you?"
    d mad "..."
    l "Hey, none of your friends are here to laugh at you for watching Mr. Sprinkles."
    d side "C-Cut it out, Mom!"
    l "Heh. Fine, I'll stop."
    $l_exp = "smile"
    l "Well, no matter why you want to go to the show tonight, I'll be sure to count your vote in the final decision."
    d neutral "..."
    "I then heard Richard walking back down the stairs."
    show dakota zorder 2:
        ease 0.5 two2_short
    show richard crossed concerned at two1 zorder 1 with dissolve
    pause 0.1
    $l_exp = "neutral"
    l "How is she?"
    "He didn't reply right away; he looked at Dakota with a look of disappointment."
    d sad "..."
    r "Kate's fine. She'll get over it pretty quickly."
    $l_exp = "smile"
    l "Well, that's good to hear."
    show richard glare
    "Richard continued to glare at Dakota."
    "I guess he's finally had time to think about what she had said."
    $l_exp = "mad"
    l "You can spare the lecture. She knows what she did wrong."
    l "Isn't that right, Dakota?"
    d crossed "Y-Yes... I'm really sorry, Dad."
    r "Well, I'm not the one you should be apologizing to."
    d "..."
    "More slow footsteps could be heard coming down the stairs."
    show dakota:
        ease 0.5 right_short
    show richard zorder 2:
        ease 0.5 middle
    pause 1
    show kate crying fidget at left_short zorder 1
    with Dissolve(1.5)
    pause 1
    k "Mommy?"
    $l_exp = "neutral"
    l "Yes?"
    k "Does Kota hate me?"
    show richard concerned
    $l_exp = "surprised"
    d side "No! I don't hate you, Kate! Don't ever think something like that!"
    k "But you said--"
    d "I know, and I'm so sorry! I didn't mean it!"
    show kate:
        ease 0.5 xalign 0.25
    "Despite Dakota's claim, Kate latched on to her father for comfort."
    r "..."
    r down smile "Hey, you know what I think would cheer us all up?"
    k confused "What?"
    show richard:
        middle
        ease 0.5 ypos 100
    "He then bent down to the same level as his daughters."
    r "Going to see Mr. Sprinkles tonight!"
    show kate shocked
    show dakota neutral
    $l_exp = "shocked"
    l "Richard...?"
    r laughing "What do you say, girls?"
    show kate happy up:
        xalign 0.25
        ease 0.25 ypos 80
        ease 0.25 ypos 100
        repeat
    k "Yeah! Mr. Sprinkles! Mr. Sprinkles!!"
    "Kate jumped in excitement while still holding on to Richard."
    r laughing "Alright, Kate. I can certainly see that you're happy."
    show kate:
        ease 0.5 ypos 0
    show richard:
        ease 0.5 ypos 0
    "Richard then picked her up with a chuckle and held her against him."
    r smile "Dakota? What do you say?"
    d small_smile crossed "...{w}yeah! Let's go!"
    r laughing "Alright, then! It's decided!"
    r "The Farrs are going to see Mr. Sprinkles tonight!"
    k "YAAAAAAY!!"
    show kate:
        ease 0.5 left_short
    "Kate clapped with joy as Richard put her back down."
    $l_exp = "smile"
    l "Alright, but don't forget that it'll be a long night, so be sure to get plenty of rest!"
    k down "I will!"
    "Richard then gave a small yawn."
    r crossed smile "I suppose we could all use some more shut-eye."
    r "Everyone back to bed; that's an order."
    k "Okay~!"
    d determined hips "Alright."
    scene bg livingroom_night
    hide screen laura
    with dissolve
    pause 0.1
    "The girls went back upstairs."
    "Honestly, I won't blame them if they don't actually fall back asleep."
    "I then looked at my husband with a cheeky grin."
    $l_exp = "smug"
    show richard down smile at middle
    show screen laura
    with dissolve
    pause 0.1
    l "Look at you being the world's greatest father."
    r crossed "Hey, it's like you said: tonight's about them."
    hide richard
    hide screen laura
    with dissolve
    "We looked at each other for a second or so before giving a slow, meaningful kiss."
    "After breaking apart, Richard sighed and rubbed his eyes."
    $l_exp = "neutral"
    show richard crossed smile at middle
    show screen laura
    with dissolve
    pause 0.1
    r "Alright, it really is going to be a long night; we should really get some sleep."
    l "We should."
    $l_exp = "smug"
    l "But..."
    "I then slowly ran my hand up his leg and onto his thigh."
    l "...I'm sure you've got SOME energy."
    r concerned "..."
    "He then took a peek towards the staircase."
    r down "You realize they might hear us, right?"
    $l_exp = "neutral"
    l "..."
    "I slowly took my hand off and nodded."
    l "You're right. Sorry."
    "I got up off the couch."
    $l_exp = "surprised"
    "I got up off the couch.{fast}.. but Richard reached up and grabbed my arm, pulling me down close to him."
    r smile "I'm sure the TV can drown us out."
    "He then reached over to the remote and raised the volume on the still-on TV."
    $l_exp = "smile"
    "We both giggled before he leaned over and kissed my neck."
    call sceneend
    if not persistent.scenes["ch2_s1"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch2_s1"] = True
    

label backstagedrama:
    python:
        currenttime = "2:42 PM"
        timeleft = "4 hours and 18 minutes"
        s_name = "Krag"
    call chapterstart
    pause 1
    scene bg dressingroom
    with Dissolve(2.0)
    pause 0.5
    play sound door_knock
    pause 2
    window show dissolve
    s "Come in!"
    play sound door_open
    pause 1
    show sprinkles happy rightdown leftdown at two1
    show madeline down blank at two2
    with dissolve
    pause 0.1
    s "Ah, Madeline! What can I do for you?"
    "Madeline" "\"You can start by explaining what's going on.\""
    s jeer "Now, Madeline, I would hate to insult your intelligence~"
    show madeline glare
    "Madeline" "\"Krag, the show is starting in 4 hours and the stage is empty!\""
    show madeline shrug
    "Madeline" "\"I'm not even seeing anyone rehearsing anything!\""
    "Madeline" "\"This live show is what could make or break our future, and it's like you're not taking it seriously! And frankly, it's really starting to piss me off!\""
    s hm "..."
    show madeline blank down
    "Madeline" "\"Krag, I'm saying all this because I want {i}Mr. Sprinkles{/i} to succeed. To get through this rough patch.\""
    s wut "And yet you told the network to put the show on a hiatus."
    show madeline glare
    "Madeline" "\"I could have told them to cancel it altogether, you know.\""
    "Madeline" "\"Believe me, I don't want to be in this situation any more than you do, but we need to think through this logically.\""
    show madeline blank
    "Madeline" "\"You're still relatively new to how show business works here on Earth. These things happen.\""
    s "..."
    s "{i}Mr. Sprinkles{/i} is an entire life's worth of ideas and planning put together at last."
    s "I'm not going to let anyone take my show away from me."
    show madeline glare
    "Madeline" "\"{b}Our{/b} show, Krag.\""
    "Madeline" "\"You may have created it, and you may be the title character, but you're not the {b}only{/b} character.\""
    "Madeline" "\"You're not the only one who loves to perform on the show. Seeing children's happiness from our antics is something I've treasured all these years.\""
    show madeline shrug
    "Madeline" "\"But you can't always get what you want, Krag.\""
    "Madeline" "\"Sometimes, there are situations that are hard to fix.\""
    show madeline down
    "Madeline" "\"I'm sorry, but that's just how it works.\""
    s hm "..."
    show madeline blank
    "Madeline" "\"That said, it's not impossible to fix this.\""
    "Madeline" "\"We need to do everything we can for this live show to be a success. Our careers depend on it. Understand?\""
    s "..."
    s jeer "Of course I do."
    s "I'll get to work on rehearsals."
    show madeline excited
    "Madeline" "\"Thank you.\""
    hide madeline with easeoutright
    pause 1
    show sprinkles:
        ease 1.0 middle_sprinkles
    pause 1.5
    s hat evilgrin "Oh, this show will be successful, don't you worry..."
    call sceneend
    if not persistent.scenes["ch2_s2"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch2_s2"] = True
    

label arriveatshow:
    python:
        currenttime = "3:51 PM"
        timeleft = "3 hours and 9 minutes"
        l_exp = "neutral"
        s_name = "Mr. Sprinkles"
        clothing = "show"
        k_hat = True
    call chapterstart
    pause 2
    show screen laura
    window show dissolve
    pause 0.1
    "We were finally on our way to the show."
    "We all tried our best to be happy, but in the back of our minds, we still had that fear about what was to come to our city at 7."
    "Having the radio on didn't really help, either; no matter where you went, there was something about the REDD War."
    "Even the normal FM channels didn't help with their constant ads."
    $l_exp = "concerned"
    "{i}'Come on down to Crazy Jack's Gun Barrel for all your REDD War needs, whether you be the predator or the prey!'{/i}"
    "You really can't escape this event if you tried."
    $l_exp = "neutral"
    "Eventually, we decided to just turn the radio off; I certainly wouldn't want the girls to be focusing on anything other than the live show."
    "It shouldn't be hard to do, since a certain child of mine used this time to watch a certain TV show on her tablet."
    play music sprinkles_theme
    scene bg showstage
    show sprinkles happy cane rightdown at middle_sprinkles
    hide screen laura
    with dissolve
    pause 0.1
    s "Alright, everyone! Let's start the show!"
    m "Not without me, you're not!"
    s huh "Huh? Who said that?"
    m "I did!"
    show sprinkles at two2_sprinkles with easeinleft
    show madeline down excited:
        zoom 0.75
        xalign 0.25 ypos 1000
        ease 0.5 ypos -100
        ease 0.25 ypos 10
        ease 0.25 two1
    pause 1.1
    play sound applause
    pause 0.5
    s laugh hat "Aha! Hello there, Ms. Madeline!"
    m "Hello there, Mr. Sprinkles!"
    s happy rightdown "What were you just up to?"
    m "I was helping a family of gophers redecorate their house!"
    s laugh "Wow! How incredible!"
    m shrug "That's my life~!"
    play sound "audio/se/audience_laugh.ogg"
    pause 1
    $l_exp = "smile"
    scene bg fade
    show screen laura
    show kate happy down at middle
    with dissolve
    pause 0.1
    k "Ehehehe!"
    "That outfit of hers certainly wasn't cheap, but the smile she gave when she first put it on was enough to make it worth it."
    hide kate with dissolve
    pause 0.1
    $l_exp = "neutral"
    "As we drove, I occasionally checked Twitter for any potential updates I should be aware of."
    "Apparently, there are protests breaking loose outside of city hall, the central Government Safehouse, as many people are being denied access inside."
    "{i}\"Many people are calling it 'unfair' and 'proof that the poor are the ones meant to die'.\"{/i}"
    "{i}\"The mayor has yet to comment on this.\"{/i}"
    $l_exp = "concerned"
    "Sounds about right."
    $l_exp = "neutral"
    "{i}\"Meanwhile, smaller Safehouses across town are setting up shop, including Frank's Bar in downtown Atlanta.\"{/i}"
    "{i}\"According to the owner, Frank Morris, the bar is opened up to anyone who needs help, but space in the building is limited.\"{/i}"
    "{i}\"He also states that to reduce the risk of random intruders who wish to enter and potentially cause harm, all people who enter must say the password, \"{color=#d00000}Martini{/color}\".\"{/i}"
    $l_exp = "concerned"
    "Ah, yes. Frank's Bar."
    $l_exp = "smug"
    "I can only imagine what it would be like to be so rich that you could afford to turn your business into a Safehouse."
    $l_exp = "neutral"
    "Though I have to say it's a bit sad that he needs a password to prevent random intruders."
    $l_exp = "sad"
    "I guess maybe Safehouses aren't as safe as I thought..."
    s "Our first game of the day is..."
    s "{i}Wild, Wild Races!{/i}"
    play sound applause
    pause 1.0
    show kate happy down at middle with dissolve
    pause 0.1
    $l_exp = "smile"
    k "Kota, that's your favorite game!!"
    show kate:
        ease 0.5 two2
    show dakota small_smile hips at two1 with dissolve
    pause 0.1
    d "I know, Kate."
    k "Ooo! Ooo! Do you think they'll play it on stage tonight?"
    d "It's a 12-hour show, Kate. I'm sure they'll find time."
    k excited "That would be AWESOME!!!"
    d "Heh. Yes, it would."
    $l_exp = "concerned"
    "Dakota certainly has been acting a bit weird the entire way here."
    $l_exp = "surprised"
    "There's no doubt that she's still thinking about the REDD War."
    r "Alright, here we are!"
    stop music fadeout(3)
    show dakota neutral
    show kate confused
    $l_exp = "concerned"
    "I honestly hadn't been paying attention our location, but sure enough..."
    scene bg theater_ext with dissolve
    pause 0.1
    $l_exp = "smile"
    "...we were here!"
    play music classy_ghouls
    show kate happy up at middle with dissolve
    pause 0.1
    k "YAAAAAAY!!"
    "Kate clapped with joy as we pulled into the massive parking lot."
    hide kate
    show richard crossed glare at middle
    with dissolve
    pause 0.1
    r "Well, we may be here, but it's still gonna be a while before we park and get inside..."
    $l_exp = "neutral"
    "He wasn't kidding; the line of cars in the parking lot was massive and moving slower than a snail."
    $l_exp = "surprised"
    l "We should be able to get inside before 7 o'clock, right?"
    r concerned "Hopefully."
    show richard:
        ease 0.5 two1
    show kate mad fidget at two2_short with dissolve
    pause 0.1
    k "I hope we do!"
    k excited up "I don't wanna miss a second of the show!"
    $l_exp = "smug"
    "Oh, you innocent child..."
    r laughing down "I know you don't, Kate."
    r smile "We should be fine."
    r glare "Maybe."
    r crossed "If this guy would just pick up the pace..."
    hide kate
    show dakota confused crossed at two2_short
    with dissolve
    pause 0.1
    d "Hey, Mom?"
    $l_exp = "neutral"
    l "Yes?"
    d "Isn't that the crazy lady you always complain about?"
    "She asked as she pointed out her window."
    $l_exp = "concerned"
    "I looked to where she was pointing."
    "..."
    $l_exp = "rage"
    l "...oh, you have got to be kidding."
    scene bg theater_ext
    show jessica stand_up at middle
    hide screen laura
    with dissolve
    pause 0.1
    j "Turn back now if you value your children's lives!"
    j "{i}Mr. Sprinkles{/i} is a menace that must be destroyed!"
    "Crowd" "\"Yeah!!\""
    hide jessica
    show screen laura
    with dissolve
    pause 0.1
    l "I swear, that bi--"
    $l_exp = "mad"
    l "{b}woman{/b} doesn't know when to stop."
    show kate happy down at middle with dissolve
    pause 0.1
    k "Ooooooo~! Mommy almost said a bad word~!"
    $l_exp = "smug"
    l "That's right, Kate. {i}Almost{/i}."
    "Everyone in the car then gave a laugh before changing the subject."
    $l_exp = "neutral"
    hide kate with dissolve
    pause 0.1
    "I still couldn't believe that Jessica Tate was here protesting."
    "The theater is a Government Safehouse because of Krag Dovason's willingness to help."
    $l_exp = "mad"
    "Of course, that would imply that Krag is a nice guy, thus destroying her narrative."
    $l_exp = "concerned"
    "What exactly is she planning on doing once it's time for the REDD War, anyway?"
    "Does she actually have the courage to go inside the arena for protection?"
    $l_exp = "mad"
    "Of course, maybe she'll continue protesting once she's inside because she has nothing better to do with her time."
    $l_exp = "neutral"
    "Ah, whatever. If she wants to be a dumb bitch, let her."
    $l_exp = "smile"
    "I'm here for a fun night with my family."
    "I'm not going to let some lunatic take that from me."
    call sceneend
    if not persistent.scenes["ch2_s3"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch2_s3"] = True


label meetandgreet:
    python:
        currenttime = "5:13 PM"
        timeleft = "1 hour and 47 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    play ambience crowd
    play music the_calm
    scene bg livestage
    with Dissolve(2.0)
    pause 0.5
    show screen laura
    window show dissolve
    pause 0.1
    "Thankfully, the wait wasn't as long as we thought it would be."
    $l_exp = "smile"
    "We were still very early, but given the circumstances, that's not necessarily a bad thing."
    $l_exp = "concerned"
    "Well, unless you've got a child who takes any chance she can to complain about being bored."
    show dakota mad hips at middle with dissolve
    pause 0.1
    d "What are we supposed to do for 2 hours?"
    $l_exp = "neutral"
    l "We could always walk around a bit to see what they've got."
    $l_exp = "smile"
    l "They're selling a lot of merch, if you're interested."
    d neutral crossed "Eh."
    $l_exp = "smug"
    l "I'm not saying you need to be as decked out as your sister."
    d mad "I know."
    $l_exp = "neutral"
    l "..."
    l "Well, it's either that or sit here on your phone."
    l "But I'm sure you're gonna want to use it to take pictures during the show, right?"
    d neutral "..."
    l "So I'd save the battery if I were you."
    d "..."
    l "..."
    $l_exp = "concerned"
    "I guess feeling out of harm's way is enough to turn her back into her usual self."
    "Though there's something to be said about having a sense of normalcy."
    show dakota zorder 2:
        ease 0.5 two1_short
    show richard crossed glare at two2 zorder 1 with dissolve
    pause 0.1
    r "Don't go crying to us when your battery dies, Dakota. You were warned."
    d mad "..."
    stop music fadeout(3)
    stop ambience fadeout(3)
    play sound "audio/se/chime.ogg"
    pause 1
    show dakota confused
    show richard concerned
    "Suddenly, a chime could be heard from the speakers."
    s "Hey, howdy, hey, everyone~! It's Mr. Sprinkles here!"
    s "In a few short moments, I will be sitting in the west hall for photos, autographs, or a simple hello~!"
    s "I'll only be there until 6:30, so if you wish to stop by, you better hurry over to the west hall!"
    s "Safely, of course~"
    s "I can't wait to see you there!"
    play music the_calm fadein(3)
    play ambience crowd fadein(3)
    pause 1
    show dakota:
        ease 0.5 left_short
    show richard:
        ease 0.5 right
    show kate excited up at middle_short with dissolve
    pause 0.1
    $l_exp = "surprised"
    k "Come on!! Let's go!!"
    "Kate grabbed on to me and tried yanking me out of my seat."
    k "I wanna see Mr. Sprinkles!!"
    $l_exp = "sad"
    l "Kate, not so loud, please."
    k @ fidget shocked "Sorry."
    k "I just wanna see him!"
    $l_exp = "smile"
    l "I know you do."
    "I then looked over to my other daughter."
    $l_exp = "smug"
    l "What do you say? Wanna take time away from your phone to see Mr. Sprinkles?"
    d small_smile "..."
    $l_exp = "smile"
    "I suppose that answers that."
    r laughing "I guess we better hurry; that line is gonna get long pretty quickly."
    $l_exp = "neutral"
    "Sure enough, the exits to the room were nearly blocked by families trying to get out."
    $l_exp = "excited"
    l "Well, we've got about an hour until the session ends; let's get to it!"
    hide screen laura
    pause 1
    scene bg arena_hall_day with fade
    pause 1
    $l_exp = "neutral"
    show screen laura
    pause 0.6
    "By the time we got settled in the line, there were certainly a lot of people in front of us."
    $l_exp = "concerned"
    "We couldn't even see the front of the line or any indication that the end led to a meet-and-greet."
    $l_exp = "neutral"
    "But at least the line was moving at a decent pace."
    "I'm sure the people in front are only getting less than a minute to meet him and get autographs, but for kids, that should be enough."
    $l_exp = "concerned"
    "Hopefully."
    show richard glare crossed at middle with dissolve
    pause 0.1
    r "It's kinda weird, don't you think?"
    $l_exp = "surprised"
    l "What is?"
    r "An autograph session {b}before{/b} the show?"
    r "That's usually something these things do {b}after{/b} the show."
    $l_exp = "smug"
    l "You really think you're going to have the energy to stay for a meet-and-greet after a 12-hour overnight show?"
    r @ concerned "Well, I guess that's fair."
    r "Still. A bit weird."
    l "Richard, we're going to watch an alien perform a show for 12 hours while other aliens outside the building cause chaos. Everything about this night is going to be weird."
    r smile "Heh. Fair enough."
    "{color=#d00000}???{/color}" "\"Excuse you!\""
    $l_exp = "surprised"
    show richard concerned
    "We looked forward and saw a middle-aged REDD turned around and glaring at us."
    redd "We are not 'aliens'! This planet is our home, as well! Not just yours!"
    $l_exp = "sad"
    "I was taken aback, to say the least."
    l "I-I'm terribly sorry, Ma'am. I didn't mean to be offensive."
    "She sighed before continuing."
    redd "Just watch yourself. If the wrong REDD hears you say that, especially with the upcoming event, you could get yourself in deep trouble."
    $l_exp = "surprised"
    l "..."
    "She then faced forward again as the line moved up a bit."
    "..."
    "Well, that was awkward."
    $l_exp = "concerned"
    "I guess with the REDD, you really do need to watch what you do. Even the smallest, seemingly insignificant thing can set them off."
    hide richard
    show kate excited down at middle
    with dissolve
    pause 0.1
    k "Mommy?"
    $l_exp = "smile"
    l "Yes, sweetie?"
    k "Do you think Mr. Sprinkles will like my costume?"
    $l_exp = "smug"
    l "Are you kidding? He's going to love it!"
    l "I don't see anyone else here wearing such an authentic-looking Mr. Sprinkles outfit, do you?"
    k happy "Nope~!"
    k "Ooo! I bet he'll remember me and let me go on stage during the show!"
    $l_exp = "excited"
    l "Well, let's not get ahead of ourselves, Kate."
    l "There are a lot of people here; any one of them has a chance of being picked."
    k mad "Yeah, but none of them are wearing costumes as good as mine!"
    $l_exp = "smile"
    l "Still. I don't want you to get your hopes up too much, honey. Okay?"
    k alert "Okay, Mommy..."
    $l_exp = "sad"
    "I hate to break the poor girl's spirit, but it would be hurt a lot worse if she fully believed she had a guaranteed chance."
    hide kate with dissolve
    pause 0.1
    $l_exp = "concerned"
    "I looked over at Dakota and saw her scrolling through her phone."
    $l_exp = "mad"
    "I don't know what her percentage is at, but I know she's certainly not doing herself any favors by using her phone right now."
    "Oh well. Her loss."
    stop music fadeout(5)
    hide screen laura
    pause 1
    scene bg arena_hall_day with fade
    pause 1
    $l_exp = "neutral"
    show screen laura
    pause 0.6
    "About a half hour later, as well as Kate rambling on about what she's the most excited about tonight, we finally saw the front of the line ahead of us."
    $l_exp = "smile"
    "And at the front of the line was..."
    show kate shocked fidget at middle with dissolve
    pause 0.1
    k "Mr. Sprinkles!"
    hide kate with dissolve
    pause 0.1
    stop ambience fadeout(3)
    play music sprinkles_theme
    show sprinkles happy leftdown hat at middle_sprinkles with dissolve
    pause 0.1
    "Sure enough, there he was behind the table talking to a young fan."
    $l_exp = "smug"
    "I have to admit that there's always something surreal about seeing someone in person after seeing them behind a screen for so many years."
    $l_exp = "determined"
    "I mean, I've been to my fair share of concerts and the like before, but the feeling never goes away."
    "But for people like Kate and Dakota who have never felt the feeling before..."
    hide sprinkles
    show kate happy up at two1
    show dakota small_smile side at two2
    with dissolve
    pause 0.1
    k "I can't believe it! He's right there!"
    d "Yeah! And he actually looks happy to be here, too!"
    k excited down "Of course he does! He's awesome like that!"
    $l_exp = "excited"
    "...it's just sweet and innocent."
    scene bg arena_hall_day with dissolve
    pause 0.1
    $l_exp = "smile"
    "Finally, it came the big moment."
    show sprinkles laugh hat leftdown at middle_sprinkles with dissolve
    pause 0.1
    s "It was nice to meet you, Mandy! I hope you enjoy the show!"
    s happy rightdown "Next~!"
    show sprinkles at right_sprinkles with easeinleft
    show kate happy down at middle_short
    show dakota small_smile crossed at left_short
    with easeinleft
    pause 0.5
    "He then looked at Kate with awe."
    s huh "My word!"
    k concerned fidget "..."
    "Mr. Sprinkles then turned to Dakota."
    s happy "I must say that this is one fine mirror you have here!"
    show kate happy
    show dakota smirk
    "Both girls gave out a giggle."
    s huh hat "Although it appears to be a bit broken."
    "He commented as he waved his arm a bit while looking at Kate."
    "Taking the hint, Kate tried to mimic his movements."
    s jeer "Hm. A bit delayed, I see."
    "Finally, Kate giggled more and took off her hat."
    $k_hat = False
    k up "I'm not a mirror, Mr. Sprinkles! I'm Kate!"
    s laugh rightdown "Oh! Ahahaha!"
    s happy "Well, you certainly had me fooled, Kate!"
    s "And who's this with you?"
    $k_hat = True
    k excited fidget "This is my sister, Kota!"
    d small_smile side "I-It's {b}Da{/b}kota, actually."
    s jeer "I see. Well, it's still a very nice name."
    d "Th-Thank you."
    k happy down "Mommy, can you take a picture of us with Mr. Sprinkles??"
    $l_exp = "determined"
    l "Of course!"
    "I then took out my phone as everyone got into position."
    l "Everyone smile~!"
    $quickhide = True
    hide screen laura
    window hide
    pause 0.5
    scene bg flash
    with Dissolve(0.25)
    scene bg fade # Will be replaced by CG of the photo
    with Dissolve(1.0)
    pause 1.0
    window show dissolve
    k "How does it look?"
    l "Perfect."
    k "Yay~!"
    $quickhide = False
    scene bg arena_hall_day
    show screen laura
    show sprinkles happy rightdown leftdown at right_sprinkles
    show kate happy down at middle_short
    show dakota small_smile side at left_short
    with dissolve
    pause 0.1
    s "It was certainly nice to meet you both!"
    k "You, too, Mr. Sprinkles!"
    d "Y-Yeah. You, too."
    s laugh "Ne-"
    show kate:
        ease 0.5 alpha 0.0
    show dakota:
        ease 0.5 alpha 0.0
    show sprinkles:
        ease 0.5 two2_sprinkles
    show richard down glare at two1 with easeinleft
    pause 0.1
    stop music fadeout(3)
    r "Hold on. Can I ask you something, first?"
    $l_exp = "surprised"
    "Richard, what the hell are you doing...?"
    s huh "Oh."
    extend laugh " Why, certainly, Sir."
    r concerned "I just..."
    "He then lowered his voice a bit as he leaned forward."
    r crossed "...wanna make sure we're gonna be safe."
    r "You know, concerning the {b}other{/b} event going on tonight."
    s hm "..."
    "He sat there for a second before regaining a smile and answering."
    s jeer "I understand your concern, Sir, but there's nothing to worry about."
    s "We have the best guards on the planet protecting the building, as well as the best window and door shields money can buy."
    s hat "Once the event starts, nobody is getting inside this building. You have my word."
    r "..."
    r smile "Thanks."
    s laugh rightdown "No problem at all, Sir."
    s jeer "Any other questions?"
    r "No, that's it."
    s "Very well."
    s laugh "Next~!"
    scene bg arena_hall_day with dissolve
    pause 0.1
    $l_exp = "neutral"
    "After the four of us got out of the line and started heading back towards the main stage, I leaned a bit closer to Richard."
    show richard down concerned at middle with dissolve
    pause 0.1
    $l_exp = "mad"
    l "Was that necessary?"
    r @ glare "To me? Yes."
    r "I just want to make sure we get through this night in one piece. Is that such a bad thing?"
    $l_exp = "neutral"
    l "Of course not."
    r "..."
    l "..."
    hide richard with dissolve
    pause 0.1
    "Well, the show will begin soon."
    $l_exp = "concerned"
    "I suppose we have enough time to look around at the vendors and get some merchandise."
    $l_exp = "smug"
    "Maybe even a quick meal before the show."
    "..."
    $l_exp = "neutral"
    "..."
    hide screen laura
    nvl clear
    nvl show dissolve
    $nvl = True
    narrate """
    Who am I kidding?

    I can try and be ignorant about the situation all I want, but at the end of the day, I can't fault Richard.

    Once it's 7 and that siren sounds, people in Atlanta are going to die.

    And the concept of a Safehouse might not be enough to deter some rebel from trying to break in.

    I know I'm supposed to feel safe in a Safehouse, but when it comes to the REDD War, crazy, unexpected things can happen when you least expect them.

    Maybe staying here was a mistake.

    Maybe we should've left when we had the chance.

    ...
    
    {clear}

    Well, it's a bit too late to go back, now isn't it?

    Besides, I'm just working myself up for no reason.

    I have to be.

    ....
    """
    $nvl = False
    nvl hide
    scene bg fade
    with dissolve
    "Please, let me be."
    call sceneend
    if not persistent.scenes["ch2_s4"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch2_s4"] = True
    

label showbegins:
    python:
        currenttime = "6:55 PM"
        timeleft = "5 minutes"
        l_exp = "surprised"
    call chapterstart
    pause 2
    play ambience crowd
    scene bg livestage
    with Dissolve(3)
    play sound "audio/se/chime.ogg"
    pause 2
    window show dissolve
    pause 0.1
    s "Okay, everyone~! The show will begin in exactly 5 minutes!"
    s "Please use this time to head to your seats so we may start the show with a full house~!"
    s "This will truly be a good night of fun; I can't wait to share it with you all!"
    pause 1
    show screen laura
    pause 0.6
    "Well, we're almost there."
    show kate excited down:
        middle
        alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.25 ypos -20
            ease 0.25 ypos 0
            repeat
    pause 0.1
    "Kate was jumping in her seat."
    hide kate
    show dakota neutral crossed at middle
    with dissolve
    pause 0.1
    "Dakota was tapping her foot quickly as her hands sat in her lap."
    hide dakota
    show richard down concerned at middle
    with dissolve
    pause 0.1
    "And Richard was still, but was clearly showing signs of nervousness."
    hide richard with dissolve
    pause 0.1
    stop ambience fadeout(3)
    show dark:
        alpha 0.0
        ease 1.0 alpha 1.0
    $l_exp = "neutral"
    "Finally, after what seemed like forever, the lights started to dim."
    "I looked at the time."
    "6:59"
    play ambience "audio/se/warning.ogg"
    "That's when we could hear the alert horn blare outside the building."
    hide screen laura
    pause 0.6
    stop ambience
    play sound "audio/voice/commence01.ogg"
    an "This is not a test. This is the official commencement of the Annual REDD War."
    play sound "audio/voice/commence02.ogg"
    an "At the siren, all REDD within certified War Zones will be exempt from any and all crime, including murder, for 12 consecutive hours."
    play sound "audio/voice/commence03.ogg"
    an "All humans who commit crime during these hours, excluding crimes committed for self-defense purposes, will receive the appropriate punishment at the conclusion of the REDD War."
    play sound "audio/voice/commence04.ogg"
    an "Weapons of Class 3 and lower have been authorized for use; all other weapons are forbidden."
    play sound "audio/voice/commence05.ogg"
    an "Government Safehouses, and by extension the contents within, have been granted immunity from the REDD War and must not be harmed."
    play sound "audio/voice/commence06.ogg"
    an "All emergency services will be suspended until the siren sounds again at the conclusion of the REDD War."
    play sound "audio/voice/commence07.ogg"
    an "On behalf of your government and the REDD, we thank you for your cooperation and wish you the best of luck."
    play sound "audio/voice/commence08.ogg"
    an "The REDD War will begin in 5... 4... 3... 2... 1."
    play sound siren
    pause 5
    $l_exp = "sad"
    show screen laura
    pause 0.6
    "Well, this is it."
    "No turning back now."
    "..."
    $l_exp = "surprised"
    "It's kinda funny."
    "I'd been dreading this moment for 24 hours, and now that it's here..."
    $l_exp = "concerned"
    "...I don't feel as scared as I thought I would've."
    $l_exp = "surprised"
    "That's when I felt Richard grab my hand."
    show richard down concerned at middle with dissolve
    pause 0.1
    "He looked at me with a face of worry, and I can't blame him."
    "I looked at my daughters."
    hide richard with dissolve
    show dakota sad side at middle with dissolve
    pause 0.1
    "Dakota was breathing very heavily while she stared ahead."
    "It almost looked like she was going to cry."
    hide dakota
    show kate fidget confused at middle
    with dissolve
    pause 0.1
    "Kate, meanwhile, looked a bit confused as to what just happened and why everyone seemed to be upset."
    play sound drumroll_buildup loop
    pause 1
    $l_exp = "concerned"
    show kate happy
    m "Okay, everyone!"
    m "Put your hands together for the one..."
    m "...the only..."
    m "...Mr. Sprinkles!"
    play sound drumroll_finish
    pause 1
    play sound applause
    "The curtain then started to rise."
    show kate:
        ease 0.5 two2
    show dakota small_smile hips at two1 with dissolve
    pause 0.1
    $l_exp = "smile"
    "Dakota seemed to suddenly forget about the commencement, as well."
    "With that, we all got relaxed and watched the stage."
    scene bg fade
    hide screen laura
    with dissolve
    pause 1.5
    play sound "audio/se/spotlight.ogg"
    scene bg stage
    show sprinkles cane hat jeer at middle_sprinkles
    with Dissolve(0.1)
    pause 1
    play music sprinkles_theme
    s laugh "Good evening, my friends~!"
    s happy rightdown "My, oh, my. We certainly have a lot of you in the audience tonight, don't we?"
    s "Well, with the long night we have ahead of us, that will certainly prove to be in our favor~!"
    s "So, what do you say? Are you ready to have fun tonight?"
    "Audience" "\"Yeah!\""
    s jeer "Oh, come now; you can all do better than that!"
    s laugh "Are you ready to have fun tonight??"
    "Audience" "{i}{b}\"YEAH!!\"{/b}{/i}"
    s happy hat "Splendid! Then let's start the show!"
    m "Not without me, you're not!"
    s huh "Huh? Who said that?"
    m "I did!"
    "That's when a door at the back of the theater opened up."
    $l_exp = "neutral"
    scene bg livestage
    show screen laura
    with dissolve
    pause 0.1
    "We turned around and saw a bright-clothed woman enter the room with a wave."
    play sound applause
    show madeline down excited at middle with dissolve
    pause 0.1
    $l_exp = "smile"
    s "Aha! Hello there, Ms. Madeline!"
    m "Hello there, Mr. Sprinkles!"
    s "What were you just up to?"
    m "I was eating popcorn and pretzels!"
    s "Wow! How delicious!"
    m shrug "That's my life~!"
    play sound "audio/se/audience_laugh.ogg"
    pause 1
    $l_exp = "smile"
    hide madeline with dissolve
    pause 0.1
    "Ms. Madeline then made her way towards the stage, giving high-fives to people in the aisles along the way."
    "Finally, she walked onto the stage and stood next to Mr. Sprinkles."
    scene bg stage
    show sprinkles happy cane rightdown at two2_sprinkles
    hide screen laura
    with dissolve
    pause 0.1
    show madeline down excited at two1 with easeinleft
    pause 0.1
    s "Alright, are you ready to have fun?"
    m smile "I sure am!"
    s laugh "Splendid~!"
    "{color=#d00000}Mr. Sprinkles{/color}" "\"Then let's {nw}"
    stop music
    play sound "audio/se/spotlight.ogg"
    scene bg fade
    window hide
    $renpy.pause(delay=2)
    play ambience crowd fadein(3)
    $l_exp = "concerned"
    show screen laura
    window show dissolve
    pause 0.1
    "Well, the power turning off certainly seemed unexpected."
    "Several children in the audience screamed, a few started crying, but for the most part, it was the adults chattering with confusion."
    $l_exp = "neutral"
    "Fortunately, my children were well-behaved."
    s "L-Ladies and gentlemen, please refrain from panicking!"
    s "We seem to be having some technical difficulties, but I'm sure we'll be able to work them out quickly!"
    "{color=#d00000}Mr. Sprinkles{/color}" "\"In the meantime, {nw}"
    $l_exp = "surprised"
    play sound "audio/se/Door Open.ogg"
    stop ambience fadeout(3)
    "Before he could finish that sentence, the doors at the back of the theater slammed open, but the building was too dark to see anything."
    play sound "audio/se/spotlight.ogg"
    scene bg livestage
    with Dissolve(0.1)
    pause 1
    $l_exp = "sad"
    "As the power came back on, we were all in shock at what we saw:"
    "A small army of REDD in full body armor storming into the room."
    show richard down glare at middle with dissolve
    pause 0.1
    r "What the hell is going on??"
    l "I-I'm not sure...!"
    play sound smack
    m "{b}Gah!!!{/b}"
    "We turned back to the stage, only to see..."
    show richard concerned
    $l_exp = "surprised"
    "...Ms. Madeline lying on the ground, as if she just fell."
    "And Mr. Sprinkles had his walking stick in his hand as if it was a baseball bat."
    $l_exp = "sad"
    "Surely it can't be what I think it was..."
    play sound smack
    "But my suspicion was met when he swung his stick back and smacked the already-fallen woman right in the face, resulting in a cry of pain!"
    scene bg stage
    hide screen laura
    show madeline down shocked at middle
    with dissolve
    pause 0.1
    m "Krag, what are you--??"
    play sound smack
    show madeline:
        linear 0.1 ypos 20
        linear 0.1 ypos 0
    "Another smack in the face."
    show madeline at two2 with easeinright
    pause 0.5
    show sprinkles rightdown cane evilgrin at two1
    with Dissolve(1)
    pause 0.5
    "He then stood right over her."
    show madeline:
        ease 0.5 xalign 0.85
        pause 1
        ease 0.5 xalign 0.9
        pause 1
        ease 0.5 xalign 0.95
    "While still on the ground, she backed up slowly, staring at him with terror in her eyes."
    show sprinkles:
        ease 2.0 xalign 0.65
    "But he just kept walking towards her, that sinister grin still plastered on his face."
    show madeline:
        xalign 0.95 ypos 0
    show sprinkles:
        xalign 0.65 ypos 0
    m "K-Krag, what are you doing??"
    "He then gave a quiet, yet terrifying chuckle."
    s "There's been a slight change to the schedule, Ms. Madeline."
    s "You see, we don't have any room for you tonight."
    s "I'm afraid I'm going to have to..."
    "He then turned the ball on top of his walking stick, revealing something coming out of the bottom."
    "Something silver and pointed."
    s "...{b}terminate you.{/b}"
    "Then, in one swift motion, he reached up..."
    show sprinkles:
        linear 0.1 ypos -50
        linear 0.1 ypos 0
    pause 0.2
    play sound stab
    show madeline stabbed:
        linear 0.1 ypos 20
        linear 0.1 ypos 0
    "...and jammed the stick into her chest!"
    play ambience crowd_screaming
    play sound children_screaming
    play sound2 "audio/voice/madeline_choke.ogg" loop
    "As the crowd screamed, Madeline gasped, but it sounded more like an attempt at a gasp."
    "She grasped at the stick, trying to possibly get it out, but it was to no avail; she couldn't wrap her hands around it."
    "She sounded like she was both gagging on something and gasping for air, struggling to breathe."
    stop sound2
    $l_exp = "shocked"
    scene bg livestage
    show kate shocked fidget at middle
    show screen laura
    with dissolve
    pause 0.1
    k "Mommy, what's happening??"
    l "I don't know, Kate, but we're getting out of here!"
    show kate zorder 2:
        ease 0.5 left_short
    with None
    show richard down rage at middle
    show dakota sad side at right_short
    with dissolve
    r "Excellent idea! Come on, girls!"
    "I saw several other people nearby stand up and try to get into the aisle."
    show richard concerned
    "But they were quickly stopped when several of the armored REDD pulled out a gun and pointed it at them, which only added to the audience panic."
    redd "Get your asses back in your seats!"
    "Richard and I looked back at each other with worry, realizing that it's probably smarter to listen to him."
    "That's when Mr. Sprinkles leaned in towards Ms. Madeline's face."
    $cane_blood = True
    scene bg stage
    hide screen laura
    show sprinkles evilgrin cane rightdown zorder 2:
        zoom 0.75
        xalign 0.65 ypos 0
    show madeline down stabbed zorder 1:
        zoom 0.75
        xalign 0.95 ypos 0
    with dissolve
    pause 0.1
    "Still sporting that sinister look, he told her:"
    s "{i}That's your death~!{/i}"
    s laugh hat "Ehehe. Hahaha!"
    show sprinkles:
        ease 0.5 middle_sprinkles
    s "Ahahaha!!! HAHAHAHAHAHAHA!!!!!"
    "His maniacal laugher echoed throughout the room as Madeline's arms slowly dropped to her chest and her head slightly tilted to the side."
    show madeline:
        ease 0.5 alpha 0.0
    show sprinkles rightdown leftdown jeer
    "He then cleared his throat and faced the rightfully panicked crowd."
    hide madeline
    s "May I have your attention, please?"
    "The audience continued to scream and panic."
    show sprinkles hm
    "He then looked towards the back of the room and gave a small nod."
    play sound machine_gun
    call gunflash
    "Suddenly, a REDD in the back fired his weapon in the air and shouted."
    redd "{b}HEY! THE REDD'S TALKING!!{/b}"
    stop ambience fadeout(5)
    "That seemed to do the trick."
    "Everyone then looked at the stage whether they wanted to or not."
    s jeer "Thank you."
    s hat "Now, I'm sure you've all got some questions going through your mind, so allow me to answer them."
    play music sprinkles_spooky
    s laugh "You see, I wasn't lying just now when I said there's been a change to the schedule."
    s "I had a realization recently: while {i}The Mr. Sprinkles Show{/i} has a large, human-based audience..."
    s evilgrin "...I figured it was time to expand my demographic."
    s "So tonight's show is going to be dedicated to all my fellow REDD who are watching this show from their television sets."
    s laugh "I'm going to give you all a performance that will not disappoint~!"
    s jeer rightdown "But in order to do that, I'm going to ask all the adults in the audience to please follow these fine gentlemen."
    scene bg livestage
    show screen laura
    with dissolve
    pause 0.1
    "On cue, the armored REDD all drew out their weapons and spread out across the room."
    redd "Let's go! Move it! All adults! No exceptions!"
    $l_exp = "sad"
    "This can't be happening."
    "I'm dreaming."
    "I have to be."
    "I just fell asleep while waiting for the show to start."
    "I have to have."
    "There's no way this is happening."
    "No way."
    redd "I said move it!"
    man "Hell no! You're not--"
    play sound machine_gun
    call gunflash
    play ambience crowd_screaming fadein(1)
    $l_exp = "shocked"
    "Without hesitation, the REDD shot the man dead."
    "The blood-covered woman and children next to him started screaming and crying as they watched him fall over."
    redd "Anyone else wanna be uncooperative?!"
    show richard crossed concerned at middle zorder 2 with dissolve
    pause 0.1
    r "..."
    l "..."
    "Can I please wake up from this nightmare now?"
    $renpy.music.set_volume(0.5, delay=3, channel='ambience')
    redd "Let's go!!"
    show kate crying fidget at left_short zorder 1
    show dakota bawl side at right_short zorder 1
    with dissolve
    pause 0.1
    k "Mommy, I'm scared!"
    $l_exp = "sad"
    l "I know, Kate. I am, too."
    "I then gave her a big hug and a kiss on the head."
    $l_exp = "excited"
    l "Everything's going to be okay, I promise."
    "I knew for a fact that was a lie, but what else could I say?"
    $l_exp = "sad"
    "That's when Dakota grabbed onto me."
    d "Please don't leave!"
    show richard:
        ease 0.5 ypos 100
    "Richard leaned down and looked her in the eye."
    r down "I don't think we have much of a choice, Dakota."
    r "We just need to go along with what they're saying for now. We'll be back before you know it, okay?"
    d "No!!"
    "The tears were starting to come out."
    "Not just from Dakota, but from Richard and myself."
    "He then hugged her tightly for a few seconds before looking her in the eye."
    r crossed "No matter what happens, just know that I love you, Dakota."
    r "Please never forget that."
    r "And that goes for you, too, Kate."
    r down "I love both of you so much!"
    "That's when the REDD came over to us and grabbed Richard."
    show richard:
        ease 0.25 ypos 0
    redd "Save the sentiment. Move it!"
    d crying "{b}NO!! LET HIM GO!!!{/b}"
    show dakota:
        ease 0.5 xalign 0.7
    "With eyes full of tears and rage, Dakota latched on to her father."
    redd "Get off him, you brat!"
    r rage "Don't you {b}dare{/b} call my daughter that!"
    redd "And what are you gonna do about it?"
    r glare "..."
    "I then tried to pry Dakota off him."
    d "NO!!!"
    $l_exp = "crying"
    l "Dakota, please..."
    "I'm trying to keep my cool here, but there's only so much I can do to stop myself from breaking down right now."
    show dakota:
        ease 0.5 middle
    with None
    hide richard
    hide kate
    with dissolve
    pause 0.1
    l "We'll be okay. Just sit here and keep your sister safe."
    l "Okay?"
    "She still looked furious and horrified."
    show dakota bawl
    "But she eventually loosened her grip on Richard."
    l "Please keep your sister safe. We'll be back."
    "Dakota looked at Richard, then back to me."
    "Finally, she closed her eyes and let go."
    "The REDD didn't hesitate in yanking Richard away while another REDD approached me to grab me."
    show dakota:
        ease 0.5 two2
    show kate crying fidget at two1 with dissolve
    pause 0.1
    k "Mommy! Daddy!"
    l "I love you girls so much!!"
    scene bg livestage with dissolve
    pause 0.1
    $renpy.music.set_volume(1.0, delay=3, channel='ambience')
    hide screen laura
    nvl clear
    $nvl = True
    nvl show dissolve
    narrate """
    As Richard and myself, as well as all the adults in the audience, human and REDD, were taken out of the room like we were prisoners...

    Well, I guess there's no 'like' about it.

    Regardless, as we were taken out, the room could be heard with the cries and screams of the children, as well as some more gunshots of uncooperative parents.

    Where we were going, we didn't know.

    What we would do when we got there, we didn't know.

    Whether or not we would live, we didn't know.

    I'm still trying to convince myself that this isn't really happening.

    But the longer this goes on, the less reason I have to believe that.

    {clear}

    I still don't understand how this is happening, though. This is a Government Safehouse.

    ...{w}right?

    That's what we were told.

    That's why we're here.

    That's why a lot of people are here!

    ...

    {clear}

    Well, I suppose the 'why' and 'how' isn't the biggest issue we have right now.

    These guys have shown they won't shy away from killing us if we don't listen to them.

    I know for a fact that I wanna see my babies again, so I guess I'll have to do whatever it takes for me to stay alive.

    For their sake.
    """
    call sceneend
    if not persistent.scenes["ch2_s5"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch2_s5"] = True
    jump chapter_3
    