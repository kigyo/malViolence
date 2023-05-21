define description_color = "#fff"
define note_color = "#ccc"

style evidence_note_text:
    color "#000000" font "gui/font/TitilliumWeb-Regular.ttf" size 22 line_spacing -10 justify True
    outlines [(absolute(0), "#00000000", absolute(0), absolute(0))]
    xalign 0.0

style evidence_explination_text:
    color "#000000" font "gui/font/TitilliumWeb-Regular.ttf" size 22 line_spacing -10 justify True
    outlines [(absolute(1), "#cc444488", absolute(0), absolute(0))]
    xalign 0.0


label test:
    $ evidence_init()
    call screen room2_evidence

init python:
    def evidence_init(start=False):
        if difficulty_level == 1:
            store.evidence_board = EvidenceBoard()
        elif difficulty_level == 2:
            store.evidence_board = EvidenceBoard(notes=medium_notes, evidence=medium_evidence, solution=medium_solution, zoom=0.75)
        elif difficulty_level == 3:
            store.evidence_board = EvidenceBoard(notes=hard_notes, evidence=hard_evidence, solution=hard_solution, zoom=0.6)
        if not start:
            renpy.notify(_("Invalid. Restarting..."))

        store.evidence_level = difficulty_level

        renpy.retain_after_load()
        renpy.restart_interaction()

    class EvidenceBoard(renpy.Displayable):
        def __init__(self, zoom=0.85,
                     evidence=[('toy_plane', (75, 214), (125,20)),
                               ('suburbs', (395, 292), (125,20)),
                               ('harmonica', (20, 720), (125,20)),
                               ('red_haired_kid', (360, 683), (125,20)),
                               ('bracelet', (708, 40), (125,20)),
                               ('blonde_haired_kid', (1209, 30), (125,20)),
                               ('brown_haired_kid', (1369, 539), (125,20)),
                               ('mountains', (1562, 128), (125,20)),
                               ('city', (1097, 706), (125,20)),
                               ],
                     solution=[["blonde_haired_kid", "harmonica", "mountains"],
                               ["red_haired_kid", "toy_plane", "suburbs"],
                               ["brown_haired_kid", "bracelet", "city"]],
                     notes=[[[_("During our last operation, we only managed to save three test subjects.\n\nWe also found some incomplete records and a box of their personal belongings. \n\nClick on notes for a detailed view. In the detailed view, click on written notes to {s}stike{/s} strike them out. \n\nUsing what information we have, {i}figure out which item belongs to who, and who grew up where{/i}.\n\nClick on notes to examine them. Drag the pins around to make connections.")], (612, 349), 500],
                            [[_("The harmonica has traces of wild pollen found only in remote regions that have yet to be extensively developed.")], (330, 20), 300],
                            [[_("The red-headed child is certain they did not live in the city.")], (108, 496), 250],
                            [[_("The bracelet is too big for the red-headed child.")], (1118, 387), 250],
                            [[_("The blonde child managed to play a tune on the harmonica when asked, but the other two children could not.")], (1597, 503), 300]]):
                                   self.evidence = evidence
                                   self.split_evidence = []
                                   for e in self.evidence:
                                       if len(e[2]) > 2:
                                           for s in e[2]:
                                               self.split_evidence.append((s[0], e[1], s[1]))
                                       else:
                                           self.split_evidence.append(e)
                                   self.connections = []
                                   self.notes = notes
                                   self.zoom = zoom
                                   for j in range(len(notes)):
                                       for k in range(len(notes[j][0])):
                                           setattr(self, "note_striked_%s_%s" % (j, k), False)
                                   self.current = None
                                   self.pin = None
                                   self.fail = None
                                   self.solution = solution
                                   super(EvidenceBoard, self).__init__()
        def render(self, width, height, st, at):
            child_render = renpy.render(Null(), width, height, st, at)
            render = renpy.Render(width, height)
            can = render.canvas()

            for (start, end) in self.connections:
                start_e = [e for e in self.split_evidence if e[0] == start][0]
                end_e = [e for e in self.split_evidence if e[0] == end][0]
                can.line((255, 0, 0, 180),
                         (start_e[1][0]+start_e[2][0], start_e[1][1]+start_e[2][1]),
                         (end_e[1][0]+end_e[2][0], end_e[1][1]+end_e[2][1]), 8)
            if self.current:
                can.line((255, 0, 0, 180), self.current, self.pin, 8)
            render.blit(child_render, (0, 0))
            renpy.redraw(self, 0.0)
            return render

        def validate(self):
            solution = self.solution[:]
            while len(solution) > 0:
                self.check_solution(solution.pop())
                if self.fail: self.game_over()
            store.room2["evidence"] = "solved"
            clear_puzzle("room2_1")
            return True

        def game_over(self):
            if preferences.puzzle_resets:
                renpy.notify(_("Not a valid solution."))
                renpy.retain_after_load()
                renpy.restart_interaction()
            else:
                renpy.jump("evidence_game_over")

        def check_solution(self, graph):
            self.fail = False
            graph = sorted(graph)
            for n in graph:
                self.check_node(n, graph)
                if self.fail: self.game_over()
            queue = [graph[0]]
            seen = []
            while queue:
                self.traverse_node(queue.pop(), graph, seen, queue)
            self.fail = graph != sorted(seen)

        def check_node(self, node, graph):
            conns = [c for c in self.connections if node in c]
            for c in conns:
                if c[0] not in graph or c[1] not in graph:
                    self.fail = c
                    return

        def traverse_node(self, node, graph, seen, queue):
            seen.append(node)
            paths = [c for c in self.connections if node in c]
            for p in paths:
                if p[0] == node and p[1] == node: continue
                n = [n for n in p if n != node][0]
                if n not in seen and not n in queue:
                    queue.append(n)

    def note_dragged(drags, drop):
        drag = drags[0]
        # if isinstance(drag.drag_name, tuple):
        #     if len(drag.drag_name) >= 3:
        #         glog((drag.drag_name[0], (drag.x, drag.y), drag.drag_name[2]))
        #     else:
        #         glog((drag.drag_name[0], (drag.x, drag.y)))
        # else:
        #     glog((drag.drag_name, (drag.x, drag.y)))

    def evidence_dragged(board, drags, drop):
        drag = drags[0]
        board.current = None
        board.pin = None
        if place_pins:
            # glog((drag.drag_name[0], drag.drag_name[1], (drag.x-drag.drag_name[1][0]+pin_half, drag.y-drag.drag_name[1][1]+pin_half)))
            pass
        else:
            drag.snap(drag.drag_name[1][0]+drag.drag_name[2][0]-pin_half, drag.drag_name[1][1]+drag.drag_name[2][1]-pin_half)
        if drop:
            if drag.drag_name[0] == drop.drag_name[0]: return
            conn = None
            if len(drop.drag_name[2]) == 2:
                conn = sorted((drag.drag_name[0], drop.drag_name[0]))
            else:
                (x, y) = renpy.get_mouse_pos()
                x -=  drop.drag_name[1][0]
                y -=  drop.drag_name[1][1]
                for sub in drop.drag_name[2]:
                    rv = renpy.render(Transform("images/puzzles/room_2_puzzle_1/refactor/evi_%s.png" % sub[0].lower(), zoom=evidence_board.zoom), config.screen_width, config.screen_height, 0.0, 0.0)
                    if rv.is_pixel_opaque(x, y):
                        conn = sorted((drag.drag_name[0], sub[0]))
                        continue
            if conn:
                if conn in board.connections:
                    board.connections.remove(conn)
                else:
                    board.connections.append(conn)

        renpy.retain_after_load()
        renpy.restart_interaction()

    def evidence_dragging(board, drags):
        drag = drags[0]
        board.pin = (drag.x+pin_half, drag.y+pin_half)
        board.current = (drag.drag_name[1][0]+drag.drag_name[2][0],
                         drag.drag_name[1][1]+drag.drag_name[2][1])
    def mouse_pos(t, st, at):
        t.pos = renpy.get_mouse_pos()
        return 0.0

