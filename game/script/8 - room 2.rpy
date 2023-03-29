default room2 = {"solved":[], "investigated":[], "blueprints":0, "post-its":0, "limbs":0, "corkboard":0, "clippings":0, "panopticon":0, "recalibration":0, "evidence":0, "word":0,
    "notes":[]}

screen room2():
    sensitive not inspect
    layer "master"
    tag room

    fixed at zoomed(0.34):
        add "bg room2"
        imagebutton idle Null(940, 805) action [SetVariable("inspect", "corkboard"), Jump("room_2")] pos (4800, 1085) mouse "inspect"
        imagebutton idle Null() action [SetVariable("inspect", "blueprints"), Jump("room_2")] focus_mask Image("rooms/room2_blueprints_mask.png") pos (0, 1175) mouse "inspect"
        imagebutton idle Null() action [SetVariable("inspect", "clippings"), Jump("room_2")] focus_mask Image("rooms/room2_clippings_mask.png") pos (2811, 1235) mouse "inspect"
        imagebutton idle Null() action [SetVariable("inspect", "limbs"), Jump("room_2")] focus_mask Image("rooms/room2_limbs_mask.png") pos (0, 2766) mouse "inspect"
        imagebutton idle Null(300,565) action [SetVariable("inspect", "post-its"), Jump("room_2")] pos (3460, 1285) mouse "inspect"

        imagebutton idle Null() action [SetVariable("inspect", "word"), Jump("room_2")] focus_mask Image("rooms/room2_word_mask.png") pos (3790, 1070) mouse "puzzle"
        imagebutton idle Null() action [SetVariable("inspect", "panopticon"), Jump("room_2")] focus_mask Image("rooms/room2_panopticon_mask.png") pos (4109, 1941) mouse "puzzle"
        imagebutton idle Null(1563, 620) action [SetVariable("inspect", "evidence"), Jump("room_2")] pos (1175, 1194) mouse "puzzle"
        imagebutton idle Null() action [SetVariable("inspect", "recalibration"), Jump("room_2")] focus_mask Image("rooms/room2_recalibration_mask.png") pos (0, 2058) mouse "puzzle"

        if 1 not in room2["notes"]:
            imagebutton idle "rooms/room2_note1.png" action [SetVariable("inspect", "note1"), Jump("room_2")] pos (160, 1484) mouse "inspect"
        if 2 not in room2["notes"]:
            imagebutton idle "rooms/room2_note2.png" action [SetVariable("inspect", "note2"), Jump("room_2")] pos (1417, 1767) mouse "inspect"
        if 3 not in room2["notes"]:
            imagebutton idle "rooms/room2_note3.png" action [SetVariable("inspect", "note3"), Jump("room_2")] pos (3870, 2217) mouse "inspect"
        
    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_2")] style "main_menu_button"

