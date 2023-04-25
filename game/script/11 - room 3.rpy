default room3 = {"room":"down", "solved":[], "pages":[], "read_pages":[], "diary":0, "mannequin":0, "scrapbook":0, "health_record":0, "locked_container":0,
    "confidence_workbook":0, "sewing_book":0, "quilt":0, "cooking":0, "scrapbook_new":0, "toys":0}
default room3_investigated = []

screen room3():
    sensitive (not inspect and not _menu)
    layer "master"
    tag room

    if room3["room"] == "down":
        fixed at zoomed(0.335):
            add "bg room3_downstairs"
            imagebutton idle Null() hover "rooms/room3/downstairs/room3_downstairs_selection_scrapbook.png" action [SetVariable("inspect", "scrapbook"), Jump("room_3")] focus_mask "rooms/room3/downstairs/room3_downstairs_selection_scrapbook.png" mouse "inspect" at room_hover
            imagebutton idle Null() hover "rooms/room3/downstairs/room3_downstairs_selection_workbook.png" action [SetVariable("inspect", "confidence_workbook"), Jump("room_3")] focus_mask "rooms/room3/downstairs/room3_downstairs_selection_workbook.png" mouse "inspect" at room_hover
            imagebutton idle Null() hover "rooms/room3/downstairs/room3_downstairs_selection_lockbox.png" action [SetVariable("inspect", "locked_container"), Jump("room_3")] focus_mask "rooms/room3/downstairs/room3_downstairs_selection_lockbox.png" mouse "inspect" at room_hover

            imagebutton idle Null() hover "rooms/room3/downstairs/room3_downstairs_selection_metapuzzle.png" action [SetVariable("inspect", "scrapbook_new"), Jump("room_3")] focus_mask "rooms/room3/downstairs/room3_downstairs_selection_metapuzzle.png" mouse "puzzle" at room_hover(0.5)
            imagebutton idle Null() hover "rooms/room3/downstairs/room3_downstairs_selection_miseenplace.png" action [SetVariable("inspect", "cooking"), Jump("room_3")] focus_mask "rooms/room3/downstairs/room3_downstairs_selection_miseenplace.png" mouse "puzzle" at room_hover(0.5)

            if 1 in room3["pages"] and 1 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note1.png" hover "rooms/room3/room3_note1.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 1), Jump("room_3")] pos (834, 2859) mouse "inspect"
            if 2 in room3["pages"] and 2 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note2.png" hover "rooms/room3/room3_note2.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 2), Jump("room_3")] pos (4944, 2568) mouse "inspect"
            if 6 in room3["pages"] and 6 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note6.png" hover "rooms/room3/room3_note6.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 6), Jump("room_3")] pos (4665, 3034) mouse "inspect"
        if not inspect:
            textbutton _("UP") action [SetDict(room3, "room", "up"), Play("sound", "audio/sfx/Room 3 SFX/Stairs 1.ogg"), With(Fade(1,0.5,1))] style "main_menu_button" xalign 0.94 yalign 0.4

    elif room3["room"] == "up":
        fixed at zoomed(0.335):
            add "bg room3_upstairs"
            imagebutton idle Null() hover "rooms/room3/upstairs/room3_upstairs_selection_sewingkit.png" action [SetVariable("inspect", "sewing_book"), Jump("room_3")] focus_mask "rooms/room3/upstairs/room3_upstairs_selection_sewingkit.png" mouse "inspect" at room_hover
            imagebutton idle Null() hover "rooms/room3/upstairs/room3_upstairs_selection_wigmannequin.png" action [SetVariable("inspect", "mannequin"), Jump("room_3")] focus_mask "rooms/room3/upstairs/room3_upstairs_selection_wigmannequin.png" mouse "inspect" at room_hover
            imagebutton idle Null() hover "rooms/room3/upstairs/room3_upstairs_selection_healthrecord.png" action [SetVariable("inspect", "health_record"), Jump("room_3")] focus_mask "rooms/room3/upstairs/room3_upstairs_selection_healthrecord.png" mouse "inspect" at room_hover

            imagebutton idle Null() hover "rooms/room3/upstairs/room3_upstairs_selection_quiltpuzzle.png" action [SetVariable("inspect", "quilt"), Jump("room_3")] focus_mask "rooms/room3/upstairs/room3_upstairs_selection_quiltpuzzle.png" mouse "puzzle" at room_hover(0.5)
            imagebutton idle Null() hover "rooms/room3/upstairs/room3_upstairs_selection_plushpuzzle.png" action [SetVariable("inspect", "toys"), Jump("room_3")] focus_mask "rooms/room3/upstairs/room3_upstairs_selection_plushpuzzle.png" mouse "puzzle" at room_hover(0.5)

            if 3 in room3["pages"] and 3 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note3.png" hover "rooms/room3/room3_note3.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 3), Jump("room_3")] pos (4112, 2632) mouse "inspect"
            if 4 in room3["pages"] and 4 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note4.png" hover "rooms/room3/room3_note4.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 4), Jump("room_3")] pos (1356, 2968) mouse "inspect"
            if 5 in room3["pages"] and 5 not in room3["read_pages"]:
                imagebutton idle "rooms/room3_note5.png" hover "rooms/room3/room3_note5.png" action [SetVariable("inspect", "diary"), AddToSet(room3["read_pages"], 5), Jump("room_3")] pos (4900, 2456) mouse "inspect"

        if not inspect:
            textbutton _("DOWN") action [SetDict(room3, "room", "down"), Play("sound", "audio/sfx/Room 3 SFX/Stairs 2.ogg"), With(Fade(1,0.5,1))] style "main_menu_button" xalign 0.97 yalign 0.97

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_room_3")] style "main_menu_button"


