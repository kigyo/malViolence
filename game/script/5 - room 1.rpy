default room1 = {"investigated":[], "solved":[], "oil":0, "chair":0, "megaphone":0, "marble":0, "hacking":0, "decanting":0, "bomb":0}

define hacking_description = _("""Using the given list of codes, break into the system, but be careful! Codes are only half the hack. They need to be used at the correct time and place otherwise you may end up locking yourself out of the system.

Use the mouse or keybaord to clear out codes as you see them in the system, but be aware of how clearing out codes rearranges the system and changes what codes will be available for you afterwards.

ALL the codes must be used to fully clear the fire wall and sucessfully break into the system.
    
Codes are unodered, so long as the three individual components are the same, the codes count as the same.""")


define decanting_description = _("""Cautionne needs your help poisoning a top STOP official, but his toxin of choice is pretty particular!

Using three vials of {color=#fff}18cc, 10cc,{/color}  and {color=#fff}7cc{/color}  - {color=#fff}measure the poison into two equal doses of 9cc.{/color} Note that {color=#fff}the 18cc vial contains the poison itself.{/color}

But be careful! {color=#fff}If the poison's disturbed too much, it'll give off nasty vapors...{/color}
    
Drag the vials in order to pour their contents into each other.""")

define bomb_description = _("")

screen room1():
    sensitive not inspect
    layer "master"
    tag room

    fixed at zoomed(0.335):
        add "bg room1"
        imagebutton idle Null() action [SetVariable("inspect", "oil"), Jump("room_1")] focus_mask Image("rooms/room1_oil_mask.png") pos (232, 2634) mouse "inspect"
        imagebutton idle Null(618, 1000) action [SetVariable("inspect", "megaphone"), Jump("room_1")] pos (2610, 1166) mouse "inspect"

        imagebutton idle Null(724, 1014) action [SetVariable("inspect", "marble"), Jump("room_1")] pos (1212, 1420) mouse "puzzle"
        imagebutton idle Null() action [SetVariable("inspect", "hacking"), Jump("room_1")] focus_mask Image("rooms/room1_hacking_mask.png") pos (3232, 1376) mouse "puzzle"
        imagebutton idle Null() action [SetVariable("inspect", "decanting"), Jump("room_1")] focus_mask Image("rooms/room1_decanting_mask.png") pos (1952, 2214) mouse "puzzle"
        imagebutton idle Null() action [SetVariable("inspect", "bomb"), Jump("room_1")] focus_mask Image("rooms/room1_bomb_mask.png") pos (68, 2160) mouse "puzzle"

        imagebutton idle Null() action [SetVariable("inspect", "chair"), Jump("room_1")] focus_mask Image("rooms/room1_chair_mask.png") pos (3682, 1519) mouse "inspect"

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_1")] style "main_menu_button"
            