define mouse_pos = Transform(function=mouse_pos, xanchor=0.5)

define pin_half = 45

transform evidence_alpha:
    alpha 0.01

transform evidence_zoom(z):
    zoom z

screen room2_evidence():
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"
    key ["focus_left", "focus_right", "focus_up", "focus_down"] action NullAction()
    if difficulty_level != evidence_level:
        timer 0.1 action Function(evidence_init, True)

    frame style "puzzle_frame":
        padding (0, 0)
        viewport:
            yoffset -1
            default description = ""
            if not place_notes:
                for n in [0]+room2["notes"]:
                    frame:
                        background Solid("#0000004a")
                        offset (20, 20)
                        pos evidence_board.notes[n][1]
                        xsize evidence_board.notes[n][2]
                        padding (50, 50)
                        yminimum evidence_board.notes[n][2]
                        has vbox
                        align (0.5, 0.5)
                        for t in range(len(evidence_board.notes[n][0])):
                            text evidence_board.notes[n][0][t] align (0.5,0.5) style ("evidence_note_text" if n else "evidence_explination_text") strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n, t)) xalign 0.0
                    button:
                        pos evidence_board.notes[n][1]
                        action ShowTransient("enhance_note", note=evidence_board.notes[n], n_i=n)
                        frame:
                            background Solid(note_color if n else description_color)
                            xsize evidence_board.notes[n][2]
                            padding (50, 50)
                            yminimum evidence_board.notes[n][2]
                            has vbox
                            align (0.5, 0.5)
                            for t in range(len(evidence_board.notes[n][0])):
                                text evidence_board.notes[n][0][t] align (0.5,0.5) style ("evidence_note_text" if n else "evidence_explination_text") strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n, t)) xalign 0.0
            if not place_evidence:
                for e in evidence_board.evidence:
                    frame:
                        at evidence_zoom(evidence_board.zoom), evidence_alpha
                        background Solid("#0000004a")
                        offset (10, 10)
                        pos e[1]
                        add "evi_%s" % e[0].lower()
                    fixed:
                        pos e[1]
                        fit_first True
                        at evidence_zoom(evidence_board.zoom)
                        add "evi_%s" % e[0].lower()
                    if len(e[2]) == 2:
                        add "big_pin" pos (e[1][0]+e[2][0], e[1][1]+e[2][1]) anchor(0.5, 0.5)
                    else:
                        for s in e[2]:
                            add "big_pin" pos (e[1][0]+s[1][0], e[1][1]+s[1][1]) anchor(0.5, 0.5)
            add evidence_board
            draggroup:
                if place_notes:
                    for n in range(5):
                        drag:
                            drag_offscreen True
                            dragged note_dragged
                            # draggable False
                            drag_name n
                            pos evidence_board.notes[n][1]
                            frame:
                                background Solid(note_color if n else description_color)
                                xsize evidence_board.notes[n][2]
                                padding (50, 50)
                                yminimum evidence_board.notes[n][2]
                                has vbox
                                align (0.5, 0.5)
                                for t in range(len(evidence_board.notes[n][0])):
                                    text evidence_board.notes[n][0][t] align (0.5,0.5) style ("evidence_note_text" if n else "evidence_explination_text") strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n, t)) xalign 0.0
                for e in evidence_board.evidence:
                    if len(e[2]) == 2 or place_evidence:
                        drag:
                            pos e[1]
                            fixed:
                                if not place_evidence:
                                    at evidence_alpha, evidence_zoom(evidence_board.zoom)
                                else:
                                    at evidence_zoom(evidence_board.zoom)
                                fit_first True
                                imagebutton:
                                    idle "evi_%s" % e[0].lower()
                                    focus_mask True
                                    if not place_evidence and len(e[2]) == 2:
                                        hovered SetScreenVariable("description", e[0].replace("_", " "))
                                        unhovered SetScreenVariable("description", "")
                                        action ShowTransient("enhance", dissolve, evidence=e[0])
                            drag_name e
                            mouse_drop True
                            dragged note_dragged
                            draggable place_evidence
                            drag_offscreen True
                            focus_mask True
                            droppable not place_evidence
                        use pin(*e)
                    elif not place_evidence:
                        drag:
                            drag_name e
                            mouse_drop True
                            # dragged note_dragged
                            draggable place_evidence
                            drag_offscreen True
                            focus_mask True
                            droppable not place_evidence
                            pos e[1]
                            fixed:
                                at evidence_zoom(evidence_board.zoom)
                                fit_first True
                                for s in e[2]:
                                    imagebutton:
                                        at evidence_alpha
                                        idle "evi_%s" % s[0].lower()
                                        focus_mask True
                                        if not place_evidence:
                                            hovered SetScreenVariable("description", s[0].replace("_", " "))
                                            unhovered SetScreenVariable("description", "")
                                            action ShowTransient("enhance", dissolve, evidence=e[0], label=s[0])
                        for s in e[2]:
                            use pin(s[0], e[1], s[1])
            text description xalign 0.5 offset (-50, -100) at mouse_pos outlines [(absolute(6), "#000", absolute(0), absolute(0))]

            vbox xfill True yalign 1.0 ysize 100 spacing 30 xoffset -25 yoffset -20:
                textbutton "RESET" style "confirm_button" action SetField(evidence_board, "connections", []) xalign 1.0 yalign 0.5 at zoomed(0.75)
                textbutton "SUBMIT" style "confirm_button" action Function(evidence_board.validate) xalign 1.0 yalign 0.5
                textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5

            if puzzle_cleared("room2_1") or ("dead7" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode:
                use skip_button(room2, "evidence", "room2_1", xalign=1.0, xoffset=-25, yoffset=20)

        if config.developer:
            vbox:
                textbutton _("Skip Puzzle") action [SetDict(room2, "evidence", "solved"), Return()] style "confirm_button"
                textbutton _("Game Over") action [Jump("evidence_game_over")] style "confirm_button"
image big_pin:
    "pin"
    zoom 1.5

screen enhance_note(note, n_i):
    modal True
    imagebutton idle "#000000aa" action Hide("enhance_note", dissolve)
    viewport:
        xsize 1000
        xalign 0.5
        scrollbars "vertical"
        frame:
            background None
            yminimum 1080
            frame:
                background Solid(note_color if n else description_color)
                xsize 1000
                yminimum 800
                align (0.5, 0.5)
                padding (85, 85)
                vbox:
                    yalign 0.5
                    for i in range(len(note[0])):
                        button:
                            frame:
                                background None
                                text note[0][i] style "evidence_note_text" size 35 strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n_i, i), False)
                            if n_i and getattr(evidence_board, "note_striked_%s_%s" % (n_i, i), None) is not None:
                                action ToggleField(evidence_board, "note_striked_%s_%s" % (n_i, i))

