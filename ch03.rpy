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
    # She's strapped to a chair, her arms and legs tied to the chair's arms and legs and her head tied across her forehead so she's looking forward. She's also had her mouth gagged.
    pause 2
    $l_exp = "sad"
    show screen laura
    with dissolve
    "Oh, my God!"
    "She looked just as terrified as the rest of us, but given her current situation, I'm sure she's even more so."
    hide screen laura
    with dissolve
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
    s "So, tonight, I brought Jessica onto the show to teach her, as well as all of you, an important lesson:"
    s "While it's okay to dislike someone for a reason only you can understand..."
    s hm "...it's never okay to use that disliking to harm that person. If you do..."
    s evilgrin "...you might just have some very bad things happen to you in return."
    stop music fadeout(5)
    s laugh "Here, Jessica. Why don't we show the folks at home what I mean?"
    "Jessica then started giving some screams through her gag, and her eyes started darting side to side, almost as if she were trying to shake her head."
    s happy "Don't worry. I won't be too harsh."
    s evilgrin "...yet."
    "On cue, Jingle skipped onto the stage and handed Mr. Sprinkles an aluminum baseball bat."
    "After he accepted the gift, she gave a small curtsy and skipped back off."
    $l_exp = "concerned"
    show screen laura
    with dissolve
    pause 0.1
    "...so, Jingle and presumably Jangle are in on this?"
    $l_exp = "neutral"
    "I mean, they're REDD, as well, so I guess I shouldn't be too surprised, given the circumstances..."
    hide screen laura
    with dissolve
    pause 0.1
    s hm "Now, Jessica, despite everything that's happened tonight, I'm not going to lie to you."
    s "What's about to happen right now..."
    s evilgrin "...is gonna hurt a lot."
    "He then wound up the bat..."
    play sound smack
    "And smacked Jessica right in the face with it!"
    "She cried out in pain, but her gag muffled the noise."
    play sound smack
    "He smacked her again, only this time, seemingly harder."
    "His sinister grin never left his face while he did."
    play sound children_screaming fadein(5)
    "The screaming children certainly didn't help lighten the atmosphere."
    $l_exp = "surprised"
    show screen laura
    with dissolve
    pause 0.1
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
    hide screen laura
    with dissolve
    show sprinkles laugh
    "After a few more swings, Mr. Sprinkles dropped and bat and cackled like a madman."
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
    show trosh at middle with dissolve
    pause 0.1
    t "Alright! You and you are coming with me!"
    "He then pointed to a man and woman near the front of the pile."
    man "Wha-"
    t "{b}Now!{/b}"
    woman "B-But he hasn't even picked the game yet!"
    t "Ahahaha!!"
    t "You really think the games are selected at random?"
    t "Grow up."
    t "Now {b}move!!{/b}"
    "Given no other option, the two exited the room with the REDD keeping his weapon pointed at them at all times."
    hide trosh with dissolve
    pause 0.1
    "After the door was closed, the guard REDD got back into position."
    hide screen laura
    with dissolve
    $nvl = True
    nvl clear
    nvl show dissolve
    narrate """
    As I leaned against the wall and tried to calm myself down, I couldn't help but think about the best-case scenario.

    Richard and I are pretty far back in the room, so the odds of us getting picked seem significantly lower by default.

    I mean, I know we're talking about 12 hours, but even on TV, some games last a lot longer than others.

    And even if we get picked for the game, there's a chance we could still win and survive.

    I mean, really, how lethal could these games really be?

    And assuming he's telling the truth, we'll stay alive after we win, and that's that.

    {clear}

    I know it probably won't be that simple.

    But if I want to have any chance at making through this night, I need to have positivity, even when none seems to exist.

    I mean, surely that's the way to go, right...?
    """
    $nvl = False
    nvl hide
    $l_exp = "concerned"
    show screen laura
    with dissolve
    pause 0.1
    "Mr. Sprinkles then approached the Wacky Dartboard after hitting one of the squares."
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg stage
    show sprinkles happy at middle_s
    with dissolve
    pause 0.1
    s "And our first game of the evening is..."
    s laugh "{i}Hot Quiz!{/i}"
    show game_name "Hot Quiz" at game_name_flash
    s "Ahahaha!"
    s happy "Now, what do you say we get the ball rolling right away and bring out our contestants?"
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
    with dissolve
    pause 0.1
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
    show sprinkles laugh at middle_s
    with dissolve
    pause 0.1
    s "Let's start the game!"
    s jeer "Good luck, you two~"
    stop music fadeout(3)
    "He then stood between the two chairs, albeit a bit of a distance back from them."
    "We were then greeted to two camera angles at once, one for each contestant."
    s laugh "Alright! Let's decide who will be 'it' first!"
    "Suddenly a red light bulb on top of each of the chairs alternated rapidly for a few seconds before slowing down."
    "Finally, it stopped right on top of the man."
    s happy "Oh, goody! You you get to answer the question first, Sir!"
    s "Put 60 seconds on the clock, please!"
    s laugh "And let's begin~!"
    play music ice_cream_truck
    s happy "Who was the 16th president of the United States?"
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
    s laugh "Correct!"
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
    show richard concerned at middle_r with dissolve
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
    show sprinkles jeer at middle_s
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
    s @ laugh "Oh, my! A minute certainly does fly by, doesn't it?"
    s "Congratulations, Miss! You won!"
    s jeer "As for you, Sir..."
    s evilgrin "Thank you for playing."
    play sound shotgun
    show white zorder 4
    if persistent.gore:
        show blood zorder 3
    pause 0.1
    hide white
    play sound2 children_screaming fadein(1)
    pause 1
    show screen laura
    with dissolve
    pause 0.1
    "Everyone screamed as the man's head seemed to explode out of nowhere!"
    "The camera then panned to a REDD guard pointing a shotgun in the general direction."
    "Meanwhile, the blood-and-gut covered woman covered her mouth in horror as she started bawling."
    $l_exp = "surprised"
    "I know she has to be believing that this is her fault."
    "I can't even imagine the amount of guilt going through her head."
    play music sprinkles_theme
    s laugh "Now that's what I call an exciting beginning to an exciting evening~!"
    s happy "Ma'am, for winning, you earn your freedom!"
    "Jangle then entered the stage and unhooked her from the chair."
    s jeer "You are free to exit the stage and return to where you were seated at the beginning of the night."
    $l_exp = "concerned"
    "The woman was hesitant and looked around to see if there were any indications that this was a trap."
    s laugh "I'm serious~! You can return to your seat!"
    $l_exp = "neutral"
    "She then slowly but surely got out of her seat and made her way to the edge of the stage and dropped down."
    hide sprinkles
    show bg livestage
    with dissolve
    pause 0.1
    "Once on the ground, she picked up the pace and ran towards the back of the room."
    $l_exp = "sad"
    "The guards by the doors raised their weapons, but they hesitated when a loud 'Mommy!!' could be heard nearby."
    $l_exp = "surprised"
    "Sure enough, the woman ran towards the child and hugged him tightly, sobbing loudly as she did."
    show bg stage
    show sprinkles jeer at middle_s
    with dissolve
    pause 0.1
    s "Aw, how adorable!"
    s laugh "Anyway, what do you say we take ourselves a quick break to prepare for the next game?"
    stop music fadeout(5)
    scene bg storage
    show richard concerned at middle_r
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
    "I took out my phone looked at the screen."
    $l_exp = "sad"
    "It was a text from Dakota!"
    play music vast_places
    dt "Mom r u ok"
    $l_exp = "excited"
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
    hide screen laura
    hide richard
    with dissolve
    window hide dissolve
    pause 1.0
    stop music fadeout(3.0)
    scene bg fade
    with Dissolve(2.0)
    pause 4
    $renpy.end_replay()
    $persistent.chapter3_scene1 = True


label girlsescape:
    python:
        currenttime = "7:43 PM"
        timeleft = "11 hours and 17 minutes"
    call chapterstart
    pause 2
    play music sprinkles_spooky
    scene bg livestage
    with Dissolve(2.0)
    pause 0.5
    window show dissolve
