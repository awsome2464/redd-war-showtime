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
    "Crowd" "\"Yeah!!\""
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
    play ambience crowd
    play music the_calm
    scene bg livestage with dissolve
    window show dissolve
    show screen laura
    with dissolve
    "Thankfully, the wait wasn't as long as we thought it would be."
    $l_exp = "smile"
    "We were still very early, but given the circumstances, that's not necessarily a bad thing."
    $l_exp = "concerned"
    "Well, unless you've got a child who takes any chance she can to complain about being bored."
    show dakota mad at middle with dissolve
    pause 0.1
    d "What are we supposed to do for 2 hours?"
    $l_exp = "neutral"
    l "We could always walk around a bit to see what they've got."
    $l_exp = "smile"
    l "They're selling a lot of merch, if you're interested."
    d neutral "Eh."
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
    show dakota:
        ease 0.5 two1
    show richard glare at two2_r with dissolve
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
        ease 0.5 left
    show richard:
        ease 0.5 right_r
    show kate happy at middle with dissolve
    pause 0.1
    $l_exp = "surprised"
    k "Come on!! Let's go!!"
    "Kate grabbed on to me and tried yanking me out of my seat."
    k "I wanna see Mr. Sprinkles!!"
    $l_exp = "sad"
    l "Kate, not so loud, please."
    k @ shocked "Sorry."
    k "I just wanna see him!"
    $l_exp = "smug"
    l "I know you do."
    "I then looked over to my other daughter."
    l "What do you say? Wanna take time away from your phone to see Mr. Sprinkles?"
    d small_smile "..."
    $l_exp = "excited"
    "I suppose that answers that."
    r laughing "I guess we better hurry; that line is gonna get long pretty quickly."
    $l_exp = "neutral"
    "Sure enough, the exits to the room were nearly blocked by families trying to get out."
    $l_exp = "smile"
    l "Well, we've got about an hour until the session ends; let's get to it!"
    hide screen laura
    with dissolve
    pause 0.5
    scene bg arena_hall with fade
    pause 1
    $l_exp = "neutral"
    show screen laura
    with dissolve
    pause 0.1
    "By the time we got settled in the line, there were certainly a lot of people in front of us."
    $l_exp = "concerned"
    "We couldn't even see the front of the line or any indication that the end led to a meet-and-greet."
    $l_exp = "neutral"
    "But at least the line was moving at a decent pace."
    "I'm sure the people in front are only getting less than a minute to meet him and get autographs, but for kids, that should be enough."
    $l_exp = "concerned"
    "Hopefully."
    show richard glare at middle_r with dissolve
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
    $l_exp = "concerned"
    show richard concerned
    "We looked forward and saw a middle-aged REDD turned around and glaring at us."
    "{color=#d00000}REDD{/color}" "\"We are not 'aliens'! This planet is our home, as well! Not just yours!\""
    $l_exp = "sad"
    "I was taken aback, to say the least."
    l "I-I'm terribly sorry, Ma'am. I didn't mean to be offensive."
    "She sighed before continuing."
    "{color=#d00000}REDD{/color}" "\"Just watch yourself. If the wrong REDD hears you say that, especially with the upcoming event, you could get yourself in deep trouble.\""
    $l_exp = "surprised"
    l "..."
    "She then faced forward again as the line moved up a bit."
    "..."
    "Well, that was awkward."
    $l_exp = "concerned"
    "I guess with the REDD, you really do need to watch what you do. Even the smallest, seemingly insignificant thing can set them off."
    hide richard
    show kate excited at middle
    with dissolve
    pause 0.1
    k "Mommy?"
    $l_exp = "smile"
    l "Yes, sweetie?"
    k "Do you think Mr. Sprinkles will like my costume?"
    $l_exp = "smug"
    l "Are you kidding? He's going to love it!"
    l "I don't see anyone else here wearing such an authentic-looking Mr. Sprinkles outfit, do you?"
    k "Nope~!"
    k "Ooo! I wonder if he'll remember me and let me go on stage during the show!"
    $l_exp = "excited"
    l "Well, let's not get ahead of ourselves, Kate."
    l "There are a lot of people here; any one of them has a chance of being picked."
    k mad"Yeah, but none of them are wearing outfits as good as mine!"
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
    with dissolve
    pause 0.5
    scene bg arena_hall with fade
    pause 1
    $l_exp = "neutral"
    show screen laura
    with dissolve
    pause 0.1
    "About a half hour later, as well as Kate rambling on about what she's the most excited about tonight, we finally saw the front of the line ahead of us."
    $l_exp = "smile"
    "And at the front of the line was..."
    show kate shocked at middle with dissolve
    pause 0.1
    k "Mr. Sprinkles!"
    hide kate with dissolve
    pause 0.1
    stop ambience fadeout(3)
    play music sprinkles_theme
    show sprinkles happy at middle_s with dissolve
    pause 0.1
    "Sure enough, there he was behind the table talking to a young fan."
    $l_exp = "smug"
    "I have to admit that there's always something surreal about seeing someone in person after seeing them behind a screen for so many years."
    $l_exp = "determined"
    "I mean, I've been to my fair share of concerts and the like before, but the feeling never goes away."
    "But for people like Kate and Dakota who have never felt the feeling before..."
    hide sprinkles
    show kate happy at two1
    show dakota small_smile at two2
    with dissolve
    pause 0.1
    k "I can't believe it! He's right there!"
    d "Yeah! And he actually looks happy to be here, too!"
    k excited "Of course he does! He's awesome like that!"
    $l_exp = "excited"
    "...it's just sweet and innocent."
    scene bg arena_hall with dissolve
    pause 0.1
    "Finally, it came the big moment."
    show sprinkles laugh at middle_s with dissolve
    pause 0.1
    s "It was nice to meet you, Mandy! I hope you enjoy the show!"
    s happy "Next~!"
    show sprinkles at right_s with easeinleft
    show kate happy at middle
    show dakota small_smile at left
    with easeinleft
    pause 0.5
    "He then looked at Kate with awe."
    s huh "My word!"
    k shocked "..."
    "Mr. Sprinkles then turned to Dakota."
    s happy "I must say that this is one fine mirror you have here!"
    show kate happy
    show dakota smirk
    "Both girls gave out a giggle."
    s huh "Although it appears to be a bit broken."
    "He commented as he waved his arm a bit while looking at Kate."
    "Taking the hint, Kate tried to mimic his movements."
    s jeer "Hm. A bit delayed, I see."
    "Finally, Kate giggled more and took off her hat."
    k "I'm not a mirror, Mr. Sprinkles! I'm Kate!"
    s laugh "Oh! Ahahaha!"
    s happy "Well, you certainly had me fooled, Kate!"
    s "And who's this with you?"
    k excited "This is my sister, Kota!"
    d small_smile "I-It's {b}Da{/b}kota, actually."
    s jeer "I see. Well, it's still a very nice name."
    d "Th-Thank you."
    k happy "Mommy, can you take a picture of us with Mr. Sprinkles??"
    $l_exp = "determined"
    l "Of course!"
    "I then took out my phone as everyone got into position."
    l "Everyone smile~!"
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
    scene bg arena_hall
    show screen laura
    show sprinkles happy at right_s
    show kate happy at middle
    show dakota small_smile at left
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
        ease 0.5 two2_s
    show richard glare at two1_r with easeinleft
    pause 0.1
    stop music fadeout(3)
    r "Hold on. Can I ask you something, first?"
    $l_exp = "sad"
    "Richard, what the hell are you doing...?"
    s huh "Oh.{w=0.5}{nw}"
    s laugh "Oh.{fast} Why, certainly, Sir."
    r concerned "I just..."
    "He then lowered his voice a bit as he leaned forward."
    r "...wanna make sure we're gonna be safe."
    r "You know, concerning the {b}other{/b} event going on tonight."
    s hm "..."
    "He sat there for a second before regaining a smile and answering."
    s jeer "I understand your concern, Sir, but there's nothing to worry about."
    s "We have the best guards on the planet protecting the building, as well as the best window and door shields money can buy."
    s "Once the event starts, nobody is getting inside this building. You have my word."
    r "..."
    r smile "Thanks."
    s laugh "No problem at all, Sir."
    s jeer "Any other questions?"
    r "No, that's it."
    s "Very well."
    s laugh "Next~!"
    scene bg arena_hall with dissolve
    pause 0.1
    $l_exp = "neutral"
    "After the four of us got out of the line and started heading back towards the main stage, I leaned a bit closer to Richard."
    show richard concerned at middle_r with dissolve
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
    "Well, the show's about to begin soon."
    $l_exp = "concerned"
    "I suppose we have enough time to look around at the vendors and get some merchandise."
    $l_exp = "smug"
    "Maybe even a quick meal before the show."
    "..."
    $l_exp = "neutral"
    "..."
    hide screen laura
    with dissolve
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
    """
    nvl clear
    narrate """
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
    window hide dissolve
    pause 4
    $renpy.end_replay()
    $persistent.chapter2_scene4 = True
    

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
    pause 1
    play sound "audio/se/chime.ogg"
    pause 3.5
    window show dissolve
    s "Okay, everyone~! The show will begin in exactly 5 minutes!"
    s "Please use this time to head to your seats so we may start the show with full seats~!"
    s "This will truly be a good night of fun; I can't wait to share it with you all!"
    pause 1
    show screen laura
    with dissolve
    pause 0.1
    "Well, we're almost there."
    show kate happy at middle with dissolve
    show kate:
        ease 0.5 yalign 0.45
        ease 0.5 yalign 0.5
        repeat
    pause 0.1
    "Kate was jumping in her seat."
    hide kate
    show dakota neutral at middle
    with dissolve
    pause 0.1
    "Dakota was tapping her foot quickly as her hands sat in her lap."
    hide dakota
    show richard concerned at middle_r
    with dissolve
    pause 0.1
    "And Richard was still, but was clearly showing signs of nervousness."
    $l_exp = "excited"
    hide richard with dissolve
    pause 0.1
    "Well, at least one of the Farrs were focused on the show."
    $l_exp = "neutral"
    stop ambience fadeout(3)
    "Finally, after what seemed like forever, the lights started to dim."
    "A bright red square projected onto the curtain."
    "I looked at the time."
    "6:59"
    hide screen laura
    window hide
    queue sound ["audio/se/warning.ogg", "audio/se/commencement.ogg"]
    scene bg commencement
    show commencement_overlay
    with Dissolve(5)
    show announcetext "This is not a test. This is the official commencement of the Annual REDD War." at truecenter with dissolve
    pause 3.5
    hide announcetext with dissolve
    show announcetext "At the siren, all REDD within certified War Zones will be exempt from any and all crime, including murder, for 12 consecutive hours. All humans who commit crime during these hours, excluding crimes committed for self-defense purposes, will receive the appropriate punishment at the conclusion of the REDD War." at truecenter with dissolve
    pause 16
    hide announcetext with dissolve
    show announcetext "Weapons of Class 3 and lower have been authorized for use; all other weapons are forbidden." at truecenter with dissolve
    pause 4.5
    hide announcetext with dissolve
    show announcetext "Government Safehouses, and by extension the contents within, have been granted immunity from the REDD War and must not be harmed." at truecenter with dissolve
    pause 5.5
    hide announcetext with dissolve
    show announcetext "All emergency services will be suspended until the siren sounds again at the conclusion of the REDD War." at truecenter with dissolve
    pause 5
    hide announcetext with dissolve
    show announcetext "On behalf of your government and the REDD, we thank you for your cooperation and wish you the best of luck." at truecenter with dissolve
    pause 4.5
    hide announcetext with dissolve
    pause 7
    play sound siren
    pause 3
    scene bg fade
    with Dissolve(3)
    pause 1
    scene bg livestage
    with Dissolve(3)
    "End"