screen enhance(evidence, label=None):
    modal True
    imagebutton idle "#000000aa" action Hide("enhance", dissolve)
    add "evi_%s" % evidence.lower() align (0.5, 0.5) zoom 2.0
    text (label or evidence).replace("_", " ") align (0.5, 1.0) outlines [(absolute(6), "#000", absolute(0), absolute(0))] size 64


define medium_notes = [[[_("During our last operation, we only managed to save four test subjects.\n\nWe also found some incomplete records that indicated all the subjects at this facility arrived within the same calendar year, and a box of their personal belongings. \n\nClick on notes for a detailed view. In the detailed view, click on written notes to {s}stike{/s} strike them out. \n\nUsing what information we have, {i}figure out which item belongs to who, when each subject arrived at the facility, and who grew up where{/i}.")], (616, 300), 520],

                       [["- The blonde child seems to have a musical inclination.",
                         "- The bracelet has a notable tarnish. Upon sampling it seems to be a coating of coastal salt.",
                         "- The city-dweller was abducted in the Spring.",], (8, 8), 350],
                       [["- The red-headed child said they have never been to the suburbs or to open water.",
                         "- Whoever lived in the mountains arrived in either June or December.",
                         "- The child from the suburbs was processed before the subject from the mountains."], (1200, 690), 400],
                       [["- The bracelet arrived at the facility before the toy plane.",
                         "- Subject G does not know how to use a yo-yo.",
                         "- The yo-yo trickster did not arrive first.",], (245, 374), 310],
                       [["- The child whose designation comes first in the alphabet was the second-to-last arrival.",
                         "- Subject R arrived in June.",
                         "- The child wearing a bracelet arrived in September."], (1130, 100), 350]]


