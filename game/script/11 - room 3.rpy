default room3 = {"investigated":[], "diary":0, "room":"down"}

screen room3():
    sensitive not inspect
    layer "master"
    if room3["room"] == "down":
        fixed at zoomed(0.35):
            add "bg room3_downstairs"
            imagebutton idle "room3_mannequin" action [SetVariable("inspect", "mannequin"), Jump("room_3")] pos (3575, 1150) at zoomed(0.2)

        textbutton _("UP") action SetDict(room3, "room", "up") style "main_menu_button" xalign 0.97 yalign 0.6
    elif room3["room"] == "up":
        fixed at zoomed(0.35):
            add "bg room3_upstairs"
            imagebutton idle "room3_scrapbook" action [SetVariable("inspect", "scrapbook"), Jump("room_3")] pos (3575, 1150) at zoomed(0.2)
            imagebutton idle "room3_diary" action [SetVariable("inspect", "diary"), Jump("room_3")] pos (2575, 2150) at zoomed(0.4)
        textbutton _("DOWN") action SetDict(room3, "room", "down") style "main_menu_button" xalign 0.97 yalign 0.97

label room_3:
    if inspect not in room3["investigated"]:
        $room3["investigated"].append(inspect)
    show screen room3
    if inspect == "mannequin":
        "(When you look at the bust in front of you, you recall a half-serious lesson on disguising yourself - back when you were a trainee. From what you remember, this appears to be a mannequin for a wig.)"
        "(But Dr. Danger had a full head of hair.)"
        "(Did she need to disguise herself? Intel's always suggested that her mastery over tech kept her off any camera she cared about.)"
    elif inspect == "scrapbook":
        "(You pick up what appears to be a generic scrapbook, like those shoved to the back shelves of charity stores. Looking closely, you can still see remnants of price sticker glue.)"
        "(It feels normal. {i}Too{/i} normal. The book's clearly hiding some deep, dark secret.)"
        "(But the inner contents are equally... {i}normal. {/i}All you find are photographs of a woman who looks a lot like Dr Danger, and a young boy with a crooked, toothy grin.)"
        "(The craftsmanship on display isn't anything remarkable, with poorly cut edges and tacky glitter glue smeared across the cheap cardstock. At least the pages seem to be in chronological order.)"
        "(In the earliest photos, the boy is bedridden. His skin is unnaturally pale, and his gaze is unfocused – empty, even.)"
        "(But as you flick though the pages, he grows stronger. He gets out of bed. His eyes shine with inspiration and intelligence. He smiles.)"
        "(The woman in these photos must've been taking good care of him.)"
        "(The later photos are self-explanatory. Playing videogames, reading bedtime stories... and what seems to be a movie night.)"
        "(You know the film they're watching. It's that one cartoon about an alien supervillain; one with a very big brain, but very little common sense.)"
        "(...Hold on. Wasn't the film released in cinemas three months later?)"
        "(Looks like STOP will have to add \"digital piracy\" to Dr. Danger's long list of crimes.)"
    elif inspect == "health record":
        "(You pick up a clipboard with a thick stack of charts and diagrams pinned to the front.)"
        "(\"SUBJECT RECUPERATION LOG\" is printed at the top in a harsh, black lettering. At the bottom of the page, you spot an acronym: \"YTDI\".)"
        "(You flip through the log. The recuperation described here is difficult to read.)"
        "(Seizures, phantom pain, memory loss and brain damage are all expected results, not side effects. Scrawled notes speculate that these symptoms would last for several years, or decades - perhaps even permanently.)"
        "(Implanting cybernetics in individuals under 18 isn't illegal, but it is frowned upon. And from the logbook, a lot of children were implanted" "(Implanting cybernetics in individuals under 18 isn't illegal, but it {i}is {/i}children well under the age of 18.)"
        "(There's nothing here about informed consent or parental permissions. Evidently, parents weren't involved.)"
    elif inspect == "sewing book":
        "(You find an assortment of patterns, books, and materials for sewing.)"
        "(There's a little stack of half-finished items; a skirt and a blouse in conservative colors. Right next to it, there's a whole pile of hand-stitched garments in garish yellows, greens, and reds.)"
        "(Seems like someone handed their sewing books down to a more imaginative type.)"
        "(You're well-aware that sewing isn't just a simple hobby. Many of STOP's associated security forces take up the practice when they receive their first cybernetics. After such a big operation, the skill rehabilitates their hand-eye coordination.)"
        "(But you doubt they'd make such a large collection of fuzzy mittens.)"
    elif inspect == "locked container":
        "(After entering the combination, there's a small click. You give the handle a tug.)"
        "(There's no dust inside, but a stale odor wafts out. Clearly, this hasn't been opened for a long time.)"
        "(You find a lab coat with an ID pinned above its breast pocket. There's no photo, but the name Deirdre Destrange is clearly printed alongside a worn barcode.)"
        "(The coat itself is high-quality, but it's worn around the edges. Deirdre must've worn it for a long time, taking good care of it all the while.)"
        "(You see framed photos, diplomas, certificates and awards - all of them belonging to this \"Deirdre Destrange\". In and of itself, a doctorate in cybernetic biology is impressive, but Deirdre received this years ago.)"
        "(To be {i}that {/i}experienced at a young age, and when the science was still so {i}new...{/i} Deirdre must've been on the cutting edge of the field.)"
        "(At the bottom of the pile, you find a dented medal. An award for \"continued service to the international security community\"?)"
        "(The medal's name has been violently scratched out. And yet, you think you see the remnants of a familiar logo...)"
    elif inspect == "confidence workbook":
        "(It's a crumpled, heavily-worked-over notebook filled with grandiose, third-person ramblings. Lots of exclamation points and capital letters and ego-massaging in spidery handwriting.)"
        "(But the more you flip back through the pages, the more those writings grow negative. They're accompanied by notes on how to aim them in a more positive direction.)"
        "(Even further back, the spidery handwriting disappears. Instead, there are grids and examples written by someone with clean, crisp penmanship.)"
        "(It almost looks like a therapeutic exercise - or a homework assignment. Maybe it's both. What's clear is that the notebook's author hasn't used it for a long, long time.)"
        "(Personally, you wouldn't be caught dead speaking, writing, or even thinking in the third person.)"
        "(You only use the second person. And even then, only for gathering your thoughts in high-stakes scenarios.)"
    elif inspect == "diary":
        if room3["diary"] == 0:
            "(It's a loose page with handwriting on it. Judging by the page number in the corner and the heavily worn letters, it must be a small part of a much larger document.)"
        elif room3["diary"] == 1:
            #"FIRST ENTRIES"
            n "\"Still not psyched about the name, but it's nice to have job security right out of school. I had my doubts during junior year, of course, but I don't think anyone could've predicted how the sector's grown these past few months. The developments in cybernetic technology have been explosive. Sometimes {i}literally. {/i}"
            n "It's troubling, but all great technology has the potential for misuse. And now I'm going to be part of an organization that works to keep that tech under control. "
            n "Though I'll be honest, the name's pretty silly. "
            n "Oh well. They could always change the acronym later.\""
        elif room3["diary"] == 2:
            #"SUCCESS WITH LIMITING PROLIFERAITON OF TECH, PROMOTION, DISCOVERY OF POTENTIAL FOR YOUNGER SUBJECTS"
            n "\"I thought that things were moving fast before - but the growth we're seeing now makes those earlier years look glacial. STOP is doing good work that needs to get done, and it's making the countries that only paid for its formation as lip-service to international cooperation put the money where their mouth is. "
            n "Last month we managed to craft a Digital Data Management system that could tell us whenever a dangerous cybernetic schematic was downloaded and where it was downloaded to.  This month we finalized our report on maximizing cybernetic synchronization for patients - confirming my earlier theory that said the younger the better. "
            n "The difference really was astounding. And I must admit, it felt good to shove that 19\%-point increase right in that stuffy old bastard's smug face.\""
            n "\"Dr. Tan asked if the trend would continue if we started surgery any earlier. A weird question, since this tech is only approved for anyone old enough to enlist, but I guess she was just being thorough. The theory is sound.\""
            n "\"The promotion was nice. I deserve it, and I was the only obvious choice, but still. It felt nice to be recognized.\""
        elif room3["diary"] == 3:
            #"STAGNATION, LOTS OF RESEARCH WORK DISILLUSIONMENT, PARANOIA"
            n "\"Another month where the Security Advisory Council looked completely lost. It's like they don't know what to do with peacetime. They do amazing work - obviously. The world is secure, and cybernetic technology is finally getting regulated. The laws are catching up with the science. That's a good thing, even if it makes their job a little less exciting. Or maybe a little less secure.\""
            n "\"I requested another transfer. My third in three years, but they didn't seem to mind. I just can't find work as engrossing as I used to. It probably doesn't help that I'm not sure what it is I do anymore. "
            n "I mean I know what I do - I research cybernetics. But I'm not sure what I do for STOP. They haven't had a major security incident in months- And the last \"incident\" they did respond to was just a protest outside the building that got a little rowdy.\""
            n "\"Staff morale's been down ever since. A little controversy's expected, given the power STOP has nowadays. They're being naive if they expect people to be grateful to the organization forever.\""
            n "\"I might've transferred a few times too many. "
            n "I came into work today and clocked out without recognizing a single face the entire time. New people, places, committees, projects, and always more acronyms. "
            n "And for the first time in years, I was denied access to internal data. I didn't think anything was above my paygrade anymore. Note to self: look up \"YTDI \"\""
        elif room3["diary"] == 4:
            #"Meeting CAUTIONNE"
            n "\"\"I was very disappointed with the state of the Youth Training and Development Initiative.\""
            n "That's how I put it in writing. "
            n "I don't really have the right words to express my disgust with the fact that it exists at all. The idea that cybernetic sync rates increase the earlier in life treatment starts was based on a completely different timeline - assuming that we were talking about 18 vs 24. "
            n "It was never supposed to justify... whatever the hell they're doing now.\""
            n "\"They don't actually care about reducing rejection symptoms or making the cybernetics work more seamlessly. They care about cutting costs by experimenting on children that no one else cares about, and they care about producing \"Trainees\" that are unflinchingly obedient to authority. "
            n "They care about keeping the groups that fund STOP in power.\""
            n "\"I got a transfer to the YTDI. No one even seemed ashamed to give me full access.\""
            n "\"He smiled at me. "
            n "Even though everyone else he's seen - dressed like me, acting like me, working for the same people as me – has made him suffer. "
            n "He {i}smiled {/i}at me.\""
            n "\"I'm getting better at coming up with excuses to visit him, at least. "
            n "Or maybe my superiors aren't paying that close attention. That might be the most infuriating part for me - they don't even care that much about the success or failure of this program. "
            n "The implication I'm getting is that there are many, many others like it.\""
        elif room3["diary"] == 5:
            #"SEVEN FLEE, ON THE RUN"
            n "\"I'm never going to be able to forget the look on his face when the convulsions started. "
            n "He knew it was coming, and he knew there was nothing he could do to even brace himself for the pain. "
            n "He's been through it countless times. I never want to see it ever again.\""
            n "\"They claimed that it was a clerical error that he didn't receive his anti-seizure medications that morning. "
            n "I know that it was a perfectly un-subtle punishment for his refusal to obey during yesterday's exercises. "
            n "You wouldn't treat an {i}animal{/i} like this. He's less than that, to them.\""
            n "\"I triggered the false alarm right on schedule, down to the second. My not-at-all false improvised explosive went off right on schedule as well, also down to the second. "
            n "Logically, I understood that the chemical reaction was very simple to set up and hard to get wrong, but I still expected my first felony to present more challenges than that. Maybe I have a knack for this kind of thing. "
            n "In all seriousness, what I'm really happy about is the look on his face when I rushed him through the fire exit. When I asked him to come with me, he didn't hesitate for one second.\""
            n "\"Maybe he should have hesitated. At least from now on, he'll have that choice.\""
        elif room3["diary"] == 6:
            #"FIGHTING BACK, CAUTIONNE WANTING TO HELP"
            n "\"I've no right to call myself a parent, but even so - parenthood is hard. "
            n "His rehab is going as well as can be expected, but this is no way to raise a child. I can educate him, and keep him fed, and care for him. "
            n "But I can't give him any kind of a future - not while STOP is trying to erase our very existence.\""
            n "\"I managed to section away enough resources to last us a while, but all my internal records within STOP were destroyed by the fire. "
            n "They still know I'm out here, but now I have no proof that I was ever as big a part of them as I say. It's my word against theirs, and they have a much, much, much larger audience.\""
            n "\"As I expected, bombs and sabotage and cryptic public addresses on shady message boards get much better traction than just sending my research notes to major news outlets. "
            n "No one cares what Deirdre Destrange has to say. But when \"Dr. Danger\" blows up an energy pipeline, people look up from their food and {i}watch.{/i}"
            n "He chose the name. It's got a nice, old-world appeal to it.\""
            n "\"Cautionne has always been eager to please and happy to spend time with me. Is it any wonder he wants to help the nefarious Dr. Danger in her fight against STOP? "
            n "I should tell him no. Revenge is poison, and he's already been through so much. "
            n "But I still can't even bear to calculate how much of what he's been through is my fault. I don't have the heart to tell him no - and I'd sooner die than judge him for how much he hates STOP.\""
            n "\"Dr Danger and Cautionne are becoming a household name, but that's about it. "
            n "STOP is still in power. People are still too scared to say no to them. And there are still YTDI centers all over the world. If I destroy one, they move the \"subjects\" to another. "
            n "That's horrible, but what if they don't? What if they just figure it's just not worth the cost? What'll happen to those kids afterwards?"
            n "Something needs to change, but I'm not sure it's something that Dr. Danger can do. "
            n "...And I'm not sure that Deirdre Destrange is enough for him.\""
        elif room3["diary"] > 6:
            #text for when all entries have been read
            pass
        $ room3["diary"] += 1
        nvl clear
    $ inspect = None
    call screen room3

    "{u}{b}Death Scenes{/b}{/u}
    You are helping Cautionne finish a quilt that has some sentimental value (either it was started by Dr Danger and left unfinished by her death, or it is made from costume scraps from Dr Danger and Cautionne's old outfits, or something similar). If you mess up, Cautionne will trigger a trap that shoots a barrage so sewing needles at you, inducing death by a thousand pricks. "

    "Puzzle 1 Death Scene" "{u}{b}{/b}{/u}
    {i}W{/i}{i}ow.{/i}{i} {/i}You're no deft hand, are you?
    I'd like to think of myself as a lenient kinda guy... But watching you butcher that sentimental quilt is pretty painful.
    Like, death by a thousand cuts...
    ...or needles, in this case.
    (You hear a switch go off, and-)
    {i}{b}CUT TO BLACK{/b}{/i}
    {i}{b}[sound of protag getting stabbed with needles]{/b}{/i}

    {i}{/i}{i}Lab rat failed to appreciate the value of good stitchwork, and so was impaled by a thousand and twenty-four needles.{/i}"

    "(NB" "{i}It needed to be a square number for the triggering mechanism to hit its mark){/i}"

    "Contributing Factors to Death" "{i}{/i}{i} Couldn't sew their way out of a wet paper bag.{/i}"

    "Puzzle 2" "You are digging into a pile of toys/plushes you found in Dr Danger/Cautionne's room. You are helping Cautionne sort them. If you mess up sorting them Cautionne giggles and [death scene]"

    "Puzzle 2 Death Scene" "{b}{/b}"

    "(You set down the toys and pause to think.)
    (The task is a lot harder than you thought it would be. Maybe-)
    Having trouble organizing? I get it.
    I was horrible at putting my stuff away. A total {i}mess, {/i}every time.
    But whenever I got into a pickle, Dr. Danger always helped me out.
    {b}[pause]{/b}
    ...Hey, remind me. 
    Where {i}is {/i}Dr Danger right now?
    (The sudden quietness in his voice makes you freeze.)
    {i}Right.{/i}
    {i}{b}SLICING SFX, CUT TO BLACK{/b}{/i}"

    "Lab Report #414" "{i}{/i} {i}Subject was transported to the automated disposal department via trap door, whereupon the automated disposal department did what it does best.{/i}"

    "Contributing Factors to Death" "{i}{/i}{i}Expected leniency where there was none to be found.{/i}"

    "Puzzle 3" "WIP – The context of the third puzzle in the bedroom is that you are trying to recreate a recipe Dr Danger used to make for Cautionne and herself. The specifics of the ingredients and recipe can be remixed as would like to fit the script, so long as there are 9 ingredients total. While designing I wrote them with the idea that it was loosely based on a pancake recipe with some unique additions based on Dr Danger and Cautionne's personal tastes (the ingredients used were bacon, strawberries, flour, snappers, sticks of butter, blue berries, eggs, bolts, milk)."

    "Puzzle 3 Death Scene" "{b}{/b}
    {b}[PLAYER FAILS PUZZLE]{/b}

    (There. That should be the right ingredients for the pancakes. Now if you pour the batter-)

    {i}Stop right there,{/i} lab rat. I don't want that affront to all things edible anywhere near my nice, tasteful, kitchen appliances.

    How the {i}hell {/i}do you screw up pancakes that bad? Did STOP suck out your common sense as well as your brains?

    (You open your mouth to protest and-)

    {b}[SPLAT sound]{/b}
    {b}[death screen]{/b}

    {i}{/i}{i} Lab rat perished soon (but not soon enough) after being plastered against the wall by a gigantic frying-pan-shaped-mallet. {/i}

    {i}Good riddance, although I have to admit, I was looking for an opportunity to get a use out of that particular trap.{/i}

    {i}Contributing Factors to Death{/i}{i}Committed sacrilege against breakfast food.{/i}"

    "Meta Puzzle" "This is the scrapbook puzzle. Cautionne is mad you did not get something so sentimental to them right, and comes to shoot you himself."

    "Meta Puzzle Death Scene" "{b}{/b}"

    "(You place the scrapbook down to get a fresh look at what you've got so far.)
    (But when you step back, you feel like {i}something's{/i} out of place.)
    (And if {i}you {/i}can tell, then {i}he {/i}can tell. Better-)
    It's okay to suck at arts and crafts, lab rat. Not everyone's born to make masterpieces.
    But... that scrapbook meant a lot to me.
    If you were gonna screw up {i}that {/i}badly, you could've at least used the {i}non-permanent glue.{/i}
    (A bead of sweat trickles down your back.)
    (Was... was that an option?)
    ...Wait, I left that out, didn't I? My bad!
    My bad! If memory serves me, this button should-
    {b}[BEEP]{/b}
    {b}[sound of lazer charging up]{/b}
    Whoopsie doopsie! Looks like I pressed the wrong-
    {b}BLAST SFX, CUT TO BLACK{/b}"

    "Lab Report #891" "{i}Subject succeeded in proving the fatality of ray gun protoype Delta-9.{/i}"

    "Contributing Factors to Death" "{i}They messed up my scrapbook – so now, we're even!{/i}"