label room_3:
    if inspect not in room3_investigated and inspect in ["sewing_book", "scrapbook", "health_record", "locked_container", "confidence_workbook", "mannequin"]:
        $room3_investigated.append(inspect)
    show screen room3
    $renpy.block_rollback()

    if inspect == "mannequin":
        if room3["mannequin"] == 0:
            show room3_wig with dissolve:
                yalign 0.2 xalign 0.5
            "(When you look at the bust in front of you,{w=0.1} you recall a half-serious lesson on disguising yourself back when you were a trainee.)"
            "(From what you remember,{w=0.1} this appears to be a mannequin for a wig.)"
            "(But Dr. Danger had a full head of hair.)"
            "(Did she need to disguise herself?{w} Intel's always suggested that her mastery over tech kept her off any camera she cared about.)"
            hide room3_wig with dissolve
        else:
            show room3_wig with dissolve:
                yalign 0.2 xalign 0.5
            "(It's a wig mannequin.{w} But it doesn't seem to be Dr. Danger's...)"
            hide room3_wig with dissolve
        $ room3["mannequin"] += 1

    elif inspect == "scrapbook":
        if room3["scrapbook"] == 0:

            ### sound of paper being picked up
            show room3_scrapbookcg with dissolve:
                yalign 0.2 xalign 0.5
            $ play_sound(paperpickup)
            "(You pick up what appears to be a generic scrapbook,{w=0.1} like those shoved to the back shelves of charity stores.{w} Looking closely, you can still see remnants of price sticker glue.)"
            "(It feels normal.{w} {i}Too{/i} normal.{w} The book's clearly hiding some deep,{w=0.1} dark{w=0.1} secret.)"
            $ play_sound(paperturn)
            "(But the inner contents are equally...{w=0.5} {i}normal.{/i})"
            "(All you find are photographs of a woman who looks a lot like Dr. Danger,{w=0.1} and a young boy with a crooked,{w=0.1} toothy{w=0.1} grin.)"
            "(The craftsmanship on display isn't anything remarkable,{w=0.1} with poorly cut edges and tacky glitter glue smeared across the cheap cardstock.)"
            "(At least the pages seem to be in chronological order.)"
            $ play_sound(paperturn)
            "(In the earliest photos,{w=0.1} the boy is bedridden.{w} His skin is unnaturally pale,{w=0.1} and his gaze is unfocused —{w=0.5} empty, even.)"
            $ play_sound(paperturn)
            "(But as you flick though the pages,{w=0.1} he grows stronger.)"
            "(He gets out of bed.{w} His eyes shine with inspiration and intelligence.{w} He smiles.)"
            pause 1
            "(The woman in these photos must've been taking good care of him.)"
            pause 1
            $ play_sound(paperturn)
            "(The later photos are self-explanatory.{w} Each moment is carefully dated and annotated.{w} Playing videogames,{w=0.1} reading bedtime stories...{w=0.5} and what seems to be a movie night.)"
            "(You know the film they're watching.{w} It's that one cartoon about an alien supervillain;{w=0.5} one with a very big brain,{w=0.1} but very little common sense.)"
            pause 0.5
            "(...Hold on.{w} Wasn't the film released in cinemas three months after the time written down?)"
            "(...)"
            "(Looks like STOP will have to add digital piracy to Dr. Danger's long list of crimes.)"
            hide room3_scrapbookcg with dissolve
        else:
            "(A surprisingly ordinary scrapbook.{w} Featuring crimes against copyright.)"
        $ room3["scrapbook"] += 1

    elif inspect == "health_record":
        if room3["health_record"] == 0:
            ### sound of paper being picked up
            show room3_report with dissolve:
                yalign 0.2 xalign 0.5
            $ play_sound(paperpickup)
            "(You pick up a clipboard with a thick stack of charts and diagrams pinned to the front.)"
            "(\"SUBJECT RECUPERATION LOG\" is printed at the top in a harsh,{w=0.1} black{w=0.1} lettering.{w} At the bottom of the page,{w=0.1} you spot an acronym:{w=0.5} \"YTDI\".)"
            $ play_sound(paperturn)
            "(You flip through the log.{w} The recuperation described here is difficult to read.)"
            "(Seizures,{w=0.1}  phantom pain,{w=0.1}  memory loss{w=0.1}  and brain damage are all expected results,{w=0.1} not side effects.)"
            "(Scrawled notes speculate that these symptoms would last for several years or decades —{w=0.5}  perhaps even permanently.)"
            "(Implanting cybernetics in individuals under 18 isn't illegal,{w=0.1} but it {i}is {/i} frowned upon.)"
            "(And from the logbook,{w=0.1} a lot of children were implanted.{w=0.5} Children well under the age of 18.)"
            "(There's nothing here about informed consent or parental permissions.)"
            "(Evidently,{w=0.1} parents weren't involved.)"
            hide room3_report with dissolve
        else:
            show room3_report with dissolve:
                yalign 0.2 xalign 0.5
            "(You don't really want to touch that clipboard again.{w} It gives you...{w=0.5} a {i}sinking{/i} feeling.)"
            hide room3_report with dissolve
        $ room3["health_record"] += 1

    elif inspect == "sewing_book":
        if room3["sewing_book"] == 0:
            show room3_sewingsetup with dissolve:
                yalign 0.2 xalign 0.5
            "(You find an assortment of patterns,{w=0.1}  books,{w=0.1}  and materials for sewing.)"
            "(There's a little stack of half-finished items.{w=0.5} A skirt and a blouse in conservative colors.{w} Right next to it,{w=0.1} a whole pile of hand-stitched garments in garish yellows,{w=0.1} greens,{w=0.1} and reds.)"
            "(Seems like someone handed their sewing books down to a more imaginative type.)"
            "(You're well aware that sewing isn't just a simple hobby.{w} Many of STOP's associated security forces take up the practice when their first cybernetics are implanted.)"
            "(After such a big operation,{w=0.1} fine needlework quickly rehabilitates hand-eye coordination.)"
            "(But you doubt they'd make such a large collection of fuzzy mittens.)"
            hide room3_sewingsetup with dissolve
        else:
            show room3_sewingsetup with dissolve:
                yalign 0.2 xalign 0.5
            "(A superb sewing setup.{w} But what's with all the mittens?{w} It's not winter anymore.)"
            hide room3_sewingsetup with dissolve
        $ room3["sewing_book"] += 1

    elif inspect == "locked_container":
        if room3["locked_container"] == 0:
            "(This appears to be a locked box...{w=0.5}but it's without a lock.{w} You give the lid a small tug, and it opens.)"
            $ play_sound(boxunlock)
            $ queue_sound(boxopen)
            pause 2
            "(There's no dust inside,{w=0.1}  but a stale odor wafts out.{w} Clearly, this hasn't been opened for a long time.)"
            show room3_lockedbox with dissolve:
                yalign 0.2 xalign 0.5
            "(You find a lab coat with an ID pinned above its breast pocket.{w} There's no photo,{w=0.1}  but the name \"Deirdre Destrange\" is clearly printed on the plastic card alongside a worn barcode.)"
            "(The coat itself is high-quality,{w=0.1} but it's worn around the edges.{w} Deirdre must've used it for a long time,{w=0.1}  taking good care of it all the while.)"
            "(You see framed photos,{w=0.1} diplomas,{w=0.1}  certificates and awards —{w=0.5} all of them belonging to this \"Deirdre Destrange\".)"
            "(In and of itself,{w=0.1} a doctorate in cybernetic biology is impressive,{w=0.1} but Destrange received this {i}years{/i} ago.)"
            "(To be {i}that {/i}experienced at a young age,{w=0.1}  and when the science was still so {i}new...{/i}{w=0.5} she must've been on the cutting edge of the field.)"
            "(At the bottom of the pile,{w=0.1} you find a dented,{w=0.1} dusty medal. {w}An award for \"continued service to the international security community\"?)"
            "(The medal's name has been violently scratched out. {w}And yet,{w=0.1} you think you see the remnants of a familiar logo...)"
            hide room3_lockedbox with dissolve
        else:
            "(Seems like the contents of this container were meant to be kept a secret.{w} Maybe it's better to leave it be.)"
        $ room3["locked_container"] += 1

    elif inspect == "confidence_workbook":
        if room3["confidence_workbook"] == 0:
            ### sound of paper being picked up
            show room3_notebook with dissolve:
                yalign 0.2 xalign 0.5
            $ play_sound(paperpickup)
            "(It's a crumpled,{w=0.1} heavily worked-over notebook filled with grandiose ramblings in the third person.)"
            "(Lots of exclamation points and capital letters and ego-massaging in spidery handwriting.)"
            $ play_sound(paperturn)
            "(But the more you flip back through the pages,{w=0.1} the more the writing grows negative in tone.)"
            "(A second distinct set of handwriting accompanies the first,{w=0.1} leaving notes on how to aim the subject matter in a more positive direction.)"
            $ play_sound(paperturn)
            "(Even further back,{w=0.1} the spidery handwriting disappears altogether.{w} Instead,{w=0.1} there are grids and examples written with clean,{w=0.1} crisp penmanship.)"
            "(Shaky,{w=0.1} barely-legible scribbles sit below,{w=0.1} rounding out vague, letter-like shapes.)"
            "(It almost looks like a therapeutic exercise —{w=0.5} or a homework assignment.{w} Maybe it's both.)"
            "(What's clear is that the notebook's author hasn't used it for a long,{w=0.1} long{w=0.1} time.)"
            hide room3_notebook with dissolve
            "(Personally,{w=0.1} you wouldn't be caught dead using the third person.)"
            "({i}You{/i} only use the second person.{w} And even then,{w=0.1} only for gathering your thoughts in high-stakes scenarios.)"
        else:
            show room3_notebook with dissolve:
                yalign 0.2 xalign 0.5
            "(A crumpled,{w=0.1} heavily worked-over notebook.{w} It clearly hasn't been used in a while.)"
            hide room3_notebook with dissolve
        $ room3["confidence_workbook"] += 1

    elif inspect == "diary":
        $ nvl_heading = "Entry Set #" + str(room3["diary"]+1)
        if room3["diary"] == 0:
            $ play_sound(paperpickup)
            "(It's a loose page with handwriting on it.{w} Judging by the number in the corner and the fading ink,{w=0.1} it must be a small part of a much larger document.)"
            #"FIRST ENTRIES"
            n "\"It's nice to have job security right out of school.{w} I had my doubts during junior year, of course, but I don't think anyone could've predicted how the sector's grown these past few months."
            if gui.text_size > 40:
                n "The developments in cybernetic technology have been explosive."
                n "Sometimes {i}literally.{/i}"
            else:
                n "The developments in cybernetic technology have been explosive.\n{w}Sometimes {i}literally.{/i}"
            nvl clear
            $ play_sound(paperturn)
            n "It's troubling, but all great technology has the potential for misuse.\n{w}And now I'm going to be part of an organization that works to keep that tech under control. "
            n "Though I'll be honest, the name's pretty silly."
            n "Oh well.{w} They could always change the acronym later.\""
        elif room3["diary"] == 1:
            #"SUCCESS WITH LIMITING PROLIFERAITON OF TECH, PROMOTION, DISCOVERY OF POTENTIAL FOR YOUNGER SUBJECTS"
            $ play_sound(paperpickup)
            n "\"I thought that things were moving fast before — but the growth we're seeing now makes those earlier years look glacial."
            n "STOP is doing good work that needs to get done, and it's making countries put money where their mouths are when it comes to international cooperation efforts."
            nvl clear
            $ play_sound(paperturn)
            n "Last month, we managed to craft a Digital Data Management system that could tell us whenever a dangerous cybernetic schematic was downloaded and where it was downloaded to."
            n "This month, we finalized our report on maximizing cybernetic synchronization for patients — confirming my earlier theory that the younger, the better. "
            n "The difference really was astounding.{w} And I must admit, it felt good to shove that 19\% performance increase right in that stuffy old bastard's smug face.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"Dr. Tan asked if the trend in performance would improve further if we started surgery any earlier."
            n "A weird question, since this tech is only approved for anyone old enough to enlist, but I guess she was just being thorough."
            n "The theory is sound.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"The promotion was nice."
            n "I deserve it, and I was the only obvious choice, but still.{w} It felt nice to be recognized.\""
        elif room3["diary"] == 2:
            #"STAGNATION, LOTS OF RESEARCH WORK DISILLUSIONMENT, PARANOIA"
            $ play_sound(paperpickup)
            n "\"Another month where the Security Advisory Council looked completely lost.{w} It's like they don't know what to do with peacetime."
            n "They do amazing work — obviously.{w} The world is secure, and cybernetic technology is finally getting regulated.{w} The laws are catching up with the science."
            n "That's a good thing, even if it makes their job a little less\nexciting."
            n "Or maybe a little less secure.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I requested another transfer.{w} My third in three years, but they didn't seem to mind."
            n "I just can't find work as engrossing as I used to.{w} It probably doesn't help that I'm not sure what it is I do anymore. "
            if gui.text_size > 40:
                n "I mean, logically, I know what I do — I research cybernetics.\n{w}But I'm not sure what I do for STOP.\""
            else:
                n "I mean, logically, I know what I do — I research cybernetics."
                n "But I'm not sure what I do for STOP.\""
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"STOP hasn't had a major security incident in months."
            n "The last \"incident\" they responded to was just a protest outside the building that got a little rowdy."
            n "Staff morale's been down ever since.{w} A little controversy's to be expected, given the power STOP has nowadays."
            n "They're being naive if they expect people to be grateful to the organization forever.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I might've transferred a few times too many."
            n "I came into work today and clocked out without recognizing a single face the entire time.{w} New people, places, committees, projects, and always more acronyms. "
            n "And, for the first time in years, I was denied access to internal data."
            n "I didn't think anything could be above my paygrade anymore.\n{w}Note to self: look up \"YTDI \"."
        elif room3["diary"] == 3:
            #"Meeting CAUTIONNE"
            $ play_sound(paperpickup)
            n "\"\'I was very disappointed with the state of the Youth Training and Development Initiative.\'"
            n "That's how I put it in writing. "
            n "I don't really have the right words to express my disgust with this program's existence."
            nvl clear
            $ play_sound(paperturn)
            n "The idea that cybernetic sync rates increase the earlier in life treatment starts was based on a completely different timeline — assuming that we were talking about 18 vs 24.\n"
            n "It was never supposed to justify...{w} whatever the hell they're doing now.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"They don't actually care about reducing rejection symptoms or making the cybernetics work more seamlessly."
            n "They care about creating a product by experimenting on children.\n{w}Children that no one else cares about."
            if gui.text_size > 40:
                $ play_sound(paperturn)
                nvl clear
            else:
                $ play_sound(paperturn)
                nvl clear
            n "They want to produce cybernetic \"Trainees\" that are powerful, unthinking, and unflinchingly obedient to authority. "
            n "STOP plans to sell these trainees as a force to keep its donors on top.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I got a transfer to the YTDI as a supervisor.{w} No one even seemed ashamed to give me full access."
            n "I get the sense that my superiors aren't paying attention to what is happening.{w} That might be the most infuriating part for me —{w=0.5} they don't care whether this program succeeds or fails. "
            n "The implication I'm getting is that this is far from the only program of its kind.{w} It might be one of many, many more.\""
            nvl hide
            nvl clear
        elif room3["diary"] == 4:
            #"MEETING CAUTIONNE AND FLEEING"
            nvl show
            $ play_sound(paperpickup)
            n "\"He smiled at me. "
            n "Even though everyone else he's seen here —{w=0.5} everyone dressed like me, acting like me, working for the same people as me —{w=0.5} has made him suffer. "
            n "He {i}smiled{/i} at me.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I'm getting better at coming up with excuses to visit him, at least."
            n "I need to evaluate how he's coping with procedures - just like the other YTDI trainees."
            n "I might need to test his reflexes."
            n "Hell, he might need a snack to make him more cooperative."
            nvl clear
            $ play_sound(paperturn)
            n "All my explanations are superficially believable at best."
            n "I'm no medical professional.{w} I'm a supervisor - I oversee things."
            n "By all means, I should've been reprimanded for getting too involved."
            n "But no such warnings have come my way.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I'm never going to be able to forget the look on his face when the convulsions started. "
            n "He knew it was coming, and he knew there was nothing he could do to even brace himself for the pain. "
            n "He's been through it countless times.{w} I don't want to see it ever again.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"They claimed that it was a clerical error that he didn't receive his anti-seizure medications that morning. "
            n "I know that it was actually punishment.{w} He refused to obey during yesterday's mandatory exercises. "
            n "You wouldn't treat an {i}animal{/i} like this, much less another human."
            n "To them, he's less than that.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I triggered the false alarm right on schedule, down to the second."
            n "My not-at-all false explosive followed suit."
            n "I had always understood that the chemical reaction was very simple to set up."
            n "But, I still expected my first felony to present more challenges than this.{w} Maybe I have a knack for this kind of thing."
            nvl clear
            $ play_sound(paperturn)
            n "He didn't hesitate for one second when I asked him to come with me.{w} As I rushed him through the fire exit, the look on his face at that moment has stuck with me."
            n "Could anyone have looked more relieved?\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"Maybe he should have hesitated.{w} All that awaits him is a life in hiding."
            n "..."
            n "...At least he'll have a choice from now on.\""
        elif room3["diary"] == 5:
            $ play_sound(paperpickup)
            n "\"I've no right to call myself a parent, but even so —{w=0.5} parenthood is hard. "
            n "His rehab is going as well as can be expected, but this is no way to raise a child."
            n "I can educate him, keep him fed, and care for him."
            n "But I can't give him any kind of a future —{w=0.5} not while STOP is trying to erase our very existence.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"I managed to section away enough resources to last us a while, but all my internal records within STOP were destroyed by the fire. "
            n "They still know I'm out here, but now I have no proof that I was ever as big a part of them as I say."
            n "It's my word against theirs, and they have far larger, more powerful allies.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"Bombs, sabotage, and cryptic messages on shady websites get much better traction than just sending my research notes to major news outlets."
            n "No one cares what Deirdre Destrange has to say.{w} But when \"Dr. Danger\" blows up an energy pipeline, people look up from their food and {i}watch.{/i}"
            n "He chose the name.{w} It's got a nice, old-school appeal to it.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"Cautionne has always been eager to please and happy to spend time with me.{w} Is it any wonder he wants to help the nefarious Dr. Danger in her fight?"
            n "I should tell him no.{w} Revenge is poison, and he's already been through too much. "
            n "But I still can't bear to calculate how much of his suffering is my fault.{w} I don't have the heart to tell him no — and I'd sooner die than judge him for how much he hates STOP.\""
            nvl hide
            $ play_sound(paperturn)
            pause 2
            nvl clear
            nvl show
            n "\"Dr. Danger and Cautionne are becoming a household name, but that's about it. "
            n "STOP is still in power.{w} People are still too scared to take them to task.{w} And there are still YTDI centers all over the world."
            n "If I destroy one, they move the children to another."
            $ play_sound(paperturn)
            nvl clear
            n "That's horrible as-is, but what if they don't care enough to do even that?"
            n "What if they believe the YTDI is just not worth the cost?"
            n "What'll happen to those children then?"
            $ play_sound(paperturn)
            nvl clear
            n "Something needs to change, but I'm not sure it's something that Dr. Danger can do. "
            n "...And I'm not sure that Deirdre Destrange is enough for him.\""
            $room3_investigated.append("diary")
        $ room3["diary"] += 1
        nvl clear

    elif inspect == "quilt":
        if "quilt" in room3["solved"]:
            "(You've already solved the quilt puzzle.)"
        else:
            if room3["quilt"] == 0:
                $quilt_reset()
                "(Ouch!)" with vpunch
                "(Seems like you stepped on a rogue sewing pin.)"
                show screen room3_quilt(_layer="master") with easeintop
                "(What's a large, unfinished sewing project doing, all spread out on the floor?)"
                "(Looks like a quilt.{w} Must've been too big for the little sewing desk.)"
                "(Hmm...{w} For some reason, you want to finish it.)"
            else:
                show screen room3_quilt(_layer="master") with easeintop
                "(Before you sit down with the quilt,{w=0.1} you carefully inch your way around the stray pins on the floor.)"
            $renpy.block_rollback()
            $ room3["quilt"] += 1
            $ inspect = None
            $renpy.hide_screen("room3_quilt", "master")
            call screen room3_quilt
            if room3["quilt"] == "solved":
                jump quilt_solved

    elif inspect == "toys":
        if "toys" in room3["solved"]:
            "(You've already solved the plushie puzzle.)"
        else:
            if room3["toys"] == 0:
                call init_toy_board from _call_init_toy_board
                "(There are a few plushies sitting on the shelf.{w} They're suprisingly soft!)"
                "(You investigate the cupboard below the plushies where—{w=0.5} {i}woah!{/i})"
                $play_sound(plushiesqueak)
                $queue_sound(plushiesqueak)
                show screen toy_playspace(tb, False, _layer="master") with easeintop
                "(An avalanche of plushies spills out,{w=0.1} burying you in a soft, fuzzy pile.)"
                "(This {i}would{/i} be a comfy way to go out,{w=0.1} but you should probably put everything back.)"
            else:
                "(A pile of plushies sprawl out on the bed, right where you left them.)"
                show screen toy_playspace(tb, False, _layer="master") with easeintop
                "(Okay,{w=0.1} one more time.{w} Just gotta neatly sort the toys neatly into sets...)"
            $renpy.block_rollback()
            $ room3["toys"] += 1
            $ inspect = None
            $renpy.hide_screen("toy_playspace", "master")
            call screen toy_playspace(tb)
            if room3["toys"] == "solved":
                jump toys_solved

    elif inspect == "cooking":
        if "cooking" in room3["solved"]:
            "(You've already solved the {i}mise en place{/i} puzzle.)"
        else:
            if room3["cooking"] == 0:
                $init_mise_en_place()
                "(There's a small kitchenette.{w} It looks like it hasn't been used recently...)"
                "(Did Dr Danger take care of all the cooking?)"
                show screen mise_en_place(False, _layer="master") with easeintop
                "(A handwritten note sits on the counter.{w} Looks like...{w=0.5}a recipe for pancakes?)"
                "(Fridge seems well stocked too.{w} Let's see if Cautionne likes your take on Dr Danger's recipe.)"
            else:
                show screen mise_en_place(False, _layer="master") with easeintop
                "This recipe seems simple enough.{w} One more time..."
            $renpy.block_rollback()
            $ room3["cooking"] += 1
            $ inspect = None
            $renpy.hide_screen("mise_en_place", "master")
            $ renpy.retain_after_load()
            call screen mise_en_place(True)
            if room3["cooking"] == "solved":
                jump cooking_solved

    elif inspect == "scrapbook_new":
        if room3["scrapbook_new"] == 0:
            $scrapbook_init()
            $ room3["scrapbook_new"] = 1
            show screen room3_meta(_layer="master") with easeintop
            "(The \"lock\" for the door is a...{w=0.5} scrapbook?{w} Its pages are empty,{w=0.1} though...)"
        else:
            show screen room3_meta(_layer="master") with easeintop
        $renpy.block_rollback()
        $ inspect = None
        $renpy.hide_screen("room3_meta", "master")
        call screen room3_meta
        if room3["scrapbook_new"] == "solved":
            jump post_room_3

    $inspector_achievement()

    $ inspect = None
    $renpy.block_rollback()
    call screen room3

