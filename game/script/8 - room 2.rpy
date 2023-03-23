default room2 = {"investigated":[], }

screen room2():
    sensitive not inspect
    layer "master"
    fixed at zoomed(0.35):
        add "bg room2"
        imagebutton idle Null(1570, 650) action [SetVariable("inspect", "corkboard"), Jump("room_2")] pos (1175, 1150)
        imagebutton idle "room2_blueprints" action [SetVariable("inspect", "blueprints"), Jump("room_2")] pos (3575, 1150) at zoomed(0.2)
        imagebutton idle "room2_postits" action [SetVariable("inspect", "post-its"), Jump("room_2")] pos (3575, 1550) at zoomed(0.2)
        imagebutton idle "room2_limbs" action [SetVariable("inspect", "limbs"), Jump("room_2")] pos (1575, 2150) at zoomed(0.2)
        imagebutton idle "room2_clippings" action [SetVariable("inspect", "clippings"), Jump("room_2")] pos (2575, 2150) at zoomed(0.2)

label room_2:
    if inspect not in room2["investigated"]:
        $room2["investigated"].append(inspect)
    show screen room2
    hide screen room2_panopticon
    if inspect == "blueprints":
        "(You survey the diagrams before you.)"
        "(From a distance, they seem to be your average blueprints. Blueprints for weapons of all makes, shapes and sizes.)"
        "(But on closer inspection, they reveal a certain quirkiness that doesn't belong on a technical document. The handwriting is also... {i}distinct,{/i} for lack of a better word.)"
        "(That said, poor penmanship hasn't dulled the designs themselves. The least dangerous of these would be devastating out in the field.)"
        "(The oldest of the blueprints - the ones hidden at the bottom of the pile, look wildly different. Clearly, another person authored them.)"
        "(In fact, if you squint... you can still find the signatures at the bottom.)"
        "(\"Destrange,\" they say. They're dated more than 15 years ago.)"
    elif inspect == "post-its":
        "(You eye over the mass of scrawled notes pinned in front of you. There're two distinct handwritings here, but the contents are mostly the same - and mostly {i}domestic{/i}.) "
        "(Notes on what to eat for breakfast and when to start preparing it. Notes on how much sleep to get and... what stories to read? Birthdays, exercises, meal plans and chores?)"
        "(Whoever left these notes for each other weren't just sharing the same space. They were {i}living{/i} together.)"
    elif inspect == "limbs":
        "(These documents appear to be designs for cybernetic limbs like the ones produced by STOP - at first glance. On closer inspection, there are more differences than there are similarities.) "
        "(STOP's technology is more generalized, more efficient... and {i}angular.{/i} These plans are heavily customized. They could've only been suitable for a very small number of subjects - possibly as few as one.)"
        "(Perhaps Dr. Danger based it off stolen data? You make a note to tell your superiors about possible reverse-engineering.)"
    elif inspect == "corkboard":
        "(As you look over the sprawling web of photos, documents, and diagrams, you realize everything in front of you is perfectly orderly.)"
        "(These are the notes of a hunter, and STOP was their prey. You recognize dozens of names, operations, and places; vital parts of STOP's organization that had suffered heavy blows in the last few years.)"
        "(But you're disturbed by how many places you {i}don't{/i} recognize.)"
        "(Laboratories, factories and armories that must be high above your clearance level – crossed out like someone was just going down a checklist.)"
        "(All these top-secret sites share the same acronym: \"YTDI.\")"
        "(...No, you don't recognize it. That's par for the course with STOP: If you don't know what an acronym means, it's probably above your paygrade.)"
    elif inspect == "clippings":
        "(Printouts and clippings of various news articles - all related to Dr. Danger's exploits... with a certain colorful sidekick occasionally breaking into the opening paragraphs.)"
        "(In fact, when you look at them all together, Cautionne seems to show up more over time. Dr. Danger must've been pleased with her pupil's growth.)"
        "(At the bottom of the pile, a heavily weathered photo peeks out. Based on what you can make out of the caption - it seems to be of some kind of commemorative occasion: \"__rdre Des__ge, et al. celebr_e breakthr__ in cyb_netics, sec_ity\".)"
        "(You can't recognize any of the faces, but you do recognize the logo as-)"
        #"{b}[pause as the clippings disappear]{/b}"
        "(...Never mind. It's just similar, that's all.)"
        $ inspect = None
        call screen room2_panopticon
    elif inspect == "panopticon solved":
        "(Solved the panopticon.)"
    $ inspect = None
    call screen room2