label room_1:
    if inspect not in room1["investigated"] and inspect in ["oil", "chair", "megaphone"]:
        $room1["investigated"].append(inspect)
    show screen room1
    $renpy.block_rollback()
    
    if inspect == "oil":
        if room1["oil"] == 0:
            "(You approach the glistening puddle for a closer look.)"
            show room1_oil with dissolve:
                yalign 0.2 xalign 0.5
            "(The smell's pretty unambiguous,{w=0.1} but just to be sure -{w=0.1} you gingerly swipe a finger across the surface.)"
            "(Oil.{w} Most likely for some kind of machine.)"
            "(It's not unfamiliar.{w} STOP has a massive array of equipment and vehicles that need regular maintenance.)"
            "(An agent like you is expected to know how to repair and service them -{w=0.1} especially when your bosses are displeased with you.)"
            "(But it's strange to see oil out in the open here.{w} Maybe it's a spill,{w=0.1} or a leak?)"
            "(Either way,{w=0.1} something {i}clearly{/i} isn't working.)"
            hide room1_oil with dissolve
        else:
            show room1_oil with dissolve:
                yalign 0.2 xalign 0.5
            "(Oil.{w} Something clearly isn't working here.)"
            hide room1_oil with dissolve
            pass
        $ room1["oil"] += 1

    elif inspect == "chair":
        #"{b}Primary Source Extractor (Electric Chair){/b} "
        if room1["chair"] == 0:
            show room1_electricchair with dissolve:
                yalign 0.2 xalign 0.5
            "(From a comfortable distance,{w=0.1} you eye over the \"Primary Source Extractor\".{w} You approach carefully,{w=0.1} listening closely for any hints of it roaring to life.)"
            "(Agents are expected to keep their wits about them and not jump to conclusions…{w} but it's hard to see the device in front of you as anything but an electric chair.)"
            "(It looks crude and cruel,{w=0.1} like a child's re-imagining of something scary from a history book.)"
            "(That may be exactly what it is.{w} Whatever its purpose,{w=0.1} you give quiet thanks that it seems to be out of commission.)"
            hide room1_electricchair with dissolve
        else:
            show room1_electricchair with dissolve:
                yalign 0.2 xalign 0.5
            "(You're thankful this {i}horrible{/i} device is out of commission.)"
            hide room1_electricchair with dissolve
            #repeated investigation

            pass
        $ room1["chair"] += 1

    elif inspect == "megaphone":
        #"{b}Megaphone Collection {/b}"
        if room1["megaphone"] == 0:
            show room1_megaphones with dissolve:
                yalign 0.2 xalign 0.5
            "(You paused when you saw the silhouettes from across the room...{w=0.5} but on closer inspection these aren't firearms at all.{w} They're {i}megaphones.{/i})"
            "(So many colors,{w=0.1} materials,{w=0.1} variations… {w}It's far from organized,{w=0.1} but it does look like a collection.)"
            "(It's hard to picture Dr. Danger,{w=0.1} one of STOP's most wanted criminals,{w=0.1} picking up such a quirky hobby.)"
            "(And yet,{w=0.1} half of them are tagged with the initials \"DD\".)"
            hide room1_megaphones with dissolve
            pause 0.5
            "(...Every supervillain's bound to have a quirk or two.)"
        else:
            show room1_megaphones with dissolve:
                yalign 0.2 xalign 0.5
            "(So many megaphones...{w} Every supervillain's bound to have a quirk or two.)"
            hide room1_megaphones with dissolve
            pass
        $ room1["megaphone"] += 1

    elif inspect == "marble":
        if room1["marble"] == 0:
            "<TODO: Marble puzzle.>"
        else:
            pass
        $ room1["marble"] += 1

    elif inspect == "hacking":
        if "hacking" in room1["solved"]:
            "(You've already solved the hacking puzzle.)"
        else:
            if room1["hacking"] == 0:
                call init_puzzle_board
                #"<TODO: Insert intro script and rules.>"
            else:
                pass
            show screen puzzle_playspace(pb, False) with easeintop
            $ room1["hacking"] += 1
            call screen puzzle_playspace(pb)
            if room1["hacking"] == "solved":
                jump hacking_solved
        
    elif inspect == "decanting":
        if "decanting" in room1["solved"]:
            "(You've already solved the decanting puzzle.)"
        else:
            if room1["decanting"] == 0:
                $decanting_init()
                #decanting introduction
                pass
            else:
                #repeated investigation
                pass
            show screen room1_decanting with easeintop
            $ room1["decanting"] += 1
            $ inspect = None
            call screen room1_decanting
            if room1["decanting"] == "solved":
                jump decanting_solved

    elif inspect == "bomb":
        if room1["bomb"] == 0:
            "<TODO: bomb puzzle.>"
        else:
            pass
        $ room1["bomb"] += 1

    $ inspect = None
    $renpy.block_rollback()
    call screen room1