label scrapbook_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room3_meta
    show black onlayer screens with dissolve:
        alpha 0.5

    stop music fadeout 1.0

    "(You place the scrapbook down to get a fresh look at what you've got so far.)"
    "(But when you step back,{w=0.1} you feel like {i}something's{/i} out of place.)"
    "(And if {i}you {/i}can tell,{w=0.1} then {i}he {/i}can tell.{w} Better—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "It's okay to suck at arts and crafts, lab rat.{w=0.5} Not everyone's born to make masterpieces."
    hide black onlayer screens
    hide screen room3_meta
    with puzzle_hide
    pause 1
    cr "But...{w=0.5} that scrapbook meant a lot to me."
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "If you were gonna screw up {i}that {/i}badly,{w=0.1} you could've at least used the {i}non-permanent{/i} glue."
    "(A bead of sweat trickles down your back.)"
    "(Was...{w=0.5} was that an option?)"
    cr "...Wait,{w=0.1} I left that out,{w=0.1} didn't I?"
    cr "My bad!{w=0.5} If memory serves me,{w=0.1} this button should—"
    $ play_sound(switchon)
    pause 1
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmm.ogg"
    $ play_sound(lazercharge)
    cr "Whoopsie doopsie!{w=0.5} Looks like I pressed the wrong—{w=1}{nw}"
    $ play_sound(lazerblast)

    scene black with small_shake
    pause 3
    $nvl_heading = "Lab Report #891"
    l "Subject succeeded in proving the fatality of ray gun protoype Delta-9."
    l "{b}Contributing Factors to Death:{/b} They messed up my scrapbook — so now, we're even!"

    $deadend("dead10")
    le "DEAD END 10: Holy Scrap!"
    pause 2
    nvl clear
    $game_over(3)
    return

