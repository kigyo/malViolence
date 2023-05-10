default room1 = {"solved":[], "oil":0, "chair":0, "megaphone":0, "marble":0, "hacking":0, "decanting":0, "bomb":0}
default room1_investigated = []

define hacking_description = _("""With {color=#fff}the list of codes to your left,{/color} Cautionne wants you to hack into one of STOP's computer systems.

{color=#fff}Use the mouse or keyboard{/color} to clear out {color=#fff}the codes in the system (shown on the right).{/color}

{color=#fff}All of the codes must be used{/color} to destroy the firewall and sucessfully break into the system.

But be careful! If you don't use these codes at the right time, you might lock yourself out...

""")


define decanting_description = _("""Cautionne needs your help poisoning a top STOP official, {color=#fff}but his toxin of choice is pretty particular!{/color}

Using three vials of {color=#fff}[decanting_size_vial1]cc, [decanting_size_vial2]cc,{/color}  and {color=#fff}[decanting_size_vial3]cc{/color}  — {color=#fff}measure the poison into two equal doses of [decanting_solution]cc.{/color} Note that {color=#fff}the [decanting_size_vial1]cc vial{/color} contains the poison itself.

Be quick, though. {color=#fff}If the poison's disturbed too much, it'll give off nasty vapors...{/color}

Drag the vials in order to pour their contents into each other.""")


define bomb_description = _("""{color=#fff}Fit all of the bomb pieces inside the bomb casing!{/color}\nUse {color=#fff}your mouse{/color} to drag pieces around. {color=#fff}Left click{/color} to rotate them {color=#fff}clockwise,{/color} {color=#fff}right click{/color} to rotate things {color=#fff}counterclockwise.{/color} \nBe sure to {color=#fff}give every piece its own space{/color}, or else things might get explosive...

""")

define marble_description = _("""{color=#fff}Knock down{/color} these effigies of STOP officials {color=#fff}in the same order you encountered them.{/color}

{u}So far, you've found:{/u}""")


