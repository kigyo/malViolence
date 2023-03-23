screen menu():
    hbox:
        align (1.0, 1.0)
        button:
            action [Jump("test_puzzles")]
            use colorized_frame:
                text "Select Puzzle" color colors["text"]

screen colorized_frame(xysize=None, padding=None, xalign=None, offset=None):
    frame:
        background colors["accent"]
        if offset:
            offset offset
        frame:
            background colors["background"]
            if xysize:
                xysize xysize
            if padding:
                padding padding
            if xalign is not None:
                xalign xalign
            transclude

transform hover_brighten:
    on hover:
        matrixcolor BrightnessMatrix(0.5)
    on idle:
        matrixcolor BrightnessMatrix(0.0)