label quilt_solved:
    $renpy.block_rollback()
    $ inspect = "quilt"
    show screen room3_quilt
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room3["solved"].append("quilt")
    $ room3["pages"].append(1)
    $ room3["pages"].append(5)
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen room3_quilt
    with puzzle_hide
    pause 0.1
    show memory1:
        xalign 0.5 yalign 0.1 alpha 0
        ease 1 xalign 0.5 yalign 0.3 alpha 1
    pause 1
    "(You notice that you can now lift up the quilt.{w} There's a photo underneath it.)"
    "(Something is written on the back.)"
    nvl clear
    $ nvl_heading = ""
    n "There was all this heat and smoke and energy.{w} There were alarms blaring and people shouting."
    n "That's what she told me,{w=0.1} but I barely remember any of it."
    nvl clear
    n "Here's what I did remember.{w} When we stopped running,{w=0.1} she seemed more tired than I was."
    n "She did carry me the entire time.{w} But she didn't seem any weaker than before.{w} Her hold on my body didn't loosen."
    n "She was just looking at what was left of my shoulder."
    nvl clear
    n "I was hurting like you wouldn't believe.{w} But I don't think I cared."
    n "Because,{w=0.1} that day,{w=0.5} I got to see the sky again."
    nvl clear
    hide memory1 
    with dissolve
    "(...)"
    $ inspect = None
    call screen room3