screen room1():
    sensitive (not inspect and not _menu)
    layer "master"
    tag room

    fixed at zoomed(0.335):
        add "bg room1"
        imagebutton idle Null() hover "rooms/room1/room1_selection_oil.png" action [SetVariable("inspect", "oil"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_oil_mask.png" mouse "inspect" at room_hover
        imagebutton idle Null() hover "rooms/room1/room1_selection_megaphones.png" action [SetVariable("inspect", "megaphone"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_megaphones_mask.png" mouse "inspect" at room_hover

        imagebutton idle Null() hover "rooms/room1/room1_selection_marblepuzzle.png" action [SetVariable("inspect", "marble"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_marblepuzzle.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room1/room1_selection_hackingpuzzle.png" action [SetVariable("inspect", "hacking"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_hackingpuzzle_mask.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room1/room1_selection_decantingpuzzle.png" action [SetVariable("inspect", "decanting"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_decantingpuzzle_mask.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room1/room1_selection_bombpuzzle.png" action [SetVariable("inspect", "bomb"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_bombpuzzle.png" mouse "puzzle" at room_hover(0.5)

        imagebutton idle Null() hover "rooms/room1/room1_selection_electricchair.png" action [SetVariable("inspect", "chair"), Jump("room_1")] focus_mask "rooms/room1/room1_selection_electricchair.png" mouse "inspect" at room_hover

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_1")] style "main_menu_button"

label room_1:
    if inspect not in room1_investigated and inspect in ["oil", "chair", "megaphone"]:
        $room1_investigated.append(inspect)
    show screen room1
    $renpy.block_rollback()

    if inspect == "oil":
        if room1["oil"] == 0:
            "(You approach the glistening puddle for a closer look.)"
            show room1_oil with dissolve:
                yalign 0.2 xalign 0.5
            "(The smell's pretty unambiguous,{w=0.1} but just to be sure —{w=0.1} you gingerly swipe a finger across the surface.)"
            "(Oil.{w} Most likely for some kind of machine.)"
            "(It's not unfamiliar.{w} STOP has a massive array of equipment and vehicles that need regular maintenance.)"
            "(An agent like you is expected to know how to repair and service them —{w=0.1} especially when your bosses are displeased with you.)"
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
            "(Agents are expected to keep their wits about them and not jump to conclusions..."
            "...but it's hard to see the device in front of you as anything but an electric chair.)"
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
            "(So many colors,{w=0.1} materials,{w=0.1} variations... {w}It's far from organized,{w=0.1} but it does look like a collection.)"
            "(It's hard to picture Dr. Danger,{w=0.1} one of STOP's most wanted criminals,{w=0.1} picking up such an odd hobby.)"
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

    elif inspect == "hacking":
        if "hacking" in room1["solved"]:
            "(You've already solved the hacking puzzle.)"
        else:
            if room1["hacking"] == 0:
                call init_puzzle_board from _call_init_puzzle_board
                "(Four large monitors are displaying an intimidating wall of code.)"
                "(You were hoping you didn't have to deal with them,{w=0.1} but...)"
                show screen puzzle_playspace(pb, False, _layer="master") with easeintop
                "(...Ah well. {w}Time for some good ol' computer wrangling.)"
            else:
                "(You {i}really{/i} wish you brought your rubber duck right now.)"
            $renpy.block_rollback()
            show screen puzzle_playspace(pb, False, _layer="master") with easeintop
            $ inspect = None
            $ room1["hacking"] += 1
            $renpy.hide_screen("puzzle_playspace", "master")
            call screen puzzle_playspace(pb)
            if room1["hacking"] == "solved":
                jump hacking_solved

    elif inspect == "decanting":
        if "decanting" in room1["solved"]:
            "(You've already solved the decanting puzzle.)"
        else:
            if room1["decanting"] == 0:
                $decanting_init()
                "(Three differently-sized vials are placed on the table.{w} There are instructions written next to them.)"
            else:
                "(Dare you decant differently?{w} You dare.)"
            $renpy.block_rollback()
            show screen room1_decanting(_layer="master", **decant_kwargs) with easeintop
            $ room1["decanting"] += 1
            $ inspect = None
            $renpy.hide_screen("room1_decanting", "master")
            call screen room1_decanting(**decant_kwargs)
            if room1["decanting"] == "solved":
                jump decanting_solved

    elif inspect == "bomb":
        if "bomb" in room1["solved"]:
            "(You've already solved the bomb puzzle.)"
        else:
            if room1["bomb"] == 0:
                "(It looks like there's an open...{w=0.5} tool box?{w} You approach it to take a closer look.)"
                show bomb_puzzle with easeintop
                "(Nope!{w} It's a bomb.{w} No big deal.{w} What could {i}possibly{/i} go wrong?)"
                call init_bomb from _call_init_bomb
            else:
                "(It's a bomb!{w} Again,{w=0.1} what could {i}possibly{/i} go wrong?)"
                if bomb_level != difficulty_level:
                    $init_bomb_function(None)
                show screen room1_bomb(bomb, False, _layer="master") with easeintop
            $renpy.block_rollback()
            $ room1["bomb"] += 1
            $ inspect = None
            hide bomb_puzzle
            $renpy.hide_screen("room1_bomb", "master")
            call screen room1_bomb(bomb, True)
            if room1["bomb"] == "solved":
                jump bomb_solved

    elif inspect == "marble":
        if room1["marble"] == 0:
            $ room1["marble"] = 1
            $marble_init()
            "(You approach the strange,{w=0.1} locked door.)"
            show screen room1_marble(_layer="master") with easeintop
            "(Turns out it's even stranger up close.)"
        else:
            "(You decide to look at this marble-ous contraption once more...)"
            show screen room1_marble(_layer="master") with easeintop
            "(Sorry.{w} You couldn't help yourself.)"
        $renpy.block_rollback()
        $ inspect = None
        $renpy.hide_screen("room1_marble", "master")
        call screen room1_marble
        if room1["marble"] == "solved":
            jump post_room_1

    $ inspect = None
    $renpy.block_rollback()
    call screen room1

label bomb_solved:
    $renpy.block_rollback()
    $ inspect = "bomb"
    show screen room1_bomb(bomb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("bomb")
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    $ play_sound(marbleroll)
    show marble1:
        xalign 0.8 yalign 0.4 alpha 0.0
        ease 1.5 rotate 360 xalign 0.5 yalign 0.4 alpha 1.0
    hide black onlayer screens
    hide screen room1_bomb
    with puzzle_hide
    pause 1
    "(A marble rolls out of the bomb case.{w} Attached to it is a note reading \"Colby Padilla\".)"
    if len(room1["solved"]) == 1 and room1["marble"] == 0:
        "(You wonder what that could mean...)"
    elif room1["marble"] > 0:
        "(You think you've seen that name somewhere before.)"
    hide marble1 with dissolve
    $ inspect = None
    call screen room1

label bomb_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room1_bomb(bomb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 0.5
    "(Carefully,{w=0.1} you finish the assembly and set it down in front of you.)"
    "(...Huh.{w} It doesn't seem like it's ticking.)"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "Well, well, well.{w=0.5} You've successfully made a bomb."
    hide black onlayer screens
    hide screen room1_bomb
    with puzzle_hide
    pause 0.5
    cr "I can say with {i}100%% certainty{/i} that it'll make a fantastic explosion."
    "({i}Phew.{/i}{w} Looks like you've done what you were supposed to.)"
    $ play_sound(timeralarm)
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "That said,{w=0.1} the timer—{w=1}{nw}"
    $ play_sound(bombexplosion1)
    scene black with small_shake
    pause 2.75
    cr "...needs some work."
    pause 3
    nvl clear
    $nvl_heading = "Lab Report #414"
    l "Subject passed away due to an overexposure to high-yield explosives."
    l "{b}Contributing Factors to Death:{/b} A lack of detail-oriented problem solving skills."
    l "Nothing more, nothing less."
    $deadend("dead3")
    le "DEAD END 03: A Mindblowing Conclusion!"
    pause 2
    nvl clear
    $game_over(1)
    return

label hacking_solved:
    $renpy.block_rollback()
    $ inspect = "hacking"
    show screen puzzle_playspace(pb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("hacking")
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    $ play_sound(marbleroll)
    show marble2:
        xalign 0.8 yalign 0.4 alpha 0.0
        ease 1.5 rotate 360 xalign 0.5 yalign 0.4 alpha 1.0
    hide black onlayer screens
    hide screen puzzle_playspace
    with puzzle_hide
    pause 1
    "(The computer ejects a marble,{w=0.1} along with a note reading \"Asiya Bishop\".)"
    if len(room1["solved"]) == 1 and room1["marble"] == 0:
        "(You wonder what that could mean...)"
    elif room1["marble"] > 0:
        "(You think you've seen that name somewhere before.)"
    hide marble2 with dissolve
    $ inspect = None
    call screen room1

label hacking_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen puzzle_playspace(pb, False)
    show black onlayer screens with dissolve:
        alpha 0.5

    stop music fadeout 0.5

    $ play_sound(timeralarm2)

    "(It's too late.{w} The counter-trace just found you and—){w=1}{nw}"
    "(Wait.{w} Does that mean you've alerted STOP?{p}That rescue could be—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "Hey, lab rat!{w=0.5} I've got good news and bad news.{w=0.5} In that order,{w=0.1} 'cause time's short."
    hide black onlayer screens
    hide screen puzzle_playspace
    with puzzle_hide
    pause 0.5
    cr "Good news!{w=0.5} STOP found your computer."
    cr "Bad news!{w=0.5} Standard operating procedure is to overload the offending console ASAP."
    cr "By the way,{w=0.1} you're standing very,{w=0.1} {i}very{/i} close to the computer.{w=0.5} I'll have you know that's bad for your eye—{w=1}{nw}"

    $ play_sound(bombexplosion2)
    scene black with small_shake

    pause 3

    $nvl_heading = "Lab Report #615"
    l "Subject died after computer shrapnel blew up into their face.\n"
    l "{b}Contributing Factors to Death:{/b} “Tech-savvy”? On {i}their{/i} resumé? Guess STOP wasn't thorough enough with their background check."
    $deadend("dead4")
    le "DEAD END 04: Trouble-shooting?"
    pause 2
    nvl clear
    $game_over(1)
    return

label decanting_solved:
    $renpy.block_rollback()
    $clear_puzzle("room1_3")
    $ inspect = "decanting"
    show screen room1_decanting
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room1["solved"].append("decanting")
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    $ play_sound(marbleroll)
    show marble3:
        xalign 0.8 yalign 0.4 alpha 0.0
        ease 1.5 rotate 360 xalign 0.5 yalign 0.4 alpha 1.0
    hide black onlayer screens
    hide screen room1_decanting
    with puzzle_hide
    pause 1
    "(A small compartment opens up,{w=0.1} revealing a marble.{w} Underneath it is a note reading \"Brooke Yang\".)"
    if len(room1["solved"]) == 1 and room1["marble"] == 0:
        "(You wonder what that could mean...)"
    elif room1["marble"] > 0:
        "(You think you've seen that name somewhere before.)"
    hide marble3 with dissolve
    $ inspect = None
    call screen room1

label decanting_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room1_decanting with None
    show black onlayer screens:
        alpha 0.5
    with dissolve
    stop music fadeout 0.5
    "(You're getting close, now...{w=0.5} Right?)"
    $ play_sound(liquidpour)
    "(If you just pour {i}this{/i}{i} {/i}into {i}that—{/i})"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "Wow, lab rat — you've made {i}quite{/i} the concoction!"
    hide black onlayer screens
    hide screen room1_decanting
    with puzzle_hide
    scene bg room1:
        parallel:
            yalign 0.0 xalign 0.0 zoom 0.335
    pause 0.5
    "(Really?!{w} Did you find a solution that {i}he {/i}hadn't thought of?)"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "Y'know,{w=0.1} I {i}did {/i}say that two doses would be lethal..."

    "(...By the way,"

    show bg room1 at dizzy with dissolve:
        parallel:
            yalign 0.0 xalign 0.0 zoom 0.335

    extend " {cps=20}have your legs always been made of jelly?){/cps}"
    cr "...But if your bio signs are anything to go by...{w=0.5} it looks like overexposure to the vapors does the job too!"


    show bg room1 at dizzy:
        zoom 0.335 yalign 0.0
        easeout 0.3 zoom 1.0 xalign 0.2 yalign 1.0
    pause 0.3
    $ play_sound(bodyfall)
    scene black with small_shake

    pause 3

    $nvl_heading = "Lab Report #786"
    l "Subject experienced cardiac arrest after extended exposure to fumes in the workplace."
    l "{b}Contributing Factors to Death:{/b} Didn't perform their duties under a fume hood."
    l "STOP will have to screen its employees for basic lab safety if they're gonna keep sending them my way."
    $deadend("dead5")
    le "DEAD END 05: A Venom-enal End!"
    pause 2
    nvl clear
    $game_over(1)
    return

label marble_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room1_marble with None
    stop music fadeout 0.5
    show black onlayer screens with dissolve:
        alpha 0.5
    "(You step back and pause.{w} Something about the order doesn't seem—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "Oof.{w=0.5} {i}Not quite.{/i} "
    hide black onlayer screens
    hide screen room1_marble
    with puzzle_hide
    pause 0.5
    cr "But it's okay!{w=0.5} I can fix this,{w=0.1} easy-peasy."
    cr "Just, uh...{w=0.5} stand still...{w=0.5}{cps=20}foooooor oooone secoooooond aaaaand—{/cps}{w=0.5}{nw}"

    #"{b}SPLAT{/b}
    #{b}[a giant marble comes and crushes the protag — screen cuts to black]{/b}"

    $ play_sound(marbledeath)

    pause 1.127

    scene black with small_shake

    pause 3

    $nvl_heading = "Lab Report #909"
    l "Subject was crushed by a comically large marble."
    l "Dropped just high enough for instantaneous death and perfect comedic timing."
    l "{b}Contributing Factors to Death:{/b} Didn't recognize good slapstick even when it hit them."

    $deadend("dead2")
    le "DEAD END 02: Marble-ous Slapstick!"
    pause 2
    nvl clear
    $game_over(1)
    return
