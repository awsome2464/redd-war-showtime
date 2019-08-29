label chapter_2:
    stop music
    call chaptername
    call chapterstart
    pause 1
    scene bg livingroom
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
    pause 0.1
    "I had made my way downstairs, where I found my husband watching the news on TV."
    $l_exp = "neutral"
    show screen laura
    show richard concerned at middle_r
    with dissolve
    pause 0.1
    l "Has anything happened?"
    r glare "Yes. A lot, actually."
    "He pointed to the screen."
    "The main headline along the bottom was {i}'MR. SPRINKLES' STAR KRAG DOVASON SPEAKS OUT AGAINST ATLANTA WAR ZONE ANNOUNCEMENT{/i}."
    $l_exp = "concerned"
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
    a "{i}No matter which choice you make, I wish you, as well as everyone else, good luck. The next few days are going to be crazy. {color=#00aced}#REDDWar2030{/color}"
    $l_exp = "excited"
    scene bg livingroom
    show richard glare at middle_r
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
    "I stared at him for a second before giving a smirk and crossing my arms."
    $l_exp = "smug"
    l "You're debating whether or not to stay, aren't you?"
    r @ rage "..."
    r "..."
    r smile "Alright. You've got me."
    $l_exp = "smile"
    l "See?"
    "I asked as I playfully pushed him away with a grin."
    l "I told you you just needed to wait and see what happens."
    r laughing "Yeah, yeah. You were right, as usual."
    "We could then hear footsteps coming down the stairs."
    show richard at two1_r with easeinright
    pause 0.5
    show dakota neutral at two2 with dissolve
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
    r concerned "But like your mother said, we haven't decided yet."
    r "We still need to talk this over as a family."
    d "..."
    d "We'd really be safe?"
    d "Like, no REDD would kill us?"
    r "Yes, that's what was said."
    d "...{w}then..."
    d small_smile "...maybe we could go see Mr. Sprinkles after all?"
    r glare "Dakota, that doesn't mean we can just go to the show."
    $l_exp = "neutral"
    d sad "But Mom said it's at one of the safe places!"
    r "I know, but..."
    d mad "You just don't wanna go because you hate Mr. Sprinkles!"
    r "That has nothing to do with this, Dakota!"
    stop music fadeout(3.0)
    d "You know what? You're right!"
    d "It's not because of Mr. Sprinkles!{w} It's because of me!"
    $l_exp = "shocked"
    r concerned "What are you talking about?"
    d "If Kate told you she wanted to stay, you'd say we could stay!"
    d "But because {b}I{/b} want to stay, it's wrong!"
    r rage "That's not true at all!"
    d "Yes, it is!!"
    d "I never get what I want! It's always about Kate!"
    d "I wish she was never born so you would actually care about me!!"
    $l_exp = "sad"
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
    d "...are you mad at me...?{nw}"
    menu:
        d "...are you mad at me...?{fast}"
        "\"Yes, a little.\"":
            jump yesalittle
        "\"No, I'm not.\"":
            jump noimnot

label yesalittle:
    $l_exp = "mad"
    l "Yes, a little."
    $l_exp = "neutral"
    l "But I won't ground you or anything over it."
    d "...okay..."
    jump dakotaissorry

label noimnot:
    l "No, I'm not, sweetie."
    d "...you promise?"
    l "I promise."
    d "..."

