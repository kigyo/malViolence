define description_color = "#fff"
define note_color = "#ccc"

style evidence_note_text:
    color "#000000" font "gui/font/TitilliumWeb-Regular.ttf" size 22 line_spacing -10 justify True
    outlines [(absolute(0), "#00000000", absolute(0), absolute(0))]

style evidence_explination_text:
    color "#000000" font "gui/font/TitilliumWeb-Regular.ttf" size 22 line_spacing -10 justify True
    outlines [(absolute(1), "#cc444488", absolute(0), absolute(0))]


label test:
    $ evidence_init()
    call screen room2_evidence

init python:
    def evidence_init(start=False):
        if difficulty_level == 1:
            store.evidence_board = EvidenceBoard()
        elif difficulty_level == 2:
            store.evidence_board = EvidenceBoard(notes=medium_notes, evidence=medium_evidence, solution=medium_solution, zoom=0.85)
        elif difficulty_level == 3:
            store.evidence_board = EvidenceBoard(notes=hard_notes, evidence=hard_evidence, solution=hard_solution, zoom=0.65)
        if not start:
            renpy.notify(_("Invalid. Restarting..."))

        store.evidence_level = difficulty_level

        renpy.retain_after_load()
        renpy.restart_interaction()

    class EvidenceBoard(renpy.Displayable):
        def __init__(self, zoom=1.0,
                     evidence=[('toy_plane', (42, 652), (40, 44)),
                               ('harmonica', (391, 686), (146, 60)),
                               ('suburbs', (310, 216), (69, 258)),
                               ('red_haired_kid', (578, 40), (97, 15)),
                               ('bracelet', (863, 41), (98, 127)),
                               ('city', (1097, 694), (31, 47)),
                               ('blonde_haired_kid', (1201, 315), (164, 33)),
                               ('brown_haired_kid', (1476, 303), (170, 217)),
                               ('mountains', (1580, 46), (159, 42))],
                     solution=[["blonde_haired_kid", "harmonica", "mountains"],
                               ["red_haired_kid", "toy_plane", "suburbs"],
                               ["brown_haired_kid", "bracelet", "city"]],
                     notes=[[[_("{color=#27718f}During our last operation, we only managed to save three test subjects.\n\nWe also found some incomplete records and a box of their personal belongings from the subjects on-site. \n\nUsing what information we have, {i}figure out which item belongs to who, and who grew up where{/i}.\n\nClick on notes to examine them. Drag the pins around to make connections.{/color}")], (626, 349)],
                            [[_("- The harmonica has traces of wild pollen found only in remote regions that have yet to be extensively developed.")], (0, 0)],
                            [[_("- The red-headed child is certain they did not live in the city.")], (108, 496)],
                            [[_("- The bracelet is too big for the red-headed child.")], (1088, 182)],
                            [[_("- The blonde child managed to play a tune on the harmonica when asked, but the other two children could not.")], (1320, 600)]]):
                                   self.evidence = evidence
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
                start_e = [e for e in self.evidence if e[0] == start][0]
                end_e = [e for e in self.evidence if e[0] == end][0]
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
            if ("dead7" in persistent.dead_ends and not preferences.hard_mode):
                evidence_init()
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
                if [n for n in p if n != node][0] not in seen and not [n for n in p if n != node][0] in queue:
                    queue.append(p[1])

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
            conn = sorted((drag.drag_name[0], drop.drag_name[0]))
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