label room2_deaths:
    "{u}{b}Death Scenes{/b}{/u}"

    "Puzzle 1" "This is the evidence board puzzle. I wanted to touch base with the writers to see what kind of scenario could fit here, and then it seems like the dead end would depend on that, so any ideas? I can come up with the hints and clues, but it seems like it oculd be a good exposition oppertunity so I wanted to ask writers about it. "

    "Puzzle 1 Death Scene" "{b}{/b}
    (You carefully insert one more pin into the board, which leaves-)
    Whoa, you {i}suck {/i}at this!
    (Something about his unusually straightforward insult puts ice into your veins.)
    It's like you're solving this puzzle with your eyes closed and your nose plugged.
    ...There some reason you don't want to look at the truth in front of you, lab rat?
    (...No, no, it's just-)
    I know you're not taking this seriously. Maybe we should just move on?
    You know what? Yeah. 
    {i}Let's put a pin in it.{/i}
    {i}{b}PIERCING SFX, CUT TO BLACK.{/b}{/i}"

    "Lab Report #273" "{b}{/b}{i}Subject experienced permanent loss-of-life after one of the facility's reconfigurable nano-stakes jetted out of the floor and impaled them to the ceiling. {/i}"

    "{i}Guess they were worth the trouble of installation!{/i}"

    "Contributing Factors to Death" "{i}{b}{/b}{/i}{i}Couldn't put progress on the board.{/i}"

    "Puzzle 2" "You are helping Cautionne break out young captives at a STOP panopticon like facility. "
    "If you use too many \"turns\" to arrange the cells in the proper order, STOP will notice your interference and kick you out. "
    "Cautionne, enraged at losing the opportunity to save the prisoners, will decide that if they cannot be free then you do not deserve to be either, and simply turn off the lights to the facility you are being held in and abandon you, locked in, to wither away and die a slow, isolated death. "

    "Puzzle 2 Death Scene" "{b}{/b}
    (You re-arrange another two cells and-)
    (-and suddenly, your controls freeze up. There's a notification in the corner.)
    Seems like you've run out of time, lab rat.
    That's it. The jailbreak is broken. You screwed up.
    (So it {i}was {/i}a prison? Then-)
    If it was just between you and me, I'd be \"whatever\" about it.
    We all make mistakes, y'know? So, I'm super forgiving and cool and mature about this kind of thing.
    ...But you just lost those kids a chance to get out before the operations start.
    (...Sorry, {i}operations?{/i})
    They could've gotten out clean. Now I'll have to step in and bust them out {i}dirty{/i}.
    And it's all because of {i}you.{/i}
    Now, go sit in the corner and think about what you've done!
    {b}SFX LARGE SWITCH FLIPPING, CUT TO BLACK{/b}
    I'll come back for you when you're sorry enough."

    "Lab Report #893" "{b}{/b}Subject expired after 3 days due to lack of water, light, food, and mental stimulation. Scratched their nails bloody on the exit door before losing consciousness, so I'll have to clean {i}that {/i}mess up."

    "Contributing Factors to Death" "{i}{b}{/b}{/i}Didn't take the consequences of imprisonment very seriously."

    "Puzzle 3" "(NOTE"

    "NB" "{i}Protagonist doesn't have cybernetic implants, so maybe Cautionne puts you under and uses your live limbs as transplants for the former test subject. Unfortunately(?), he doesn't have a lot of experience with surgery, so he ends up killing you in the process.{/i}"

    "Puzzle 3 Death Scene" "{b}{/b}
    (You confirm your choice, and a beeping starts.)
    (It's tone sets the hairs on the back of your neck on edge.)
    You're losing ‘em, Doc.
    (...Wait. This is an actual {i}person?{/i})
    As they are now, they can't be re-stabilized. Their own nervous system will rip them apart with spasming.
    ...But they shouldn't be punished for your mistake, right?
    (...Well, uh-)
    Don't worry, I can fix this.
    But I'm gonna need a hand.
    (Suddenly, your body feels a lot heavier. Is that mist in the corner of the room?)
    ...And a liver. And a stomach. And a heart. And most of your spinal cord.
    {b}[pause]{/b}
    {i} {/i}And I'm gonna need them{i} right now.{/i}
    {i}{b}COLLAPSE SFX{/b}{/i}"

    "Lab Report #062" "{b}{/b}{i}Patient was eventually re-stabilized and should wake up within the next few days. {/i}"

    "{i}On the other hand, the lab rat won't get up ever again. Seems like they're missing a few too many critical parts.{/i}"

    "Contributing Factors to Death" "{i}{b}{/b}{/i}{i}They gave too much of themselves to my cause.{/i}"

    "Meta Puzzle" "This is the acronym word puzzle. If you enter a valid word that is too short, Cautionne just kills you while making a terrible pun about the word you entered."

    "Meta Puzzle Death Scene" "{b}{/b}
    *Player enters wrong answer*
    Holy crap! Did you just manage to guess that right on your first try?
    (Huh? Really?)
    {b} {/b}{i}Kidding!{/i}{i} {/i}
    {i}{/i}(You-)
    God, lighten up. Here, let me help!
    {b}ZAP SFX, CUT TO BLACK{/b}"

    "*Player enters wrong answer*
    Whoa... You got it.
    ...Are you looking up a walkthrough our something?
    (You-)
    If so, go back and complain in the comments. 
    They led you to a dead end!
    {b}SMASH SFX, CUT TO BLACK{/b}"

    "*Player enters wrong answer*
    You're a fast one, aren't you?
    (Huh? What do you-)
    But next time, {i}do {/i}look before you leap.
    {b}TRAP DOOR SFX, CUT TO BLACK{/b}"

    "*Player enters wrong answer*
    I see you're the type who likes to gamble.
    Alas, you didn't hit the jackpot. Better luck next time!
    (You-)
    But since you're here, I've got another game for you to play.
    Place your bet, lab rat! Is the gun next to you loaded or unloaded?
    (What gu-)
    {b}GUNSHOT SFX, CUT TO BLACK{/b}"

    "*Player enters wrong answer*
    ...Wow. That wasn't even {i}close. {/i}
    You'd have better luck just smashing keys.
    (You-)
    Like.{i} {/i}{i}So{/i}{i}.{/i}
    {b}SMASHING SFX, CUT TO BLACK{/b}"