label room_2:
    if inspect not in room2["investigated"] and inspect in ["blueprints", "limbs", "clippings", "post-its", "corkboard"]:
        $room2["investigated"].append(inspect)
    show screen room2
    hide screen room2_panopticon

    if inspect == "note1":
        #TODO flavor text for note on the wall
        $room2["notes"].append(1)
    elif inspect == "note2":
        #TODO flavor text for note on the blackboard
        $room2["notes"].append(2)
    elif inspect == "note3":
        #TODO flavor text for note on the desk
        $room2["notes"].append(3)

    elif inspect == "blueprints":
        if room2["blueprints"] == 0:
            show room2_blueprintcollection with dissolve:
                yalign 0.2 xalign 0.5
            "(You survey the diagrams before you.)"
            "(From a distance,{w=0.1} they seem to be your average blueprints.{w} Blueprints for weapons of all makes,{w=0.1} shapes{w=0.1} and sizes.)"
            "(But on closer inspection,{w=0.1} they reveal a certain {i}quirkiness{/i} that doesn't belong on a technical document.{w} The handwriting is also... {w=0.5}{i}distinct,{/i}{w=0.1} for lack of a better word.)"
            "(That said,{w=0.1} poor penmanship hasn't dulled the designs themselves.{w} The {i}least{/i} dangerous of these would be devastating out in the field.)"
            "(The oldest of the blueprints -{w=0.1} the ones hidden at the bottom of the pile,{w=0.1} look wildly different.{w} Clearly,{w=0.1} another person authored them.)"
            "(In fact,{w=0.1} if you squint...{w=0.5} you can still find the signatures at the bottom.)"
            "(\"Destrange,\"{w=0.1} they say.{w} They're dated more than 15 years ago.)"
            hide room2_blueprintcollection with dissolve
        else:
            show room2_blueprintcollection with dissolve:
                yalign 0.2 xalign 0.5
            "(Blueprints for a variety of dangerous weapons. {w}Honestly,{w=0.1} they're pretty scary.)"
            hide room2_blueprintcollection with dissolve
            pass
        $ room2["blueprints"] += 1

    elif inspect == "post-its":
        if room2["post-its"] == 0:
            show room2_postitnotes with dissolve:
                yalign 0.2 xalign 0.5
            "(You eye over the mass of scrawled notes pinned in front of you.{w} There're two distinct handwritings here,{w=0.1} but the contents are mostly the same{w=0.5} - and mostly {i}domestic{/i}.) "
            "(Notes on what to eat for breakfast and when to start preparing it.{w} Notes on how much sleep to get and...{w=0.5} what {i}stories{/i} to read?)"
            "(Birthdays,{w=0.1} exercises,{w=0.1} meal plans{w=0.1} and {i}chores?{/i})"
            "(Whoever left these notes for each other weren't just sharing the same space.\n{w}They were {i}living{/i} together.)"
            hide room2_postitnotes with dissolve
        else:
            show room2_postitnotes with dissolve:
                yalign 0.2 xalign 0.5
            "(A wall of scrawled notes. {w}And they all talk about...{w=0.5} domestic tasks?)"
            hide room2_postitnotes with dissolve
            pass
        $ room2["post-its"] += 1

    elif inspect == "limbs":
        if room2["limbs"] == 0:
            show room2_limbsdesigns with dissolve:
                yalign 0.2 xalign 0.5
            "(These documents appear to be designs for cybernetic limbs like the ones produced by STOP -{w=0.5} at first glance.)"
            "(On closer inspection,{w=0.1} there are more differences than there are similarities.) "
            "(STOP's technology is more generalized,{w=0.1} more efficient...{w=0.5} and {i}angular.{/i})"
            "(These plans are heavily customized.{w} They could've only been suitable for a very small number of subjects -{w=-0.5} possibly as few as {i}one.{/i})"
            "(Perhaps Dr. Danger based it off stolen data?{w} You make a note to tell your superiors about possible reverse-engineering.)"
            hide room2_limbsdesigns with dissolve
        else:
            show room2_limbsdesigns with dissolve:
                yalign 0.2 xalign 0.5
            "(Designs for cybernetic limbs.{w} They're pretty similar to the ones produced by STOP...)"
            hide room2_limbsdesigns with dissolve
            pass
        $ room2["limbs"] += 1

    elif inspect == "corkboard":
        if room2["corkboard"] == 0:
            show room2_evidenceboard with dissolve:
                yalign 0.2 xalign 0.5
            "(As you look over the sprawling web of photos,{w=0.1} documents,{w=0.1} and diagrams,{w=0.1} you realize everything in front of you is perfectly orderly.)"
            "(These are the notes of a hunter,{w=0.1} and STOP was their prey.)"
            "(You recognize dozens of names,{w=0.1} operations,{w=0.1} and places;{w=0.5} vital parts of STOP's organization that had suffered heavy blows in the last few years.)"
            "(But you're disturbed by how many places you {i}don't{/i} recognize.)"
            "(Laboratories,{w=0.1} factories{w=0.1} and armories that must be high above your clearance level –{w=0.5} crossed out like someone was just going down a checklist.)"
            "(All these top-secret sites share the same acronym:{w=0.5} \"YTDI.\")"
            "(...No,{w=0.1} you {i}don't{/i} recognize it.)"
            hide room2_evidenceboard with dissolve
            "(That's par for the course with STOP.{w} If you don't know what an acronym means,{w=0.1} it's probably above your paygrade.)"
        else:
            show room2_evidenceboard with dissolve:
                yalign 0.2 xalign 0.5
            "(A sprawling web of photos,{w=0.1} documents{w=0.1}  and diagrams. {w}And they're all related to STOP...)"
            hide room2_evidenceboard with dissolve
            pass
        $ room2["corkboard"] += 1

    elif inspect == "clippings":
        if room2["clippings"] == 0:
            show room2_news with dissolve:
                yalign 0.2 xalign 0.5
            "(Printouts and clippings of various news articles -{w=0.1} all related to Dr. Danger's exploits...{w=0.5} with a {i}certain{/i} colorful sidekick occasionally breaking into the opening paragraphs.)"
            "(In fact,{w=0.1} when you look at them all together,{w=0.1} Cautionne seems to show up more over time.{w} Dr. Danger must've been pleased with her pupil's growth.)"
            "(At the bottom of the pile,{w=0.1} a heavily weathered photo peeks out.)"
            "(Based on what you can make out of the caption - {w=0.1}it seems to be of some kind of commemorative occasion.)" 
            "(\"__rdre Des__ge, et al. celebr_e breakthr__ in cyb_netics, sec_ity\".)"
            "(You can't recognize any of the faces,{w=0.1} but you do recognize the logo as-{w=0.3}{nw})"
            hide room2_news with dissolve
            pause 1
            #"{b}[pause as the clippings disappear]{/b}"
            "(...Never mind.{w} It's just similar,{w=0.1} that's all.)"
        else:
            show room2_news with dissolve:
                yalign 0.2 xalign 0.5
            "Newspaper printouts and clippings. {w}They all feature Dr. Danger...{w=0.5} as well as a {i}certain{/i} colorful sidekick."
            hide room2_news with dissolve
            pass
        $ room2["clippings"] += 1

    elif inspect == "panopticon":
        if "panopticon" in room2["solved"]:
            "(You've already solved the panopticon puzzle.)"
        else:
            if room2["panopticon"] == 0:
                #panopticon introduction
                pass
            else:
                #repeated investigation
                pass
            show screen room2_panopticon with easeintop
            $ room2["panopticon"] += 1
            $ inspect = None
            call screen room2_panopticon 
            if room2["panopticon"] == "solved":
                jump panopticon_solved

    elif inspect == "evidence":
        if "evidence" in room2["solved"]:
            "(You've already solved the evidence board puzzle.)"
        else:
            if room2["evidence"] == 0:
                #evidence introduction
                pass
            else:
                #evidence investigation
                pass
            $ room2["evidence"] += 1
            $ inspect = None

    elif inspect == "recalibration":
        if "recalibration" in room2["solved"]:
            "(You've already solved the recalibration puzzle.)"
        else:
            call init_cybernetics from _call_init_cybernetics
            if room2["recalibration"] == 0:
                "<TODO: Insert intro script and rules.>"
                pass
            else:
                #repeated investigation
                pass
            show screen cybernetics(cyb) with easeintop
            $ room2["recalibration"] += 1
            $ inspect = None
            call screen cybernetics(cyb)

    elif inspect == "word":
        if room2["word"] == 0:
            #word introduction
            pass
        else:
            #repeated investigation
            pass
        show screen room2_word with easeintop
        $ room2["word"] += 1
        $ inspect = None
        call screen room2_word
        if room2["word"] == "solved":
            jump post_room_2

    $ inspect = None
    call screen room2