label hacking_solved:
    $renpy.block_rollback()
    $ inspect = "hacking"
    show screen puzzle_playspace(pb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("hacking")
    #Show a marble
    "(Congratulations! {w}You solved the hacking puzzle.)"
    hide black onlayer screens
    hide screen puzzle_playspace
    with dissolve
    $ inspect = None
    call screen room1

label hacking_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen puzzle_playspace(pb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    "(It's too late. The counter-trace just found you and-)"
    "(Wait. Does that mean you've alerted STOP? That rescue could be-)"
    cr "Hey, lab rat! I've got good news and bad news. In that order, 'cause time's short."
    cr "Good news! STOP found your computer."
    cr "Bad news! Standard operating procedure is to overload the offending console ASAP."
    cr "By the way, you're standing very, very close to the computer. I'll have you know that's bad for your eye-"

    #"{b}BOOM, CUT TO BLACK{/b}"
    scene black with small_shake

    pause 3

    $nvl_heading = "Lab Report #615"
    l "Subject died after computer shrapnel blew up into their face."
    $deadend(achievement_dead4)
    le "DEAD END 04: NAME!"
    pause 2
    nvl clear
    $game_over(1)
    return

label decanting_solved:
    $renpy.block_rollback()
    $ inspect = "decanting"
    show screen room1_decanting
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("decanting")
    #Show a marble
    "(Congratulations! {w}You solved the decanting puzzle.)"
    hide black onlayer screens
    hide screen room1_decanting
    with dissolve
    $ inspect = None
    call screen room1

label decanting_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show bg room1:
        xalign 0.4 yalign 0.9
    show screen room1_decanting with None
    show black onlayer screens:
        alpha 0.5
    with dissolve
    "(You're getting close, now...{w=0.5} Right?)"
    "(If you just pour {i}this{/i}{i} {/i}into {i}that-){/i}"
    cr "Wow, lab rat – you've made {i}quite{/i} the concoction!"
    hide black onlayer screens
    hide screen room1_decanting 
    hide screen room1
    with easeouttop
    "(Really?!{w} Did you find a solution that {i}he {/i}hadn't thought of?)"
    cr "Y'know,{w=0.1} I {i}did {/i}say that two doses would be lethal..."

    "(...By the way,"

    show bg room1 at dizzy with dissolve:
        parallel:
            yalign 0.0 xalign 0.0 zoom 0.335

    extend " {cps=20}have your legs always been made of jelly?){/cps}"
    cr "...But if your bio signs are anything to go by...{w=0.5} it looks like overexposure to the vapors does the job too!"

    play sound "audio/sfx/Body Fall 1.ogg"

    show bg room1 at dizzy:
        zoom 0.335 yalign 0.0
        easeout 0.4 zoom 1.0 xalign 0.2 yalign 1.0
    pause 0.4

    scene black with small_shake

    pause 3

    $nvl_heading = "Lab Report #786"
    l "Subject experienced cardiac arrest after extended exposure to fumes in the workplace."
    l "{b}Contributing Factors to Death:{/b} Didn't perform their duties under a fume hood."
    l "STOP will have to screen its employees for basic lab safety if they're gonna keep sending them my way."
    $deadend(achievement_dead5)
    le "DEAD END 05: A Venom-enal End!"
    pause 2
    nvl clear
    $game_over(1)
    return

label room1_deaths:

    ##### NOTE: i commented out the death scenes for now, but once they're re-implemented - LMK and i'll edit them and their atl! 
    ### Mado
    #"{u}{b}Death Scenes{/b}{/u}"

    #"Puzzle 1" "{b}{/b} Player is helping Cautionne by making a bomb. It is possible to put the ingredients in the wrong order and blow yourself up."

    #"Puzzle 1 Death Scene"
    #{b}[death scene writing goes here]{/b}
    #"(Carefully, you finish the assembly and set it down in front of you.)"
    #(...Huh. It doesn't seem like it's ticking.)""
    #cr "Well, well, well. You\'ve successfully made a bomb."
    #cr "I can say with {i}100\% certainty{/i} that it\'ll make a fantastic explosion."
    #"(Phew. Looks like I've done what I was supposed to.)"
    #cr "That said, the timer-"
    #{b}BOOM SFX, CUT TO BLACK{/b}
    #cr "...needs some work."

    #"Lab Report #414" "{b}{/b}{i}Subject passed away due to an overexposure to high-yield explosives.{/i}"

    #"Contributing Factors to Death" "{i}{b}{/b}{/i}{i}A lack of detail-oriented problem solving skills. Nothing more, nothing less. {/i}"

    

    # "{b}Puzzle {/b}{b}{/b} Cautionne has presented you with three unmarked cups of irregular shape, and notes they hold 18, 10, and 7cc of liquid respectively. They need your help poisoning a top STOP official, but the poison they are using is very particular and must be administered in two separate doses of 9cc each. The 18cc cup is filled with the poison that will be used. Using only the cups present, Cautionne is asking you to measure the poison into two equal doses. Be careful though! The poison is quite volatile, and if disturbed too much may give off vapors which will not be good for your health in any way shape or form."

    #"Meta Puzzle" "{b}{/b}You are putting marbles into a marble machine to knock down effigies of STOP officials that Cautione has killed/plans to kill/or was in the process of killing and forced you to actively participate in killing. You must knock down the effigies in order of how the died/will die. If you get the order wrong Cautionne scolds you for not paying attention and activates a death trap (maybe a door in the ceiling opens up and a giant marble falls and crushes you)"

    # "Meta Puzzle Death Scene" "{b}{/b}
    #{b}[death scene writing goes here]{/b}
    #(You step back and pause. Something about the order doesn't seem-)
    #CautionneOof. {i}Not quite.{/i} 
    #CautionneBut it's okay! I can fix this, easy-peasy.
    #CautionneJust, uh... stand still... foooooor oooone secoooooond aaaaand-"

    #"{b}SPLAT{/b}
    #{b}[a giant marble comes and crushes the protag – screen cuts to black]{/b}"

    #"Lab Report#909" "{i}{b}{/b}{/i}{i} Subject was crushed by a comically large marble. Dropped just high enough for instantaneous death and perfect comedic timing{/i}"

    #"Contributing Factors to Death" "{i}{b}Contributing Factors to Death{/b}{/i}{i}{b}{/b}{/i}{i}Didn't{/i}{i} recognize good slapstick even when it hit them.{/i}"


