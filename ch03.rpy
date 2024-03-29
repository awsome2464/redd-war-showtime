label chapter_3:
    python:
        save_name = "Chapter 3"
        save_subtitle = "The Storm Arrives"
    call chaptername from _call_chaptername_1
label firstgame:
    python:
        currenttime = "7:14 PM"
        timeleft = "11 hours and 46 minutes"
        event = "REDD War ends"
        l_exp = "excited"
        cane_blood = False
    stop music
    call chapterstart from _call_chapterstart_5
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

    There were several hundred of us total, yet they didn't hesitate to cram us all in the same room.

    Though despite all this, I'm grateful for one thing:
    """
    $nvl = False
    window show
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    show richard down concerned at middle with dissolve
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
    show sprinkles laugh hat leftdown at middle_sprinkles with dissolve
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
    show sprinkles hm rightdown
    "Mr. Sprinkles then raised his hand towards the guard."
    s "Easy there."
    s evilgrin "We wanna make sure we have enough volunteers to last us the whole night."
    $l_exp = "mad"
    "{i}\'Volunteers\'{/i} isn't the word I'd use."
    s happy "It's safe to assume you all have a basic understanding of how my show works, so I'll spare you the rundown."
    s "Instead, I'll cut right to the point:"
    s jeer "Whether or not you live to see your children again is entirely up to you."
    $l_exp = "sad"
    s laugh hat "If you cooperate and be a good sport, you'll be given the chance to participate in one of the many games we have planned tonight!"
    s happy "Although compared to the games from the television show, these games are a lot less..."
    s evilgrin "...safe."
    s laugh "But they're not impossible, I assure you~"
    s rightdown "You just have to play the games to the best of your abilities."
    s "If you win, you keep your life!"
    s "If you lose..."
    s jeer hat "Well, I'm sure you can finish that sentence."
    s happy "But don't forget that this is still a show~!"
    s "A show that the entire world is watching!"
    s jeer "Not to put you under any unneeded stress, of course...~"
    s happy "So just remember to have fun!"
    s laugh "Ooo, this is just going to be a fantastic night, I can tell~!"
    s @ jeer "Anyway, just sit back and behave yourselves; we'll get you when we're ready for you."
    s "In the meantime, you can watch the show from the screen we have set up here!"
    "As he said that, he gestured towards a flat-screen TV along the back wall, which was currently displaying a \'We\'ll Be Right Back!\' message."
    s happy rightdown "Well, that's it for now!"
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
    s hat "Because you were stupid enough to trust a REDD."
    stop music fadeout(3)
    hide sprinkles
    with Dissolve(2)
    $l_exp = "neutral"
    "He then exited the room and closed the door behind him."
    "The guards looking over us then got back in position, with one in front of the door and the other 4 in one of the room's corners."
    "They certainly didn't stop keeping their hands on their guns."
    $l_exp = "surprised"
    "These didn't look like your average guns, though; they looked more 'futuristic', for a lack of a better term."
    "It was unlike anything I had ever seen."
    $l_exp = "sad"
    "Though they still kill people just as well as a human gun, as we've seen."
    "..."
    "The room was uncomfortably silent."
    "Everyone just looked at each other with terror in their faces."
    "What else could we do?"
    "You know, that wouldn't end with getting killed?"
    $l_exp = "concerned"
    "Suddenly, the TV changed to a live feed of the stage."
    play music sprinkles_theme
    hide screen laura
    scene bg stage
    show sprinkles laugh cane hat at middle_sprinkles
    with dissolve
    pause 0.1
    s "Thank you for your patience, everyone!"
    s happy rightdown "To start this show properly, I would like to bring out a special guest who will be joining us throughout the evening!"
    s "Please give a big round of applause to our guest..."
    s laugh "...Jessica Tate!"
    hide sprinkles with dissolve
    pause 0.5
    show jessica chair base:
        zoom 0.6
        xalign 1.75
        ease 1.5 middle_jessica
    pause 2
    $l_exp = "sad"
    show screen laura
    pause 0.6
    "Oh, my God!"
    "She looked just as terrified as the rest of us, but given her current situation, I'm sure she's even more so."
    hide screen laura
    pause 0.1
    show jessica left zorder 2:
        ease 0.5 two2_jessica
    show sprinkles happy rightdown leftdown at two1 zorder 1 with dissolve
    pause 0.1
    s "I must say it's nice to finally meet you, Mrs. Tate!"
    s jeer "I do wish it was under different circumstances."
    s laugh hat "But better late than never, I always say~!"
    "He then wrapped his arm around her shoulder and leaned in towards her as he grinned at the camera."
    s happy rightdown "Now, there's a chance that some of you might not have heard of Jessica Tate, so allow me to explain:"
    s "You see, Jessica here..."
    s hm "...doesn't like me very much."
    s laugh "But that's okay! It really is!"
    s happy hat "After all, everyone feels different ways about different people, and there's nothing you can do to change that."
    s "So, tonight, I brought Jessica onto the show to teach her, as well as all of you, an important lesson:"
    s "While it's okay to dislike someone for a reason only you can understand..."
    s hm "...it's never okay to use that disliking to harm that person. If you do..."
    s evilgrin "...you might just have some very bad things happen to you in return."
    stop music fadeout(5)
    s laugh "Here, Jessica. Why don't we show the folks at home what I mean?"
    show jessica base
    "Jessica then started giving some screams through her gag, and her eyes started darting side to side, almost as if she were trying to shake her head."
    s happy rightdown "Don't worry. I won't be too harsh."
    s evilgrin "...yet."
    show jingle bat open_smile at left zorder 3
    show sprinkles at middle_sprinkles
    show jessica at right_jessica
    with easeinleft
    pause 0.1
    "On cue, Jingle skipped onto the stage and handed Mr. Sprinkles an aluminum baseball bat."
    show jingle down
    "After he accepted the gift, she gave a small curtsy and skipped back off."
    hide jingle
    show sprinkles at two1
    show jessica at two2_jessica
    with easeoutleft
    pause 0.1
    $l_exp = "concerned"
    show screen laura
    pause 0.6
    "...so, Jingle and presumably Jangle are in on this?"
    $l_exp = "neutral"
    "I mean, they're REDD, as well, so I guess I shouldn't be too surprised, given the circumstances..."
    hide screen laura
    pause 0.6
    s hm "Now, Jessica, despite everything that's happened tonight, I'm not going to lie to you."
    s "What's about to happen right now..."
    s evilgrin "...is gonna hurt a lot."
    "He then wound up the bat..."
    play sound smack
    show jessica screaming:
        linear 0.1 ypos -10
        linear 0.1 ypos 0
    show sprinkles:
        linear 0.1 xalign 0.27
        linear 0.1 xalign 0.25
    "And smacked Jessica right in the face with it!"
    play sound2 "audio/voice/jessica_bat.ogg"
    show jessica screaming:
        linear 0.1 ypos -10
        linear 0.1 ypos 0
        pause 0.25
        repeat
    show sprinkles:
        linear 0.1 xalign 0.27
        linear 0.1 xalign 0.25
        pause 0.25
        repeat
    "He then repeatedly hit her, seeming to get louder and faster with each one!"
    "She cried out in pain, but her gag muffled the noise."
    "He continued to hit her, his sinister grin never left his face while he did."
    play sound children_screaming fadein(5)
    "The screaming children certainly didn't help lighten the atmosphere."
    $l_exp = "surprised"
    show screen laura
    pause 0.6
    "Wait a minute... the children!"
    "They're still in the audience!"
    "My God... how scared out of their minds do they have to be right now?"
    "All their parents gone, some of them are 'gone' gone..."
    "...and now they have to watch this?"
    $l_exp = "sad"
    "...Dakota! Kate!"
    "What are they going through right now?"
    "What are they thinking right now?"
    "Oh, my poor girls..."
    stop sound2 fadeout(1.0)
    hide screen laura
    pause 0.6
    show sprinkles hat laugh:
        ease 0.5 xalign 0.25
    show jessica:
        ease 0.5 ypos 0
    "After a few more swings, Mr. Sprinkles dropped the bat and cackled like a madman."
    show jessica tears
    "Jessica, on the other hand, had blood all over the bottom of her face and tears pouring out of her eyes."
    play music sprinkles_theme
    s "Don't you worry, dear audience!"
    s @ jeer "I've got more than a baseball bat in store for this fine lady~"
    s "In the meantime, what do you say we get started with our first game?"
    s happy "Bring out the Wacky Dartboard!"
    $l_exp = "neutral"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg storage
    show screen laura
    with dissolve
    pause 0.1
    "Jessica was then rolled off the stage as the dartboard was brought on."
    $l_exp = "sad"
    play sound door_open
    "A few seconds later, the door opened up, revealing yet another REDD."
    show trosh gun angry at middle with dissolve
    pause 0.1
    t "Alright! You and you are coming with me!"
    "He then pointed to a man and woman near the front of the pile."
    man "Wha-"
    t "{b}Now!{/b}"
    woman "B-But he hasn't even picked the game yet!"
    t laugh "Ahahaha!!"
    t "You really think the games are selected at random?"
    t concerned "Grow up."
    t angry "Now {b}move!!{/b}"
    "Given no other option, the two exited the room with the REDD keeping his weapon pointed at them at all times."
    hide trosh with dissolve
    pause 0.1
    "After the door was closed, the guard REDD got back into position."
    hide screen laura
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    As I leaned against the wall and tried to calm myself down, I couldn't help but think about the best-case scenario.

    Richard and I are pretty far back in the room, so the odds of us getting picked seem significantly lower by default.

    I mean, I know we're talking about 12 hours, but even on TV, some games last a lot longer than others.

    And even if we get picked for the game, there's a chance we could still win and survive.

    I mean, really, how lethal could these games actually be?

    And assuming he's telling the truth, we'll stay alive after we win, and that's that.

    {clear}

    I know it probably won't be that simple.

    But if I want to have any chance at making through this night, I need to have positivity, even when none seems to exist.

    I mean, surely that's the way to go, right...?
    """
    $nvl = False
    $l_exp = "concerned"
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    "Mr. Sprinkles then approached the Wacky Dartboard after hitting one of the squares."
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg stage
    show sprinkles happy cane hat at middle_sprinkles
    with dissolve
    pause 0.1
    s "And our first game of the evening is..."
    s laugh "{i}Hot Quiz!{/i}"
    show game_name "Hot Quiz" at game_name_flash
    s "Ahahaha!"
    s happy rightdown "Now, what do you say we get the ball rolling right away and bring out our contestants?"
    hide game_name
    "The two adults taken from the back were then brought onto the stage by guards while Jingle and Jangle placed two large chairs in the center."
    s jeer "If you could please sit in these chairs..."
    $l_exp = "sad"
    "Realizing they didn't have much of a choice, the parents sat down."
    $l_exp = "concerned"
    "The chairs were facing each other, sitting about 10 feet apart."
    $l_exp = "surprised"
    "They also had straps across the waist, which Jingle and Jangle then proceeded to attach and lock."
    hide screen laura
    pause 0.6
    s happy "Splendid~!"
    s "Alright, for those who are unaware of how this game works, here are the rules:"
    s "Our contestants here will have 60 seconds to answer simple trivia questions."
    s @ laugh "The catch is that they have to take turns, the person currently answering the question being 'it'!"
    s "If the one who's 'it' answers the question correctly, then their opponent becomes 'it'."
    s laugh "Whoever is 'it' when the timer counts down loses!"
    s evilgrin "And believe me, folks, you do not want to lose this game."
    s happy "Everyone understand the rules?"
    $l_exp = "sad"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    show screen laura
    scene bg storage
    with dissolve
    pause 0.1
    "The contestants looked at each other with horror."
    "There was no way they could both win."
    "One of them was going to die."
    $l_exp = "concerned"
    "I mean, in hindsight, I guess it's not really possible for a game to have everyone win, but..."
    $l_exp = "sad"
    "This isn't going to be like your typical game on {i}The Mr. Sprinkles Show{/i}, and they both knew it."
    "Normally, the loser of Hot Quiz would get a bucket of water dumped on their head."
    "But here, if we're to go by what he said..."
    $l_exp = "surprised"
    "...who knows what will happen, instead?"
    man "Y-Yes, I understand."
    woman "I do, too..."
    s "Alrighty, then~!"
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg stage
    hide screen laura
    show sprinkles laugh leftdown hat at middle_sprinkles
    with dissolve
    pause 0.1
    s "Let's start the game!"
    s jeer "Good luck, you two~"
    stop music fadeout(3)
    "He then stood between the two chairs, albeit a bit of a distance back from them."
    "We were then greeted to two camera angles at once, one for each contestant."
    s laugh rightdown "Alright! Let's decide who will be 'it' first!"
    "Suddenly a red light bulb on top of each of the chairs alternated rapidly for a few seconds before slowing down."
    "Finally, it stopped right on top of the man."
    s happy "Oh, goody! You get to answer the question first, Sir!"
    s "Put 60 seconds on the clock, please!"
    s laugh hat "And let's begin~!"
    play music ice_cream_truck
    s happy rightdown "Who was the 16th president of the United States?"
    man "L-Lincoln! Abraham Lincoln!"
    s laugh "Correct!"
    "The light then switched from the man to the woman."
    "Mr. Sprinkles then faced her."
    s happy "What year did comedian Robin Williams pass away?"
    woman "Uh...!"
    "She closed her eyes tightly and tapped her feet quickly, trying to think."
    woman "2013?"
    play sound buzzer_short
    "A buzzer went off."
    s jeer "Try again~"
    woman "2014?"
    s laugh hat "Correct!"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg storage
    show screen laura
    with dissolve
    pause 0.1
    "They kept receiving and answering questions, moving as quickly as they could."
    "I'll give them credit for actually managing to think clearly under the circumstances."
    $l_exp = "concerned"
    "Of course, when your life is on the line, maybe your brain works differently."
    $l_exp = "surprised"
    "All the while, the timer in the corner was going down."
    "I know I probably shouldn't be watching this, especially knowing the outcome, but..."
    "...I can't help it. This is actually getting me engaged a bit."
    $l_exp = "sad"
    "I certainly hope that doesn't make me a bad person."
    "I looked over at Richard to see how he was taking it."
    show richard crossed concerned at middle with dissolve
    pause 0.1
    $l_exp = "surprised"
    "He looked just as engaged as I was."
    "And also just as horrified."
    "I mean, by this point, we'd seen enough REDD War footage to sort of be a bit immune to it, but this is an entirely new context."
    $l_exp = "sad"
    "Finally, we were at the final 10 seconds, with the woman being 'it'."
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg stage
    hide screen laura
    show sprinkles leftdown rightdown jeer at middle_sprinkles
    with dissolve
    pause 0.1
    s "What is the capital of Florida?"
    woman "Oh, God...!!"
    woman "O-Orlando?"
    play sound buzzer_short
    s "Nope. Guess again."
    woman "Uh..!!"
    s evilgrin "5 seconds!"
    "The man in the opposite chair held his breath."
    woman "...!"
    woman "OH! TALLAHASSEE!!!"
    s laugh "Correct!"
    "The amount of dread that came across the man's face as Mr. Sprinkles turned to him was unexplainable."
    s happy "How many people--"
    stop music
    window hide
    play sound buzzer_full
    pause 1
    window show dissolve
    s laugh hat "Oh, my! A minute certainly does fly by, doesn't it?"
    s happy "Congratulations, Miss! You won!"
    s jeer "As for you, Sir..."
    s evilgrin "Thank you for playing."
    play sound shotgun
    show blood zorder 3
    call gunflash from _call_gunflash_2
    play sound2 children_screaming fadein(1)
    pause 1
    $l_exp = "shocked"
    show screen laura
    pause 0.6
    "Everyone screamed as the man's head seemed to explode out of nowhere!"
    "The camera then panned to a REDD guard pointing a shotgun in the general direction."
    "Meanwhile, the blood-and-gut covered woman covered her mouth in horror as she started bawling."
    $l_exp = "sad"
    "I know she has to be believing that this is her fault."
    "I can't even imagine the amount of guilt going through her head."
    play music sprinkles_theme
    s laugh "Now that's what I call an exciting beginning to an exciting evening~!"
    s happy rightdown "Ma'am, for winning, you earn your freedom!"
    "Jangle then entered the stage and unhooked her from the chair."
    s jeer "You are free to exit the stage and return to where you were seated at the beginning of the night."
    $l_exp = "concerned"
    "The woman was hesitant and looked around to see if there were any indications that this was a trap."
    s laugh hat "I'm serious~! You can return to your seat!"
    $l_exp = "neutral"
    "She then slowly but surely got out of her seat and made her way to the edge of the stage and dropped down."
    hide sprinkles
    show bg livestage_open
    with dissolve
    pause 0.1
    "Once on the ground, she picked up the pace and ran towards the back of the room."
    $l_exp = "sad"
    "The guards by the doors raised their weapons, but they hesitated when a loud 'Mommy!!' could be heard nearby."
    $l_exp = "surprised"
    "Sure enough, the woman ran towards the child and hugged him tightly, sobbing loudly as she did."
    show bg stage
    show sprinkles rightdown leftdown jeer at middle_sprinkles
    with dissolve
    pause 0.1
    s "Aw, how adorable!"
    s laugh hat "Anyway, what do you say we take ourselves a quick break to prepare for the next game?"
    stop music fadeout(5)
    scene bg storage
    show richard down concerned at middle
    with dissolve
    pause 0.1
    "I leaned in towards Richard and whispered:"
    $l_exp = "smile"
    l "Well, at least he's being true to what he said, right?"
    r glare "..."
    $l_exp = "neutral"
    l "..."
    "Obviously, he's not as optimistic as I am."
    "I guess I can't fault him for that."
    $l_exp = "surprised"
    "That's when I saw something at the bottom of my peripheral vision."
    "My phone was lighting up in my pocket."
    "I took a quick look at all the guards. None of them were looking in our general direction."
    show richard concerned
    "I took out my phone and looked at the screen."
    $l_exp = "sad"
    "It was a text from Dakota!"
    play music vast_places
    dt "Mom r u ok"
    $l_exp = "smile"
    "The fact that I have some sort of contact with my daughter is very relieving."
    "Trying to hold the tears in, I replied while looking around to make sure I was still in the clear."
    lt "I'm okay honey. How are you and Kate?"
    $l_exp = "sad"
    "Those poor girls..."
    "I wonder if they actually witnessed what happened to that man or if they managed to look away..."
    $l_exp = "surprised"
    "She responded."
    dt "Were scared and Kate keeps asking when shes gonna see u guys again"
    $l_exp = "sad"
    "That was a punch in the gut if there ever was one."
    "I looked over at Richard and showed him the messages."
    "He just closed his eyes and sighed."
    "After a few seconds, he opened them up, although they were noticeably watery."
    "I finally replied to the message."
    lt "We'll do what we can to see you girls again. We promise"
    lt "We both love you"
    dt "We both love you to"
    $l_exp = "excited"
    "You know, I don't think there would ever be a time where seeing that message wouldn't make me happy."
    show richard smile
    "Even Richard's mood seemed to boost a bit."
    "Don't worry, girls."
    "We'll get through this for you."
    $l_exp = "surprised"
    "All I ask is for you to be safe..."
    call sceneend from _call_sceneend_5
    if not persistent.scenes["ch3_s1"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s1"] = True


label gottago:
    python:
        currenttime = "7:43 PM"
        timeleft = "11 hours and 17 minutes"
    call chapterstart from _call_chapterstart_6
    pause 2
    play music classy_ghouls
    scene bg livestage_open
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
    show dakota neutral crossed at two1 zorder 2
    show kate concerned fidget at two2 zorder 1
    with dissolve
    pause 0.1
    d "She said they'll try and get back here."
    k "When?"
    d confused "How should I know?"
    k mad "I want them to come back {b}now{/b}!"
    d mad side "So do I, Kate, but that's not gonna happen!"
    k alert down "I wanna talk to Mommy and make her."
    d neutral hips "You can try, but good luck."
    "Dakota then handed the phone over to Kate."
    "But just when she tried to use it..."
    show dakota sad
    show kate confused
    "...the phone shut off."
    d "Oh, great! The battery must have died!"
    k shocked "We can't talk to Mommy or Daddy?"
    d "Nope."
    k mad "But I wanted to talk to them!"
    d mad crossed "Well, I'm sorry, Kate! There's nothing I can do about it!"
    play music sprinkles_theme
    show dakota sad
    show kate shocked
    s "Okay, my good friends!"
    s "It's time to once again spin the Wacky Dartboard for another fun game~!"
    show kate:
        ease 0.5 xalign 0.4
    "Kate then grabbed onto Dakota in fear."
    k crying "K-Kota, I'm scared! I don't want him to play another game!"
    d side "Me neither!"
    "Dakota figured Kate might just assume that all the bad stuff that's happening is fake, although still terrifying."
    "Unfortunately, Dakota knew the truth."
    "This wasn't an act."
    "This wasn't pretend."
    "This was real."
    k concerned fidget "Why would Mr. Sprinkles do this? He's supposed to be nice!"
    d crossed "I don't know, Kate! I wish I did, but I don't!"
    "Dakota then hugged her sister tightly, wondering what to do."
    "She didn't want to watch the show."
    "Kate didn't want to watch the show."
    "But the people with the guns weren't going to let them walk out of here."
    "...right?"
    k "Kota...?"
    d confused "Yes?"
    k "I have to go potty."
    d neutral "..."
    "Well, it wouldn't hurt to try."
    "Dakota looked and saw a guard walking by."
    show dakota zorder 2:
        ease 0.5 middle
    hide kate with dissolve
    pause 0.1
    d small_smile side "E-Excuse me?"
    "The guard stopped and looked at her with a look of absolute evil."
    $t_name = "Guard"
    t "What?" # Not actually Trosh, but makes more sense than making a new character object.
    d sad "Uh..."
    d "M-My sister has to g-go to the bathroom."
    "The guard then gasped and raised his eyebrows."
    t "Really? Oh! Well, in that case..."
    "His glare returned."
    t "Too bad."
    t "She'll have to hold it."
    d mad hips "You expect her to hold it for 12 hours?"
    t "There are scheduled times for restroom breaks, the first being at 9 o'clock."
    d "She can't wait that long!"
    t "She can, and she will!"
    "The guard then walked away."
    show dakota neutral
    "Dakota then slumped down in her chair in defeat."
    "Movies make things like that seem so easy."
    show dakota zorder 2:
        ease 0.5 two1
    show kate concerned fidget at two2 zorder 1 with dissolve
    pause 0.1
    d "Well, I tried."
    k "But I have to go!"
    d sad crossed "I'm sorry, Kate. I don't know what to tell you besides just wait."
    k "..."
    d "..."
    "With that, the girls accepted their defeat and tried to wait patiently for 9 o'clock."
    "However long it is until then."
    call sceneend from _call_sceneend_6
    if not persistent.scenes["ch3_s2"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s2"] = True


label secondbeating:
    python:
        currenttime = "8:27 PM"
        timeleft = "10 hours and 33 minutes"
        l_exp = "concerned"
    call chapterstart from _call_chapterstart_7
    pause 2
    play music sprinkles_theme
    scene bg stage
    show sprinkles laugh hat cane at middle_sprinkles
    with Dissolve(2.0)
    window show dissolve
    pause 0.1
    s "Ahahaha! Great work, Sir!"
    s happy "You may return to your seat."
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg storage
    show screen laura
    with dissolve
    pause 0.1
    "On one hand, eating a pie without your hands to get a key inside isn't that dangerous."
    $l_exp = "surprised"
    "On the other hand, using said key to unlock yourself from a chair set to detonate is a bit more so."
    $l_exp = "excited"
    "Thankfully, the guy managed to stomach his way through it."
    $l_exp = "smug"
    "Pun fully intended."
    $l_exp = "surprised"
    "Still, not everyone before him was so fortunate."
    "In the hour we've been doing this so far, we've had around 15 or so casualties. I haven't really been keeping track."
    "Innocent parents who died with so many people, including their children, watching."
    $l_exp = "sad"
    "And there's nothing anyone can do to stop this...?"
    "REDD War or not, there has to be someone willing to try and end this, right?"
    s "Alright, then~!"
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg stage
    show sprinkles rightdown cane happy at middle_sprinkles
    hide screen laura
    with dissolve
    pause 0.1
    s "I think we could use a quick break from games for the moment."
    s jeer "After all, we need to make sure our fun lasts all night~"
    s laugh "So, instead, I think we could all do with some jokes!"
    s "Everyone loves a good joke, right~?"
    s hm "Hmm... but I can't tell these jokes by myself."
    s happy "Oh, I know who can help!"
    play sound snap
    "He then snapped his fingers."
    "On cue, Jangle pushed out something covered up with a curtain and stopped it right next to Mr. Sprinkles."
    stop music fadeout(3)
    s laugh hat "Ladies and gentlemen, boys and girls, please welcome back to the stage..."
    show sprinkles:
        ease 0.5 two2_sprinkles
    "He then yanked off the curtain."
    show madeline dead at two1
    with Dissolve(0.25)
    s "...Ms. Madeline~!"
    $l_exp = "shocked"
    play sound children_screaming
    pause 0.5
    show screen laura
    pause 0.6
    "Jesus Christ!"
    "That's a whole new level of fucked up!"
    hide screen laura
    pause 0.6
    s "Ahahaha~!"
    "He then stepped closer to the body."
    stop sound fadeout(3)
    play music sprinkles_spooky
    s happy rightdown "Say, Ms. Madeline, how many tickles does it take to make an octopus laugh?"
    show sprinkles hat
    "He then cupped his hand around his ear and leaned in close to her, pausing for a few seconds."
    s jeer "I'm afraid you'll have to speak up a bit, Ms. Madeline; I can't hear you."
    "This time, when cupping his ear, he spoke in a mocking high-pitched voice."
    s happy "{i}I don't know, Mr. Sprinkles; how many tickles {b}does{/b} it take to make an octopus laugh?{/i}"
    s laugh "It takes..."
    s "...{b}ten tickles!!{/b}"
    "He then laughed and applauded at his joke."
    s happy rightdown "Ooo! Here's another one!"
    s "Where's the best place to learn about making ice cream?"
    s @ jeer "{i}I don't know, Mr. Sprinkles. I'm too stupid to figure that out!{/i}"
    s "The best place to learn how about making ice cream is..."
    s laugh hat "{b}...{i}sundae{/i} school!!{/b}"
    $l_exp = "concerned"
    show screen laura
    pause 0.6
    "He continued to laugh and tell jokes to the corpse while the children in the audience continued to cry."
    $l_exp = "surprised"
    "I wonder how many of those children actually loved Ms. Madeline and considered her their favorite?"
    "There had to have been at least one..."
    $l_exp = "sad"
    "And then to see her not only dead, but being treated like this..."
    "Has he really been this crazy all these years?"
    "Has he just been really good at hiding it?"
    $l_exp = "surprised"
    "If that's the case, then I guess I'm an idiot for thinking we could trust him."
    s jeer rightdown "Alright, I suppose that's enough for now."
    s evilgrin "I don't wanna be like you and work myself {b}to death!{/b}"
    s laugh "You can wait backstage until we need you again, Ms. Madeline~!"
    show madeline:
        ease 1.5 xalign -0.6
    show sprinkles:
        ease 0.5 middle_sprinkles
    "Madeline was then rolled off the stage while Mr. Sprinkles cleared his throat."
    hide madeline
    s happy "Although I do believe that now it's time to bring back out our special guest of the evening!"
    s "Please welcome Mrs. Jessica Tate back to the stage!"
    show sprinkles at two1 zorder 2 with easeinright
    pause 0.5
    show jessica chair left_tears zorder 1:
        zoom 0.6
        xalign 1.75
        ease 1.5 two2_jessica
    pause 2
    s jeer leftdown "So, Jessica, how are you enjoying the show so far?"
    "She responded with more cries through her gag."
    s laugh hat "Ahaha! Well, at least you're speaking louder than Ms. Madeline was~!"
    play sound snap
    "He then snapped his fingers, cuing Jingle to skip onto the stage, only this time, instead of holding a bat, she was holding a sledgehammer."
    $l_exp = "sad"
    "This is not gonna be a pretty sight..."
    s jeer rightdown "Thank you, Jingle."
    show jessica tears
    "Jessica went into full panic mode, squirming around in her chair, trying to break free."
    show sprinkles laugh
    "But Sprinkles just chuckled and seemingly ignored her efforts."
    s "Oh, don't be so blue, Jessica!"
    s evilgrin "It'll only make this harder on you than it needs to be."
    "He then lifted the sledgehammer into a swinging position."
    s jeer "You know, Jessica, I realized that you're going to be in that chair all night."
    s "So, really, there's no need for your legs tonight, correct?"
    $l_exp = "surprised"
    show jessica:
        linear 0.1 xalign 0.805
        block:
            linear 0.2 xalign 0.795
            linear 0.2 xalign 0.805
            repeat
    "Sensing where this was going, Jessica squirmed around even more, but to no avail."
    s evilgrin "Then allow me to get this burden out of your way!"
    "He wound up the hammer."
    $l_exp = "sad"
    "I looked away in fear."
    $quickhide = True
    show black zorder 5
    hide screen laura
    stop music
    play sound hammer
    pause 0.1
    play sound2 "audio/voice/jessica_sledgehammer.ogg"
    $quickhide = False
    pause 1.5
    show screen laura
    pause 0.6
    "Jessica's scream through the gag rang through my ears."
    "I then got the courage to open my eyes and look at the screen."
    $quickhide = True
    hide screen laura
    window hide
    show jessica screaming oneknee at two2_jessica
    show sprinkles laugh rightdown leftdown
    hide black with dissolve
    pause 1
    $quickhide = False
    show screen laura
    window show dissolve
    "Her jeans were covering her legs, but a dark red puddle was forming on her right knee."
    "Jessica herself was still screaming, eyes tightly closed, tears flowing down, and her hands clenched in tight fists."
    s wut "Hmm. You don't seem very grateful."
    s jeer hat "I suppose I'll leave you to consider if you want the other one taken care of the next time we meet."
    s laugh "Alright! Let us take one more short break before we continue on with our night!"
    scene bg storage
    show richard down concerned at middle
    with dissolve
    pause 0.1
    "I looked over at Richard, who was looking away from the screen, sitting against the wall."
    r "God... I can't even imagine how much pain she's in right now..."
    "He whispered quietly."
    $l_exp = "concerned"
    "I couldn't help but notice that he was rubbing his own knee."
    $l_exp = "sad"
    l "Yeah, I know..."
    "I replied as I sat next to him."
    r smile "Heh."
    $l_exp = "concerned"
    l "What?"
    r crossed "I just never thought I'd see you show empathy for Jessica Tate."
    $l_exp = "neutral"
    l "..."
    "I get what he means, but the way he said that makes it seem like I'm a heartless monster."
    $l_exp = "concerned"
    "You know, like the REDD who have us held captive here."
    $l_exp = "neutral"
    l "Well, she's just as human as the rest of us."
    l "Not even she deserves this."
    r concerned "Yeah, no kidding..."
    $l_exp = "sad"
    "We then looked back to the TV, which showed Jingle and Jangle performing a skit."
    "We're only an hour into this nightmare, yet it feels like it should be almost over by now."
    "Or maybe that's just how I want it to be."
    "It all begs the question of how much worse could this possibly get for everyone..."
    hide screen laura
    window hide dissolve
    pause 1.0
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(2.0)
    pause 1
    scene bg basement
    with Dissolve(2.0)
    show jessica oneknee left_tears at two1_jessica zorder 1 with dissolve
    pause 1
    play sound footsteps
    show jessica right_tears with dissolve
    pause 5.5
    show sprinkles evilgrin cane hat at two2_sprinkles zorder 2
    with Dissolve(1.0)
    pause 0.5
    window show dissolve
    play music into_the_haunted_forest
    $s_name = "Krag"
    s "Hello, Mrs. Tate."
    j "!!!"
    s laugh "Ahaha! There's no need to be worried, my dear!"
    s "I'm not gonna torture you in private."
    s evilgrin "That would be a waste of potentially higher ratings~!"
    s happy rightdown "I just wanted to thank you for being a good sport, despite everything."
    s jeer "I mean, not that you have much of a choice..."
    s happy hat "Still, you're playing along beautifully, and the audience loves it!"
    s laugh "Well, the REDD ones, anyway~"
    j "..."
    s jeer "Heh."
    s "You look upset."
    s "Dare I say you look a bit angry."
    "He then bent down and looked at her eye-to-eye."
    s rightdown "You can't put all the blame on me, my dear."
    s evilgrin "After all, this is technically {b}your{/b} fault."
    s jeer "I mean, think about it. {b}Really{/b} think about it."
    s wut "You were so convinced that the REDD were these evil, heartless, unforgiving monsters. You even managed to convince so many others of the same thing."
    s "And what did you do despite having that belief?"
    s "You {b}threatened{/b} one!"
    s "You threatened to take away his show and everything he had ever worked for!"
    s huh "I mean, I still cannot understand what was going through your mind."
    s hm "I can only assume that {b}nothing{/b} was."
    s @ happy hat "{i}Hur dee durr!! I think this guy has the desire to kill us all! The most logical way to retaliate is to {b}piss him off!!{/b}{/i}"
    s "What, did you really think I wasn't going to fight back?"
    s "Did you really think I would just sit idly by while you took everything from me?"
    s wut "All because of something you {b}assumed{/b} could happen?"
    s "..."
    s jeer "I mean, yes, I suppose there's some irony in the fact that you were right, but..."
    s hm "It would have never came to this had you just kept your big fat trap shut."
    s "So just remember:"
    s "Every person who died here tonight?{w} That's on you."
    s "Every person who {b}will{/b} die here tonight?{w} That's on you."
    s "Every child who is traumatized and scarred for life from having their idol degrade to a heartless monster who killed their parent because he had nothing left to lose?"
    show sprinkles:
        linear 0.25 xalign 0.88
    s "That's."
    show sprinkles:
        linear 0.25 xalign 0.78
    s "On."
    show sprinkles:
        linear 0.25 xalign 0.68
    s evilgrin "{b}You.{/b}"
    window hide
    stop music fadeout(5)
    pause 6
    window show
    show sprinkles laugh hat:
        linear 0.25 two2_sprinkles
    s "Ahaha~!"
    s happy "Well, I better get back on stage!"
    s jeer "The show must go on, as they say."
    pause 0.5
    play sound footsteps
    hide sprinkles
    with Dissolve(1.0)
    pause 1
    j left_tears "..."
    $s_name = "Mr. Sprinkles"
    call sceneend from _call_sceneend_7
    if not persistent.scenes["ch3_s3"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s3"] = True


label girlsescape:
    python:
        currenttime = "9:00 PM"
        timeleft = "10 hours"
        t_name = "Guard"
    call chapterstart from _call_chapterstart_8
    pause 2
    play music sprinkles_theme
    scene bg stage
    show sprinkles happy rightdown cane at middle_sprinkles
    with Dissolve(2.0)
    window show dissolve
    pause 0.1
    s "Alright, folks, it's time for a proper 15-minute break!"
    s "The helpful people by the doors will guide you to the restrooms if you need to go, and you may also use this opportunity to grab some snacks and refreshments."
    s laugh hat "We'll see you all back here in 15 minutes~!"
    s jeer "And for our lovely viewers at home, as well as those in the audience who don't wish to get up, please enjoy the live footage outside of the theater, where I'm sure something exciting is bound to be happening!"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    $l_exp = "concerned"
    scene bg storage
    show screen laura
    with dissolve
    pause 0.1
    "That ought to get the people in the audience to conveniently need to use the restroom."
    $l_exp = "surprised"
    "I mean, at least now there were some adults in the audience, so it shouldn't be as chaotic compared to if it were just children."
    $l_exp = "sad"
    "Still... the poor kids whose parents are trapped back here..."
    "The uncertainty they must be feeling..."
    "Kate... Dakota..."
    "How in the world are they right now??"
    "They must be worried sick about Richard and I!"
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg livestage_open
    show dakota sad crossed at two1
    show kate shocked down at two2
    hide screen laura
    with dissolve
    pause 0.1
    k "Kota, I still have to gooooooo!!"
    d "I know, Kate! We'll be there soon. Just hold it for a little longer!"
    k crying "I caaaaaan't!!"
    d "Just try, okay?"
    t "Alright! If anyone needs to go out, move it!"
    d small_smile side "C'mon, Kate!"
    stop music fadeout(3)
    scene bg lobby with dissolve
    pause 0.1
    "A large crowd of children and a small amount of adults exited into the lobby in a slow, yet organized fashion, with guards surrounding them at all times."
    "Fortunately for Kate, the restrooms weren't too far away."
    "Though, they weren't exactly as close as she would have liked."
    show kate shocked fidget:
        two2
        alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.25 ypos -20
            ease 0.25 ypos 0
            repeat
    show dakota sad hips at two1 with dissolve
    k "Nnnnggg...!"
    d "We're almost there, Kate! Try to think about something else!"
    k "I can't!"
    d "You have to!"
    k crying "I...!!"
    "Dakota could tell Kate wasn't going to be able to contain it much longer."
    "She honestly couldn't tell if the tears going down her sister's face were more from fear or stress."
    play music autumn_changes
    d crossed "Kate, listen to me."
    d "I know you're scared."
    d "I know you're scared about Mom and Dad, about what Mr. Sprinkles is doing, about whether or not you'll wet yourself. I get it, Kate."
    show kate:
        ease 0.5 two2
    k concerned "..."
    d mad "Believe me, I'm scared, too, Kate."
    d "I don't know why this is happening or if Mom and Dad will come back to us."
    d hips small_smile "But I do know that Mom and Dad would want us to be brave right now, even though we're scared."
    d "We're together right now, and as long as that's true, nothing will get in our way."
    k "..."
    d crossed smirk "So what do you say we make Mom and Dad proud by being brave?"
    k crying "B-But I'm not brave!"
    d determined "Yes, you are, Kate!"
    show kate shocked
    show dakota confused
    t "Hey! You goin' in or what?"
    show dakota neutral
    "Dakota then noticed that they were in front of the line for the restrooms."
    d small_smile side "See, Kate? You were able to get here without wetting yourself!"
    k concerned "!!"
    k happy "I did~!"
    show kate:
        ease 0.25 ypos -20
        ease 0.25 ypos 0
        repeat
    k shocked "B-But I still have to go!"
    d smirk hips "Alright, then get in there!"
    k concerned "Can you come in with me?"
    d small_smile "I don't need to go, Kate."
    k "Please?"
    d @ neutral "..."
    d "O-Okay, Kate."
    scene bg restroom with dissolve
    pause 0.5
    show dakota sad side at middle with dissolve
    pause 0.1
    "While Dakota waited for Kate, she looked around at the other girls in the restroom with them."
    "They looked just as scared and lost as she was, though there were a few mothers in there, as well, so at least they had someone with them."
    "Girl" "\"Excuse me...\""
    d confused "Hm?"
    "She then noticed she was blocking the only empty sink."
    d sad crossed "Oh. Sorry."
    "Right as she moved out of the way, the stall Kate was in opened up and she rushed right out."
    show dakota at two2
    show kate excited down at two1
    with easeinleft
    pause 0.1
    d small_smile "Feel better?"
    k "Yeah!"
    d smirk "Good to hear."
    stop music fadeout(3)
    t "Come on, hurry it up!"
    show dakota sad
    show kate shocked fidget
    "They heard a nearby girl guard yell at a girl at the sink."
    woman "Hey! Don't talk to my daughter that way!"
    "The guard gave a small laugh and looked at the lady with a scary smile."
    t "And what exactly do you think you're gonna do if I do?"
    "The other girls in the restroom were either staring uncomfortably or walking away as quickly as they could."
    d side "C-C'mon, Kate. Let's go."
    k concerned "But I haven't washed my hands."
    d small_smile "You'll be fine."
    "Dakota then took Kate's hand and walked her towards the restroom exit."
    woman "Oh, please! Don't act like you have the guts to shoot me in front of all these kids!"
    t "You think I give a fuck about that kind of shit??"
    woman "Watch yourself!"
    t "In case you haven't noticed, you're not the boss of me, bitch!"
    woman "Whatever. Come on, Candy."
    woman "The less we bother this alien, the better."
    t "I'm sorry, what did you just call me?"
    show dakota neutral
    "Dakota tried to pick up the pace, but there was a lengthy line trying to get out."
    "A few seconds later, she heard a struggle behind her."
    t "I asked you a damn question!"
    woman "Hey! Get your hands off me!"
    t "What? Did you just? Call me??"
    "The woman replied with a rude voice."
    woman "Oh, I'm sorry. Are you offended by that word, you {b}alien{/b}?"
    play sound machine_gun
    call gunflash from _call_gunflash_3
    show dakota sad
    show kate shocked
    pause 0.25
    play sound2 children_screaming
    play ambience crowd_screaming
    pause 0.5
    d "{b}{i}KATE, RUN!!!{/i}{/b}"
    hide dakota
    hide kate
    with easeoutright
    pause 0.1
    "She wasn't the only one taking that advice; everyone in the restroom seemed to rush right out and got as far from there as they could."
    t "H-Hey!! Get back here!!"
    t "...Shit!"
    scene bg lobby with dissolve
    pause 0.5
    show dakota sad side at two1
    show kate shocked down at two2
    with dissolve
    pause 0.1
    k "Where are we going??"
    d "Anywhere but here!!"
    "All around them, people were bumping into them, scrambling away from the guards and the stage entrance."
    play sound machine_gun
    call gunflash from _call_gunflash_4
    pause 0.5
    t "Everyone get your asses back here or I {b}will{/b} shoot you!!"
    k crying "K-Kota!!"
    d "Keep running, Kate! We'll be fine!!"
    play sound machine_gun
    call gunflash from _call_gunflash_5
    scene bg lobby with dissolve
    pause 1.0
    scene bg arena_hall with dissolve
    pause 0.1
    "Kate then got bumped into so hard that she fell down!"
    show dakota sad side at middle with dissolve
    pause 0.1
    d "Kate!"
    "After pulling her sister back up, she held onto her hand and kept running."
    $k_hat = False
    show dakota zorder 2:
        ease 0.5 two1
    show kate shocked up at two2 zorder 1 with dissolve
    pause 0.1
    k "Kota, my hat!"
    d "You'll be okay, Kate! Let's move!!"
    play sound machine_gun
    call gunflash from _call_gunflash_6
    scene bg arena_hall with dissolve
    call sceneend from _call_sceneend_8
    if not persistent.scenes["ch3_s4"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s4"] = True


label showmustgoon:
    python:
        currenttime = "9:18 PM"
        timeleft = "9 hours and 42 minutes"
        l_exp = "neutral"
        t_name = "Big REDD"
    call chapterstart from _call_chapterstart_9
    pause 2
    play music classy_ghouls
    scene bg storage
    with Dissolve(2.0)
    show screen laura
    window show dissolve
    pause 0.1
    "It didn't take long for us to learn what had happened."
    "We didn't have the specifics, of course, but the basic rundown was 'a REDD shot someone, kids ran in panic, now they're being hunted'."
    $l_exp = "smile"
    "A good portion of the audience didn't run and returned to their seats ASAP."
    $l_exp = "surprised"
    "But a lot of them ran away to different parts of the theater."
    $l_exp = "concerned"
    "Last we knew, Krag was being informed of the situation and being asked what they should do."
    "His show is already being delayed thanks to this mishap, so it begs the question of how he's going to handle it."
    show richard down concerned at middle with dissolve
    pause 0.1
    $l_exp = "surprised"
    r "...do you think..."
    "I grabbed his hand tightly."
    $l_exp = "smile"
    l "Our girls are smart, especially with Dakota in charge."
    l "They wouldn't get themselves in danger."
    r glare "They're still kids, Laura. And they must be scared out of their minds."
    $l_exp = "surprised"
    l "I know that, Richard."
    $l_exp = "sad"
    l "But if I don't assume the best right now, I'm gonna go insane."
    r concerned "..."
    "That's when the screen cut to the stage, with the REDD of the hour having a grin on his face."
    stop music fadeout(0.6)
    scene bg stage
    hide screen laura
    show sprinkles happy rightdown cane at middle_sprinkles
    with dissolve
    pause 0.1
    play music sprinkles_theme
    s "Ahaha~! Sorry for the delay there, folks."
    s wut "We had a bit of an issue during the break."
    s jeer hat "Thankfully, it's being sorted out, and it shouldn't interfere with our show."
    s laugh rightdown "That said, let's select another game to play~!"
    $l_exp = "surprised"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg storage
    show screen laura
    show richard concerned down at middle
    with dissolve
    pause 0.1
    play sound door_open
    "On cue, the big REDD came back in."
    hide richard
    show trosh gun angry at middle
    with dissolve
    pause 0.1
    t "Alright, you two are next!"
    "He exclaimed as he pointed to two of the people near the front."
    woman "P-Please! I can't!"
    t concerned "Is that right?"
    "He then pointed his gun at her in the blink of an eye."
    t "Then you're of no use to us."
    woman "WAIT!!"
    woman "I-I'll go..."
    t laugh "That's what I thought."
    redd "Hey!"
    $l_exp = "concerned"
    show trosh concerned
    "The big REDD turned to face the doorway, where a fellow REDD could be seen looking in."
    t "What??"
    redd "We found this in one of the hallways."
    "He then held up something."
    $l_exp = "neutral"
    "It looked very bright yellow, just like--"
    stop music fadeout(3)
    $l_exp = "shocked"
    "..."
    "Oh, my God..."
    "He was holding Kate's hat."
    show black zorder 3
    with Dissolve(1.0)
    pause 0.5
    $nvl = True
    nvl clear
    hide screen laura
    nvl show dissolve
    play music vast_places
    $renpy.music.set_volume(1.0, channel="music")
    narrate """
    No, that can't be right.

    There's no way Kate would have been in a position where her hat would be in a hallway.

    That has to be someone else's hat.

    Someone else with a Mr. Sprinkles top hat.

    Something I even pointed out hours ago that no one else was wearing...

    I must have missed the other person who was wearing one.

    It's the only thing that makes sense.

    Kate has to be safe in her seat.

    Dakota has to be right there beside her.

    They have to be safe.

    They have to be...
    """
    $nvl = False
    nvl hide
    hide black
    show screen laura
    with dissolve
    pause 0.1
    t "Have you searched the hall thoroughly?"
    redd "We have a team working on it now."
    t "Alright. Once we get these next contestants out, I'll get someone to cover my position so I can search with you."
    redd "Roger that. What should we do if we find someone?"
    t "Krag said if you find a child, bring them back to their seat alive."
    t "But if you 'accidentally' hurt one..."
    t laugh "...I wouldn't be upset, ehehe."
    $l_exp = "mad"
    "I stood up without thinking."
    "Richard looked at me with confusion and fear."
    l "Don't you dare hurt those kids!"
    t fear "..."
    "All eyes were on me now."
    "The big REDD just looked a bit confused."
    t "I'm sorry, I must be hearing things incorrectly."
    t concerned "It sounded like you just gave me an order."
    l "Oh, you heard correctly."
    t angry "Is that right?"
    stop music fadeout(5)
    "He then walked over to me slowly, everyone in his path quickly trying to move away."
    "He finally stopped about a foot away from me, looking me in the eye."
    $l_exp = "neutral"
    "I was scared shitless, but there's no turning back now."
    menu:
        t "What's your name?"
        "\"Laura.\"":
            jump nameislaura
        "\"Why do you care?\"":
            $l_exp = "concerned"
            l "Why do you care?"
            l "You see us as nothing but future corpses. Why do you care about names?"
            t concerned "..."
            "The room was dead silent."
            "..."
            t "Fair point."
            $l_exp = "neutral"
            "He then turned around to the REDD in the hall."
            t "Take the one in the black shirt and one in the red shirt to the stage."
            "He ordered as he pointed to the women he selected when he came in."
            t "And close the door behind you."
            "The guard did just that, with the terrified women shedding tears as they left."
            "He then looked at me with a grin."
            t "You're right. Humans are nothing but future corpses."
            t laugh "And you're about to meet your destiny."
            $l_exp = "surprised"
            "The next thing I knew, the barrel of his gun was on my chest."
            $quickhide = True
            hide screen laura
            window hide
            play sound machine_gun
            call gunflash from _call_gunflash_7
            play sound2 crowd_screaming
            if persistent.gore == '':
                scene bg blood
                with Dissolve(2.0)
            else:
                pause 2
            stop sound2 fadeout(5)
            pause 3
            scene bg fade
            with Dissolve(2.0)
            pause 1
            if not persistent.achievements["futurecorpses"]:
                $persistent.achievements["futurecorpses"] = True
                $renpy.notify("Achievement Unlocked: {i}Future Corpses{/i}")
                $persistent.achievelist.append(1)
            $renpy.end_replay()
            jump gameover
label nameislaura:
    l "...{w}Laura."
    t "Well, Laura, I must commend you for your bravery."
    t laugh "As idiotic as it is."
    t angry "But let me tell you something as clear as I can."
    "He then took off his helmet and leaned even closer to me."
    $helmet = ""
    with dissolve
    pause 0.1
    $l_exp = "concerned"
    "His breath smelled repulsive, but I kept my cool."
    $l_exp = "neutral"
    t "The only person I take orders from is Krag Dovason."
    t yelling "{b}NOT{/b} puny, pathetic humans such as yourself."
    $l_exp = "rage"
    l "Then why would you say it would be okay to harm those children when Krag said not to?"
    t concerned "Are you deaf, Laura?"
    t "I said I wouldn't be upset if it happened. I never said it would be okay."
    "That's when we could hear rapid footsteps approach the doorway."
    s "Trosh!"
    play music sprinkles_spooky
    $l_exp = "surprised"
    show trosh intrigued zorder 2:
        ease 0.5 two1
    show sprinkles wut rightdown leftdown at two2_sprinkles zorder 1 with dissolve
    pause 0.1
    s "Where are the next contestants?!"
    t concerned "Sorry. Had a bit of a conflict."
    s hm "Well, resolve it!! I can't afford any more delays!!"
    t "Understood. I'll bring them out now."
    "After taking a deep breath, Mr. Sprinkles walked away quickly."
    show trosh:
        ease 0.5 middle
    hide sprinkles with dissolve
    pause 0.1
    $l_exp = "concerned"
    l "Trosh?"
    l "As in Trosh Dovason?"
    show trosh angry
    "He glared at me for a second before putting his helmet back on and walking back towards the women he initially chose."
    $helmet = "_helmet"
    with dissolve
    pause 0.1
    $t_name = "Trosh"
    t "Move it."
    $l_exp = "neutral"
    "The women, clearly a bit surprised he hadn't forgotten about them, complied and walked out of the room by gunpoint."
    stop music fadeout(3)
    hide trosh with dissolve
    pause 0.5
    "I finally sat back down."
    show richard crossed glare at middle with dissolve
    pause 0.1
    "My husband didn't exactly look thrilled with me."
    play music vast_places
    $l_exp = "mad"
    l "Don't give me that look."
    r rage "I know you're scared about the girls and want them to be safe, but that does not mean you can just go picking a fight with the guys with guns!"
    $l_exp = "rage"
    l "So you would have just rather me sit here and do nothing while he talks about potentially hurting your daughters?"
    r glare "Oh, I'm sorry, I thought you were assuming the best so you could keep your sanity!"
    $l_exp = "mad"
    "I lightly growled as I covered my face with my hands."
    show black zorder 3:
        alpha 0.0
        ease 0.5 alpha 1.0
    $nvl = True
    nvl clear
    hide screen laura
    nvl show dissolve
    narrate """
    I felt a whole range of emotions at that moment.

    Anger, sadness, confusion, fear...
    
    Richard's right. I'm scared about Dakota and Kate.

    I can only be so optimistic before I accept the reality of the situation.
    
    {clear}

    My girls might be running around the theater, scared and lost.

    And there are REDD looking for them.

    And they might hurt them. Or worse.

    {nw}

    How can anyone stay calm knowing that?

    {nw}

    That's when I felt the tears come.

    That's when the sobs came out.

    That's when Richard grabbed my hand.
    """
    $nvl = False
    $l_exp = "crying"
    show richard concerned crossed
    hide black
    show screen laura
    nvl hide
    with dissolve
    pause 0.1
    r "Look..."
    r "I'm just as scared as you are, Laura."
    r "Believe me, I want to go out and find them just as much as you."
    r down "But if we get ourselves killed trying to find them, then what purpose does that serve?"
    $l_exp = "sad"
    "I wiped my eyes and took a deep breath."
    "I know he's right, but I don't wanna accept it."
    "He just continued to hold my hand as we sat there in silence."
    r smile "Hey."
    r crossed "What if we texted them, just for kicks?"
    $l_exp = "surprised"
    l "!!"
    $l_exp = "excited"
    l "Good idea."
    "I then took out my phone and texted Dakota."
    lt "Just wanted to check up on you girls to make sure you're okay"
    $l_exp = "surprised"
    "I wasn't exactly expecting an instant reply, but at least it's something she can reply to."
    $l_exp = "sad"
    "Eventually."
    r "Everything will be fine, Laura."
    $l_exp = "surprised"
    l "You really think that?"
    r concerned "..."
    r "Well, it's like you said. We just gotta assume the best, even if we don't believe it."
    "I guess that's all we really {b}can{/b} do..."
    stop music fadeout(3)
    $l_exp = "neutral"
    s "Come on, ladies, you got this!"
    play music ice_cream_truck
    play ambience saw
    $renpy.music.set_volume(0.25, channel="ambience")
    scene bg stage
    show sprinkles cane hat happy at middle_sprinkles
    with dissolve
    pause 0.1
    s "Keep pulling!"
    "The two women were playing a game of tug-of-war."
    $l_exp = "concerned"
    "It looked relatively safe at first."
    $l_exp = "surprised"
    extend " But then I noticed the giant horizontal spinning saw blade in the middle."
    "It was under the rope, at about thigh-level."
    "If someone got too close to it, they'd have a really bad leg day."
    $l_exp = "concerned"
    "And it appears that in order to prevent them from being detached from the rope, it's tied tightly to each of their wrists."
    "Currently, the woman with the red shirt was winning, though not by much."
    "It seems like anyone's game."
    s jeer rightdown "Let's go, ladies~!"
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    $renpy.music.set_volume(0.125, delay=0.5, channel="ambience")
    scene bg storage
    show richard concerned down at middle
    with dissolve
    pause 0.1
    $l_exp = "surprised"
    "You know we're in a fucked-up situation when watching a deadly tug-of-war game on TV was the best way to calm ourselves down."
    "Still, I can't help but keep Dakota and Kate in the back of my mind."
    "I really hope they're safe..."
    "Of course, how am I really supposed to know if they are?"
    $l_exp = "neutral"
    s "Ohoho, folks! This is getting interesting~!"
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    $renpy.music.set_volume(0.25, delay=0.5, channel="ambience")
    scene bg stage
    show sprinkles laugh cane rightdown at middle_sprinkles
    with dissolve
    pause 0.1
    s "Come on, you can win this!"
    "Now the woman in the black shirt was winning. By a decent amount, even."
    "Both women looked exhausted, their faces almost resembling that of a REDD's."
    $l_exp = "surprised"
    "Their arms were shaking like mad, their feet inching back and forth across the floor."
    "Tears of stress and pain were rolling down their cheeks."
    "The woman in red was getting closer and closer to the saw, her red, sweaty face showing every fearful expression imaginable."
    $l_exp = "sad"
    "Eventually, she seemed to show an expression of defeat."
    "Bracing herself, she loosened her grip and was thrust forward by her opponent."
    $quickhide = True
    hide screen laura
    window hide
    $renpy.music.set_volume(1.0, channel="ambience")
    $quickhide = False
    $l_exp = "surprised"
    stop music fadeout(5)
    play sound blood
    pause 0.1
    play sound2 children_screaming
    show blood
    pause 0.25
    show blood2
    pause 0.25
    show blood3
    pause 0.1
    show blood4
    pause 1
    show screen laura
    window show dissolve
    pause 0.1
    "The screen was pretty obscured with blood, but it was still not a pretty sight."
    "The poor woman couldn't fall back or get away because of the knot on her wrist, so her opponent had to step forward a bit in order for her to back up and topple to the ground."
    $renpy.music.set_volume(0.25, delay=1, channel="ambience")
    s happy hat "Oh, what a great game, ladies!"
    "Jingle and Jangle came out onto the stage, with Jingle untying the winner."
    "The loser, meanwhile, with tears and a cry, had her face dragged closer to the saw by Jangle."
    scene bg fade with dissolve
    pause 0.1
    $l_exp = "sad"
    $renpy.music.set_volume(1.0, channel="ambience")
    play sound blood
    "I closed my eyes tightly as I heard the woman's cries mixed in with the slicing of her face."
    "Please let this night end faster."
    "Please..."
    "I don't know how much more of this I can take..."
    call sceneend from _call_sceneend_9
    if not persistent.scenes["ch3_s5"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s5"] = True


label kidshiding:
    python:
        currenttime = "10:27 PM"
        timeleft = "8 hours and 33 minutes"
    call chapterstart from _call_chapterstart_10
    pause 2
    play music autumn_changes
    scene bg janitorcloset
    with Dissolve(2.0)
    window show dissolve
    pause 0.5
    show dakota sad crossed at two1
    show kate concerned down at two2
    with dissolve
    pause 0.1
    k "...Kota?"
    d "Yeah?"
    k "How much longer are we staying in here?"
    d "...I don't know, Kate."
    d "We may have to stay in here all night."
    k mad "But I don't wanna stay here all night!"
    d mad "I don't either, but we don't have many choices!"
    show dakota neutral
    show kate shocked fidget
    b "{b}Shhh!!{/b}"
    b "They're gonna hear you and find us!"
    d side "...Sorry."
    "The boy who was a few years older than Dakota then turned back to his younger brothers, who seemed to be around Kate's age."
    "Dakota looked at the other kids hiding in the closet with them."
    "The only light in the room was coming from a window high up along the wall, where street lights barely let anything in, though some light was better than none."
    "Some kids had a sibling with them, some had friends, and some were alone."
    "Tear stains were all over most of their faces, with a lot of them still crying, though very quietly."
    "All of them were sitting in a spot that couldn't easily be seen by anyone who opened the door."
    "At least, they hoped they couldn't be seen."
    "Kate then leaned against Dakota for comfort."
    k concerned "...I miss Mommy and Daddy."
    d sad "I do, too."
    d small_smile hips "But don't worry. They'll come back for us."
    d "I know they will."
    k alert "No, you don't."
    d sad "..."
    d "Yeah, I know."
    d small_smile side "I'm just trying to make you happy, I guess..."
    k "..."
    d sad "..."
    show dakota neutral
    show kate concerned
    "That's when Kate gave a yawn and rested her head on Dakota's shoulder."
    "Dakota then gave a small yawn, as well, as her eyes started to close a bit."
    "It had to have been really late right now, and all the running certainly did take a lot of energy."
    "But she didn't feel like she was in a situation where she could fall asleep."
    "After all, how could she do what her mom asked her to do if she was asleep?"
    show dakota small_smile
    "Kate, meanwhile, deserved a bit of a rest."
    hide kate with dissolve
    pause 0.1
    "After a few minutes, Dakota looked and saw Kate's eyes were closed."
    $b_name = "Older Boy"
    b "Wow. She actually fell asleep?"
    d confused "Huh?"
    "The older boy was looking at Dakota with a small grin."
    show dakota at middle with easeinleft
    pause 0.1
    b "I just wasn't expecting that. I thought she would've been too scared to sleep."
    d small_smile crossed "Yeah, I'm shocked, too."
    d smirk "Not that I'm complaining."
    "The older boy then gave a light laugh before looking back at his brothers."
    "They seemed to be awake, yet quiet."
    show dakota sad
    "They almost seemed to just be staring blankly ahead of them, showing no emotion at all."
    d "They're really scared, huh?"
    b "Aren't you?"
    d @ mad "Of course I am."
    d side "But they look so much more scared."
    b "Well, our mom..."
    b "Sh-She was..."
    d "One of the people who lost?"
    b "Yeah..."
    b "She was one of the ones who lost on {i}Sprinkles Says{/i}."
    d crossed "I'm so sorry!"
    b "Thanks..."
    d "D-Do you have a dad?"
    b "In Texas, yeah."
    d small_smile "Hey, that's something, right?"
    b "We haven't seen him in years, though."
    d sad "Oh..."
    "A few seconds of silence passed."
    b "What about you?"
    d confused "Huh?"
    b "Are your parents still alive?"
    d small_smile hips "Well, I haven't seen them on the stage, so I guess so."
    d sad "But we've been back here for a while. Maybe they've been on since and I just haven't realized..."
    b "Ah..."
    "More silence."
    d small_smile crossed "Heh..."
    d "For all I know, she's all I have left."
    "She whispered as she looked down at Kate."
    "It was more of a comment to herself than to the boy."
    stop music fadeout(5)
    play sound footsteps
    show dakota sad
    "That's when footsteps could be heard approaching the closet."
    "The older kids in the room got quiet, save for the small shushes they were giving to the younger ones."
    show dakota:
        ease 0.5 alpha 0.0
    window hide dissolve
    hide dakota
    pause 1.0
    play sound door_creak
    pause 9
    play sound slow_footsteps
    pause 5
    $t_name = "Guard"
    window show dissolve
    pause 0.1
    t "Alright, let's make this easy on all of us, shall we?"
    t "We've been given orders not to hurt any of you kids, and we plan to follow those orders."
    t "But if you decide to pull any sneaky tricks, we will not hesitate to take drastic measures."
    t "So do yourselves a favor and come with us calmly and quietly."
    show dakota sad side at middle with dissolve
    pause 0.1
    d "..."
    play sound slow_footsteps
    "The silence throughout the room was broken with more footsteps."
    t "Final warning! Everyone follow us back to the seating area or there will be consequences!"
    t "Trust me: your odds of survival will be 100\% if you comply with us."
    d "..."
    "That's when Dakota noticed several of the children getting up from their positions and following the voice."
    t "Aha! Thank you for your cooperation."
    queue sound [snap, "<silence .25>", snap, "<silence .25>", snap]
    t "Boys, start lining them up outside the room."
    "Several voices of other guards could be heard as they ordered the children to line up."
    d "..."
    play sound slow_footsteps
    "The footsteps then got closer."
    pause 2
    show dakota at two1_short with easeinright
    show trosh gun concerned at two2
    with Dissolve(1)
    pause 1
    t "Hello."
    play music classy_ghouls
    "The guard looked over all the kids in the area."
    "The older boy just glared at him while his brothers continued to stare blankly ahead."
    show dakota neutral
    "Dakota felt scared, but didn't want the guard to know that."
    "The guard then stopped and stared at Kate, who was still asleep."
    "Finally, he turned to Dakota."
    t "By any chance..."
    t "...is your mother's name Laura?"
    d sad "!!!"
    t "Heh heh... I'll take that as a yes."
    d "H-How do you know that?"
    "He then squatted down and looked at her in the eye."
    show trosh hips:
        ease 0.5 two2_short
    pause 0.6
    show trosh smile with dissolve
    pause 0.1
    $helmet = ""
    t "I actually had a little chat with Laura a while ago."
    t "She's a very brave woman. You're lucky to have her as a mother."
    "Dakota continued to stare in fear, unsure how to feel about this."
    t "Say, you know what will make her happy? Seeing her daughters."
    t laugh "I'm sure you'd love that, as well, right?"
    d crossed "Uh... I..."
    "He then extended his hand towards her."
    t intrigued "No tricks. I'll take you back to see her."
    t smile "She is alive, after all."
    d small_smile "She is?"
    d "My dad, too?"
    t "Cross my heart."
    d sad "..."
    "Every lesson on Stranger Danger came flooding into Dakota's mind."
    "And for the REDD War, it felt even more appropriate."
    "But..."
    "This could be their last chance to see their parents again."
    "Plus, just knowing that they're alive..."
    "She then lightly shook Kate."
    d "Kate?"
    k "Mmm..."
    "She lightly moaned while keeping her eyes closed."
    d small_smile hips "Kate, we're gonna see Mommy."
    "That did the trick."
    show dakota zorder 2:
        ease 0.5 middle_short
    show trosh zorder 2:
        ease 0.5 right
    show kate shocked fidget at left_short with dissolve
    pause 0.1
    k "Mommy??"
    d "Come on..."
    scene bg arena_hall with dissolve
    pause 0.1
    "The girls then got up and followed the guard to the doorway."
    $helmet = "_helmet"
    show trosh gun concerned at middle with dissolve
    pause 0.1
    t "Gather up the rest of the kids."
    t "I'm gonna take these two to see their mother."
    "The other guard nodded with a grin before turning back into the closet."
    hide trosh
    show dakota confused side at middle
    with dissolve
    pause 0.1
    "Something definitely felt wrong, but it felt like it was too late to back out now."
    show dakota zorder 2:
        ease 0.5 two2
    show kate confused fidget at two1 with dissolve
    pause 0.1
    k "Kota, why isn't anyone else going to see their mommies and daddies?"
    d "That's a good question, Kate."
    d "Hey, Mister?"
    show kate zorder 2:
        ease 0.5 left_short
    show dakota:
        ease 0.5 middle_short
    show trosh angry gun at right with dissolve
    pause 0.1
    t "What?"
    d crossed "Why are we the only ones who get to see their parents?"
    t concerned "Heh. Technically, I'm not even supposed to be taking you two to your parents."
    t laugh "But something about your mother tells me she'd be {i}really{/i} happy to see you two, so I thought I'd make an exception."
    d "So? I'm sure all the parents back there want to see their kids right now."
    t angry "If you're gonna be ungrateful, I can take you right back to the others."
    show dakota sad
    k shocked "No!"
    t concerned "That's what I thought."
    show kate concerned:
        ease 0.5 two1
    show dakota side:
        ease 0.5 two2
    hide trosh with dissolve
    pause 0.1
    "The girls stayed silent as the guard led them down the hallways."
    show dakota small_smile
    "Though the idea of seeing her parents again really made Dakota happy..."
    "The best she could do is hope he's telling the truth about everything."
    call sceneend from _call_sceneend_10
    if not persistent.scenes["ch3_s6"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s6"] = True


label deadlygame:
    python:
        currenttime = "11:11 PM"
        timeleft = "7 hours and 49 minutes"
        l_exp = "surprised"
    call chapterstart from _call_chapterstart_11
    pause 2
    play music sprinkles_theme
    scene bg stage
    show madeline dead at two1
    show sprinkles happy cane rightdown at two2_sprinkles
    with Dissolve(2.0)
    window show dissolve
    pause 0.1
    s "Why was the football stadium so hot after the game?"
    s jeer "{i}I don't know, Mr. Sprinkles. Why {b}was{/b} the football stadium so hot after the game?{/i}"
    s laugh hat "Because all the fans had left! Ahahaha!!"
    s happy "Alright, that's enough jokes for now, Ms. Madeline. We'll see you later~!"
    show sprinkles:
        ease 0.5 middle_sprinkles
    hide madeline with easeoutleft
    pause 0.1
    s rightdown "And now, friends, it's time for yet another game~!"
    s laugh "The Wacky Dartboard, please!"
    stop music fadeout(5)
    scene bg storage
    show richard down concerned at middle
    show screen laura
    with dissolve
    pause 0.1
    "On cue, Trosh came back in and took more contestants."
    "Four of them, to be exact."
    $l_exp = "concerned"
    "It might have been my imagination, but it feels like as he did, he looked at me and gave me a small smirk."
    $l_exp = "neutral"
    "It had to have been my imagination."
    $l_exp = "surprised"
    "Still, the fact that he's been back to bringing out contestants has to mean something about their hunt for the children, yet there were still no updates."
    $l_exp = "concerned"
    "Not that they would go out of their way to tell us, anyway."
    $l_exp = "surprised"
    "Still, I guess not knowing for sure gives you the chance that nothing is wrong."
    "But that doesn't mean it's not eating you up on the inside."
    "Richard looked around the room a bit before sighing."
    play music vast_places
    r crossed "It feels so much emptier in here..."
    $l_exp = "sad"
    "He wasn't wrong. After all the time that's passed, the room has become less and less populated as contestants were selected."
    $l_exp = "surprised"
    "There was still a decent amount of people inside, no doubt, but it feels less claustrophobic."
    $l_exp = "excited"
    l "Well, at least a good amount of people who left the room made it back to their seats, right?"
    r "Yeah, but..."
    r "It's still unnerving knowing a good amount of them didn't..."
    $l_exp = "sad"
    l "Yeah, I know."
    "Sensing the conversation wasn't going anywhere else, I looked back at the TV."
    $l_exp = "surprised"
    "It looks like the next game was Memory Mania, the game where a bunch of different things happen on a screen and you had to answer a question about what you saw."
    $l_exp = "concerned"
    "Like {i}'How many penguins were holding ice cream cones?'{/i} or {i}'Were there more giraffes or elephants?'{/i}"
    $l_exp = "surprised"
    "I've personally never been good at the game, and neither was Kate."
    $l_exp = "smug"
    "Though Dakota, being the genius she is, was always pretty good at it."
    $l_exp = "surprised"
    "Let's just hope that the contestants here are good at it, as well..."
    stop music fadeout(3.0)
    hide screen laura
    pause 0.5
    scene bg stage
    show sprinkles rightdown leftdown jeer at middle_sprinkles
    with Fade(1.0, 0.5, 1.0)
    pause 0.1
    play music ice_cream_truck
    s "Alright, final round!"
    s hat evilgrin "Good luck, you two~!"
    show screen laura
    pause 0.6
    "More images then moved across the screen."
    $l_exp = "concerned"
    "Incredibly fast, as well."
    s laugh "Alright, your question is:"
    s "How many elephants were holding bananas?"
    "...I suppose that wasn't the most unfair of questions."
    $l_exp = "neutral"
    "The two remaining contestants wrote their answers on their white board."
    stop music
    play sound buzzer_full
    pause 1
    s happy rightdown "Time's up~!"
    s jeer "What are your final answers?"
    $l_exp = "surprised"
    "The contestants shakily lifted up their boards."
    s hm "Hmm..."
    s "One says 2, the other says 4."
    s laugh "Well, either one of you is right, or none of you are!"
    s evilgrin hat "Let's see what the result is."
    play sound drumroll_buildup loop
    hide sprinkles with dissolve
    pause 0.1
    "The video replayed itself, only this time, the banana-holding elephants were highlighted."
    "1...{w} 2...{w} ..."
    $l_exp = "sad"
    extend " 3...{w} ..."
    $l_exp = "surprised"
    "The clip ended."
    play sound drumroll_finish
    pause 1
    show sprinkles laugh leftdown rightdown at middle_sprinkles with dissolve
    pause 0.1
    s "And the correct answer is '3'!"
    s huh "Oh, my! It appears neither of you were correct!"
    s wut "What a shame."
    s evilgrin hat "Well, thank you for playing~!"
    play sound shotgun
    show blood2
    call gunflash from _call_gunflash_8
    pause 0.1
    play ambience crowd_screaming
    play sound2 shotgun
    show blood4
    call gunflash from _call_gunflash_9
    pause 1
    s laugh "Ahaha~!"
    stop ambience fadeout(3.0)
    scene bg storage
    show richard down concerned at middle
    with dissolve
    pause 0.1
    r "It'll never end, will it?"
    l "I mean, technically, it will at 7, but..."
    $l_exp = "sad"
    l "...it certainly doesn't feel like it."
    play sound door_open
    $l_exp = "concerned"
    "That's when Trosh entered the room."
    $t_name = "Trosh"
    hide richard with dissolve
    play music classy_ghouls
    show trosh gun laugh at middle with dissolve
    pause 0.1
    t "Alright, up next is a really special game that I'm going to need a specific volunteer for."
    "He then walked towards the back of the room."
    $l_exp = "surprised"
    "Closer to me."
    $l_exp = "sad"
    "And stopped directly in front of me."
    t angry "You.{w} You're coming with me."
    $l_exp = "shocked"
    l "W-What??"
    t "You heard me! Move it!"
    show trosh zorder 2:
        ease 0.5 two1
    show richard down rage at two2 zorder 1 with dissolve
    pause 0.1
    r "Hey! You can't just--!"
    "Trosh then pointed his gun at Richard."
    t concerned "I can't just what?"
    show richard glare
    "My husband then glared at the REDD before looking back at me."
    t "That's what I thought."
    "Trosh then looked back at me."
    t angry "Let's go."
    r rage "Wait! Take me, instead!"
    $l_exp = "sad"
    l "Richard!!"
    t fear "I'm sorry?"
    r glare "Take me instead of her!"
    t concerned "..."
    l "..."
    r "..."
    "Trosh then looked at me with a smug look on his face."
    t laugh "Well, what do you say?"
    $l_exp = "surprised"
    l "I..."
    show trosh angry
    "He then pointed his gun at me."
    $renpy.music.set_volume(0.5, delay=1, channel="music")
    menu:
        t "Well? Is he taking your place or not?"
        "Let Richard Take Your Place":
            $renpy.music.set_volume(1.0, delay=1, channel="music")
            jump richardtakesplace
        "Don't Let Richard Take Your Place":
            $renpy.music.set_volume(1.0, delay=1, channel="music")
label richarddoesnttakeplace:
    $l_exp = "neutral"
    l "N-No. I'll go."
    r shocked "Laura, please!"
    t laugh "Heh. You heard the lady, bub."
    $l_exp = "sad"
    "He then grabbed on to my upper arm."
    t "Let's go!"
    r "Laura!"
    $l_exp = "surprised"
    l "I'll be fine, Richard! I love you!"
    stop music fadeout(3.0)
    scene bg basement_hall with dissolve
    pause 0.1
    "I was then dragged backstage, right by a door that seemed to lead outside."
    "Several other REDD guards were there waiting."
    t "If you try to run or pull any stunts--"
    $l_exp = "mad"
    l "You'll shoot me. I get it."
    "He then growled before opening the door and taking me outside."
    $renpy.music.set_volume(0.75, channel="ambience")
    play music into_the_haunted_forest
    play ambience rapid_gunfire
    scene bg alley with dissolve
    pause 0.5
    $l_exp = "neutral"
    "We entered a back alley, with a nearby street being pretty close."
    $l_exp = "concerned"
    "Nothing here indicated that we were headed to one of Mr. Sprinkles' death traps."
    l "You're sure you're taking me to a game?"
    show trosh gun concerned at middle with dissolve
    pause 0.1
    t "This one can't be played on the stage; we needed more space."
    t "Don't worry; we're not going too far."
    $l_exp = "neutral"
    "Silence, save for the gunfire and hollering of joy in the distance."
    nvl clear
    $nvl = True
    hide trosh with dissolve
    hide screen laura
    nvl show dissolve
    narrate """
    It was then when I realized that this was the first time I had been outside since the REDD War started.

    When we walked out onto the street, I glanced around.

    There weren't any REDD in sight, but we could definitely hear their presence.

    All around me, the city seemed to still be somewhat standing, but fires and the occasional explosion reminded me that we still had plenty of time for that to change.

    It's kinda funny, really.{w} I've been exposed to the horrors the REDD War can bring for the past 4 hours, yet I still can't believe that it's happening.

    The fact that the War isn't even halfway done yet brings a shiver down my spine.

    After all, there's still plenty of time for things to get worse...
    """
    $nvl = False
    nvl hide
    show screen laura
    with dissolve
    pause 0.1
    "We finally made it to a parking garage a block away."
    scene bg parkinggarage with dissolve
    pause 0.1
    "When we approached, I noticed a television camera near the entrance with a REDD giving the guards a thumb's up as we approached."
    "There was also a large line that said 'START' written by the entrance."
    $l_exp = "surprised"
    "But then, I noticed something by the starting line."
    "Something I definitely didn't expect to see."
    $l_exp = "shocked"
    l "Oh, my God!!"
    show kate crying fidget at two1
    show dakota sad side at two2
    with dissolve
    pause 0.1
    k "Mommy!!"
    "My daughters were sitting in chairs with armed guards behind them."
    "They weren't tied down, it seemed, but it's safe to assume they understood what would happen if they tried to get up."
    $helmet = ""
    show kate zorder 2:
        ease 0.5 left
    show dakota zorder 2:
        ease 0.5 right
    show trosh gun laugh at middle zorder 1 with dissolve
    pause 0.1
    t "See, girls? I told you you'd get to see your mommy again!"
    $l_exp = "rage"
    l "H-How did you--?!"
    t smile "Does it really matter?"
    t "Besides, you should be grateful."
    t laugh "No other parent tonight has gotten to see their children like this."
    t "I figure it'll give you the motivation you need to compete well."
    t smile "Or, you know, the added pressure of your children being right here to witness your potential death might fuck you up."
    t laugh "Either way, it's gonna make for some great footage!"
    l "I swear, if you lay one finger on them--!!"
    t concerned "If I wanted them dead or hurt, I would've done it by now."
    redd "Trosh, we're about to go live."
    t smile "Excellent."
    stop music fadeout(3.0)
    stop ambience fadeout(3.0)
    scene bg parkinggarage with dissolve
    pause 0.1
    "The camera then pointed towards me."
    $l_exp = "concerned"
    l "Hang on, I don't even know what I'm doing!"
    t "Have patience."
    "He then turned on a radio near the camera, where the voice of Mr. Sprinkles could be heard coming out."
    play music sprinkles_radio
    s "Alright, folks! Our brave contestant now has to tackle the {i}Wild, Wild Races{/i} course!"
    $l_exp = "mad"
    "Oh, you have got to be kidding."
    s "On each floor of our makeshift course is a series of obstacles that she must make her way through."
    s "The higher up she gets, the more challenging, {i}and dangerous{/i}, they will become!"
    s "Will she make it to the finish line in one piece? Ohoho! There's only one way to find out~!"
    $l_exp = "mad"
    l "Let me guess. I'm not gonna be told what the obstacles are."
    show trosh gun smile at middle with dissolve
    pause 0.1
    t "Bingo."
    l "Lovely."
    hide trosh with dissolve
    pause 0.1
    s "Alright, brave contestant! Head to the starting line!"
    "Realizing I don't have much of a choice, I inched my way over."
    show kate concerned concerned fidget at two1
    show dakota sad side at two2
    with dissolve
    pause 0.1
    $l_exp = "sad"
    "I then looked over at my daughters, who looked scared out of their minds."
    "Don't worry, girls. Mommy will get through this, and then we'll all be safe."
    scene bg parkinggarage with dissolve
    pause 0.1
    stop music fadeout(3.0)
    s "On your marks...!"
    $l_exp = "surprised"
    "I took a deep breath and looked ahead at the ramp."
    s "Get set...!"
    $l_exp = "neutral"
    "All I have to do is get through the course and survive. It can't be that hard."
    $l_exp = "surprised"
    "At least, I hope it isn't."
    s "{b}GO!{/b}"
    play sound airhorn
    play music into_battle
    "A horn went off, and on instinct, I started running."
    $l_exp = "concerned"
    "I suppose if I want to have any chance of surviving, I need to not go through it {b}too{/b} fast."
    $l_exp = "mad"
    "I run around the first corner."
    stop music
    show blood
    play sound stab
    $l_exp = "surprised"
    pause 1
    "And straight into a sharp pole."
    if persistent.gore == '':
        show red zorder 2:
            alpha 0.0
            ease 3.0 alpha 1.0
    "Well..."
    "That's embarrassing."
    hide screen laura
    window hide dissolve
    pause 2
    scene bg fade
    with Dissolve(2)
    pause 1
    $renpy.end_replay()
    if not persistent.achievements["epicfail"]:
        $persistent.achievements["epicfail"] = True
        $renpy.notify("Achievement Unlocked: {i}Schadenfreude{/i}")
        $persistent.achievelist.append(1)
    jump gameover
label richardtakesplace:
    "Of course I don't {b}want{/b} him to go out there."
    $l_exp = "sad"
    "But what's the alternative? Getting {b}myself{/b} killed?"
    $l_exp = "surprised"
    "Besides, Richard's stronger and more active than me. He might actually have a better chance."
    l "You're sure, Richard?"
    r crossed "If it keeps you alive, I'm completely sure."
    t laugh "Sounds like a 'yes' to me."
    "Trosh then grabbed onto Richard and dragged him out of the room."
    r down shocked "Just stay alive for them, Laura! Please!"
    r concerned "I love you! Just stay alive!!"
    stop music fadeout(3.0)
    scene bg storage
    with Dissolve(2.0)
    pause 0.5
    $l_exp = "sad"
    "Oh God..."
    "Maybe this was a mistake."
    "Maybe it should have been me going out, not him."
    $l_exp = "surprised"
    "I guess it's a bit too late for that now..."
    $l_exp = "neutral"
    "Several minutes had passed, and there was nothing about what Richard would be playing."
    $l_exp = "concerned"
    "Usually, it takes a minute or two, but we're talking closer to 5."
    $l_exp = "surprised"
    "Soon, though, I got my explanation for why that was the case."
    play music sprinkles_theme
    scene bg stage
    show sprinkles happy leftdown rightdown at middle_sprinkles
    hide screen laura
    with dissolve
    pause 0.1
    s "Alright, and the Wacky Dartboard has landed on..."
    s laugh "{i}Wild, Wild Races!{/i}"
    show game_name "Wild, Wild Races" at game_name_flash
    show screen laura
    pause 0.1
    "Oh, no!"
    "That's the most physically-challenging game on the show!"
    $l_exp = "concerned"
    "But it's usually not played on the stage, so where would it be?"
    hide screen laura
    pause 0.6
    hide game_name
    s jeer hat "And now, it is time to go live to our course and see our brave contestant!"
    scene bg parkinggarage with dissolve
    pause 0.1
    $l_exp = "neutral"
    show screen laura
    pause 0.6
    "It looked like a parking garage that had to have been near the theater."
    $l_exp = "sad"
    "And right by the starting line..."
    show richard crossed glare at middle with dissolve
    pause 0.1
    "...was Richard."
    $l_exp = "surprised"
    "He looked like he was doing his best to be brave, but I knew him well enough to where I knew he was terrified."
    s "Alright, folks! Our brave contestant now has to tackle the {i}Wild, Wild Races{/i} course!"
    s "On each floor of our makeshift course is a series of obstacles that he must make his way through."
    s "The higher up he gets, the more challenging, {i}and dangerous{/i}, they will become!"
    s "Will he make it to the finish line in one piece? Ohoho! There's only one way to find out~!"
    $l_exp = "concerned"
    "Hold on..."
    "The camera shifted a little bit to show more of the starting line."
    "It looked like there was someone sitting in a chair."
    $l_exp = "sad"
    "Someone who looked like a child...!"
    s "Alright, brave contestant! Head to the starting line!"
    $l_exp = "surprised"
    show richard down
    "My husband slowly made his way over."
    show richard concerned
    "He seemed to show his fear a bit when he got to the starting line and looked to his side."
    "That's when the camera fully panned to show what he was looking at."
    $l_exp = "shocked"
    l "Oh, my God!!"
    "I couldn't hold back the horror I felt by what I saw!"
    hide richard with dissolve
    pause 0.1
    show kate crying fidget at two1
    show dakota sad side at two2
    with dissolve
    pause 0.1
    "Kate and Dakota were out there, sitting in chairs with guards behind them!"
    "How?? Why??"
    $l_exp = "surprised"
    "I suppose this is confirmation that they're alive, and they don't seem to be injured, but..."
    $l_exp = "sad"
    "Why are they out there watching this??"
    "How did the REDD even find them and know they were his daughters??"
    $l_exp = "surprised"
    "...{w}hang on."
    $l_exp = "concerned"
    "I was the one supposed to be out there, not Richard."
    "So {b}I{/b} was supposed to be the one the girls were watching."
    $l_exp = "shocked"
    "But then, how--?"
    s "On your marks...!"
    stop music fadeout(3.0)
    $l_exp = "surprised"
    scene bg parkinggarage with dissolve
    pause 0.1
    show richard down concerned at middle with dissolve
    pause 0.1
    "The camera then cut back to Richard."
    s "Get set...!"
    show richard glare
    "He looked rightfully determined to complete the obstacle course."
    $l_exp = "sad"
    "I hope he can pull it off."
    "For the family's sake."
    s "{b}GO!{/b}"
    play sound airhorn
    play music into_battle
    "After the horn went off, Richard bolted forward."
    $l_exp = "surprised"
    "He turned the corner, and was about to keep going..."
    show richard concerned
    "But a wall of large, sharp poles stood in his way!"
    if persistent.achievements["epicfail"]:
        $l_exp = "concerned"
        "Wow. I don't think I would've been able to notice those or stop in time."
    $l_exp = "smile"
    "Fortunately, there was a fair-sized opening along the wall that he was able to get through."
    show richard glare
    "After that hurdle, he kept on going."
    hide richard
    hide screen laura
    with dissolve
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    Credit where it's due, a lot of the obstacles in the course were very similar to the ones you'd find in the proper {i}Wild, Wild Races{/i} courses.

    You had your typical swinging pendulums, slippery floor, things hurled at you, all that noise.

    The most glaring difference in this case is that the obstacles will hurt or kill you.

    The pendulums were axe blades.

    The slippery floor was on a ramp that led to a buzzsaw.

    The things being hurled were baseballs from a pitching machine.

    Richard got hit a few times by the latter, which did slow him down a bit, but he was able to recover quickly.

    He's certainly using all his strength and stamina to get through this, though I wonder if knowing that his girls are down there watching is messing with his head a bit.
    """
    $nvl = False
    nvl hide
    with dissolve
    pause 0.1
    s "And our contestant is approaching the top floor!"
    s "Will he be able to overcome the challenge that lies ahead?"
    $l_exp = "surprised"
    show richard down glare at middle
    show screen laura
    with dissolve
    pause 0.1
    "He was about to approach the final ramp."
    show richard concerned
    "And was rightfully confused."
    $l_exp = "concerned"
    "The ramp was blocked off with rubble and concrete."
    "As the camera panned around, it showed that the top of the parking garage was empty."
    "No obstacles, no REDD, nothing."
    $l_exp = "surprised"
    "That is, until he turned around."
    "There stood a long metal beam that stretched across the entire road, ending at the top of another building."
    "The top of said building housed a checkered line."
    s "Let's hope our contestant has a good sense of balance; he's gonna need it if he doesn't want to be a human pancake!"
    show richard crossed
    "Taking a deep breath, Richard approached the beam."
    "It looked about a foot in width, so he at least should have some decent walking room."
    $l_exp = "sad"
    "But we're talking about 50 feet in length."
    $l_exp = "surprised"
    "I guess it's not the longest distance in the world, but when you're around a hundred or so feet in the air..."
    show richard down glare
    "Nevertheless, Richard took one last deep breath before stepping onto the beam."
    $l_exp = "sad"
    "Come on, babe! You can do this!"
    hide richard
    hide screen laura
    with dissolve
    pause 0.1
    nvl clear
    $nvl = True
    nvl show dissolve
    narrate """
    Richard held his hands out to his side and slowly inched across.

    It didn't look fastened down on either end, so any quick and sudden movements might shift it and cause him to fall.

    I shouldn't have expected anything else from the REDD.

    Fortunately, since he doesn't have a time limit, he can take his time getting across.

    Actually, now that I think about it, why is it called {i}Wild, Wild Races{/i} if it's not a race?

    Gah! Stay focused, Laura!

    {clear}

    After what felt like 5 minutes, Richard was about halfway across.

    Sweat was dripping down his face, but his determined look never left.

    What was going through his mind at that moment, I wonder?

    Was he scared of the potential dangers?

    Was he relieved that he was almost done?

    Honestly, it was most likely both.

    Still, he pressed on, and was doing a damn good job, as well.
    """
    nvl clear
    stop music fadeout(5.0)
    narrate """
    As he slowly inched towards the end, he looked a little more relieved.
 
    Honestly, so was I.
 
    Still, that didn't prevent me from locking my eyes to the screen, holding my breath as Richard moved closer and closer.
    """
    play sound heartbeat loop
    narrate """
    I could feel my heart beating hard in my chest.

    Could he actually make it?

    Could he actually finish the game?

    Please, Richard...

    Whatever you do, finish the game!
    """
    $nvl = False
    $l_exp = "shocked"
    nvl hide
    window hide
    if persistent.vibrate:
        $renpy.vibrate(1.0)
    play sound "audio/se/explosion.ogg"
    scene bg flash with explosion
    pause 0.5
    scene bg parkinggarage
    with Dissolve(2)
    show screen laura
    window show dissolve
    pause 0.1
    "What the hell??"
    "The camera then panned to a nearby building, where an explosion of fire could be seen emerging!"
    r "Ahh!!"
    show richard down shocked:
        middle
        alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            linear 0.2 xalign 0.49
            linear 0.2 xalign 0.51
            repeat
    pause 0.6
    "Richard was clearly spooked by the sudden noise, with the top half of his body moving from side to side, trying to regain balance!"
    l "Oh, God! Richard, stay calm!!"
    "I knew he couldn't hear me, but I didn't care."
    show richard concerned:
        linear 0.4 xalign 0.49
        linear 0.4 xalign 0.51
        repeat
    "After a few seconds, he was able to regain more of his balance."
    show richard:
        linear 1.0 xalign 0.5
    pause 1.5
    $l_exp = "smile"
    show richard smile
    "A huge sigh of relief came out of him, as well as myself."
    "He then continued to walk forward."
    s "Oh, my! What a beautiful recovery from our contestant!"
    s "And before anyone asks: no, that explosion was not planned by us; I honestly have no idea why that happened."
    "{color=d00000}Mr. Sprinkles{/color}" "\"But I must say that it made for quite an unexpected{nw}"
    play sound smack
    show richard shocked:
        ease 0.25 yalign -2.0
    $l_exp = "shocked"
    r "{b}AAAAHHHHH!!!{/b}"
    l "{b}{i}RICHARD!!!{/i}{/b}"
    "Out of nowhere, the beam under him started falling, with him having no choice but to go down with it!!"
    s "Oh, my goodness!!"
    scene bg fade with dissolve
    pause 0.1
    "Richard's screams could be heard loudly as he plummeted down below, the camera being careful to stay focused on him at all times."
    "All I could do was stare in shock as he fell for what felt like forever, his screams only stopping when..."
    $l_exp = "crying"
    $quickhide = True
    hide screen laura
    window hide
    show richard down shocked:
        size(562, 1125)
        rotate 90
        xalign 0.5 yalign 1.5
        linear 0.15 yalign -0.25
    pause 0.15
    show blood3
    play sound impact
    $renpy.vibrate(1.5)
    $renpy.pause(delay=3)
    window show
    show screen laura
    l "{b}AAAAAAAAAAHHHHHHHHHHH!!!!!{/b}"
    "I let out a blood-curdling scream as tears poured out of my eyes!"
    scene bg fade with dissolve
    pause 0.1
    "I covered my face and continued to scream, my whole body trembling!"
    "My screams then quickly turned into sobs as I collapsed to the floor."
    l "I'm so sorry, Richard!!"
    l "That should have been me!!"
    l "{b}WHY COULDN'T IT HAVE BEEN ME?!?!{/b}"
    "I continued to cry and scream, barely hearing Mr. Sprinkles saying they were about to take a break."
    l "...I'm sorry..."
    "I managed to choke out in a whisper."
    hide screen laura
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    I continued to lie there with tears coming out, my cries becoming quieter and quieter.

    A few of the other adults tried to comfort me, but there was nothing they could do to bring him back.

    Richard's gone.

    Forever.

    All because of this fucking unending nightmare.

    My husband is dead.

    The father of my children is dead.

    !!!

    {nw}

    My children!!

    {clear}

    Kate and Dakota were down there at the parking garage!!

    How much of that did they see??

    Did they see him fall??

    Did they see him land??

    What's going to happen to them now??

    ...
    """
    $nvl = False
    nvl hide
    with dissolve
    pause 0.1
    r "Just stay alive for them, Laura! Please!"
    show richard down concerned at middle
    with Dissolve(1.0)
    pause 0.5
    r concerned "I love you! Just stay alive!!"
    window hide
    pause 1.0
    hide richard
    with Dissolve(2.0)
    pause 1.0
    window show dissolve
    pause 0.5
    "I will, Richard."
    "I will."
    call sceneend from _call_sceneend_11
    if not persistent.scenes["ch3_s7"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s7"] = True


label jessicaseye:
    python:
        currenttime = "12:00 AM"
        timeleft = "7 hours"
        currentdate = "April 1st"
        quickhide = False
    call chapterstart from _call_chapterstart_12
    pause 2
    play music sprinkles_theme
    scene bg stage
    show sprinkles happy hat cane at middle_sprinkles
    with Dissolve(2.0)
    window show dissolve
    pause 0.1
    s "Ahahaha~! Looks like the midnight hour is upon us now, everyone!"
    s jeer "While not halfway through our show just yet, we're certainly getting far enough along to where we're going to be getting to the more fun activities~"
    s @ laugh "That said, it's time for another 15 minute break!"
    s "Hopefully, we'll have no issues this time..."
    stop music fadeout(3.0)
    scene bg livestage_open
    with Dissolve(1.0)
    pause 1.0
    show dakota sad hips at two1
    show kate alert fidget at two2
    with Dissolve(1.0)
    pause 0.1
    d "..."
    k "..."
    d small_smile "C-Come on, Kate. Let's go to the restroom."
    k "I don't have to go."
    d sad "I don't know when the next time we'll be able to go will be, Kate. Come on."
    k mad "I don't have to go."
    d mad side "Kate, come on!"
    "Dakota then grabbed her sister's arm and tried pulling her out of her seat, a task Kate wasn't making easy to do."
    d "Kate, I'm not gonna tell you again!"
    k down "You're not Mommy! I don't have to listen to you!"
    d hips "Mom told me to take care of you while she and Dad were gone, so yes, you do!"
    k "But she's not gonna come back, just like Daddy!"
    d sad "That's not true, Kate!"
    k "I'm never gonna see Mommy again! She's gonna go away because of the games, just like Daddy did!!"
    d side "You don't know that, Kate!"
    k alert fidget "Yes, I do!"
    "She then curled up in her seat and hid her face."
    d "Kate, look..."
    k mad "Shut up! You hate me, anyway!"
    d mad crossed "No, I don't!!"
    k "You wished I wasn't born! That means you hate me!!"
    d "{b}NO, IT DOESN'T, YOU IDIOT!!{/b}"
    k "{b}I'M NOT AN IDIOT!!{/b}"
    d sad "..."
    "Dakota then sat back down in her own seat, trying to stop herself from crying."
    "But no matter what she tried to think about, she couldn't get those sounds out of her mind."
    $renpy.music.set_volume(0.25, channel="sound")
    play sound "audio/se/explosion.ogg"
    "The explosion..."
    "Her dad's screams..."
    play sound impact
    "The slam that came when he hit the ground..."
    "It felt like a bad dream."
    "It still feels like a bad dream."
    "She then closed her eyes tightly and started crying, even though it felt like she didn't have any more tears to cry."
    stop sound
    $renpy.music.set_volume(1.0, channel="sound")
    play music vast_places
    d bawl side "You're right, Kate. You're not an idiot. {b}I{/b} am."
    d "I can't protect us from what's happening."
    d "It's because of me that we were out there and saw what happened to Dad."
    d crossed "I'm sorry I can't do what Mom asked me to do."
    d "I'm sorry that I'm a terrible sister."
    d "And I'm really sorry that I wished you weren't born."
    k alert "..."
    "Kate continued to stay in her little ball, unresponsive to her sister's apologies."
    d "..."
    "Part of Dakota believes that Kate will forgive her after a while, but..."
    "...after all the crazy things that happened, who knows how she'll behave once this is all over?"
    "Dakota then just sighed and wiped her eyes."
    d side "I just want to see Mom again..."
    d "I wanna hug her and tell her that I love her..."
    "She didn't really know who she was saying it to. She just wanted to get it out there."
    "Maybe if she said it out loud, it would come true. Like a backwards birthday wish."
    "..."
    stop music fadeout(3.0)
    window hide
    pause 1.0
    scene bg stage
    show sprinkles cane rightdown jeer at middle_sprinkles
    with Fade(1.0, 0.5, 1.0)
    pause 0.1
    window show dissolve
    pause 0.1
    s "Welcome back, everyone~"
    s laugh hat "Fortunately, everything is proceeding as planned, which is good for everyone!"
    s @ evilgrin "Well, maybe not {b}everyone{/b}...~"
    s "Which segways nicely back to our guest, Mrs. Jessica Tate!"
    show sprinkles at two1 zorder 3 with easeinright
    show jessica bothknees left_tears zorder 2:
        zoom 0.6
        xalign 1.75
        ease 1.5 two2_jessica
    pause 1.6
    play music sprinkles_spooky
    s happy rightdown "Welcome back to the stage, Jessica!"
    s "How are you enjoying your evening so far?"
    j "..."
    s laugh "Great to hear~!"
    play sound snap
    pause 1.0
    show jingle down smile zorder 4:
        two1
        xalign -0.6
        ease 0.5 xalign 0.0
    pause 1.0
    hide jingle with easeoutleft
    pause 0.1
    s happy leftdown "Now, Jessica, do you know what this is in my hand?"
    j tears "..."
    s laugh "That's right: a power drill!"
    play sound snap
    pause 1.0
    show jangle down smile:
        two2
        xalign 1.6
        zoom 0.75
        ease 0.5 xalign 1.0
    pause 1.1
    scene bg stage_blur
    show cg jessicatorture1
    with dissolve
    pause 0.1
    s "You've seen a lot of rough things tonight, haven't you, Jessica?"
    s "Lots of blood, violence, death..."
    s "Why don't you let me help you with that?"
    $renpy.music.set_volume(0.25, channel="ambience")
    play ambience saw
    pause 1.0
    s "Stay still, Jessica; you might lose more than intended if you don't!"
    window hide
    $renpy.music.set_volume(0.5, delay=1.0, channel="music")
    pause 2.0
    if persistent.vibrate:
        $renpy.vibrate(2.0)
    $renpy.music.set_volume(1.0, delay=0.5, channel="ambience")
    play sound2 "audio/voice/jessica_eyeball.ogg"
    play sound blood loop
    show cg jessicatorture2
    with Dissolve(0.25)
    pause 2
    show blood4 zorder 3
    pause 0.25
    show blood zorder 3
    pause 1.5
    show blood2 zorder 3
    pause 2.25
    stop sound
    stop sound2
    stop ambience
    $renpy.music.set_volume(1.0, delay=1.0, channel="music")
    pause 0.5
    scene bg stage
    show sprinkles leftdown hat laugh at two1 zorder 2
    show jessica bothknees blank at two2_jessica zorder 2
    show jangle down happy_grin zorder 1:
        two2
        xalign 1.0
    with dissolve
    window show dissolve
    pause 0.1
    s "There! Now you'll only see {i}{b}half{/b}{/i} the rough things!!"
    s "Ahahahaha!!!"
    s happy "Alright, folks. After we get cleaned up, we'll get ready for another game~!"
    s jeer "And I assure you, it's only going to get better from here."
    call sceneend from _call_sceneend_12
    if not persistent.scenes["ch3_s8"]:
        $persistent.scenelist.append(1)
        $persistent.scenes["ch3_s8"] = True
    jump chapter_4
