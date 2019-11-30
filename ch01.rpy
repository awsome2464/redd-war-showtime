label start:
    play sound "audio/se/gong.ogg"
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(1.0)
    pause 3
    call chaptername
label meetthefarrs:
    stop music
    call chapterstart
    pause 2
    play sound drumroll_buildup loop
    scene bg curtain
    show dark
    with dissolve
    pause 0.5
    hide dark
    show spotlight at spotlight_wander
    window show dissolve
    "Okay, everyone! Put your hands together for the one...!"
    "...the only...!"
    "{i}Mr. Sprinkles!{/i}"
    show spotlight at spotlight_focus
    window hide
    play sound drumroll_finish
    pause 1.0
    hide spotlight
    show dark
    pause 0.5
    play music sprinkles_theme
    play sound applause
    scene bg showstage with slideawayup
    pause 1.0
    show sprinkles laugh cane hat at middle_sprinkles with dissolve
    pause 0.1
    window show dissolve
    s "Ahaha! Thank you! Thank you, everyone!"
    s happy rightdown "Wow! We've got quite a large audience out here tonight, don't we?"
    s laugh "Are you all excited for the show?!"
    "Audience" "\"Yeah!!\""
    s jeer "Oh, come on; you all can do better than that~!"
    s laugh "Are you all excited for the show?!"
    "Audience" "{b}{i}\"YEAH!!!\"{/i}{/b}"
    s hat "Ahahaha! Alright, then! Let's start the show!"
    window hide
    pause 1.0
    scene bg livingroom
    with Dissolve(1.5)
    pause 0.1
    show screen laura
    window show dissolve
    pause 0.1
    "Now that the girls were going to be distracted for a half hour, I sat down and looked at my phone."
    "Richard had texted me that he was going to be stopping to get groceries after work."
    "After making sure he remembered to grab an extra loaf of bread, I closed my eyes and stretched on the chair."
    k "Mommy?"
    $l_exp = "concerned"
    "That didn't take long."
    show kate happy down at middle with dissolve
    pause 0.1
    $l_exp = "smile"
    l "Yes, sweetie?"
    k "When's Daddy gonna be home?"
    show kate:
        ease 0.5 two1
    show dakota mad side at two2 with dissolve
    pause 0.1
    d "The same time he gets home every night, idiot!"
    show kate mad
    $l_exp = "mad"
    l "Dakota!"
    d confused "What?"
    l "You know better!"
    show dakota mad crossed
    "She simply turned back to the TV with a huff of anger."
    l "Apologize, young lady!"
    "Dakota turned back to me with an exaggerated angry pout on her face."
    $l_exp = "rage"
    l "{b}Now.{/b}"
    "She groaned and turned to her sister."
    d side "I'm {b}{i}sorry{/i}{/b}."
    $l_exp = "neutral"
    "As tempted as I was to get her to say it like she meant it, I didn't have the energy."
    show kate happy
    "Besides, Kate didn't seem to care, either way."
    "She just turned back to the TV as Mr. Sprinkles continued his show."
    hide screen laura
    scene bg showstage
    show sprinkles rightdown cane happy at middle_sprinkles
    with dissolve
    pause 0.1
    s "Alright, everyone! Let's start the show!"
    woman "Not without me, you're not!"
    s huh "Huh? Who said that?"
    woman "I did!"
    "Suddenly, an energetic young woman entered the set via the fireplace on the back wall."
    play sound applause
    show sprinkles at two2_sprinkles with easeinleft
    show madeline down excited at two1 with dissolve
    pause 0.5
    s laugh hat "Aha! Hello there, Ms. Madeline!"
    m "Hello there, Mr. Sprinkles!"
    "She replied as she adjusted her hat and brushed her shoulders."
    s happy rightdown "What were you just up to?"
    m "I was filling in for Santa Claus while he's on vacation!"
    s laugh "Wow! How merry!"
    "Ms. Madeline gave an exaggerated shrug as she stared at the camera."
    m shrug "That's my life~!"
    play sound "audio/se/audience_laugh.ogg"
    "The audience gave a laugh in response."
    s happy "Anyway, are you ready to have fun?"
    m smile down "I sure am!"
    s laugh hat "Splendid~!"
    s happy "Now, what do you say we spin the Wacky Dartboard to see what we'll play first?"
    m "Why, I'd say that's a great idea, Mr. Sprinkles!"
    scene bg showstage with dissolve
    pause 0.1
    play sound applause
    "The audience cheered as the large dartboard was pulled onto the stage."
    "It was basically a giant wheel that you'd spin to pick a choice, but modified to look like a dartboard, while also being motorized."
    show sprinkles laugh leftdown hat at middle_sprinkles with dissolve
    pause 0.1
    s "Alright, let's get started!"
    s happy rightdown "Ms. Madeline, if you please."
    "Ms. Madeline then handed Mr. Sprinkles a large dart with a Velcro tip as the wheel started to turn."
    "The audience cheered and encouraged him as he dramatically spun his arm in a forward motion before finally letting go of the dart."
    "With a small thunk, the dart stuck to the board, which then began to stop spinning."
    "Mr. Sprinkles walked over to the board with a grin."
    s "And our first game of the day is..."
    "He then looked at where the dart had landed."
    s laugh hat "{i}Mirror Madness!{/i}"
    show game_name "Mirror Madness" at game_name_flash
    play sound applause
    "The audience cheered again as the game's name flashed onto the screen."
    hide game_name
    s happy rightdown "Alright, we will need 4 brave volunteers to play this game with us!"
    show screen laura
    scene bg livingroom
    with dissolve
    pause 0.1
    "Mr. Sprinkles and Ms. Madeline each picked 2 children from the audience to join them on the stage."
    "As they did, Kate turned to me with a large smile."
    show kate happy down at middle with dissolve
    pause 0.1
    k "Mommy, will I get to be on stage with Mr. Sprinkles tomorrow?"
    $l_exp = "sad"
    l "Well, uh..."
    l "...I don't know, honey."
    show kate shocked fidget
    "Her smile went away in the blink of an eye."
    $l_exp = "smile"
    l "But I think you'll have a good shot at it!"
    show kate happy
    "That seemed to do the trick."
    k "Really?"
    k up "Yay!!"
    "She then began clapping ecstatically, much to Dakota's dismay."
    show kate:
        ease 0.5 two1
    show dakota neutral hips at two2 with dissolve
    pause 0.1
    d "Just don't cry when you don't actually end up on stage."
    show kate concerned fidget
    $l_exp = "concerned"
    "..."
    s "Alright, everyone!"
    hide screen laura
    scene bg showstage
    show sprinkles laugh cane hat at middle_sprinkles
    with dissolve
    pause 0.1
    s "Now that we have our players, we need to set up the game!"
    s happy rightdown "While we do, enjoy the brief performance from our very own Jingle and Jangle!"
    stop music fadeout(3.0)
    play sound applause
    hide sprinkles with dissolve
    show jingle up open_smile at two1
    show jangle up open_smile at two2
    with dissolve
    pause 0.1
    "On cue, the twin mimes entered the stage with a bow."
    play music the_twins
    "They then got into position for their skit."
    scene bg showstage with dissolve
    pause 0.5
    show jingle down smile at middle zorder 2 with dissolve
    pause 0.1
    "Jingle was sitting on an invisible chair flicking through channels on an invisible TV with an invisible remote."
    show jingle at right
    show jangle down smile at two1 zorder 1
    with easeinleft
    pause 0.1
    "Jangle walked onto the stage and stopped a few yards away."
    "After he knocked on the 'door', Jingle turned towards it and walked over."
    show jingle at two2 with easeinleft
    pause 0.1
    show jingle smile
    "She tried turning the knob and pulling..."
    show jingle confused
    "...but the door didn't open."
    show jangle confused
    "Jangle, looking a bit confused, knocked again."
    show jingle stern:
        ease 0.1 xalign 0.81
        ease 0.1 xalign 0.8
    "Jingle grabbed onto the knob with both hands and yanked hard."
    show jangle stern
    "Jangle knocked again."
    "Looking a bit more annoyed, Jingle backed up a bit and tried kicking the door."
    show jingle:
        ease 0.5 xalign 0.85
        ease 0.1 xalign 0.8
    pause 0.6
    show jangle confused:
        ease 0.25 xalign 0.2
    "Now Jangle backed up and stared at the door with confusion."
    show jingle:
        ease 0.1 ypos -10
        ease 0.1 ypos 0
        pause 0.1
        repeat 3
    "After stomping up and down a few times, Jingle took a deep breath to calm herself."
    show jingle confused:
        ease 1.5 right
    "After then stomping over to the far side of the stage, she spun around on one foot and rolled up her imaginary sleeves in an exaggerated fashion."
    show jangle:
        ease 1.0 xalign 0.25
    "Meanwhile, Jangle slowly re-approached the door."
    show jingle:
        ease 0.1 ypos -10
        ease 0.1 ypos 0
        repeat
    "Jingle jogged in place for a second before sprinting towards the door."
    "When she was halfway there, Jangle grabbed the doorknob and pulled it towards him successfully."
    window hide
    show jingle:
        ease 0.2 xalign 0.33
    pause 0.2
    play sound "audio/se/crash.ogg"
    if persistent.flash:
        show white zorder 5
        hide jingle
        hide jangle
        pause 0.05
        hide white
    else:
        scene bg showstage with dissolve
    pause 2
    window show dissolve
    "The two stood up while rubbing their heads in pain."
    show jangle down happy_grin zorder 1:
        left
        xalign -0.1
    show jingle down happy_grin at two1 zorder 2
    with dissolve
    pause 0.1
    "After realizing what had happened, the two gave off silent laughs before hugging each other."
    show jingle up smile
    show jangle smile
    "Jingle then gestured towards the doorway, inviting Jangle into the house."
    show jingle down:
        ease 1.0 xalign 1.1
    show jangle:
        ease 1.0 two2
    pause 2
    show jingle up happy_grin at two2
    show jangle up happy_grin at two1
    with easeinright
    pause 0.1
    "The twins then took center stage and bowed."
    stop music fadeout(2.0)
    play sound applause
    pause 1.5
    scene bg showstage with dissolve
    pause 0.5
    play music sprinkles_theme
    show sprinkles laugh cane rightdown at middle_sprinkles with dissolve
    pause 0.1
    s "Ahaha! Absolutely wonderful!"
    s happy hat "Alright, then! The {i}Mirror Madness{/i} maze is all set up! Let's get started, shall we?"
    hide sprinkles with dissolve
    pause 0.1
    "The screen then showed a large maze in another part of the room."
    "The maze in question had an entrance in each of its corners, with one child volunteer standing at each corner."
    "After Mr. Sprinkles went around and had each volunteer introduce themselves, he went on to explain the game."
    show sprinkles jeer rightdown cane at middle_sprinkles with dissolve
    pause 0.1
    s "Alright, here's how the game works:"
    s "Each of our players will start at one of the maze's entrances."
    s @ laugh "When I say 'go', they will all enter the maze and race to the center, the first one there being the winner!"
    s "But as you may have been able to tell, this isn't your normal maze."
    s laugh hat "The walls of this maze are covered in mirrors~!"
    s happy "Oh, this is certainly going to be exciting!"
    s "Alright, is everyone ready?"
    $l_exp = "neutral"
    show screen laura
    scene bg livingroom
    with dissolve
    pause 0.1
    "Suddenly, Dakota stood up and walked out of the room."
    $l_exp = "concerned"
    show kate confused down at middle with dissolve
    pause 0.1
    k "Kota, where are you going?"
    d "I've seen this episode before. The girl in the red shirt wins."
    "She then went up the stairs with both Kate and myself watching her."
    $l_exp = "sad"
    "..."
    "Dakota has always been a bit of a drama queen, but this seemed out of character even for her."
    "I got off the chair and made my way up the stairs."
    "Kate, meanwhile, just turned back to the TV."
    stop music fadeout(3.0)
    pause 0.5
    scene bg dakotaroom
    with dissolve
    pause 0.5
    "I found my daughter lying on her bed, phone in hand."
    show dakota neutral crossed at middle
    with dissolve
    pause 0.1
    l "Everything okay?"
    d "..."
    "I sat on the foot of the bed."
    $l_exp = "concerned"
    l "Let me guess."
    l "You're scared about tomorrow."
    d sad "..."
    "She stopped scrolling through her phone for a second before continuing."
    play music autumn_changes
    $l_exp = "sad"
    l "Listen, I get why you are."
    l "You're not the only one, I assure you."
    d neutral "..."
    $l_exp = "neutral"
    l "But sweetheart, we'd never go to the show if we didn't feel like everything would be okay."
    l "You know we'd never put you girls at risk like that, right?"
    d sad "I do, but..."
    d "...I'm not scared about the show."
    $l_exp = "surprised"
    l "..."
    $l_exp = "concerned"
    l "Ah. You're scared of what'll be going on at the same time."
    d "...yeah."
    $l_exp = "sad"
    l "Oh, Dakota..."
    "I got closer to my girl and extended my arms outward for a hug."
    "She looked at me for a second before accepting it tightly."
    l "Listen, baby, the REDD War is something we just need to accept as reality."
    l "We should be thankful that Atlanta's never been chosen for one."
    d "But what if this time, it is?"
    "She held on to me even tighter."
    $l_exp = "surprised"
    l "I..."
    l "I don't know, Dakota."
    $nvl = True
    hide screen laura
    nvl show dissolve
    narrate """
    We sat there in silence, not really sure where to go from there.

    While larger cities always have a higher chance of being picked as a War Zone, there are so many in both the country and the world that the chances of ours getting picked is like winning the lottery.

    You know, the kind you {b}don't{/b} want to win.
    """
    nvl clear
    narrate """
    We didn't always have to live in fear like this.

    It seemed like only yesterday when the world didn't know of the existence of the REDD.

    But for children like Kate and Dakota, this modern world is all they knew.

    Well, technically Dakota was already born when they first came to Earth, but she was too young to remember that.

    But just because it's all you know doesn't mean you get used to it.

    Honestly, I don't think I {b}want{/b} my little angels to be used to it.

    Thankfully, Kate's at that age where she's a bit oblivious to the world around her, always seeing the best in everything.

    Dakota, on the other hand, is growing up, despite my wishes.

    She's starting to better understand what exactly the REDD are and how that one night affects so many people.

    I know I can't shelter her in a little bubble and pretend this doesn't happen, but I'm really not sure what to do to help her.

    It's not like I went through the same thing when I was her age.
    """
    $nvl = False
    nvl clear
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    l "Look..."
    $l_exp = "smile"
    l "If nothing else, just know that all 4 of us will be together."
    l "And as long as that's true, nothing will stand in our way."
    show dakota small_smile
    "She gave a small laugh."
    d side "Do you have any idea how lame that sounded?"
    $l_exp = "determined"
    l "Of course I do. I just wanted to see if you were listening to me."
    d smirk hips "Either you're telling the truth, or that was the fastest recovery ever made."
    l "My lips are sealed."
    d small_smile "Haha..."
    "I gave her a quick kiss on the top of her head before I heard a noise from downstairs."
    $l_exp = "smile"
    k "Daddy!!"
    "Dakota broke from the hug and turned towards her bedroom door."
    $l_exp = "smug"
    l "Go on."
    hide dakota with easeoutleft
    pause 0.1
    "She bolted out of the room and down the stairs."
    $l_exp = "smile"
    "Well, I'm glad that went okay."
    "Maybe Richard and I can talk about this tonight."
    "With that, I went downstairs."
    stop music fadeout(0.6)
    scene bg livingroom
    show kate excited up at middle_short zorder 1
    with dissolve
    pause 0.1
    play music the_calm
    k "Hi, Daddy~!!"
    show kate:
        ease 0.5 two2_short
    show richard down laughing at two1 zorder 2 with dissolve
    pause 0.1
    r "Ahaha! Hey there, pumpkin!"
    show kate:
        ease 0.5 two2
    "He picked up his daughter and gave her a hug."
    r smile "How was your day?"
    k happy down "Amazing!"
    r "Oh? Why is that?"
    k up "I got to eat a burger as big as my head!"
    r laughing "Oh, is that right?"
    "He then glanced over at me for confirmation."
    $l_exp = "determined"
    l "She {b}wishes{/b} it was that big."
    "I ratted as I walked over and rubbed Kate's back with a chuckle."
    show richard at left
    show kate at middle
    show dakota confident hips at right_short
    with easeinright
    pause 0.1
    d "Yeah, and I'M the one who had to end up finishing it for her!"
    k shocked fidget "Nuh-uh!"
    d smirk "I'm literally the only person who knows for a fact that I did!"
    show kate mad down
    "Clearly caught in her lie, Kate buried her head in her father's shoulder in defeat."
    r smile "Hahaha! Alright, did anything else exciting happen today?"
    k happy up "I got to watch Mr. Sprinkles!"
    show richard concerned
    "He then looked towards the TV."
    r "...is that right?"
    $l_exp = "neutral"
    show dakota neutral
    l "..."
    k "Yeah, and it was awesome!!"
    r laughing "Oh, I'm sure it was, sweetie!"
    show kate:
        ease 0.5 middle_short
    "He then set her down."
    r smile "Anyway, we've got groceries to get in! Everyone helps!"
    hide screen laura
    stop music fadeout(3.0)
    scene bg livingroom
    with dissolve
    pause 0.1
    "After we all got the groceries in the house, the girls went back into the living room to watch TV, leaving Richard and I to put them all away."
    show screen laura
    play music autumn_changes
    show richard crossed concerned at middle with dissolve
    pause 0.1
    r "Laura, we talked about Mr. Sprinkles."
    $l_exp = "sad"
    l "I'm sorry, but Kate wouldn't stop asking."
    $l_exp = "neutral"
    l "Besides, we're still going to that show tomorrow, anyway, so what's the harm?"
    r "I just..."
    "He placed the cans in the cupboard before slowly closing it, clearly stalling to find a way to finish that sentence."
    r down "I just don't want her to get hurt."
    r "Sooner or later, she's going to realize what he is and what they do."
    $l_exp = "concerned"
    l "Richard--"
    r @ glare "I know not all of them are like that."
    r "But as long as there's a REDD War, the ones that {b}are{/b} like that will continue to just..."
    r crossed glare "Well, you know what that producer did last year."
    $l_exp = "neutral"
    "I took a deep breath and looked down."
    l "Yes, I do."
    r "How am I supposed to trust any of those things when they kill entire households?"
    r "Households that had {b}children{/b} in them?"
    r rage "That's just fu--"
    show richard concerned
    "He then shot a quick glance towards the living room and then back at me."
    r "...{b}messed{/b} up."
    $l_exp = "sad"
    l "I'm not denying that, Richard."
    l "But I'm not going to judge them all based on the actions of the majority."
    $l_exp = "surprised"
    l "Plus, Krag Dovason has made it very clear that he disapproved his brother's actions."
    r glare "Oh, I'm sure anyone who has their show being boycotted would say something like that."
    $l_exp = "sad"
    "We looked at each other in the eye, unsure where to take this discussion before it evolves into a full argument."
    show richard concerned
    "He sighed before turning towards the living room."
    "Kate's eyes were glued to the TV while Dakota's were on her phone."
    r down "I just want our girls to be safe."
    r "To have long, healthy lives."
    l "And I do, too, Richard. I want that more than anything."
    l "But the REDD aren't going anywhere, and neither is the REDD War."
    l "If it hasn't gone away in 7 years of protest, what chance does it have of ever going away in the future?"
    r glare "..."
    $l_exp = "surprised"
    "I gave him a small hug and leaned my head on his shoulder."
    l "We live in a new world, Richard. We just gotta accept it. Work with it. Adapt to it."
    r concerned "..."
    "He finally sighed."
    r "I don't think I'll ever be able to accept it, Laura."
    r crossed "I'm sorry, but there's just no way I can see those things as anything but monsters."
    $l_exp = "sad"
    l "..."
    $l_exp = "determined"
    "I then grimaced as I pulled back a bit."
    l "Well, if nothing else, can you try and accept it for your daughters?"
    r glare "..."
    $l_exp = "excited"
    l "At least for the show tomorrow."
    l "They're really looking forward to this, honey. Don't let your bias get in the way of their fun."
    $l_exp = "determined"
    l "Tomorrow's about {b}them{/b}."
    r concerned "..."
    "Finally he gave a small smile."
    r down smile "Alright, you win."
    $l_exp = "smug"
    l "As usual."
    "We then gave each other a quick kiss before putting the rest of the groceries away, sans the ones needed for that night's meal."
    call sceneend
    if not persistent.scenes["ch1_s1"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch1_s1"] = True


label kragonnews:
    python:
        l_exp = "neutral"
        currenttime = "6:39 PM"
        timeleft = "21 minutes"
        timeofday = "night"
    call chapterstart
    pause 1
    play music the_calm
    scene bg livingroom
    with Dissolve(2.0)
    pause 0.5
    show screen laura
    window show dissolve
    pause 0.1
    "After dinner, the girls went upstairs to do their own thing while Richard and I stayed in the living room."
    "Though we weren't really talking to each other much; we were mostly just scrolling through our phones, only occasionally showing each other funny or relevant posts."
    "But then..."
    show richard down glare at middle with dissolve
    pause 0.1
    r "Have you seen what Jessica Tate's doing right now?"
    $l_exp = "mad"
    l "Ugh. Do I want to know?"
    "Richard then pointed his phone at me to show me his Twitter feed."
    "There was a woman a bit older than us standing outside the arena where the Mr. Sprinkles show was to be held."
    $l_exp = "rage"
    l "Wow."
    l "What bullshit is she spreading now?"
    "Richard then played the video."
    scene bg theater_ext
    hide screen laura
    show jessica stand_hip at middle
    with dissolve
    pause 0.1
    j "The simple fact is that hypocritical REDD like Krag and Trosh Dovason need to be taught a lesson!"
    "Crowd" "\"Yeah!!\""
    j stand_up "They need to see what happens when you preach about love and peace but then go and kill people! {b}CHILDREN{/b}, no less!"
    "Crowd" "\"Yeah!!\""
    $l_exp = "rage"
    $quickhide = True
    show screen laura
    l "Oh, for God's sake! Krag didn't even kill anyone, you dumbass!"
    r "You know she can't hear you, right?"
    $l_exp = "mad"
    l "..."
    hide screen laura
    j stand_hip "Do we want our children being exposed to these liars??"
    "Crowd" "\"No!!\""
    j "Then let's make our voices heard! Let's show Krag Dovason that Mr. Sprinkles is not welcome in our homes!"
    j stand_up "We will not rest until {i}Mr. Sprinkles{/i} is dead and forgotten!!"
    "Crowd" "\"Yeah!!!\""
    $quickhide = False
    scene bg livingroom
    show screen laura
    show richard down concerned at middle
    with dissolve
    pause 0.1
    l "Ugh..."
    l "The things some people will do for attention."
    r crossed "I mean, I'm not a fan of the REDD, either, but I couldn't imagine protesting them like that."
    $l_exp = "rage"
    l "It's not even REDD, in general; it's that one in particular!"
    l "I really can't believe that she has the balls to say that Krag Dovason had involvement in Trosh's actions!"
    r glare "Well, it wouldn't be the first time a pure-hearted celebrity got thrown into the mud for someone's 15 minutes of fame."
    r "Not to mention him being a REDD isn't doing him any favors."
    $l_exp = "mad"
    l "Right, because he can snap his fingers and change the fact that he's a REDD."
    r concerned "That's not what I meant at all, Laura."
    r down "Look, let's just drop it. The last thing we need to do right now is stress."
    $l_exp = "neutral"
    l "..."
    l "You're right. I'm sorry."
    r smile "Nah, I should've known that little ol' Jessica would rustle your feathers, and for that, {b}I'm{/b} sorry."
    "Before we could get into this more, Dakota came downstairs."
    show richard:
        ease 0.5 two2
    show dakota neutral crossed at two1_short with easeinleft
    pause 0.1
    d "Can I watch TV?"
    $l_exp = "smile"
    l "Sure."
    "I turned on the TV and passed her the remote."
    "I honestly expected her to turn it to some cartoon channel."
    $l_exp = "concerned"
    show richard concerned
    "So it was a bit odd when she switched to the evening news."
    a "With only 15 minutes until the 5 War Zones are announced for the world to hear, we now welcome a special guest to the studio, mister Krag Dovason!"
    $l_exp = "neutral"
    "Ah. That explains it."
    a "Some of you might know Mr. Dovason by the name that so many children know him as, Mr. Sprinkles."
    play music neon_runner
    scene bg newsroom
    hide screen laura
    with dissolve
    pause 0.5
    a "Thank you for coming, Mr. Dovason!"
    show krag laughing down at middle with dissolve
    pause 0.1
    kr "Oh, thank you for having me, Chuck."
    "Wow. Without that bright outfit and blue hair, he looks like a completely different person."
    "...well, a completely different REDD."
    "Actually, if anything, he looks just like an average REDD."
    a "So, Krag, first of all, I'd like to apologize if I at any point call you Mr. Sprinkles."
    kr smile "Hahaha! Oh, I would take no offense to that at all."
    a "That's a relief. But speaking of Mr. Sprinkles, I suppose we should bring up why you're here."
    a "Your recent decision to host a live show here in Atlanta during the REDD War, what is undoubtedly the most dangerous event in the world, has sparked some controversy."
    kr concerned down "Yes, it certainly has received more backlash than I had anticipated."
    kr "But as you said, the REDD War is the most dangerous thing that modern society has done, leading to many people of all ages dreading it."
    kr smile hips "So I decided to try and do something to take people's minds off the event and give them something more fun to do."
    kr laughing "Instead of watching TV and seeing murder, you can see non-lethal activities performed by people in a safe environment!"
    a "You certainly seem to have everyone's best interest in mind."
    kr smile "I'm an entertainer, Chuck. If I'm not entertaining someone, my life has no purpose."
    $l_exp = "neutral"
    scene bg livingroom
    show screen laura
    with dissolve
    pause 0.1
    "I turned over to Dakota, who was fully immersed in the TV and what Dovason was saying."
    $l_exp = "smile"
    "Giving a small smile, I turned back to the TV, myself."
    scene bg newsroom
    show krag smile hips at middle
    hide screen laura
    with dissolve
    pause 0.1
    a "Although I suppose the big question on everyone's minds is 'Why now?'."
    a "Why wait 7 years into the REDD War's life to host an event like this for this purpose?"
    kr concerned down "Well..."
    kr "Not to throw anyone under the bus, but this is an event I've wanted to host since the very beginning."
    kr neutral "But the people at the studio would never back it, claiming it to be too controversial, expensive, and a waste of time."
    kr smile "Looking back, I suppose I shouldn't have been too surprised at the backlash I received, ahaha."
    kr concerned hips "But with recently-revealed events, I decided it was time now, more than ever, to host this show to earn people's trust back."
    kr "However, the studio still wouldn't fund the show, so I had no choice but to use my own money and resources to pull this event off."
    a "By 'recently-revealed events', I assume you're referring to the news surrounding your brother Trosh?"
    kr neutral "I am."
    a "That truly is a horrible situation."
    a "For him, you, and your show."
    kr horror down "I very much agree, Chuck."
    kr concerned "I know people are understandably upset that I wasn't as harsh to him as I should have been, but..."
    kr "...he's still my brother, and he was very much in his legal and biological right to do what he did, even though I highly disagree with it."
    kr smile "I guess it's only fitting; he was never a fan of my life decisions, either, but he was still there for me to help me achieve my dream by providing funding for the program."
    kr worried "But REDD War or not, I couldn't imagine just..."
    kr "..."
    "Clearly sensing the darker direction the interview was turning, Chuck cleared his throat and changed the subject."
    a "Well, for this live show being a big and grand event, you really haven't gone into much detail on it."
    a "Even your co-host Madeline Jarvis has gone on record stating you've been very secretive about this."
    kr neutral "Heh. Well, uh..."
    kr "It's no secret that Madeline and I have had our share of differences on how {i}Mr. Sprinkles{/i} should be played out."
    kr @ concerned "In fact, she's even one of the people within the studio who suggested the show be put on hiatus until this whole controversy blows over."
    kr "But I still respect her as both a person and a colleague, despite our differences. I certainly don't wish to turn this into a blame game."
    a "But not even telling her about the live show's events? Doesn't that seem a bit of an issue to you?"
    kr smile hips "Rest assured, there's a method to my madness."
    kr "But back to your initial question about the live show tomorrow and what it entails."
    kr "My goal for tomorrow's show is to pull off feats you would never see on any episode of {i}Mr. Sprinkles{/i}."
    kr laughing "New games and variations of existing ones designed specifically for the event~!"
    a "Any sneak peeks on what some of these games are?"
    kr smile "Ahaha! Welllll...."
    kr "I won't go into {b}great{/b} detail, but I will say this:"
    kr "There won't just be children playing these games; there are plenty of events for the parents to play, as well!"
    a "Oh, really? Well, that sounds fantastic!"
    kr laughing "That's the idea~!"
    $l_exp = "smug"
    scene bg livingroom
    show richard down concerned at middle
    show screen laura
    with dissolve
    pause 0.1
    l "What do you think, honey? Think you can handle some of those games?"
    r laughing crossed "Ha! Yeah, like my fat self can run an obstacle course!"
    show richard:
        ease 0.5 two1
    show dakota smirk crossed at two2_short with dissolve
    pause 0.1
    d "Oh, I would {b}love{/b} to see that!"
    r smile "Over my dead body."
    hide richard
    hide dakota
    with dissolve
    pause 0.1
    $l_exp = "neutral"
    "The two on the news continued to talk about the upcoming show, as well as stating that tickets were still available for purchase."
    "All the while, the countdown in the bottom corner got lower and lower."
    $l_exp = "concerned"
    "It's funny. Every year, we always end up getting ourselves worked up, only for it to lead to nothing."
    $l_exp = "neutral"
    "Still, we can't help but feel bad for the ones who weren't so fortunate."
    "Finally, it was time for the big reveal."
    stop music fadeout(3.0)
    "Chuck thanked Krag for his time and then announced that Lord Reddington would be taking over with a live announcement from the REDD Base."
    "Almost on cue, the screen went dark, but only for a split second."
    "It then cut to the REDD leader, himself, sitting behind a desk, staring at us all with a cold, deadpan expression."
    play music bells_of_weirdness
    re "Greetings, Earth."
    $l_exp = "shocked"
    "His booming voice is certainly something I can go a year without."
    "Dakota got a bit of an uneasy expression on her face, and rightfully so."
    "Richard, though, just stared ahead, completely frozen in concentration."
    re "At exactly this time tomorrow, the 7th annual REDD War will commence."
    re "I will now reveal the locations of the 5 dedicated War Zones."
    re "These zones are the only locations on the planet where REDD War activity will be held, so if you do not live in any of these cities and wish to participate in the War, you will have 24 hours to find your way over there."
    $l_exp = "concerned"
    "I'm going to assume that message was for the REDD in the audience."
    re "Let us begin."
    $l_exp = "surprised"
    "Reddington then leaned in slightly closer to the camera, sending a shiver down my spine."
    "I certainly wouldn't want to be face-to-face with this guy in a dark alley."
    re "The War Zones for the 2030 REDD War are as follows:"
    re "Perth, Australia."
    $l_exp = "concerned"
    "Figures; like America, Australia is always the country of choice for a REDD War."
    re "Saint Petersburg, Russia."
    $l_exp = "neutral"
    "Alright, so far, so good."
    "For us, anyway."
    re "Soweto, South Africa."
    $l_exp = "concerned"
    "Huh. I can't remember the last time I saw any African country on the list."
    "Out of the corner of my eye, I saw Richard leaning closer to the TV, his hands crossed and placed on his mouth."
    "Dakota was curled up on the chair, eyes peeking over her knees."
    re "Montevideo, Uruguay."
    $l_exp = "neutral"
    "Only one War Zone left..."
    "I could feel my breathing getting a little faster."
    "I don't even think I had blinked since his face was on the screen."
    re "And the fifth and final War Zone for the 2030 REDD War is..."
    "..."
    "We were a family of statues."
    ".{w=1}.{w=1}.{w=1}{nw}"
    re "Atlanta, United States."
    stop music
    $renpy.pause(delay=3)
    "I just continued to stare forward at the screen, not moving."
    "He's obviously kidding."
    "He has to be."
    "It's just a prank on Atlanta."
    "Haha, we get it. Very funny, Reddington."
    $l_exp = "sad"
    "..."
    re "These 5 cities are the official War Zones for tomorrow's REDD War."
    re "Very shortly, official members of the REDD Base will be at these locations to place the proper barriers around the Zones."
    re "Everyone living in these zones will have exactly 24 hours to either evacuate the premises or prepare for the War."
    re "To those whose cities were not chosen for the REDD War, I wish to--"
    $l_exp = "shocked"
    "I didn't get to hear the rest of what he said because the next thing I knew, I saw Dakota bolt off her chair and run upstairs, her hands over her mouth, sobs coming out."
    l "Dakota!"
    "I ran after her to her room."
    "She tried to slam the door on me, but I was too quick for that."
    play music vast_places
    scene bg dakotaroom with dissolve
    pause 0.1
    l "Dakota, honey..."
    d "This can't be happening! It {b}CAN'T!!!{/b}"
    "Her face was stuffed into her pillow, her muffled voice still being loud enough for me to hear quite well."
    "I took a deep breath and sat down on the bed, slowly rubbing her back with comfort."
    $l_exp = "sad"
    l "Dakota..."
    $nvl = True
    hide screen laura
    nvl clear
    nvl show dissolve
    narrate """
    I could feel the tears starting to form in my eyes.

    Now that the shock has worn off, the realization of what just happened has finally hit me.

    Atlanta was a War Zone.

    Atlanta.{w} Our town.{w} Our {b}home{/b}.

    It was chosen as one of the cities to host the REDD War.

    That shouldn't be possible.

    That shouldn't be real.

    And yet...
    """
    $nvl = False
    nvl hide
    show screen laura
    with dissolve
    "I heard the door creak open a bit."
    "My other daughter's head poked through the crack."
    show kate concerned fidget at middle with dissolve
    pause 0.1
    k "...Kota? Are you okay?"
    "Dakota's head whipped from out of the pillow and towards her little sister."
    "Her face was very red and wet."
    show kate:
        ease 0.5 two1
    show dakota crying side at two2 with dissolve
    pause 0.1
    d "No, I'm not, Kate!! We're all gonna die!!"
    k shocked "We are??"
    l "Kate, sweetie, what she means is--"
    d "I mean that the REDD are gonna find us and kill us tomorrow!!"
    k crying "!!!"
    $l_exp = "mad"
    l "Dakota! You're scaring her!"
    d "{b}GOOD!!!{/b} She {b}should{/b} be scared!!!"
    "By then, I heard the footsteps in the hallway."
    "A second later, the door completely opened, revealing Richard looking in at his crying little girls."
    show kate zorder 2:
        ease 0.5 left_short
    show dakota zorder 2:
        ease 0.5 right_short
    show richard down concerned at middle zorder 1 with dissolve
    pause 0.1
    r "..."
    k "D-Daddy, are we really gonna die?"
    r "..."
    $l_exp = "neutral"
    "I don't blame Richard for his silence."
    "How exactly is he supposed to answer that?"
    "When it comes to the REDD War, nothing is promised, especially your survival."
    "He finally glanced down and looked her in the eye."
    r glare "Not if I can help it, baby."
    "He then looked at all of us."
    r crossed "Everyone, pack some bags; we're getting out of the city."
    $l_exp = "shocked"
    l "And going where?"
    r @ concerned "I don't know."
    r "But anywhere is safer than here."
    r "If we hurry, we can get out of here before the barriers go up."
    r "And even if we don't, we can still be close to the front of the line."
    r rage "Now come on, girls. Find a bag, get what you need to last you a couple days, and let's move!"
    k concerned "But Daddy, what about the Mr. Sprinkles show tomorrow?"
    r concerned "..."
    show richard:
        ease 0.5 ypos 100
    "Richard sighed and bent down, placing his hand on her shoulder."
    r down "I'm sorry, Kate, but we're not going to the show. It's too dangerous."
    k down "But, Daddy, you promised we'd go!!"
    r "I know, but..."
    $l_exp = "concerned"
    l "Richard, can I talk to you?"
    show richard glare
    "He looked up at me with a bit of a confused look."
    show richard:
        ease 0.5 ypos 0
    "Regardless, he stood back up and looked at our daughters."
    r "Start packing. Please."
    scene bg dakotaroom with dissolve
    pause 0.5
    scene bg livingroom with dissolve
    pause 0.1
    "We then made our way downstairs."
    show richard down glare at middle with dissolve
    pause 0.1
    r "..."
    $l_exp = "neutral"
    l "Look, Richard--"
    r "Please tell me you're not going to suggest we stay here."
    $l_exp = "surprised"
    l "Well..."
    r crossed rage "Oh my God, Laura!"
    l "Richard, hear me out.{w=0.5} Please."
    r glare "..."
    $l_exp = "neutral"
    l "I want us all to be out of harm's way. I do. You gotta understand that."
    r concerned "..."
    $l_exp = "sad"
    l "But do you have any idea how much it costs to exit the barrier? They charge per {b}person{/b}, Richard!"
    r down rage "That's why we need to get out before---"
    play sound helicopter_loop loop
    pause 1.0
    $l_exp = "neutral"
    show richard glare
    "It was too late; we could hear them overhead."
    $l_exp = "mad"
    l "Well, that was wishful thinking..."
    r concerned "..."
    play sound helicopter_finish
    $l_exp = "neutral"
    l "Look, Richard, we just need to think rationally about this."
    l "Last year, they charged close to $500 a person, and the price just keeps going up every year."
    $l_exp = "surprised"
    l "We wouldn't have enough left to pay the bills."
    r glare "We have REDD insurance; we could use the money we get from it."
    $l_exp = "concerned"
    l "But what if they don't touch our house? We wouldn't get a cent from insurance. Then what?"
    r concerned "..."
    $l_exp = "sad"
    l "Besides, do you know how heartbroken Kate would be if she missed this show?"
    r rage "Well, when she's older, she'll understand why her meanie-head father didn't take her to see Mr. Sprinkles!"
    r glare crossed "I'm sorry, Laura, but that's the end of this discussion. I'm getting the hell out of Atlanta as soon as I can, and I'm taking my kids with me."
    r "If you wanna be stupid enough to stay and get yourself killed, then go right ahead!"
    $l_exp = "wut"
    l "..."
    r "..."
    r concerned "..."
    show richard down
    "He sighed and placed his face in his hands."
    r "I'm sorry. I just..."
    r "It's like I told you. I want them to be safe."
    r "If I can't do what's best for them, what kind of father does that make me?"
    $l_exp = "surprised"
    l "..."
    hide richard with dissolve
    pause 0.1
    $l_exp = "crying"
    "I quickly made my way over to him and hugged him tightly, tears flowing from my eyes."
    "He hugged me back. I couldn't see his face, but I could tell by the shaky breathing that he was crying, as well."
    l "Richard, you are a {b}great{/b} father! And an {b}amazing{/b} husband!"
    l "I can't be mad at you for wanting your family to be safe!"
    "He took another deep breath."
    $l_exp = "sad"
    l "But if we leave and survive the War, only to come back with no money, then how on Earth are we gonna survive after that?"
    l "We need to look at the bigger picture, Richard."
    r "..."
    l "At the very least, let's sleep on it, okay?"
    l "We can get up early tomorrow and still have 12 hours to try and get out."
    r "..."
    "He then broke from the hug."
    show richard crossed concerned at middle with dissolve
    pause 0.1
    r "...I don't know, Laura."
    r "I get what you're saying, but..."
    r "...I just don't want to risk fighting with those monsters."
    r "To risk getting our girls or ourselves killed."
    r "We can find a way to get by after the War, where law and order are present."
    r "But during the REDD War..."
    $l_exp = "neutral"
    r "..."
    $renpy.music.set_volume(0.5, delay=1, channel='music')
    menu:
        l "Richard..."
        "\"...you're right. We should leave.\"":
            $renpy.music.set_volume(1.0, delay=1, channel='music')
            $l_exp = "sad"
            l "...you're right. We should leave."
            r down smile "I knew you'd make the right choice, honey."
            r laughing "Now come on. Let's get packing!"
            $l_exp = "smile"
            "Richard and I then went upstairs to pack."
            "It may be a challenge, but we're gonna get out of Atlanta."
            "Let's just hope it won't be {b}too{/b} chaotic out there."
            stop music fadeout(5.0)
            hide screen laura
            window hide dissolve
            pause 0.5
            scene bg livingroom with dissolve
            pause 1
            scene bg livingroom_blur
            with Dissolve(3.0)
            $badcredits = True
            if not persistent.achievements["toosafe"]:
                $persistent.achievements["toosafe"] = True
                $renpy.notify("Achievement Unlocked: {i}Playing it TOO Safe{/i}")
                $persistent.achievelist.append(1)
            jump gameover
        "\"...we should really sleep on it.\"":
            $renpy.music.set_volume(1.0, delay=1, channel='music')
label sleeponit:
    $l_exp = "surprised"
    l "...we should really sleep on it."
    r glare "..."
    l "If nothing else, do you know how chaotic it's going to be out there right now?"
    $l_exp = "sad"
    l "We could get ourselves killed just trying to get out."
    l "Trampling, getting hit by cars... It's happened before. Happens every year."
    r concerned "..."
    l "At least tomorrow morning, the chaos might have died down a bit."
    r "..."
    $l_exp = "smug"
    l "And who knows? Maybe you'll change your mind about leaving."
    r glare "..."
    "He finally sighed and grabbed my hand."
    r down "Fine. I'll sleep on it."
    r concerned "...at least, I'll try to."
    $l_exp = "smile"
    "I gave a small, nervous laugh."
    l "I don't think anyone in Atlanta is going to get sleep tonight."
    show richard smile
    "He gave his own nervous laugh before kissing my hand."
    r "I love you, Laura."
    $l_exp = "smile"
    l "And I love you, too, Richard."
    hide richard
    hide screen laura
    with dissolve
    pause 0.1
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    We then had one long kiss before making our way back upstairs to explain the plan to the girls.

    Kate didn't seem to fully understand it, still believing we were one second away from death.

    Dakota argued against the idea, saying we needed to get the hell out of Atlanta ASAP.

    Well, those weren't her exact words, but they may as well have been.

    I guess neither girl is at the age to understand the world the way we do, which I guess can be both a blessing and a curse.
    
    {clear}

    At any rate, we told them we still needed to get bags packed just in case.

    After helping Kate with her bag, as well as trying to get her to understand that she needs to pack more than a box of animal crackers, I checked up on Dakota.

    Unlike her sister, she did a better job of getting the necessities.

    Clothes, toothbrush, shampoo, phone charger, soda, cookies...

    ...hey, I said she did a better job, not a perfect one.

    {nw}

    After making sure both daughters had their bags all right, we sent them to bed.

    We repeated to Kate several times that everything was going to be okay.

    Obviously, we have no clue how true that statement is, but this is certainly the situation where we need to say positive.

    However, Dakota wasn't exactly buying what we were selling.
    """
    $nvl = False
    $l_exp = "neutral"
    nvl hide
    scene bg dakotaroom
    show dakota mad side at two2_short
    show richard down concerned at two1
    show screen laura
    with dissolve
    pause 0.1
    d "So we really might stay here {b}on purpose{/b}?!"
    $l_exp = "sad"
    l "I know it's tough, baby, but sometimes things can't always go the way we want them to."
    d crossed "But we're really gonna stay here and {b}DIE{/b}?!"
    r crossed "We don't know if we're staying or not, Dakota. We'll talk more about it in the morning."
    d "And what's gonna happen if we {b}do{/b} stay?"
    $l_exp = "neutral"
    l "That'll be one of the things we talk about."
    d "..."
    l "It's like I told you, Dakota. We'd never put you girls at risk."
    $l_exp = "smile"
    l "So no matter what ends up happening, we'll make sure you're safe."
    r smile "Your mother is right. You just have to trust us."
    d "..."
    "I bent down and gave her a quick kiss on the head."
    $l_exp = "excited"
    l "Please try and get some sleep, okay?"
    d "...okay..."
    r concerned "..."
    scene bg dakotaroom
    hide screen laura
    with dissolve
    pause 0.1
    nvl clear
    $nvl = True
    nvl show dissolve
    narrate """
    With that, Richard and I got our own bags packed.

    We didn't really say anything to each other while we did.

    I don't know what was going through his mind, but I certainly couldn't stop thinking about what's to come.

    Will we stay here? Will we try to get out of Atlanta? Would we even be able to get out in time?

    So many questions, no way to know the answers ahead of time...
    
    {clear}

    When we finally had our bags packed, we went to bed.

    I'd say 'went to sleep', but that just wasn't really possible, given our situation.

    How many people before us went through this exact situation?

    Going to bed, trying to sleep, knowing full well this might be the last time they'd get to?

    It's something I had always pondered every year, but now that I'm the one in that position...
    """
    $nvl = False
    nvl hide
    with dissolve
    pause 0.5
    scene bg fade
    with Dissolve(2.0)
    pause 0.1
    "Well, no matter what happens, tomorrow will be an eventful day."
    "I better get myself mentally prepared for it."
    call sceneend
    if not persistent.scenes["ch1_s2"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch1_s2"] = True
    jump chapter_2
