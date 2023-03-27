default room1 = {"investigated":[], "solved":[], "oil":0, "chair":0, "megaphone":0, "marble":0, "hacking":0, "decanting":0, "bomb":0,}

define panopticon_move_limit = 30

screen room1():
    sensitive not inspect
    layer "master"
    tag room

    fixed at zoomed(0.34):
        add "bg room1"
        imagebutton idle "room1_oil" action [SetVariable("inspect", "oil"), Jump("room_1")] pos (1175, 2650) mouse "inspect"
        imagebutton idle "room1_chair" action [SetVariable("inspect", "chair"), Jump("room_1")] pos (3800, 1850) mouse "inspect"
        imagebutton idle "room1_megaphone" action [SetVariable("inspect", "megaphone"), Jump("room_1")] pos (2500, 1350) mouse "inspect"
        imagebutton idle "room1_marble" action [SetVariable("inspect", "marble"), Jump("room_1")] pos (2000, 2550) mouse "puzzle"
        imagebutton idle "room1_hacking" action [SetVariable("inspect", "hacking"), Jump("room_1")] pos (2500, 2050) mouse "puzzle"
        imagebutton idle "room1_decanting" action [SetVariable("inspect", "decanting"), Jump("room_1")] pos (1500, 1550) mouse "puzzle"
        imagebutton idle "room1_bomb" action [SetVariable("inspect", "bomb"), Jump("room_1")] pos (575, 2850) mouse "puzzle"

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_1")] style "main_menu_button"
            
label room_1:
    if inspect not in room1["investigated"] and inspect in ["oil", "chair", "megaphone"]:
        $room1["investigated"].append(inspect)
    show screen room1
    
    if inspect == "oil":
        if room1["oil"] == 0:
            "(You approach the glistening puddle for a closer look.)"
            "(The smell's pretty unambiguous,{w=0.1} but just to be sure -{w=0.1} you gingerly swipe a finger across the surface.)"
            "(Oil.{w} Most likely for some kind of machine.)"
            "(It's not unfamiliar.{w} STOP has a massive array of equipment and vehicles that need regular maintenance.)"
            "(An agent like you is expected to know how to repair and service them -{w=0.1} especially when your bosses are displeased with you.)"
            "(But it's strange to see oil out in the open here.{w} Maybe it's a spill, or a leak?)"
            "(Either way,{w=0.1} something {i}clearly{/i} isn't working.)"
        else:
            "(Oil.{w} Something clearly isn't working here.)"
            pass
        $ room1["oil"] += 1

    elif inspect == "chair":
        #"{b}Primary Source Extractor (Electric Chair){/b} "
        if room1["chair"] == 0:
            "(From a comfortable distance, you eye over the \"Primary Source Extractor\".{w} You approach carefully, listening closely for any hints of it roaring to life.)"
            "(Agents are expected to keep their wits about them and not jump to conclusions… {w}but it's hard to see the device in front of you as anything but an electric chair.)"
            "(It looks crude and cruel, {w=0.1}like a child's re-imagining of something scary from a history book.)"
            "(That may be exactly what it is.{w} Whatever its purpose, you give quiet thanks that it seems to be out of commission.)"
        else:
            "(You're thankful this {i}horrible{/i} device is out of commission.)"
            #repeated investigation

            pass
        $ room1["chair"] += 1

    elif inspect == "megaphone":
        #"{b}Megaphone Collection {/b}"
        if room1["megaphone"] == 0:
            "(You paused when you saw the silhouettes from across the room... {w=0.1}but on closer inspection these aren't firearms at all.{w} They're {i}megaphones.{/i})"
            "(So many colors, materials, variations… {w}It's far from organized, but it does look like a collection.)"
            "(It's hard to picture Dr. Danger,{w=0.1} one of STOP's most wanted criminals,{w=0.1}  picking up such a quirky hobby.)"
            "(And yet, half of them are tagged with the initials \"DD\".)"
            "(...Every supervillain's bound to have a quirk or two.)"
        else:
            "(So many megaphones...{w} Every supervillain's bound to have a quirk or two.)"
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
            "(You already solved the hacking puzzle.)"
        else:
            if room1["hacking"] == 0:
                call init_puzzle_board
                show screen puzzle_playspace(pb, False)
                "<TODO: Insert intro script and rules.>"
                call screen puzzle_playspace(pb)
            else:
                call screen puzzle_playspace(pb)
        $ room1["hacking"] += 1
        
    elif inspect == "decanting":
        if "decanting" in room1["solved"]:
            "(You already solved the decanting puzzle.)"
        else:
            if room1["decanting"] == 0:
                #decanting introduction
                pass
            else:
                #repeated investigation
                pass
            $ room1["decanting"] += 1
            $ inspect = None
            call screen room1_decanting with easeintop

    elif inspect == "bomb":
        if room1["bomb"] == 0:
            "<TODO: bomb puzzle.>"
        else:
            pass
        $ room1["bomb"] += 1

    $ inspect = None
    call screen room1

label decanting_solved:
    $ inspect = "decanting"
    show screen room1_decanting
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("decanting")
    #Show a note/picture/memento which will then show up on 
    "(You solved the decanting puzzle.)"
    hide black onlayer screens
    hide screen room1_decanting
    with dissolve
    $ inspect = None
    call screen room1

label decanting_game_over:
    $ inspect = "game over"
    show screen room1_decanting
    show black onlayer screens with dissolve:
        alpha 0.5
    "(You're getting close, now... Right?)"
    "(If you just pour {i}this{/i}{i} {/i}into {i}that-){/i}"
    cr "Wow, lab rat – you've made quite the concoction!"
    "(Really?! Did you find a solution that {i}he {/i}hadn't thought of?)"
    cr "Y'know, I {i}did {/i}say that two doses would be lethal..."
    "(...By the way, have your legs always been made of jelly?)"
    cr "...But if your bio signs are anything to go by... it looks like overexposure to the vapors does the job too!"

    hide black onlayer screens
    hide screen room1_decanting 
    with easeouttop
    pause 1
    #"{b}SFX OF PLAYER COLLAPSING ON GROUND{/b}"

    nvl clear
    pause 2

    $nvl_heading = "Lab Report #786"
    l "Subject experienced cardiac arrest after extended exposure to fumes in the workplace."
    l "{b}Contributing Factors to Death:{/b} Didn't perform their duties under a fume hood. STOP will have to screen its employees for basic lab safety if they're gonna keep sending them my way."
    $deadend(achievement_dead5)
    #TODO: Add name
    le "DEAD END 05: Quilt In Action."
    pause 2
    nvl clear
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

    #"Puzzle 2" "{b}{/b} You are remotely hacking into a STOP medical facility to sabotage the cybernetic implants of a top official. A counter-trace is immediately activated, which, when finished, will remotely overlaod the computer causing it to explode."

    #"Puzzle 2 Death Scene" "{b}{/b}
    #{i}Player fails to complete the hack{/i}"

    #"(It's too late. The counter-trace just found you and-)
    #(Wait. Does that mean you've alerted STOP? That rescue could be-)
    #Hey, lab rat! I've got good news and bad news. In that order, \'cause time's short
    #Good news! STOP found your computer.
    #Bad news! Standard operating procedure is to overload the offending console ASAP.
    #By the way, you're standing very, very close to the computer. I\'ll have you know that's bad for your eye-"

    #"{b}BOOM, CUT TO BLACK{/b}"

    #"Lab Report #615" "{i}{b}{/b}{/i}{i} Subject died after computer shrapnel blew up into their face.{/i}"

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


