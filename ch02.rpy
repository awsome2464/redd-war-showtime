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
    "The main headline along the bottom was {i}'MR. SPRINKLES' STAR KRAG DOVASON SPEAKS OUT AGAINST ATLANTA WAR ZONE ANNOUNCEMENT{/i}"
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
    r concerned "...but..."
    r "I guess you weren't completely wrong about everything."
    $l_exp = "concerned"
    d neutral "Huh?"
    r "I didn't realize I had treated you so unfairly."
    r "I guess because you've always done so well at taking care of yourself, I put more focus on making sure Kate is okay."
    r "I'm sorry, Dakota. I really am."
    d sad "..."
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
    d "No, I don't hate you, Kate! Don't ever think something like that!"
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
    python:
        currenttime = "8:52 AM"
        timeleft = "10 hours and 8 minutes"
        l_exp = "neutral"
    call chapterstart
    pause 1
    play music classy_ghouls
    scene bg livingroom
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
    show screen laura
    with dissolve
    "Richard and I really did try our best to sleep, but to no avail."
    "Having the TV on didn't really help, either; no matter where you went, there was something about the REDD War."
    "Even the movie channels didn't help with their constant commercials."
    $l_exp = "concerned"
    "{i}'Come on down to Crazy Jack's Gun Barrel for all your REDD War needs, whether you be the predator or the prey!'{/i}"
    "You really can't escape this event if you tried."
    $l_exp = "neutral"
    "We finally settled on the news again; if the War is going to be on every channel, I may as well pick the channel that could give us information on what to expect."
    a "All across Atlanta, protests are breaking loose outside of city hall, the central Government Safehouse, as many people are being denied access inside."
    a "Many people are calling it 'unfair' and 'proof that the poor are the ones meant to die'."
    a "The mayor has yet to comment on this."
    $l_exp = "concerned"
    l "Sounds about right."
    show richard glare at middle_r with dissolve
    pause 0.1
    r "Speaking of protests at Safehouses, have you seen what Jessica Tate's doing right now?"
    $l_exp = "mad"
    l "Ugh. Do I want to know?"
    "Richard then pointed his phone at me to show me his Twitter feed."
    "There was a woman a bit older than us standing outside the arena where the Mr. Sprinkles show was to be held."
    $l_exp = "rage"
    l "Wow."
    l "Even after it's been revealed it's a Safehouse, she's still going to protest?"
    r concerned "Well, what do you expect? She's always been persistent."
    l "Well, what bullshit is she spreading now?"
    "Richard then played the video."
    scene bg arena_ext
    hide screen laura
    show jessica at middle
    with dissolve
    pause 0.1
    j "The simple fact is that hypocritical REDD like Krag Dovason and Trosh Ranigan need to be taught a lesson!"
    "Crowd" "Yeah!!"
    j "They need to see what happens when you preach about love and peace but then go and kill people!"
    "Crowd" "Yeah!!"
    $l_exp = "rage"
    show screen laura
    l "Oh, for God's sake! Krag didn't even kill anyone, you dumbass!"
    r "You know she can't hear you, right?"
    $l_exp = "mad"
    l "..."
    hide screen laura
    j "Do we want our children being exposed to these liars??"
    "Crowd" "No!!"
    j "Then let's make our voices heard! Let's show Krag Dovason that Mr. Sprinkles is not welcome in our homes!"
    j "We will not rest until {i}Mr. Sprinkles{/i} is dead and forgotten!!"
    "Crowd" "Yeah!!!"
    pause 0.5
    scene bg livingroom
    show screen laura
    show richard concerned at middle_r
    with dissolve
    pause 0.1
    l "Ugh..."
    l "The things some people will do for attention."
    r "I mean, I'm not a fan of the REDD, but I couldn't imagine protesting them like that."
    $l_exp = "rage"
    l "It's not even REDD, in general; it's that one in particular!"
    l "I really can't believe that she has the balls to say that Krag Dovason had involvement in Trosh's actions!"
    r glare "Well, it wouldn't be the first time a pure-hearted celebrity got thrown into the mud for someone's 15 minutes of fame."
    r "Not to mention him being a REDD isn't doing him any favors."
    $l_exp = "mad"
    l "Right, because he can snap his fingers and change the fact that he's a REDD."
    r concerned "That's not what I meant at all, Laura."
    r "Look, let's just drop it. The last thing we need to do right now is stress."
    $l_exp = "neutral"
    l "..."
    l "You're right. I'm sorry."
    r "Nah, I should've known that little ol' Jessica would rustle your feathers, and for that, {b}I'm{/b} sorry."
    r smile "But anyway, what do you say I whip up some breakfast?"
    $l_exp = "smug"
    l "Oh, really?"
    l "You realize you don't have any reason to keep buttering me up, right?"
    l "I mean, unless you want Round 2."
    r "Hey, a man can't make food for his family out of the goodness of his heart?"
    $l_exp = "smile"
    l "Well, sure, a man can, but {b}this{/b} man never does."
    r "Well, I feel like we could all use a welcome surprise."
    l "Well, alright, then. Be my guest!"
    hide richard with dissolve
    pause 0.1
    "Richard then went into the kitchen."
    "God help us."
    k "Mommy?"
    $l_exp = "neutral"


