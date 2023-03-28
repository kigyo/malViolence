screen menu():
    pass

screen colorized_frame(xysize=None, padding=None, xalign=None, offset=None, accent=None, background=None, pos=None):
    frame:
        background accent or colors["accent"]
        if offset:
            offset offset
        if pos:
            pos pos
        frame:
            background background or colors["background"]
            if xysize:
                xysize xysize
            if padding:
                padding padding
            if xalign is not None:
                xalign xalign
            transclude

transform hover_brighten:
    on hover:
        ease 0.2 matrixcolor BrightnessMatrix(0.2)
    on idle:
        ease 0.2 matrixcolor BrightnessMatrix(0.0)