define medium_evidence = [('suburbs', (16, 449), (105,20)),
                          ('subject_R', (180, 770), (105,20)),
                          ('city', (960, 775), (105,20)),
                          ('harmonica', (375, 40),(105,20)),
                          ('subject_A', (700, 760), (105,20)),
                          ('yo-yo', (1693, 217),(105,20)),
                          ('subject_G', (1117, 460),(105,20)),
                          ('bracelet', (442, 655),(105,20)),
                          ('toy_plane', (1375, 385), (105,20)),
                          ('mountains', (1625, 565), (105,20)),
                          ('subject_F', (1434, 20), (105,20)),
                          ('coast', (950, 65), (105,20)),

                          ('intake_dates', (650, 20), (('March_', (24, 67)),
                                                       ('June_', (222, 115)),
                                                       ('September_', (-14, 168)),
                                                       ('December_', (264, 267))))
                          ]

define hard_notes = [[[_("During our last operation, we only managed to save five test subjects.\n\nWe also found incomplete records that indicated all the subjects at this facility arrived within the same calendar year, and a box of their personal belongings. \n\nClick on notes for a detailed view. In the detailed view, click on written notes to {s}stike{/s} strike them out. \n\nUsing what information we have, {i}figure out which item belongs to who, which cybernetic implant each subject received, when each subject arrived at the facility, and which cell each subject stayed in{/i}.")], (434, 515), 500],

                     [[_("- The harmonica's owner arrived first."),
                       _("- Cell 3 was occupied in November."),
                       _("- The child with the bracelet was not in Cell 0, 1, or 3."),
                       _("- Subject R did not receive cybernetic legs or perspicacious processing implants."),
                       _("- The child that received the lethal legs implant arrived in February.")], (268, -81), 455],
                       [[_("- The cell of the child with the lethal legs implant was between the cells of the child who came with the knife, and the child who came with a yo-yo."),
                       _("- The cell of the child who received the perspicacious processing implant was between the cells of the children who arrived in July and February."),
                       _("- The child who received the heightened hearing implant arrived one month apart from the child who came with the yo-yo."),
                       _("- The child with the yo-yo stayed in Cell 2.")], (-32, 445), 500],
                    [[_("- Subject D received the eye implants."),
                      _("- 2 children arrived before Subject G did, and 2 children arrived after."),
                      _("- The child with the toy plane was in a higher cell number than the child who came with a yo-yo."),
                      _("- The bracelet was found in the cell directly to the right of the child who received the hearing implant. The cell to their left remained empty the longest."),
                      _("- The cell number of the subject with cybernetic arms is half of the cell number that Subject D stayed in."),
                      _("- Subject R came with a toy plane.")], (1033, 597), 500],
                     [[_("- The child who came with a knife also received the perspicacious processing implant."),
                       _("- The child who received the armed arms implant arrived last."),
                       _("- The toy plane could've belonged to the child with heightened hearing or the child who received new eyes."),
                       _("- The yo-yo belonged either to Subject F or the subject who received cybernetic legs."),
                       _("- The child who got new eyes came 1 month before the child who came with a knife.")], (1428, -75), 520]]