label quilt_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen room3_quilt
    show black onlayer screens with dissolve:
        alpha 0.5
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    stop music fadeout 1.0
    cr "{i}Wow.{/i}{w=0.5} You're far from delicate,{w=0.1} aren't you?"
    hide black onlayer screens
    hide screen room3_quilt
    with puzzle_hide
    pause 1
    cr "I'd like to think of myself as a lenient kinda guy... {w}But watching you butcher that sentimental quilt is {i}pretty painful.{/i}"
    cr "Like,{w=0.1} a death by a thousand cuts...{w=0.5}{nw}"
    cr "...or needles,{w=0.1} in this case."
    $ play_sound(switchon)
    "(You hear a switch go off,{w=0.1} and—){w=1}{nw}"
    $ play_sound(piercings)
    scene black
    pause 1
    $ queue_sound(bodypierce)
    scene black with small_shake

    #{i}{b}[sound of protag getting stabbed with needles]{/b}{/i}

    pause 3
    nvl clear

    $nvl_heading = "Lab Report #112"
    if gui.text_size > 40:
        l "Subject failed to appreciate the value of good stitchwork, and so was impaled by a thousand and twenty-four needles.\n{p}{i}(NB: It needed to be a square number for the triggering mechanism to hit its mark.){/i}"
    else:
        l "Subject failed to appreciate the value of good stitchwork, and so was impaled by a thousand and twenty-four needles."
        l "{i}(NB: It needed to be a square number for the triggering mechanism to hit its mark.){/i}"
    l "{b}Contributing Factors to Death:{/b} Couldn't sew their way out of a wet paper bag."
    $deadend("dead11")
    le "DEAD END 11: Quilt In Action."
    pause 2
    nvl clear
    $game_over(3)
    return

