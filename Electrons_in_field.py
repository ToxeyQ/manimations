from manim import *
import numpy as np
import random

class test_proton(Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(RED, opacity=0.6)
        self.scale(0.5)
        self.set(v=[0,0,0])  
        self.set_stroke(WHITE)




class Vectors(VectorScene):
    def construct(self):

        def Rand_pos(x_range=5, y_range=2):
            return [random.randint(-x_range, x_range),random.randint(-y_range, y_range),0]

        def Update_pos(mob, dt):
            pos = mob.get_center()
            velocity = mob.v
            velocity += + dt * pos / (pos[1]**2+ pos[0]**2 + 0.001)

            mob.set(v=velocity)
            mob.shift(dt*velocity[0]*RIGHT + dt*velocity[1]*UP)

        def Update_pos2(mob, dt):
            pos = mob.get_center()
            velocity = mob.v
            velocity += - dt * pos / (pos[1]**2+ pos[0]**2 + 0.001)

            mob.set(v=velocity)
            mob.shift(dt*velocity[0]*RIGHT + dt*velocity[1]*UP)


        func = lambda pos: pos / (pos[1]**2+ pos[0]**2 + 0.001) #to not /0 at origin
        func2 = lambda pos: - pos / (pos[1]**2+ pos[0]**2 + 0.001)
        p_text = Tex("+")
        e_text = Tex("-")
        vf1 =ArrowVectorField(func)
        vf2 = ArrowVectorField(func2)
        proton = Circle().scale(0.25)
        proton.set_fill(RED, opacity=0.5)

        electron = Circle().scale(0.25)
        electron.set_fill(BLUE, opacity=0.5)
        electron.set_stroke(BLUE)



        test_circ = Circle().shift(RIGHT).scale(0.1)
        init_v = [0,0,0]
        test_circ.set(v=init_v)  
        test_circ.add_updater(Update_pos)

        self.add(vf1, proton, p_text)

        
        test_ps = VGroup()
        test_ps2 = VGroup()
        nr_protons = 6

        for j in range(nr_protons):
            test_ps.add(test_proton().move_to(Rand_pos()).scale(0.1))

        for i in range(len(test_ps)):
            self.wait(1)
            test_ps[i].add_updater(Update_pos)
            self.add(test_ps[i])

        self.play(vf1.animate.become(vf2), proton.animate.become(electron), p_text.animate.become(e_text))
        

        for i in range(nr_protons):
            test_ps[i].remove_updater(Update_pos)
            test_ps[i].add_updater(Update_pos2)

        for j in range(nr_protons):
            test_ps2.add(test_proton().move_to(Rand_pos()).scale(0.1))


        self.wait(3)
        for i in range(len(test_ps2)):
            self.wait(1)
            test_ps2[i].add_updater(Update_pos2)
            self.add(test_ps2[i])



 
            #i.add_updater(Update_pos2)

        #test_circ.clear_updaters()


        self.wait(3)
