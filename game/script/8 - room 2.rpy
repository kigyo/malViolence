default room2 = {"solved":[], "blueprints":0, "post-its":0, "limbs":0, "corkboard":0, "clippings":0, "panopticon":0, "recalibration":0, "evidence":0, "word":0, "notes":[]}
default room2_investigated = []

screen room2():
    sensitive (not inspect and not _menu)
    layer "master"
    tag room

    fixed at zoomed(0.335):
        add "bg room2"
        imagebutton idle Null() hover "rooms/room2/room2_selection_evidenceboard.png" action [SetVariable("inspect", "corkboard"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_evidenceboard.png" mouse "inspect" at room_hover
        imagebutton idle Null() hover "rooms/room2/room2_selection_blueprints.png" action [SetVariable("inspect", "blueprints"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_blueprints.png" mouse "inspect" at room_hover
        imagebutton idle Null() hover "rooms/room2/room2_selection_newspaperclippings.png" action [SetVariable("inspect", "clippings"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_newspaperclippings.png" mouse "inspect" at room_hover
        imagebutton idle Null() hover "rooms/room2/room2_selection_armdesigns.png" action [SetVariable("inspect", "limbs"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_armdesigns.png" mouse "inspect" at room_hover
        imagebutton idle Null() hover "rooms/room2/room2_selection_postits.png" action [SetVariable("inspect", "post-its"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_postits.png" mouse "inspect" at room_hover

        imagebutton idle Null() hover "rooms/room2/room2_selection_metapuzzle.png" action [SetVariable("inspect", "word"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_metapuzzle.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room2/room2_selection_panopticonpuzzle.png" action [SetVariable("inspect", "panopticon"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_panopticonpuzzle.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room2/room2_selection_evidencepuzzle.png" action [SetVariable("inspect", "evidence"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_evidencepuzzle.png" mouse "puzzle" at room_hover(0.5)
        imagebutton idle Null() hover "rooms/room2/room2_selection_calibrationpuzzle.png" action [SetVariable("inspect", "recalibration"), Jump("room_2")] focus_mask "rooms/room2/room2_selection_calibrationpuzzle.png" mouse "puzzle" at room_hover(0.5)

        if 1 not in room2["notes"]:
            imagebutton idle "rooms/room2_note1.png" action [SetVariable("inspect", "note1"), Jump("room_2")] pos (160, 1484) mouse "inspect"
        if 2 not in room2["notes"]:
            imagebutton idle "rooms/room2_note2.png" action [SetVariable("inspect", "note2"), Jump("room_2")] pos (1417, 1767) mouse "inspect"
        if 3 not in room2["notes"]:
            imagebutton idle "rooms/room2_note3.png" action [SetVariable("inspect", "note3"), Jump("room_2")] pos (3870, 2217) mouse "inspect"
        if 4 not in room2["notes"]:
            imagebutton idle "rooms/room2_note3.png" action [SetVariable("inspect", "note4"), Jump("room_2")] pos (5500, 1987) mouse "inspect"

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_2")] style "main_menu_button"


define cybernetics_description = _("""It's time for a crash course in cybernetics!

{color=#fff}Lay down new synthetic neural pathways — but be mindful of the original pieces that can't be moved.{/color}

Here's some basic recalibration rules:
-{color=#fff} Neural pathways must form one continuous loop and occupy every available space.{/color}
-{color=#fff} Pathways can cross over themselves, but they can't retrace themselves{/color} (so no T intersections).
-{color=#fff} At any 4-way intersection, a neuron will always go straight through.{/color} It'll never turn.
-You can only submit possible solutions {color=#fff}where there are no open-ended pathways{/color} (including T intersections).""")


define word_description = _("""Cautionne's a big fan of word games, so he wants you to come up with {color=#fff}a word that's almost as good as the one above.{/color}

{color=#fff}...You might have to find some letters first!{/color}""")

define word_lenient_failure_message = _("Not a valid solution.")

label room_2:

####defining the tile images here
    image tile_t = "images/puzzles/room_2_meta/tile_t.png"
    image tile_a = "images/puzzles/room_2_meta/tile_a.png"
    image tile_s = "images/puzzles/room_2_meta/tile_s.png"
    image tile_e = "images/puzzles/room_2_meta/tile_e.png"
    image tile_r = "images/puzzles/room_2_meta/tile_r.png"

#####
    if inspect not in room2_investigated and inspect in ["blueprints", "limbs", "clippings", "post-its", "corkboard"]:
        $room2_investigated.append(inspect)
    show screen room2
    hide screen room2_panopticon
    $renpy.block_rollback()

    if inspect == "note1":
        $room2["notes"].append(1)
        $ play_sound(paperpickup)
        "(You spot a note on the wall,{w=0.1} and pick it up.)"
        if difficulty_level == 1:
            "(It says: \"The harmonica has traces of wild pollen found only in remote regions that have yet to be extensively developed.\")"
        elif difficulty_level == 2:
            "(It says: \"- The blonde child seems to have a musical inclination.\")"
            "(\"- The bracelet has a notable tarnish.{w} Upon sampling,{w=0.1} it seems to be a coating of coastal salt.\")"
            "(\"- The city-dweller was abducted in the Spring.\")"
        elif difficulty_level == 3:
            "(It says: \"- The child with the harmonica arrived first.\")"
            "(\"- The child in Cell 3 arrived in November.\")"
            "(\"- The child with the bracelet was not in Cell 0, 1, or 3.\")"
            "(\"- Subject R did not receive cybernetic legs or perspicacious processing implants.\")"
            "(\"- The child that received the lethal legs implant arrived in February.\")"
        else:
            "Whoops! This message SHOULDN'T appear, but it has! Might need to bugcheck."
    elif inspect == "note2":
        $room2["notes"].append(2)
        $ play_sound(paperpickup)
        "(You pick up the note beneath the blackboard.)"
        if difficulty_level == 1:
            "(It says: \"The red-headed child is certain they did not live in the city.\")"
        elif difficulty_level == 2:
            "(It says: \"- The red-headed child said they have never been to the suburbs or to open water.\")"
            "(\"- Whoever lived in the mountains arrived in either June or December.\")"
            "(\"- The child from the suburbs was processed before the subject from the mountains.\")"
        elif difficulty_level == 3:
            "(It says: \"- The cell of the child with the lethal legs implant was between the cells of the child who came with the knife and the child who came with a yo-yo.\")"
            "(\"- The cell of the child who received the perspicacious processing implant was between the cells of the child who arrived in July and the child who arrived in February.\")"
            "(\"- The child who received the heightened hearing implant arrived one month apart from the child who came with the yo-yo.\")"
            "(\"- The child with the yo-yo stayed in Cell 2.\")"
        else:
            "Whoops! This message SHOULDN'T appear, but it has! Might need to bugcheck."
    elif inspect == "note3":
        $room2["notes"].append(3)
        $ play_sound(paperpickup)
        "(There's a note stuck to the front of the desk.)"
        if difficulty_level == 1:
            "(It says: \"The bracelet is too big for the red-headed child.\")"
        elif difficulty_level == 2:
            "(It says: \"- The bracelet arrived at the facility before the toy plane.\")"
            "(\"- Subject G does not how to use a yo-yo.\")"
            "(\"- The yo-yo trickster did not arrive first.\")"
        elif difficulty_level == 3:
            "(It says: \"- Subject D received the eye implants.\")"
            "(\"- 2 children arrived before Subject G did, and 2 children arrived after.\")"
            "(\"- The child with the toy plane was in a higher cell number than the child who came with a yo-yo.\")"
            "(\"- The bracelet was found in the cell directly to the right of the child who received the hearing implant.{w} To their left was the cell that remained empty the longest.\")"
            "(\"- The cell number of the subject with cybernetic arms is half of the cell number that Subject D stayed in.\")"
            "(\"- Subject R came with a toy plane.\")"
        else:
            "Whoops! This message SHOULDN'T appear, but it has! Might need to bugcheck."
    elif inspect == "note4":
        $room2["notes"].append(4)
        $ play_sound(paperpickup)
        "(A note is stuck to the water cooler —{w=0.5} which doesn't actually dispense any water.)"
        if difficulty_level == 1:
            "(It says: \"The blonde child managed to play a tune on the harmonica when asked,{w=0.1} but the other two children could not.\")"
        elif difficulty_level == 2:
            "(It says: \"- The child whose designation comes first in the alphabet was the second-to-last arrival.\")"
            "(\"- Subject R arrived in June.\")"
            "(\"- The child wearing a bracelet arrived in September.\")"
        elif difficulty_level == 3:
            "(It says: \"- The child who came with a knife also received the perspicacious processing implant.\")"
            "(\"- The child who received the armed arms implant arrived last.\")"
            "(\"- The toy plane could've belonged to the child with heightened hearing or the child who received new eyes.\")"
            "(\"- The yo-yo belonged either to Subject F or the subject who received cybernetic legs.\")"
            "(\"- The cell number of the subject with cybernetic arms is half of the cell number that Subject D stayed in.\")"
            "(\"- The child who got new eyes came 1 month before the child who came with a knife.\")"
        else:
            "Whoops! This message SHOULDN'T appear, but it has! Might need to bugcheck."

    elif inspect == "blueprints":
        if room2["blueprints"] == 0:
            show room2_blueprintcollection with dissolve:
                yalign 0.2 xalign 0.5
            $ play_sound(paperpickup)
            "(You survey the diagrams before you.)"
            "(From a distance,{w=0.1} they seem to be your average blueprints.{w} Blueprints for weapons of all makes,{w=0.1} shapes{w=0.1} and sizes.)"
            "(But on closer inspection,{w=0.1} they reveal a certain {i}quirkiness{/i} that doesn't belong on a technical document.{w} The handwriting is also... {w=0.5}{i}distinct,{/i}{w=0.1} for lack of a better word.)"
            "(That said,{w=0.1} poor penmanship hasn't dulled the designs themselves.{w} The {i}least{/i} dangerous of these would be devastating out in the field.)"
            if gui.text_size > 40:
                "(The oldest of the blueprints —{w=0.1} the ones hidden at the bottom of the pile,{w=0.1} look wildly different.{w} Clearly,{w=0.1} another person was behind them.)"
            else:
                "(The oldest of the blueprints —{w=0.1} the ones hidden at the bottom of the\npile,{w=0.1} look wildly different.{w} Clearly,{w=0.1} another person was behind them.)"
            "(In fact,{w=0.1} if you squint...{w=0.5} you can still find the signatures at the bottom.)"
            "(\"Destrange,\"{w=0.1} they say.{w} They're dated more than 15 years ago.)"
            hide room2_blueprintcollection with dissolve
        else:
            show room2_blueprintcollection with dissolve:
                yalign 0.2 xalign 0.5
            "(Blueprints for a variety of dangerous weapons.{w} Honestly,{w=0.1} they're pretty scary.)"
            hide room2_blueprintcollection with dissolve
            pass
        $ room2["blueprints"] += 1

    elif inspect == "post-its":
        if room2["post-its"] == 0:
            show room2_postitnotes with dissolve:
                yalign 0.2 xalign 0.5
            "(You eye over the mass of scrawled notes pinned in front of you.{w} There are two distinct sets of handwriting here,{w=0.1} but the contents are mostly the same...{w=0.5} and mostly {i}domestic?{/i}) "
            "(Notes on what to eat for breakfast and when to start preparing it.{w} Notes on how much sleep to get and what stories to read.)"
            "(Birthdays,{w=0.1} exercises,{w=0.1} meal plans,{w=0.1} and chores...)"
            if gui.text_size > 40:
                "(The two who wrote these notes weren't just sharing the same space. {w}They were {i}living{/i} together.)"
            else:
                "(The two who wrote these notes weren't just sharing the same space.\n{w}They were {i}living{/i} together.)"
            hide room2_postitnotes with dissolve
        else:
            show room2_postitnotes with dissolve:
                yalign 0.2 xalign 0.5
            "(A wall of scrawled notes.{w} And they all talk about...{w=0.5} domestic tasks?)"
            hide room2_postitnotes with dissolve
            pass
        $ room2["post-its"] += 1

    elif inspect == "limbs":
        if room2["limbs"] == 0:
            show room2_limbsdesigns with dissolve:
                yalign 0.2 xalign 0.5
            $ play_sound(paperpickup)
            "(These documents appear to be designs for cybernetic limbs like the ones produced by STOP —{w=0.5} at first glance.)"
            "(On closer inspection,{w=0.1} there are more differences than there are similarities.) "
            "(STOP's technology is more generalized,{w=0.1} more efficient...{w=0.5} and {i}angular.{/i})"
            "(These plans are heavily customized.{w} They could've only been suitable for a very small number of subjects —{w=-0.5} possibly as few as {i}one.{/i})"
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
            "(Laboratories,{w=0.1} factories,{w=0.1} and armories that must be high above your clearance level —{w=0.5} crossed out like someone was just going down a checklist.)"
            "(All these top-secret sites share the same acronym:{w=0.5} \"YTDI.\")"
            "(...No,{w=0.1} you {i}don't{/i} recognize it.)"
            hide room2_evidenceboard with dissolve
            "(That's par for the course with STOP.{w} If you don't know what an acronym means,{w=0.1} it's probably above your paygrade.)"
        else:
            show room2_evidenceboard with dissolve:
                yalign 0.2 xalign 0.5
            "(A sprawling web of photos,{w=0.1} documents,{w=0.1} and diagrams.{w} And they're all related to STOP...)"
            hide room2_evidenceboard with dissolve
            pass
        $ room2["corkboard"] += 1

    elif inspect == "clippings":
        if room2["clippings"] == 0:
            show room2_news with dissolve:
                yalign 0.2 xalign 0.5
            "(Printouts and clippings of various news articles —{w=0.1} all related to Dr. Danger's exploits...{w=0.5} with a {i}certain{/i} colorful sidekick occasionally breaking into the opening paragraphs.)"
            "(In fact,{w=0.1} when you look at them all together,{w=0.1} Cautionne seems to show up more over time.)"
            "(Dr. Danger must've been pleased with her pupil's growth.)"
            "(At the bottom of the pile,{w=0.1} a heavily weathered photo peeks out.)"
            "(Based on what you can make out of the caption — {w=0.1}it looks like some kind of commemorative occasion.)"
            "(\"__rdre Des__ge, et al. celebr_e breakthr__ in cyb_netics, sec_ity\".)"
            "(You can't recognize any of the faces,{w=0.1} but you do recognize the logo as—){w=1}{nw}"
            hide room2_news with dissolve
            pause 1
            #"{b}[pause as the clippings disappear]{/b}"
            "(...Never mind.{w} It's just similar,{w=0.1} that's all.)"
        else:
            show room2_news with dissolve:
                yalign 0.2 xalign 0.5
            "Newspaper printouts and clippings.{w} They all feature Dr. Danger...{w=0.5} as well as a certain colorful sidekick."
            hide room2_news with dissolve
            pass
        $ room2["clippings"] += 1

    elif inspect == "panopticon":
        if "panopticon" in room2["solved"]:
            "(You've already solved the panopticon puzzle.)"
        else:
            if room2["panopticon"] == 0:
                $ panopticon_init(True)
                "(A computer,{w=0.1} and a small,{w=0.1} strange...{w=0.5} colosseum?{w} What on {i}earth{/i} is that?)"
                show screen room2_panopticon(_layer="master", interactable=False) with easeintop
                "(...Of course.{w} It's a puzzle.)"
            else:
                show screen room2_panopticon(interactable=False, _layer="master") with easeintop
                "(Riiiiiight.{w} That colosseum-thing is a {i}panopticon.{/i}{w} Off to puzzle-solving you go!)"
            $renpy.block_rollback()
            if room2["panopticon"] != "solved":
                $ room2["panopticon"] += 1
            $ inspect = None
            $renpy.hide_screen("room2_panopticon", "master")
            call screen room2_panopticon()
            if room2["panopticon"] == "solved":
                jump panopticon_solved

    elif inspect == "evidence":
        if "evidence" in room2["solved"]:
            "(You've already solved the evidence board puzzle.)"
        else:
            if room2["evidence"] == 0:
                $ evidence_init(True)
                show screen room2_evidence(_layer="master") with easeintop
                "(The blackboard is covered in little doodles,{w=0.1} but they don't seem to be there just for decoration.)"
                "(You hate to admit it,{w=0.1} but they're kind of cute.{w} Completely unlike their creator.)"
            else:
                "(Let's string up some evidence!)"
                show screen room2_evidence(_layer="master") with easeintop
            $renpy.block_rollback()
            if room2["evidence"] != "solved":
                $ room2["evidence"] += 1
            $ inspect = None
            $renpy.hide_screen("room2_evidence", "master")
            call screen room2_evidence
            if room2["evidence"] == "solved":
                jump evidence_solved

    elif inspect == "recalibration":
        if "recalibration" in room2["solved"]:
            "(You've already solved the cybernetics puzzle.)"
        else:
            if room2["recalibration"] == 0:
                call init_cybernetics from _call_init_cybernetics
                "(The monitor is displaying some kind of simulation.{w} Better take a closer look...)"
            else:
                "(Time to re-enroll in that cybernetics crash-course.{w} Maybe it'll be less intimidating?)"
            $renpy.block_rollback()
            show screen cybernetics(cyb, _layer="master") with easeintop
            if room2["recalibration"] != "solved":
                $ room2["recalibration"] += 1
            $ inspect = None
            $renpy.hide_screen("cybernetics", "master")
            call screen cybernetics(cyb)
            if room2["recalibration"] == "solved":
                jump recalibration_solved

    elif inspect == "word":
        if room2["word"] == 0:
            $word_init()
            "(There are five empty slots on the door's lock.{w} Your best guess is that you need to fill them up,{w=0.1} somehow.)"
        else:
            "(You're no {i}Scraddle{/i} expert,{w=0.1} but you've got this puzzle all under control.{w} Probably.)"
        $renpy.block_rollback()
        show screen room2_word(_layer="master") with easeintop
        $ room2["word"] += 1
        $ inspect = None
        $renpy.hide_screen("room2_word", "master")
        call screen room2_word
        if room2["word"] == "solved":
            jump post_room_2

    $ inspect = None
    $renpy.block_rollback()
    call screen room2

label evidence_solved:
    $renpy.block_rollback()
    $ inspect = "evidence"
    show screen room2_evidence
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room2["solved"].append("evidence")
    #obtain the "E"
    if len(room2["notes"]) < 4:
        "(...You were mostly guessing,{w=0.1} but somehow, this worked?)"
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen room2_evidence
    with puzzle_hide
    pause 0.1
    show tile_e:
        zoom 0.5 xalign 0.5 yalign 0.3 alpha 0
        ease 1 xalign 0.5 yalign 0.5 alpha 1

    pause 1
    "(A tiny blue tile falls to the ground.{w} Upon closer inspection,{w=0.1} it reads the letter \"E\",{w=0.1} for...{w=0.5} {i}evidence{/i}?)"
    "(Or maybe for {i}\"end of puzzles\", or \"enough of these silly games\"{/i}.{w} But that's just wishful thinking.)"
    "(Either way,{w=0.1} you decide to take it with you.)"
    hide tile_e with dissolve
    $ inspect = None
    call screen room2

label evidence_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room2_evidence
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 0.5
    "(You carefully insert one more pin into the board,{w=0.1} which leaves—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "Whoa, you {i}suck {/i}at this!"
    hide black onlayer screens
    hide screen room2_evidence
    with puzzle_hide
    pause 0.5
    "(Something about his unusually straightforward insult puts ice into your veins.)"
    cr "It's like you're solving this puzzle with your eyes closed and your nose plugged."
    cr "...There some reason you don't want to look at the truth in front of you,{w=0.1} lab rat?"
    "(...No, no, it's just—){w=1}{nw}"
    cr "I know you're not taking this seriously.{w=0.5} Maybe we should just move on?"
    cr "You know what?{w=0.5} Yeah. "
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "{i}Let's put a pin in it.{/i}"
    #"{i}{b}PIERCING SFX, CUT TO BLACK.{/b}{/i}"
    $ play_sound(bodypierce)
    scene black with small_shake
    pause 3
    $nvl_heading = "Lab Report #273"
    l "Subject experienced permanent loss of life after one of the facility's reconfigurable nano-stakes jetted out of the floor and impaled them to the ceiling."
    l "Guess they were worth the trouble of installation!"
    l "{b}Contributing Factors to Death:{/b} Couldn't put progress on the board."
    $deadend("dead7")
    le "DEAD END 07: Pinpricked!"
    pause 2
    nvl clear
    $game_over(2)
    return

label panopticon_solved:
    $renpy.block_rollback()
    $ inspect = "panopticon"
    show screen room2_panopticon()
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room2["solved"].append("panopticon")
    #obtain the "A" and "S" tiles
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen room2_panopticon
    with puzzle_hide
    pause 0.1
    show tile_a:
        zoom 0.5 xalign 0.3 yalign 0.3 alpha 0
        ease 1 xalign 0.3 yalign 0.5 alpha 1
    show tile_s:
        zoom 0.5 xalign 0.7 yalign 0.3 alpha 0
        ease 1 xalign 0.7 yalign 0.5 alpha 1

    pause 1
    "(In response to your hard-earned success,{w=0.1} two little {i}Scraddle{/i}-like tiles pop out of the miniature panopticon.)"
    "(They show the letters \"A\" and \"S\".{w} How quaint.)"
    hide tile_a
    hide tile_s
    with dissolve
    $ inspect = None
    call screen room2

label panopticon_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room2_panopticon
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 0.5
    "(You re-arrange another set of cells and—){w=1}{nw}"
    $ play_sound(error)
    "(—and suddenly,{w=0.1} your controls freeze up.{w} There's a notification in the corner.)"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "Seems like you've run out of time,{w=0.1} lab rat."
    hide black onlayer screens
    hide screen room2_panopticon
    with puzzle_hide
    pause 0.5
    cr "That's it.{w=0.5} The jailbreak is over.{w=0.5} You screwed up."
    "(So it {i}was {/i}a prison?{w} Then—)"
    cr "If this only concerned you and me,{w=0.1} I'd be \"whatever\" about it."
    cr "We all make mistakes,{w=0.1} y'know?{w=0.5} So,{w=0.1} I'm super forgiving and cool and mature about this kind of thing."
    cr "...But you just lost those kids a chance to get out before the {i}operations{/i} start."
    "(...Sorry,{w=0.1} {i}operations?{/i})"
    cr "They could've gotten out clean.{w=0.5} Now I'll have to step in and bust them out {i}dirty{/i}."
    cr "And it's all because of {i}you.{/i}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Shut Up 1.ogg"
    cr "Now,{w=0.1} go sit in the corner and think about what you've done!" with small_shake
    ####### industrial lights power off sound here
    $ play_sound(powerdown)
    scene black
    pause 2
    cr "I'll come back for you when you're sorry enough."

    nvl clear
    pause 3
    $nvl_heading = "Lab Report #893"
    l "Subject expired after 3 days due to lack of water, light, food, and mental stimulation."
    l "Scratched their nails to bleeding point on the exit door before losing consciousness, so I'll have to clean {i}that{/i} mess up."
    l "{b}Contributing Factors to Death:{/b} Didn't take the consequences of imprisonment very seriously."
    $deadend("dead8")
    le "DEAD END 08: A Taste of Sobering Punishment."
    pause 2
    nvl clear
    $game_over(2)
    return

label recalibration_solved:
    $renpy.block_rollback()
    $ inspect = "recalibration"
    show screen cybernetics(cyb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room2["solved"].append("recalibration")
    #obtain the "R" and "T" tiles
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen cybernetics
    with puzzle_hide
    pause 0.1
    show tile_r:
        zoom 0.5 xalign 0.3 yalign 0.3 alpha 0
        ease 1 xalign 0.3 yalign 0.5 alpha 1
    show tile_t:
        zoom 0.5 xalign 0.7 yalign 0.3 alpha 0
        ease 1 xalign 0.7 yalign 0.5 alpha 1

    pause 1
    "(The desk drawer juts open just a bit,{w=0.1} and reveals two small tiles inside.)"
    "(\"R\" and \"T\" are written on them,{w=0.1} respectively.{w} Now,{w=0.1} where could you put them to use...?)"
    hide tile_t
    hide tile_r
    with dissolve
    $ inspect = None
    call screen room2

label recalibration_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen cybernetics(cyb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 0.5
    $ play_sound(timeralarm2)
    "(You confirm your choice,{w=0.1} and a beeping starts.)"
    "(Its tone sets the hairs on the back of your neck on edge.)"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "You're losing 'em,{w=0.1} Doc."
    "(...Wait.{w} That's...{w=0.5} an actual...?)"
    hide black onlayer screens
    hide screen cybernetics
    with puzzle_hide
    pause 0.5
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "As they are now,{w=0.1} they can't be re-stabilized.{w=0.5} That person's own nervous system will rip their body apart with spasming."
    cr "...But they shouldn't be punished for {i}your{/i} mistake,{w=0.1} right?"
    "(...Well,{w=0.1} uh—){w=1}{nw}"
    cr "Don't worry,{w=0.1} I can fix this."
    cr "But I'm gonna need a hand."

    scene bg room2 at dizzy with dissolve:
        parallel:
            yalign 0.0 xalign 0.0 zoom 0.335

    "{cps=30}(Suddenly,{w=0.1} your body feels a lot heavier.{w}{/cps} {cps=20}Is that mist in the corner of the room?){/cps}"
    cr "...And a liver.{w=0.5} And a stomach.{w=0.5} And a heart.{w=0.5} And most of your spinal cord."
    pause 1
    cr "And I'm gonna need them {cps=20}{i}right now.{/i}{/cps}"

    scene bg room2 at dizzy:
        zoom 0.335 yalign 0.0
        easeout 0.2 zoom 1.0 xalign 0.2 yalign 1.0
    pause 0.2

    $ play_sound(bodyfall)

    scene black with small_shake
    #"{i}{b}COLLAPSE SFX{/b}"
    nvl clear
    pause 3
    $nvl_heading = "Lab Report #062"
    l "Patient was eventually re-stabilized and should wake up within the next few days."
    l "On the other hand, the lab rat won't get up ever again. They're missing a few too many critical parts."
    l "{b}Contributing Factors to Death:{/b} They gave too much of themselves to my cause."

    $deadend("dead9")
    le "DEAD END 09: Didn't Make The Cut."
    pause 2
    nvl clear
    $game_over(2)
    return

label word_game_over:
    $ inspect = "game over"
    show screen room2_word
    show black onlayer screens with dissolve:
        alpha 0.5
    # [error sound effect]
    $ random_choice = random.randint(1,5)
    $renpy.block_rollback()
    if word_answer == ["","","","",""] or  word_answer == ["T","A","S","E","R"]:
        stop music fadeout 0.5
        cr "..."
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
        cr "Wow,{w=0.1} lab rat."
        cr "...Did you even {i}try?{/i}"
        $ play_sound(smash)
        scene black with small_shake
        pause 3
    elif random_choice == 1:
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmm.ogg"
        cr "Holy crap!{w=0.5} Did you guess that right on your first try?"
        "(Huh?{w} Really?)"
        stop music fadeout 0.5
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
        cr "{i}Kidding!{/i}"
        "(You—){w=1}{nw}"
        cr "C'mon,{w=0.1} {i}lighten up.{/i}{w=0.5} Here,{w=0.1} let me help!"
        #"{b}ZAP SFX, CUT TO BLACK{/b}"
        $ play_sound(zap)
        scene black with small_shake
        pause 3

    elif random_choice == 2:
        stop music fadeout 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
        cr "Whoa...{w=0.5} You got it."
        cr "...Did someone write you a walkthrough online?"
        "(Huh?{w} How did you-){w=1}{nw}"
        stop music fadeout 0.5
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        cr "If so,{w=0.1} go complain in the comments."
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
        cr "You've just met a dead end!"
        $ play_sound(smash2)
        pause 0.6
        scene black with small_shake
        pause 3

    elif random_choice == 3:
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
        stop music fadeout 0.5
        cr "You're a fast one,{w=0.1} aren't you?"
        "(Huh?{w} What do you—){w=1}{nw}"
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
        cr "But next time,{w=0.1} {i}do{/i} look before you leap."
        $ play_sound(trapdoor)
        $ queue_sound(buzzsawgore)
        scene black with easeouttop
        pause 3

    elif random_choice == 4:
        stop music fadeout 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
        cr "I see you're the type who likes to gamble."
        cr "Alas,{w=0.1} you didn't hit the jackpot.{w=0.5} Better luck next time!"
        "(You—){w=1}{nw}"
        stop music fadeout 0.5
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        cr "But since you're here,{w=0.1} I'd like to play another game."
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
        cr "Time for a round of Russian Roulette!{w=0.5} Is the gun next to you loaded or not?"
        "(What gu—){w=1}{nw}"
        $ play_sound(gunshot)
        #"{b}GUNSHOT SFX, CUT TO BLACK{/b}"
        scene black with small_shake
        pause 3

    else:
        stop music fadeout 0.5
        voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
        cr "...Wow.{w=0.5} That wasn't even {i}close.{/i}"
        stop music fadeout 0.5
        hide black onlayer screens
        hide screen room2_word
        with puzzle_hide
        pause 0.5
        cr "You'd have better luck smashing keys."
        "(You—){w=1}{nw}"
        cr "Just. {w=0.5}Like. {w=0.5}{i}This.{/i}{w=1}{nw}"
        $ play_sound(smash)
        scene black with small_shake
        pause 3

    $nvl_heading = "Lab Report #404"
    l "Not much to say here."
    l "The lab rat just sucks at word games!"
    l "{b}Contributing Factors to Death:{/b} Should've dipped their toes into a few titles before meeting me. Personally, I recommend {i}Scraddle.{/i}"
    $deadend("dead6")
    le "DEAD END 06: Stop Me If You Think You've Word This One Before..."
    pause 2
    nvl clear
    $game_over(2)
    return