label toys_solved:
    $renpy.block_rollback()
    $ inspect = "toys"
    show screen toy_playspace(tb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room3["solved"].append("toys")
    $ room3["pages"].append(2)
    $ room3["pages"].append(4)
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen toy_playspace
    with puzzle_hide
    pause 0.1
    show memory3:
        xalign 0.5 yalign 0.1 alpha 0
        ease 1 xalign 0.5 yalign 0.3 alpha 1
    pause 1
    "(One of the plushies rips open,{w=0.1} revealing a photo inside.)"
    "(Turning it around reveals text reminiscent of a diary entry.)"
    nvl clear
    $ nvl_heading = ""
    if gui.text_size > 40:
        n "She told me to explore the place.{w} She said it was important that I adjust to my new environment, {w=0.1}but she's been holed up in the lab."
    else:
        n "She told me to explore the place.{w} She said it was important that\nI adjust to my new environment, {w=0.1}but she's been holed up in the lab."
    n "I don't know why she's so stressed about my surgeries.{w} She's the smartest person I know.{w} And I grew up surrounded by \"brilliant\" scientists,{w=0.1} so that's saying {i}something{/i}."
    nvl clear
    n "She says she's still concerned about making adjustments to my synthetic nerves.{w} That she's worried she'll put me through even more pain."
    n "But every time she's worked on my new limbs,{w=0.1} I haven't felt a thing."
    n "Last time,{w=0.1} I actually fell asleep."
    nvl clear
    hide memory3 with dissolve
    "(...)"
    $ inspect = None
    call screen room3

label toys_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen toy_playspace(tb, False)
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 1.0
    $ play_sound(plushiesqueak)
    "(You set down the toys and pause to think.)"
    "(The task is a lot harder than you thought it would be.{w} Maybe—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
    cr "Having trouble organizing?{w=0.5} I get it."
    hide black onlayer screens
    hide screen toy_playspace
    with puzzle_hide
    pause 1
    cr "I was {i}horrible{/i} at putting my stuff away.{w=0.5}  A total mess,{w=0.1} every time."
    cr "But whenever I got into a pickle,{w=0.1} Dr. Danger always helped me out."
    pause 1
    cr "...Hey,{w=0.1} remind me."
    cr "Where {i}is{/i} Dr. Danger right now?"
    "(The sudden quietness in his voice makes you freeze.)"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    cr "{i}Right.{/i}"

    $ play_sound(trapdoor)
    $ queue_sound(falling)
    $ queue_sound(buzzsawgore)

    scene black with easeouttop

    pause 3
    #{i}{b}SLICING SFX, CUT TO BLACK{/b}{/i}"

    $nvl_heading = "Lab Report #414"
    l "Subject was transported to the automated disposal unit via trap door, whereupon the automated disposal department did what it does best."
    l "{b}Contributing Factors to Death:{/b} Expected leniency where there was none to be found."
    $deadend("dead12")
    le "DEAD END 12: Get Stuffed."
    pause 2
    nvl clear
    $game_over(3)
    return

label cooking_solved:
    $renpy.block_rollback()
    $ inspect = "cooking"
    show screen mise_en_place(False)
    show black onlayer screens with dissolve:
        alpha 0.5
    $ room3["solved"].append("cooking")
    $ room3["pages"].append(3)
    $ room3["pages"].append(6)
    $ play_sound(puzzlesuccess)
    "You solved the puzzle!"
    hide black onlayer screens
    hide screen mise_en_place
    with puzzle_hide
    "(Suddenly,{w=0.1} the stove pops open.)"
    pause 0.1
    show memory2:
        xalign 0.5 yalign 0.1 alpha 0
        ease 1 xalign 0.5 yalign 0.3 alpha 1
    pause 1
    "(There's a photo inside of it,{w=0.1} with text written on the back.)"
    nvl clear
    $ nvl_heading = ""
    n "I don't remember what the food was like at the orphanage."
    n "Probably bland."
    n "I wish I could forget what LabScrip tastes like…{w=0.5} but meals were usually the least painful part of my day in the lab,{w=0.1} so I've got a soft spot for the stuff."
    n "But that wasn't food.{w} It was nutritious and edible and nothing more.{w} It didn't fill you up.{w} It wasn't warm.{w} There certainly was no thought in it at all."
    nvl clear
    n "Pancakes are food.{w=0.5} They sizzle in the pan and curl at the edges,{w=0.1} bubbling slightly when it's time to flip.{w}\nYou can undercook them or burn them,{w=0.1} bury them in toppings or eat them with your hands.{w} They're filling,{w=0.1} and tasty,{w=0.1} and oh-so warm."
    n "I'm sure I could easily re-create her recipe.{w} It's hardly rocket science, even with one arm."
    n "But I've never had someone cook for {i}me{/i} before."
    n "...I'd like to pretend I'm not capable for a little while longer."
    nvl clear
    hide memory2 with dissolve
    "(...)"
    $ inspect = None
    call screen room3

label cooking_game_over:
    $renpy.block_rollback()
    $ inspect = "game over"
    show screen mise_en_place(False)
    show black onlayer screens with dissolve:
        alpha 0.5
    stop music fadeout 1.0
    "({i}There.{/i}{w} That should be the right ingredients for the pancakes.{w} Now if you pour the batter—){w=1}{nw}"
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Shut Up 1.ogg"
    cr "{i}Stop right there,{/i} lab rat.{w=0.5} I don't want that {i}affront{/i} to all things edible anywhere near my nice,{w=0.1} tasteful,{w=0.1} kitchen appliances."
    hide black onlayer screens
    hide screen mise_en_place
    with puzzle_hide
    pause 1
    cr "How the {i}hell{/i} do you screw up pancakes that bad?{w=0.5} Did STOP mangle your common sense as well as your brains?"
    "(You open your mouth to protest and—){w=1}{nw}"

    $ play_sound(smash)

    scene black with small_shake

    # {b}[SPLAT sound]{/b}
    # {b}[death screen]{/b}

    pause 3
    nvl clear

    $nvl_heading = "Lab Report #406"
    l "Subject perished soon (but not soon enough) after being plastered against the wall by a gigantic frying pan-shaped mallet."
    l "Good riddance, although I have to admit, I was looking for an opportunity to get a use out of that particular trap."
    l "{b}Contributing Factors to Death:{/b} Committed sacrilege against breakfast food."
    $deadend("dead13")
    le "DEAD END 13: Flipping Miserable!"
    pause 2
    nvl clear
    $game_over(3)
    return