label dakotaissorry:
    "She then sighed and rubbed her eyes."
    play music vast_places
    d "I really am sorry, Mom."
    $l_exp = "sad"
    l "I know you are, Dakota."
    d "Not just for what I said about Kate."
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
    show dakota sad
    "Dakota grabbed on me to even tighter."
    $l_exp = "concerned"
    "I guess telling that to an already-horrified 9-year-old wasn't the smartest idea."
    $l_exp = "surprised"
    l "But..."
    l "I can't stress enough how much I care about making sure we're all safe."
    d mad "So then why don't we just go to the show tonight?! We were gonna go there, anyway!"
    $l_exp = "neutral"
    l "I know."
    d neutral "Dad doesn't seem to."
    $l_exp = "concerned"
    l "Well..."
    l "Your father wants to keep us all safe, as well; he just has a different way of doing it."
    l "He would just feel safer if we were outside of the War Zone, not inside of it."
    d "But..."
    $l_exp = "smug"
    "I gave a small chuckle and looked down at my little girl."
    l "You really wanna go see this show, don't you?"
    d mad "..."
    l "Hey, none of your friends are here to laugh at you for watching Mr. Sprinkles."
    d "C-Cut it out, Mom!"
    l "Heh. Fine, I'll stop."
    $l_exp = "smile"
    l "Well, no matter why you want to go to the show tonight, I'll be sure to count your vote in the final decision."
    d neutral "..."
    "I then heard Richard walking back down the stairs."
    show dakota zorder 2:
        ease 0.5 two2
    show richard concerned at two1_r zorder 1 with dissolve
    pause 0.1
    $l_exp = "neutral"
    l "How is she?"
    "He didn't reply right away; he looked at Dakota with a look of disappointment."
    d sad "..."
    r "..."
    r "Kate's fine. She'll get over it pretty quickly."
    $l_exp = "smile"
    l "Well, that's good to hear."
    show richard glare
    "Richard continued to glare at Dakota."
    "I guess he's finally had time to think about what she had said."
    d "..."
    $l_exp = "mad"
    l "You can spare the lecture. She knows what she did wrong."
    l "Isn't that right, Dakota?"
    d "Y-Yes... I'm really sorry, Dad."
    r "Well, I'm not the one you should be apologizing to."
    d "..."
    "More slow footsteps could be heard coming down the stairs."
    show dakota:
        ease 0.5 right
    show richard zorder 2:
        ease 0.5 middle_r
    pause 1
    show kate concerned at left zorder 1
    with Dissolve(1.5)
    pause 1
    k "Mommy?"
    $l_exp = "neutral"
    l "Yes?"
    k "Does Kota hate me?"
    d "No! I don't hate you, Kate! Don't ever think something like that!"
    k "But you said--"
    d "I know, and I'm so sorry! I didn't mean it!"
    "Despite Dakota's claim, Kate latched on to her father for comfort."
    r "..."
    r smile "Hey, you know what I think would cheer us all up?"
    k alert "What?"
    "He then bent down to the same level as his daughters."
    r "Going to see Mr. Sprinkles tonight!"
    show kate shocked
    show dakota neutral
    $l_exp = "shocked"
    l "Richard...?"
    r laughing "What do you say, girls?"
    show kate happy:
        ease 0.25 yalign 0.45
        ease 0.25 yalign 0.5
        repeat
    k "Yeah! Mr. Sprinkles! Mr. Sprinkles!!"
    "Kate jumped in excitement while still holding on to Richard."
    r smile "Alright, Kate. I can certainly see that you're happy."
    show kate:
        ease 0.25 yalign 0.5
    "Richard then picked her up with a chuckle and held her against him."
    r "Dakota? What do you say?"
    d small_smile "...{w}yeah! Let's go!"
    r laughing "Alright, then! It's decided!"
    r "The Farrs are going to see Mr. Sprinkles tonight!"
    k "YAAAAAAY!!"
    "Kate clapped with joy as Richard put her back down."
    $l_exp = "smile"
    l "Alright, but don't forget that it'll be a long night, so be sure to get plenty of rest!"
    k "I will!"
    "Richard then gave a small yawn."
    r "I suppose we could all use some more shut-eye."
    r "Everyone back to bed; that's an order."
    k "Okay~!"
    d determined "Alright."
    scene bg livingroom
    hide screen laura
    with dissolve
    pause 0.1
    "The girls went back upstairs."
    "Honestly, I won't blame them if they don't actually fall back asleep."
    "I then looked at my husband with a cheeky grin."
    $l_exp = "smug"
    show richard smile at middle_r
    show screen laura
    with dissolve
    pause 0.1
    l "Look at you being the world's greatest father."
    r "Hey, it's like you said: tonight's about them."
    hide richard
    hide screen laura
    with dissolve
    "We looked at each other for a second or so before giving a slow, meaningful kiss."
    "After breaking apart, Richard sighed and rubbed his eyes."
    $l_exp = "neutral"
    show richard concerned at middle_r
    show screen laura
    with dissolve
    pause 0.1
    r "Alright, it really is going to be a long night; we should really get some sleep."
    l "We should."
    $l_exp = "smug"
    l "But..."
    "I then slowly ran my hand up his leg and onto his thigh."
    l "...I'm sure you've got SOME energy."
    r glare "..."
    "He then took a peek towards the staircase."
    r concerned "You realize they might hear us, right?"
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
    hide richard
    hide screen laura
    with dissolve
    window hide dissolve
    pause 1.0
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(2.0)
    pause 4
    $renpy.end_replay()
    $persistent.chapter2_scene1 = True
    