label panopticon_solved:
    $ inspect = "panopticon"
    show screen room2_panopticon
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room2["solved"].append("panopticon")
    #Show a note/picture/memento which will then show up on 
    "(Congratulations! {w}You solved the panopticon puzzle.)"
    hide black onlayer screens
    hide screen room2_panopticon
    with dissolve
    $ inspect = None
    call screen room2

label panopticon_game_over:
    $ inspect = "game over"
    show screen room2_panopticon
    show black onlayer screens with dissolve:
        alpha 0.5
    "(You re-arrange another set of cells and-)"
    "(-and suddenly, your controls freeze up.{w} There's a notification in the corner.)"
    hide black onlayer screens
    hide screen room2_panopticon
    with easeouttop
    cr "Seems like you've run out of time,{w=0.1} lab rat."
    cr "That's it.{w=0.5} The jailbreak is broken.{w=0.5} You screwed up."
    "(So it {i}was {/i}a prison?{w} Then-)"
    cr "If it was just between you and me,{w=0.1} I'd be \"whatever\" about it."
    cr "We all make mistakes,{w=0.1} y'know?{w=0.5} So,{w=0.1} I'm super forgiving and cool and mature about this kind of thing."
    cr "...But you just lost those kids a chance to get out before the {i}operations{/i} start."
    "(...Sorry,{w=0.1} {i}operations?{/i})"
    cr "They could've gotten out clean.{w=0.5} Now I'll have to step in and bust them out \n{i}dirty{/i}."
    cr "And it's all because of {i}you.{/i}"
    cr "Now,{w=0.1} go sit in the corner and think about what you've done!" with small_shake
    #"{b}SFX LARGE SWITCH FLIPPING, CUT TO BLACK{/b}"
    scene black 
    pause 1
    cr "I'll come back for you when you're sorry enough."

    nvl clear
    pause 3
    $nvl_heading = "Lab Report #893"
    l "Subject expired after 3 days due to lack of water, light, food, and mental stimulation."
    l "Scratched their nails bloody on the exit door before losing consciousness, so I'll have to clean {i}that{/i} mess up."
    l "{b}Contributing Factors to Death:{/b} Didn't take the consequences of imprisonment very seriously."
    $deadend(achievement_dead8)
    le "DEAD END 08: A Taste of Sobering Punishment."
    nvl clear
    return

