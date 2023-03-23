# default colors = {"square": "#00C07A",    # Green Square
#                   "circle": "#FEB600",    # Yellow Circle
#                   "diamond": "#00ACE7",    # Blue Diamond
#                   "triangle": "#FB007D",    # Red Triangle
#                   "star": "#9844d0",    # Purple Star
#                   "background": "#000000",
#                   "text": "#588A9F",
#                   "accent": "#588A9F",
#                   "reticle": "#588A9F"}

# Fairy Flosss by sailorhg <3
default colors = {
  "square": "#bfffde",
  "triangle": "#E1A2BE",
  "reticle": "#F6F7F1",
  "text": "#F6F7F1",
  "accent": "#B8A2CE",
  "diamond": "#92dee4",
  "background": "#5A5375",
  "star": "#FDF247",
  "circle": "#e6c0a1"
}

default color = Color("#ff0000")
default color_hue = 0.5
default color_value = 0.5
default color_saturation = 0.5
# default reticle_manager = ReticleManager("images/color_picker/reticle.png", "test")
default reticle_manager = None

image color_reticle_mask:
    "images/color_picker/color_reticle_mask.png"
    alpha 0.01

init -1 python:
    class ReticleManager(renpy.Displayable):
        def __init__(self,
                     child,
                     tag,
                     color=None,
                     size=250,
                     **kwargs):
            super(ReticleManager, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.tag = tag
            self.size = size

            self.rad = self.size/2-self.size*0.060
            self.wheel_drag = Drag(d="color_reticle_mask")
            self.wheel_drag.snap(int(self.size*0.215), int(self.size*0.215))
            self.wheel_drag.dragged = renpy.curry(color_reticle_dragged)(self)
            self.vs_drag = Drag(d="images/color_picker/reticle.png")

            hsv = Color(renpy.store.colors[self.tag]).hsv
            setattr(renpy.store, self.hue_tag, hsv[0])
            setattr(renpy.store, self.saturation_tag, hsv[1])
            setattr(renpy.store, self.value_tag, hsv[2])

            angle = (1-self.hue)*(2*math.pi)
            self.x = math.cos(angle)*self.rad+self.size/2+6
            self.y = math.sin(angle)*self.rad+self.size/2+6

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                dist = math.sqrt((self.size/2-x)**2+(self.size/2-y)**2)
                self.inner = 90.0
                self.outer = 120.0
                if self.outer > dist > self.inner:
                    self.x = ((x-self.size/2)/dist*self.rad)+self.size/2+6
                    self.y = ((y-self.size/2)/dist*self.rad)+self.size/2+6
                    self.wheel_drag.snap(int(self.x), int(self.y))
                    self.update_hue()

                self.box_start = 67.0
                self.box_end = 191.0

                if self.box_start < x < self.box_end and self.box_start < y < self.box_end:
                    self.vs_drag.snap(int(x-self.box_start), int(y-self.box_start))
                    self.update_value_saturation()
        @property
        def hue_tag(self):
            return "_%s_hue" % self.tag

        @property
        def value_tag(self):
            return "_%s_value" % self.tag

        @property
        def saturation_tag(self):
            return "_%s_saturation" % self.tag

        @property
        def hue(self):
            return getattr(renpy.store, self.hue_tag)

        @property
        def value(self):
            return getattr(renpy.store, self.value_tag)

        @property
        def saturation(self):
            return getattr(renpy.store, self.saturation_tag)

        @property
        def hex(self):
            return Color(hsv=(self.hue, self.saturation, self.value)).hexcode

        def update_hue(self):
            hue = math.atan2(self.y-self.size/2, self.x-self.size/2)/(2*math.pi)
            if hue < 0: hue *= -1
            else: hue = 1 - hue
            if self.hue != hue:
                SetVariable(self.hue_tag, hue)()
                SetDict(colors, self.tag, self.hex)()

        def update_value_saturation(self):
            saturation = min(1.0, max(0.0, self.vs_drag.x/(self.size/2.0-11.0)))
            value = min(1.0, max(0.0, ((self.size/2.0-11.0)-self.vs_drag.y)/(self.size/2.0-11.0)))
            if saturation != self.saturation or value != self.value:
                SetVariable(self.saturation_tag, saturation)()
                SetVariable(self.value_tag, value)()
                SetDict(colors, self.tag, self.hex)()

        def render(self, width, height, st, at):
            render = renpy.Render(self.size, self.size)
            child_render = renpy.render(self.child, width, height, 0, 0)
            self.x = self.wheel_drag.x or self.x
            self.y = self.wheel_drag.y or self.y

            if renpy.display.focus.get_grab() is self.wheel_drag:
                dist = math.sqrt((self.size/2-self.wheel_drag.x)**2+(self.size/2-self.wheel_drag.y)**2) or 0.01
                if dist != self.rad:
                    self.x = ((self.wheel_drag.x-self.size/2)/dist*self.rad)+self.size/2+6
                    self.y = ((self.wheel_drag.y-self.size/2)/dist*self.rad)+self.size/2+6
                self.update_hue()
            elif self.wheel_drag.x != self.x and self.wheel_drag.y != self.y:
                self.wheel_drag.snap(int(self.x), int(self.y))
                self.update_hue()

            if renpy.display.focus.get_grab() is self.vs_drag:
                self.update_value_saturation()
            elif self.wheel_drag.x != self.x and self.wheel_drag.y != self.y:
                self.vs_drag.snap(int(self.saturation*(self.size/2-11)), int((1.0-self.value)*(self.size/2-11)))

            render.blit(child_render, (self.x-11, self.y-11))
            renpy.redraw(self, 0)
            return render

        def __eq__(self, other):
            return False

    def color_reticle_dragged(rm, drags, drop=None):
        drag = drags[0]
        drag.snap(int(rm.x), int(rm.y))
        SetDict(colors, rm.tag, rm.hex)
        renpy.store.colors[rm.tag] = rm.hex

    def initialize_colors():
        for t, c in renpy.store.colors.iteritems():
            setattr(renpy.store, "%s_rm" % t, ReticleManager("images/color_picker/reticle.png", t))

    renpy.register_shader("linear_gradient", variables="""
        uniform vec4 u_gradient_left;
        uniform vec4 u_gradient_right;
        uniform vec2 u_model_size;
        varying float v_gradient_done;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_done = a_position.x / u_model_size.x;
    """, fragment_300="""
        gl_FragColor *= mix(u_gradient_left, u_gradient_right, v_gradient_done);
    """)

    renpy.register_shader("quad_gradient", variables="""
        uniform vec4 u_gradient_top_left;
        uniform vec4 u_gradient_top_right;
        uniform vec4 u_gradient_bottom_left;
        uniform vec4 u_gradient_bottom_right;
        uniform vec2 u_model_size;
        varying float v_gradient_horizontal_factor;
        varying float v_gradient_vertical_factor;
        attribute vec4 a_position;
        varying vec4 f_color_top;
        varying vec4 f_color_bottom;
    """, vertex_300="""
        v_gradient_horizontal_factor = a_position.x / u_model_size.x;
        v_gradient_vertical_factor = a_position.y / u_model_size.y;
        f_color_top = mix(u_gradient_top_left, u_gradient_top_right, v_gradient_horizontal_factor);
        f_color_bottom = mix(u_gradient_bottom_left, u_gradient_bottom_right, v_gradient_horizontal_factor);
    """, fragment_300="""
        gl_FragColor *= mix(f_color_top, f_color_bottom, v_gradient_vertical_factor);
    """)

transform hsv_quad(c):
    shader "quad_gradient"
    u_gradient_top_left (1.0, 1.0, 1.0, 1.0)
    u_gradient_top_right Color(hsv=(c.hsv[0], 1.0, 1.0)).rgba
    u_gradient_bottom_left (0.0, 0.0, 0.0, 1.0)
    u_gradient_bottom_right (0.0, 0.0, 0.0, 1.0)

# rgb_r_linear
# rgb_g_linear
# rgb_b_linear

# hsv_h_linear
# hsv_s_linear
# hsv_v_linear

# hsl_h_linear
# hsl_s_linear
# hsl_l_linear

# radial


label test_color_pickepur:
    call screen color_picker

transform colorify(c):
    matrixcolor TintMatrix(c)

screen color_picker(rm=reticle_manager):
    $ color = Color(hsv=(rm.hue, rm.value, rm.saturation))
    fixed:
        xysize (rm.size+10, rm.size+10)
        add "color_wheel_outline" at wheel(rm)
        fixed:
            xysize (rm.size/2+10, rm.size/2+10)
            align (0.5, 0.5)
            add "#ffffff" at hsv_quad(color):
                align (0.5, 0.5)
                xysize (rm.size/2, rm.size/2)
            add rm.vs_drag
        use color_picker_reticle(rm)

transform wheel(rm):
    zoom rm.size/1000.0 align (0.5, 0.5)

transform transparent:
    alpha 0.01

screen color_picker_reticle(rm):
    fixed:
        add rm.wheel_drag anchor (0.5, 0.5)
    add rm