label backstagedrama:
    python:
        currenttime = "2:42 PM"
        timeleft = "4 hours and 18 minutes"
    call chapterstart
    pause 1
    scene bg dressingroom with dissolve
    pause 0.5
    play sound door_knock
    pause 2
    window show dissolve
    kr "Come in!"
    play sound door_open
    pause 1
    show sprinkles happy at two1_s
    show madeline blank at two2_m
    with dissolve
    pause 0.1
    kr "Ah, Madeline! What can I do for you?"
    "Madeline" "\"You can start by giving me a script.\""
    show sprinkles jeer
    kr "Now, Madeline, all things in due time~"
    "Madeline" "\"Krag, the show is starting in 4 hours and I have no idea what the hell I'm going to be doing!\""
    "Madeline" "\"I'm not even seeing anyone rehearsing anything on the stage!\""
    "Madeline" "\"It's like you don't even have a plan! You're being way too secretive about this whole thing, and it's really starting to piss me off!\""
    show sprinkles hm
    kr "..."
    "Madeline" "\"Krag, I'm saying all this because I want {i}Mr. Sprinkles{/i} to succeed. To get through this rough patch.\""
    show sprinkles wut
    kr "And yet you told the network to put our show on a hiatus."
    "Madeline" "\"I could have told them to cancel it altogether, you know.\""
    "Madeline" "\"Believe me, I don't want to be in this situation any more than you do, but we need to think through this logically.\""
    "Madeline" "\"You're still relatively new to how show business works here on Earth. These things happen.\""
    kr "..."
    kr "I just don't want anyone to take my show away from me."
    kr "It is an entire life's worth of ideas and planning put together at last."
    kr "I'll do whatever it takes for {i}Mr. Sprinkles{/i} to continue."
    "Madeline" "\"Well, sometimes, you can't always get what you want, Krag.\""
    "Madeline" "\"I'm sorry, but that's just how it works.\""
    kr "..."
    "Madeline" "\"If I don't have a script or {b}any{/b} kind of direction within an hour, I'm not going to be in this live show, and that's final.\""
    kr "..."
    show sprinkles jeer
    kr "Very well. I'll get back to you."
    show madeline smile
    "Madeline" "\"Thank you.\""
    hide madeline with easeoutright
    pause 1
    show sprinkles:
        ease 1.0 middle_s
    pause 1.5
    show sprinkles laugh
    kr "Oh, you'll play a big role in this show, don't you worry..."
    window hide dissolve
    pause 1
    scene bg fade
    with Dissolve(2.0)
    pause 4
    $renpy.end_replay()
    $persistent.chapter2_scene2 = True
    

