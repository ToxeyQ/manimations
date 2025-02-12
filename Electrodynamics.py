from manim import *
import numpy as np


class Eyes(Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(WHITE, opacity=0.1)
        self.scale(0.3)
        self.set_stroke(WHITE)

class Eyebrow(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(BLACK, opacity=0.5)
        self.scale([0.17 ,0.1 , 1])  

class Trial(Scene):
    def construct(self):
        a = ValueTracker(0)
        ax = Axes(x_range=[-2*np.pi, 2*np.pi], y_range=[-4, 4], x_length=9, y_length=6)
        func = ax.plot(lambda t: np.cos(t))
        func.add_updater(
            lambda mob: mob.become(ax.plot(lambda t: np.cos(t + a.get_value())))
        )

        self.camera.frame_width = 2.9*np.pi
        self.camera.frame_height = 2.9*np.pi * 9/16
        circ1 = Eyes().move_to(ax.coords_to_point(4*np.pi,0), RIGHT)
        circ2 = Eyes().next_to(circ1, RIGHT)
        circ3 = Eyes().move_to(ax.coords_to_point(8*np.pi,0), RIGHT)
        circ4 = Eyes().next_to(circ3, RIGHT)
        circ5 = Eyes().move_to(ax.coords_to_point(12*np.pi,0), RIGHT)
        circ6 = Eyes().next_to(circ5, RIGHT)

        brow1 = Eyebrow().next_to(circ1, UP).rotate(-0.25*np.pi)
        brow2 = Eyebrow().next_to(circ2, UP).rotate(0.25*np.pi)
        brow3 = Eyebrow().next_to(circ3, UP)
        brow4 = Eyebrow().next_to(circ4, UP)
        brow5 = Eyebrow().next_to(circ5, UP).rotate(0.25*np.pi)
        brow6 = Eyebrow().next_to(circ6, UP).rotate(-0.25*np.pi)


        circles_group = VGroup(circ1,circ2,circ3,circ4,circ5,circ6,brow1,brow2,brow3,brow4,brow5,brow6)
    
        circles_group.add_updater(
            lambda mobject: mobject.move_to(ax.coords_to_point(-a.get_value()+4*np.pi,0))
        )


        self.add(func, circles_group)
        #self.play(circ1.animate.to_edge(LEFT), run_time=2)
        #self.play(circ1.animate.scale(2))
        #self.play(circ1.animate.center().scale(0.5))
        self.play(a.animate.set_value(8*np.pi), run_time=5)
        self.play(brow5.animate.rotate(-0.5*np.pi),brow6.animate.rotate(0.5*np.pi))
        self.wait(1)
        #self.play(Transform(func, func2))


