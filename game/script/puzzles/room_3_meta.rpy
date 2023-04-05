define scrapbook_memories = {
    1: _("""There was all this heat and smoke and energy. There were alarms blaring and people shouting. 
That's what she told me, but I barely remember any of it.

Here's what I did remember. When we stopped running, she seemed more tired than I was. She did carry me the entire time. But she didn't seem any weaker than before. Her hold on my body didn't loosen. She was just looking at what was left of my shoulder. 

I was hurting like you wouldn't believe. But I don't think I cared. 

Because, that day, I got to see the sky again."""),

    2: _("""I don't remember what the food was like at the orphanage. Probably bland.

I wish I could forget what LabScrip tastes like... but meals were usually the least painful part of my day in the lab, so I've got a soft spot for the stuff. 

But that wasn't food. It was nutritious and edible and nothing more. It didn't fill you up. It wasn't warm. There certainly was no thought in it at all.

Pancakes are food. They sizzle in the pan and curl at the edges, bubbling slightly when it's time to flip. You can undercook them or burn them, bury them in toppings or eat them with your hands. They're filling, and tasty, and oh-so warm.

With practice, I'm sure I could re-create her recipe with ease. Compared to our regular experiments, it's hardly rocket science.

But I've never had someone cook for {i}me{/i} before. 

...I'd like to pretend I'm not capable for a little while longer."""),

    3: _("""She told me to explore the place. She said it was important that I adjust to my new environment, but she's been holed up in the lab. 

I don't know why she's so stressed about my surgeries. She's the smartest person I know. And I grew up surrounded by \"brilliant\" scientists, so that's saying something.

She says she's still concerned about making adjustments to my synthetic nerves. That's she's worried she'll put me through even more pain. But every time she's worked on me, I haven't felt a thing.

Last time, I actually fell asleep."""),

    4: _("""I like to watch her work. It's normally very calming.

But when she's making something explosive, it's really, really exciting!  

The other day, I noticed that she'd forgotten her flash-welder. I brought it over to her, saying that I wanted to test out my grip strength. She saw through my excuse, but she let me help anyway.
I even made a few suggestions of my own, and ... guess what? Guess what!!! She ended up using every single idea!

She said it was impressive how quickly I'd picked up on what her design needed. She smiled at me with such pride. But at the same time, there was this sad look in her eyes...

...I've noticed she's sad a lot. I want to do something to change that.""")
}