label recalibration_game_over:
    $ inspect = "game over"
    show screen cybernetics(cyb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    "(You confirm your choice,{w=0.1} and a beeping starts.)"
    "(It's tone sets the hairs on the back of your neck on edge.)"
    cr "You're losing 'em,{w=0.1} Doc."
    "(...Wait.{w} This is an actual {i}person?{/i})"
    hide black onlayer screens
    hide screen cybernetics 
    with easeouttop
    cr "As they are now,{w=0.1} they can't be re-stabilized.{w=0.5} Their own nervous system will rip them apart with spasming."
    cr "...But they shouldn't be punished for {i}your{/i} mistake,{w=0.1} right?"
    "(...Well,{w=0.1} uh-){p=0.3}{nw}"
    cr "Don't worry,{w=0.1} I can fix this."
    cr "But I'm gonna need a hand."
    show bg room2 at dizzy with dissolve:
        parallel:
            yalign 0.0 xalign 0.0 zoom 0.34
    "{cps=30}(Suddenly,{w=0.1} your body feels a lot heavier.{w}{/cps} {cps=20}Is that mist in the corner of the room?){/cps}"
    cr "...And a liver.{w=0.5} And a stomach.{w=0.5} And a heart.{w=0.5} And most of your spinal cord."
    pause 1
    cr "And I'm gonna need them {i}right now.{/i}"
    scene black with small_shake
    #"{i}{b}COLLAPSE SFX{/b}"
    nvl clear
    pause 3
    $nvl_heading = "Lab Report #062"
    l "Patient was eventually re-stabilized and should wake up within the next few days."
    l "On the other hand, the lab rat won't get up ever again. Seems like they're missing a few too many critical parts."
    l "{b}Contributing Factors to Death:{/b} They gave too much of themselves to my cause."

    $deadend(achievement_dead9)
    le "DEAD END 09: Didn't Make The Cut."
    nvl clear
    return
    
label word_game_over:
    $ inspect = "game over"
    show screen room2_word
    show black onlayer screens with dissolve:
        alpha 0.5
    # [error sound effect]
    $ random_choice = random.randint(1,5)
    if random_choice == 1:
        cr "Holy crap! Did you just manage to guess that right on your first try?"
        "(Huh? Really?)"
        cr "{i}Kidding!{/i}"
        "(You-)"
        cr "God, lighten up. Here, let me help!"
        #"{b}ZAP SFX, CUT TO BLACK{/b}"

    elif random_choice == 2:
        cr "Whoa... You got it."
        cr "...Are you looking up a walkthrough our something?"
        "(You-)"
        cr "If so, go back and complain in the comments. "
        cr "They led you to a dead end!"
        #"{b}SMASH SFX, CUT TO BLACK{/b}"

    elif random_choice == 3:
        cr "You're a fast one, aren't you?"
        "(Huh? What do you-)"
        cr "But next time, {i}do {/i}look before you leap."
        #"{b}TRAP DOOR SFX, CUT TO BLACK{/b}"

    elif random_choice == 4:
        cr "I see you're the type who likes to gamble."
        cr "Alas, you didn't hit the jackpot. Better luck next time!"
        "(You-)"
        cr "But since you're here, I've got another game for you to play."
        cr "Place your bet, lab rat! Is the gun next to you loaded or unloaded?"
        "(What gu-)"
        #"{b}GUNSHOT SFX, CUT TO BLACK{/b}"

    else:
        cr "...Wow. That wasn't even {i}close. {/i}"
        cr "You'd have better luck just smashing keys."
        "(You-)"
        cr "Like.{i} {/i}{i}So{/i}{i}.{/i}"
        #"{b}SMASHING SFX, CUT TO BLACK{/b}"

    $deadend(achievement_dead6)
    le "DEAD END 06: <NAME>."
    nvl clear
    return
   

#label room2_deaths:
#    "{u}{b}Death Scenes{/b}{/u}"
#
#    "Puzzle 1" "This is the evidence board puzzle. I wanted to touch base with the writers to see what kind of scenario could fit here, and then it seems like the dead end would depend on that, so any ideas? I can come up with the hints and clues, but it seems like it oculd be a good exposition oppertunity so I wanted to ask writers about it. "
#
#    "Puzzle 1 Death Scene" "{b}{/b}
#    (You carefully insert one more pin into the board, which leaves-)
#    Whoa, you {i}suck {/i}at this!
#    (Something about his unusually straightforward insult puts ice into your veins.)
#    It's like you're solving this puzzle with your eyes closed and your nose plugged.
#    ...There some reason you don't want to look at the truth in front of you, lab rat?
#    (...No, no, it's just-)
#    I know you're not taking this seriously. Maybe we should just move on?
#    You know what? Yeah. 
#    {i}Let's put a pin in it.{/i}
#    {i}{b}PIERCING SFX, CUT TO BLACK.{/b}{/i}"

#    "Lab Report #273" "{b}{/b}{i}Subject experienced permanent loss-of-life after one of the facility's reconfigurable nano-stakes jetted out of the floor and impaled them to the ceiling. {/i}"

#    "{i}Guess they were worth the trouble of installation!{/i}"

#    "Contributing Factors to Death" "{i}{b}{/b}{/i}{i}Couldn't put progress on the board.{/i}"