define hard_evidence = [('toy_plane', (78, 18), (90,20)),
                        ('subject_G', (1330, 359), (90,20)),
                        ('perspicacious_processing', (250, 885), (90,20)),
                        ('pocket_knife', (1712, 370), (90,20)),
                        ('armed_arms', (1028, 23), (90,20)),
                        ('subject_D', (511, 323), (90,20)),
                        ('subject_R', (21, 275), (90,20)),
                        ('subject_F', (909, 544), (90,20)),
                        ('super_sight', (225, 292), (90,20)),
                        ('yo-yo', (1279, 54), (90,20)),
                        ('harmonica', (9, 880), (90,20)),
                        ('bracelet', (1496, 833), (90,20)),
                        ('lethal_legs', (899, 819), (90,20)),
                        ('subject_A', (1731, 630), (90,20)),
                        ('heightened_hearing', (1521, 535), (90,20)),

                        ('panopticon', (1061, 317), (('cell_4', (203, 33)),
                                                     ('cell_3', (60, -10)),
                                                     ('cell_2', (-15, 112)),
                                                     ('cell_1', (86, 235)),
                                                     ('cell_0', (223, 155)))),

                        ('calendar', (760, 36), (('December', (16, 427)),
                                                 ('November', (194, 386)),
                                                 ('October', (18, 351)),
                                                 ('September', (197, 314)),
                                                 ('August', (15, 275)),
                                                 ('July', (192, 239)),
                                                 ('June', (21, 199)),
                                                 ('May', (198, 163)),
                                                 ('April', (12, 123)),
                                                 ('March', (190, 90)),
                                                 ('February', (15, 47)),
                                                 ('January', (198, 9))))
                        ]

define medium_solution = [["subject_G", "toy_plane", "December_", "mountains"],
                          ["subject_R", "yo-yo", "June_", "suburbs"],
                          ["subject_A", "bracelet", "September_", "coast"],
                          ["subject_F", "harmonica", "March_", "city"]]

define hard_solution = [["subject_G", "August", "cell_0", "pocket_knife", "perspicacious_processing"],
                        ["subject_R", "November", "cell_3", "toy_plane", "heightened_hearing"],
                        ["subject_A", "February", "cell_1", "harmonica", "lethal_legs"],
                        ["subject_F", "December", "cell_2", "yo-yo", "armed_arms"],
                        ["subject_D", "July", "cell_4", "bracelet", "super_sight"]]



default place_notes = False
default place_evidence = False
default place_pins = False

screen pin(name, n_pos, p_pos):
    drag:
        pos (n_pos[0]+p_pos[0]-pin_half, n_pos[1]+p_pos[1]-pin_half)
        add "big_pin"
        drag_name (name, n_pos, p_pos)
        drag_raise True
        focus_mask True
        mouse_drop True
        # drag_offscreen True
        dragged renpy.curry(evidence_dragged)(evidence_board)
        dragging renpy.curry(evidence_dragging)(evidence_board)