define mouse_pos = Transform(function=mouse_pos)

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

    if difficulty_level != evidence_level:
        timer 0.1 action Function(evidence_init, True)

    frame style "puzzle_frame":
        padding (0, 0)
        viewport:
            yoffset -1
            default description = ""
            textbutton "check" action Function(evidence_board.validate)
            if not place_notes:
                for n in [0]+room2["notes"]:
                    frame:
                        background Solid("#0000004a")
                        offset (20, 20)
                        pos evidence_board.notes[n][1]
                        xsize 500
                        padding (50, 50)
                        yminimum 400
                        has vbox
                        for t in range(len(evidence_board.notes[n][0])):
                            text evidence_board.notes[n][0][t] align (0.5,0.5) style ("evidence_note_text" if n else "evidence_explination_text") strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n, t)) xalign 0.0
                    button:
                        pos evidence_board.notes[n][1]
                        action Show("enhance_note", note=evidence_board.notes[n], n_i=n)
                        frame:
                            background Solid(note_color if n else description_color)
                            xsize 500
                            padding (50, 50)
                            yminimum 200
                            has vbox
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
                    # if len(e) >= 3:
                    #     add "big_pin" pos (e[1][0]+e[2][0], e[1][1]+e[2][1]) anchor(0.5, 0.5)
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
                                xsize 500
                                padding (50, 50)
                                yminimum 400
                                has vbox
                                for t in evidence_board.notes[n][0]:
                                    text t align (0.5,0.5) style "evidence_note_text"
                for e in evidence_board.evidence:
                    if len(e) >= 3 or place_evidence:
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
                                    if not place_evidence and len(e) >= 3:
                                        hovered SetScreenVariable("description", e[0].replace("_", " "))
                                        unhovered SetScreenVariable("description", "")
                                        action Show("enhance", dissolve, evidence=e[0])
                            drag_name e
                            mouse_drop True
                            dragged note_dragged
                            draggable place_evidence
                            drag_offscreen True
                            focus_mask True
                            droppable not place_evidence
                        if len(e) >= 3:
                            drag:
                                pos (e[1][0]+e[2][0]-pin_half, e[1][1]+e[2][1]-pin_half)
                                add "big_pin"
                                drag_name e
                                drag_raise True
                                focus_mask True
                                mouse_drop True
                                dragged renpy.curry(evidence_dragged)(evidence_board)
                                dragging renpy.curry(evidence_dragging)(evidence_board)
            text description xalign 0.5 offset (-50, -100) at mouse_pos outlines [(absolute(6), "#000", absolute(0), absolute(0))]

            vbox xfill True yalign 1.0 ysize 100 spacing 30:
                textbutton "SUBMIT" style "confirm_button" action Function(evidence_board.validate) xalign 1.0 yalign 0.5
                textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5

            if puzzle_cleared("room2_1") or ("dead7" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode:
                use skip_button(room2, "evidence", "room2_1", yalign=1.0)

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
                yminimum 500
                align (0.5, 0.5)
                padding (85, 85)
                vbox:
                    yalign 0.5
                    for i in range(len(note[0])):
                        button:
                            frame:
                                background None
                                text note[0][i] style "evidence_note_text" size 35 strikethrough getattr(evidence_board, "note_striked_%s_%s" % (n_i, i))
                            if n_i:
                                action ToggleField(evidence_board, "note_striked_%s_%s" % (n_i, i))

screen enhance(evidence):
    modal True
    imagebutton idle "#000000aa" action Hide("enhance", dissolve)
    add "evi_%s" % evidence.lower() align (0.5, 0.5) zoom 2.0
    text evidence.replace("_", " ") align (0.5, 1.0) outlines [(absolute(6), "#000", absolute(0), absolute(0))] size 64


define medium_notes = [[[_("During our last operation, we only managed to save three test subjects.\n\nWe also found some incomplete records and a box of their personal belongings from the subjects on-site. \n\nUsing what information we have, {i}figure out which item belongs to who, and who grew up where{/i}.")], (626, 349)],
                       [["- The blonde child seems to have a musical inclination.",
                        "- The bracelet has a notable tarnish. Upon sampling it seems to be a coating of coastal salt.",
                        "- The city-dweller was abducted in the Spring.",], (-73, -68)],
                       [["- The red-headed child said they have never been to the suburbs or to open water.",
                         "- Whoever lived in the mountains arrived in either June or December.",
                         "- The child from the suburbs was processed before the subject from the mountains."], (146, 454)],
                       [["- The bracelet arrived at the facility before the toy plane.",
                         "- Subject G does not how to use a yo-yo.",
                         "- The yo-yo trickster did not arrive first.",], (1398, 735)],
                       [["- The child who's designation comes first in the alphabet was the second-to-last arrival.",
                         "- Subject R arrived in June.",
                         "- The child wearing a bracelet arrived in September."], (1087, 186)]]

define hard_notes = [[[_("During our last operation, we only managed to save three test subjects.\n\nWe also found some incomplete records and a box of their personal belongings from the subjects on-site. \n\nUsing what information we have, {i}figure out which item belongs to who, and who grew up where{/i}.")], (434, 555)],
                     [[_("- The child with the harmonica arrived first."),
                       _("- The child in Cell 3 arrived in November."),
                       _("- The child with the bracelet was not in Cell 0, 1, or 3."),
                       _("- Subject R did not receive cybernetic legs or perspicacious processing implants."),
                       _("- The child that received the lethal legs implant arrived in February.")], (305, -52)],
                       [[_("- The cell of the child with the lethal legs implant was between the cells of the child who came with the knife, and the child who came with a yo-yo."),
                       _("- The cell of the child who received the perspicacious processing implant was between the cells of the child who arrived in July and the child who arrived in February."),
                       _("- The child who received the heightened hearing implant arrived one month apart from the child who came with the yo-yo."),
                       _("- The child with the yo-yo stayed in Cell 2.")], (-27, 475)],
                    [[_("- Subject D received the eyes implant."),
                      _("- 2 children arrived before Subject G did, and 2 children arrived after."),
                      _("- The child with the toy plane was in a higher cell number than the child who came with a yo-yo."),
                      _("- The bracelet was found in the cell directly to the right of the child who received the hearing implant. To their left was the cell that remained empty the longest."),
                      _("- The cell number of the subject with cybernetic arms is half of the cell number that Subject D stayed in."),
                      _("- Subject R came with a toy plane.")], (1023, 607)],
                     [[_("- The child who came with a kite also received the perspicacious processing implant."),
                       _("- The child who received the armed arms implant arrived last."),
                       _("- The toy plane could've belonged to the child with heightened hearing or the child who received new eyes."),
                       _("- The yo-yo belonged either to Subject F or the child who received cybernetic legs."),
                       _("- The child who got new eyes came 1 month before the child who came with a knife.")], (1476, -45)]]


define hard_evidence = [('bracelet', (1482, 741), (95, 93)),
                        ('subject_A', (1716, 702), (21, 130)),
                        ('lethal_legs', (1710, 390), (157, 120)),
                        ('harmonica', (1466, 389), (90, 213)),
                        ('yo-yo', (1294, 35), (29, 181)),
                        ('super_sight', (1014, 20), (170, 167)),
                        ('subject_F', (874, 546), (18, 21)),
                        ('subject_R', (793, 841), (164, 101)),
                        ('heightened_hearing', (517, 870), (29, 162)),
                        ('subject_D', (244, 887), (167, 114)),
                        ('armed_arms', (6, 883), (39, 34)),
                        ('perspicacious_processing', (317, 265), (162, 175)),
                        ('pocket_knife', (537, 313), (50, 53)),
                        ('subject_G', (98, 254), (181, 159)),
                        ('toy_plane', (31, 26), (82, 39)),

                        ('panopticon', (1116, 332)),

                        ('cell_4', (1116, 332), (204, 36)),
                        ('cell_3', (1116, 332), (111, -11)),
                        ('cell_2', (1116, 332), (-16, 109)),
                        ('cell_1', (1116, 332), (61, 215)),
                        ('cell_0', (1116, 332), (207, 199)),

                        ('calendar', (770, 36)),

                        ('December', (770, 36), (29, 471)),
                        ('November', (770, 36), (204, 434)),
                        ('October', (770, 36), (28, 389)),
                        ('September', (770, 36), (197, 348)),
                        ('August', (770, 36), (26, 309)),
                        ('July', (770, 36), (202, 272)),
                        ('June', (770, 36), (31, 229)),
                        ('May', (770, 36), (208, 194)),
                        ('April', (770, 36), (20, 149)),
                        ('March', (770, 36), (210, 111)),
                        ('February', (770, 36), (23, 69)),
                        ('January', (770, 36), (208, 29))
                        ]

define medium_evidence = [('lethal_legs', (481, 255), (10, 10)),
                          ('heightened_hearing', (265, 231), (10, 10)),
                          ('super_sight', (4, 300), (10, 10)),
                          ('coast', (1017, -14), (10, 10)),
                          ('armed_arms', (1238, -23), (10, 10)),
                          ('mountains', (1518, 2), (10, 10)),
                          ('suburbs', (1, 639), (10, 10)),
                          ('city', (519, 820), (10, 10)),
                          ('yo-yo', (1089, 524), (10, 10)),
                          ('harmonica', (937, 823), (10, 10)),
                          ('toy_plane', (1266, 799), (10, 10)),
                          ('bracelet', (1439, 500), (10, 10)),
                          ('subject_F', (1561, 300), (10, 10)),
                          ('subject_A', (406, -23), (10, 10)),
                          ('subject_R', (278, 838), (10, 10)),
                          ('subject_G', (740, 820), (10, 10)),
                          ('intake_dates', (668, 20)),

                          ('March_', (668, 20), (24, 77)),
                          ('June_', (668, 20), (252, 141)),
                          ('September_', (668, 20), (-14, 208)),
                          ('December_', (668, 20), (304, 272))]

define medium_solution = [["subject_G", "plane", "December", "mountains"],
                          ["subject_R", "diablo", "June", "suburbs"],
                          ["subject_A", "bracelet", "September", "coast"],
                          ["subject_F", "harmonica", "March", "city"]]

define hard_solution = [["subject_G," "June", "cell_0", "kite", "processing"],
                        ["subject_R," "September", "cell_3", "plane", "hearing"],
                        ["subject_A," "March", "cell_1", "harmonica", "legs"],
                        ["subject_F," "December", "cell_2", "yo-yo", "arms"],
                        ["subject_D," "May", "cell_4", "bracelet", "eyes"]]


default place_notes = False
default place_evidence = False
default place_pins = False