screen room3_meta():
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"
    frame style "puzzle_frame":
        default scrapbook_page = 1
        default memory_read = 0

        if scrapbook_page == 1:
            add "puzzles/room_3_meta/scrapbook2.png" xalign 0.5
            imagebutton idle Null(175,140) action [SetScreenVariable("scrapbook_page",2), With(dissolve)] xpos 1402 ypos 50 mouse "inspect"

        else:
            add "puzzles/room_3_meta/scrapbook1.png" xalign 0.5
            imagebutton idle Null(145,135) action [SetScreenVariable("scrapbook_page",1), With(dissolve)] xpos 203 ypos 75 mouse "inspect"
        
        vbox spacing 10:
            style_prefix "puzzle_description"
            label _("REREAD NOTES")
            imagebutton idle "memory4" action NullAction() hovered [SetScreenVariable("memory_read",4), With(dissolve)] unhovered [SetScreenVariable("memory_read",0), With(dissolve)] mouse "inspect" xalign 0.5 at zoomed(0.2)
            if "quilt" in room3["solved"]:
                imagebutton idle "memory1" action NullAction() hovered [SetScreenVariable("memory_read",1), With(dissolve)] unhovered [SetScreenVariable("memory_read",0), With(dissolve)] mouse "inspect" xalign 0.5 at zoomed(0.2)
            if "toys" in room3["solved"]:
                imagebutton idle "memory3" action NullAction() hovered [SetScreenVariable("memory_read",3), With(dissolve)] unhovered [SetScreenVariable("memory_read",0), With(dissolve)] mouse "inspect" xalign 0.5 at zoomed(0.2)
            if "cooking" in room3["solved"]:
                imagebutton idle "memory2" action NullAction() hovered [SetScreenVariable("memory_read",2), With(dissolve)] unhovered [SetScreenVariable("memory_read",0), With(dissolve)] mouse "inspect" xalign 0.5 at zoomed(0.2)

        draggroup ypos 0 xpos 0:
            if scrapbook_page == 1:
                drag:
                    pos (297,152) draggable False drag_name 1
                    dropped scrapbook_dropped
                    add Null(312,253)
                drag:
                    pos (970,100) draggable False drag_name 2
                    dropped scrapbook_dropped
                    add Null(252,252)
            else:
                drag:
                    pos (297,152) draggable False drag_name 3
                    dropped scrapbook_dropped
                    add Null(312,253)
                drag:
                    pos (970,100) draggable False drag_name 4
                    dropped scrapbook_dropped
                    add Null(252,252)

            if 4 not in scrapbook_input or (scrapbook_page == 1 and (scrapbook_input[0] == 4 or scrapbook_input[1] == 4)) or (scrapbook_page == 2 and (scrapbook_input[2] == 4 or scrapbook_input[3] == 4)):
                drag: 
                    ypos 640 xpos 0 drag_name 4
                    dragged scrapbook_dragged dropped scrapbook_dropped_note
                    add "memory4" anchor (0.5,0.5) at zoomed(0.6)
            if "quilt" in room3["solved"]:
                if 1 not in scrapbook_input or (scrapbook_page == 1 and (scrapbook_input[0] == 1 or scrapbook_input[1] == 1)) or (scrapbook_page == 2 and (scrapbook_input[2] == 1 or scrapbook_input[3] == 1)):
                    drag: 
                        ypos 570 xpos 450 drag_name 1
                        dragged scrapbook_dragged dropped scrapbook_dropped_note
                        add "memory1" anchor (0.5,0.5) at rotated(5), zoomed(0.6)
            if "toys" in room3["solved"]:
                if 3 not in scrapbook_input or (scrapbook_page == 1 and (scrapbook_input[0] == 3 or scrapbook_input[1] == 3)) or (scrapbook_page == 2 and (scrapbook_input[2] == 3 or scrapbook_input[3] == 3)):
                    drag: 
                        ypos 690 xpos 800 drag_name 3
                        dragged scrapbook_dragged dropped scrapbook_dropped_note
                        add "memory3" anchor (0.5,0.5) at zoomed(0.6)
            if "cooking" in room3["solved"]:
                if 2 not in scrapbook_input or (scrapbook_page == 1 and (scrapbook_input[0] == 2 or scrapbook_input[1] == 2)) or (scrapbook_page == 2 and (scrapbook_input[2] == 2 or scrapbook_input[3] == 2)):
                    drag: 
                        ypos 490 xpos 1100 drag_name 2
                        dragged scrapbook_dragged dropped scrapbook_dropped_note
                        add "memory2" anchor (0.5,0.5) at rotated(-5), zoomed(0.6)
        
        if memory_read:
            frame align (0.5,0.5) xsize 1200 padding 40,50:
                vbox spacing 20:
                    style_prefix "puzzle_description"
                    text scrapbook_memories[memory_read]
        
        if config.developer:
            text str(tuple(scrapbook_input)) style "puzzle_description_text" xalign 0.5

        vbox xalign 1.0 yalign 1.0 spacing 30:
            textbutton "SUBMIT" style "confirm_button" action Function(scrapbook_submit)
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)]

        if len(room3["solved"]) == 3 and ("room3_meta" in persistent.solved_puzzles or ("dead10" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode):
            textbutton "SKIP" style "confirm_button" action [SetDict(room3, "scrapbook_new", "solved"), Return()] xalign 1.0

define scrapbook_positions = [(450,570), (1100,490), (800,690,), (0,640)]
define scrapbook_correct_order = [1,2,3,4]
default scrapbook_input = [0,0,0,0]

init python:
    def scrapbook_init():
        store.scrapbook_input = [0,0,0,0]

    def scrapbook_dragged(drags,drop):
        drag = drags[0]
        drag.snap(scrapbook_positions[drag.drag_name-1][0], scrapbook_positions[drag.drag_name-1][1], 0.5)
        for i in range(len(scrapbook_input)):
            if scrapbook_input[i] == drag.drag_name:
                store.scrapbook_input[i] = 0
                break
        renpy.retain_after_load()
        renpy.restart_interaction()

    def scrapbook_dropped_note(drop, drags):
        drag = drags[0]
        drop.snap(scrapbook_positions[drop.drag_name-1][0], scrapbook_positions[drop.drag_name-1][1], 0.5)
        for i in range(len(scrapbook_input)):
            if scrapbook_input[i] == drag.drag_name:
                store.scrapbook_input[i] = 0
            elif scrapbook_input[i] == drop.drag_name:
                store.scrapbook_input[i] = 0
        renpy.retain_after_load()
        renpy.restart_interaction()

    def scrapbook_dropped(drop, drags):
        global scrapbook_input
        drag = drags[0]
        if drop.drag_name % 2 == 1:
            drag.snap(327,172, 0.2)
        else:
            drag.snap(970,150, 0.2)
        scrapbook_input[drop.drag_name-1] = drag.drag_name
        renpy.retain_after_load()
        renpy.restart_interaction()

    def scrapbook_submit():
        if scrapbook_input == scrapbook_correct_order:
            store.room3["scrapbook_new"] = "solved"
            return True
        elif ("dead10" in persistent.dead_ends and not preferences.hard_mode):
            renpy.notify(_("Invalid solution."))
        else:
            renpy.jump("scrapbook_game_over")