label arriveatshow:
    python:
        currenttime = "3:51 PM"
        timeleft = "3 hours and 9 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    window show dissolve
    show screen laura
    with dissolve
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
    show sprinkles happy at middle_s
    hide screen laura
    with dissolve
    pause 0.1
    s "Alright, everyone! Let's start the show!"
    m "Not without me, you're not!"
    s huh "Huh? Who said that?"
    m "I did!"
    show sprinkles at two2_s with easeinleft
    show madeline smile:
        xalign 0.25 yalign -2.0
        ease 0.5 yalign -0.15
        ease 0.25 two1_m
    pause 1.1
    play sound applause
    pause 0.5
    s laugh "Aha! Hello there, Ms. Madeline!"
    m "Hello there, Mr. Sprinkles!"
    s happy "What were you just up to?"
    m "I was helping a family of gophers redecorate their house!"
    s laugh "Wow! How incredible!"
    m "That's my life~!"
    play sound "audio/se/audience_laugh.ogg"
    pause 1
    $l_exp = "smile"
    scene bg fade
    show screen laura
    show kate happy at middle
    with dissolve
    pause 0.1
    # Kate is wearing a Mr. Sprinkles top hat and tuxedo
    k "Ehehehe!"
    "That outfit of hers certainly wasn't cheap, but the smile she gave when she first put it on was enough to make it worth it."
    hide kate with dissolve
    pause 0.1
    $l_exp = "neutral"
    "As we drove, I occasionally checked Twitter for any potential updates I should be aware of."
    "Apparently, there are protests breaking loose outside of city hall, the central Government Safehouse, as many people are being denied access inside."
    "\"{i}Many people are calling it 'unfair' and 'proof that the poor are the ones meant to die'.\"{/i}"
    "\"{i}The mayor has yet to comment on this.\"{/i}"
    $l_exp = "concerned"
    "Sounds about right."
    $l_exp = "neutral"
    s "Our first game of the day is..."
    s "{i}Wild, Wild Races!{/i}"
    play sound applause
    pause 1.0
    show kate happy at middle with dissolve
    pause 0.1
    k "Kota, that's your favorite game!!"
    show kate:
        ease 0.5 two2
    show dakota small_smile at two1 with dissolve
    pause 0.1
    d "I know, Kate."
    k "Ooo! Ooo! Do you think they'll play it on stage tonight?"
    d "It's a 12-hour show, Kate. I'm sure they'll find time."
    k "That would be AWESOME!!!"
    d "Heh. Yes, it would."
    $l_exp = "concerned"
    "Dakota certainly has been acting a bit weird the entire way here."
    $l_exp = "surprised"
    "There's no doubt that she's still thinking about the REDD War."
    r "Alright, here we are!"
    stop music fadeout(3)
    show dakota neutral
    show kate shocked
    $l_exp = "concerned"
    "I honestly hadn't been paying attention our location, but sure enough..."
    scene bg arena_ext with dissolve
    pause 0.1
    $l_exp = "smile"
    "...we were here!"
    play music classy_ghouls
    show kate happy at middle with dissolve
    pause 0.1
    k"YAAAAAAY!!"
    "Kate clapped with joy as we pulled into the massive parking lot."
    hide kate
    show richard glare at middle_r
    with dissolve
    pause 0.1
    r "Well, we may be here, but it's still gonna be a while before we park and get inside..."
    $l_exp = "neutral"
    "He wasn't kidding; the line of cars in the parking lot was massive and moving slower than a snail."
    $l_exp = "surprised"
    l "We should be able to get inside before 7 o'clock, right?"
    r concerned "Hopefully."
    show richard:
        ease 0.5 two1_r
    show kate shocked at two2 with dissolve
    pause 0.1
    k "I hope we do!"
    k excited "I don't wanna miss a second of the show!"
    $l_exp = "smug"
    "Oh, you innocent child..."
    r laughing "I know you don't, Kate."
    r smile "We should be fine."
    r glare "Maybe."
    r "If this guy would just pick up the pace..."
    hide kate
    show dakota confused at two2
    with dissolve
    pause 0.1
    d "Hey, Mom?"
    $l_exp = "neutral"
    l "Yes?"
    d "Isn't that that crazy lady you always complain about?"
    "She asked as she pointed out her window."
    $l_exp = "concerned"
    "I looked to where she was pointing."
    "..."
    $l_exp = "rage"
    l "...oh, you have got to be kidding."
    scene bg arena_ext
    show jessica at middle
    hide screen laura
    with dissolve
    j "Turn back now if you value your children's lives!"
    j "{i}Mr. Sprinkles{/i} is a menace that must be destroyed!"
    "Crowd" "Yeah!!"
    hide jessica
    show screen laura
    with dissolve
    pause 0.1
    l "I swear, that bi--"
    $l_exp = "mad"
    l "{b}woman{/b} doesn't know when to stop."
    show kate excited at middle with dissolve
    pause 0.1
    k "Ooooooo~! Mommy almost said a bad word~!"
    $l_exp = "smug"
    l "That's right, Kate. {i}Almost{/i}."
    "Everyone in the car then gave a laugh before changing the subject."
    $l_exp = "neutral"
    hide kate with dissolve
    pause 0.1
    "I still couldn't believe that Jessica Tate was here protesting."
    "The arena is a Government Safehouse because of Krag Dovason's willingness to help."
    $l_exp = "mad"
    "Of course, that would imply that Krag is a nice guy, thus destroying her message."
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
    hide screen laura
    with dissolve
    window hide dissolve
    pause 1.0
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(2.0)
    pause 4
    $renpy.end_replay()
    $persistent.chapter2_scene3 = True


label meetandgreet:
    python:
        currenttime = "5:13 PM"
        timeleft = "1 hour and 47 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 2
    scene bg arena_ext with dissolve
    window show dissolve
    show screen laura
    with dissolve
    $renpy.pause()
