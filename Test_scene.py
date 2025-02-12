from manim import *
import numpy as np
class demo(Scene):
    def construct(self):
        t = Tex("Maxwells equations")
        t2 = Tex("In 5 minutes").scale(0.8).next_to(t, DOWN)
        self.play(Write(t))

        tri= Triangle().scale(0.3).to_corner(DL)

        circle = Circle()  # create a circle   
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        
        self.play(Create(tri), Create(t2))  # show the circle on screen
        self.wait(1)
        
        equation1 = MathTex(r"E = mc^2").shift(LEFT)
        equation2 = MathTex(r"E = mc^2").next_to(equation1, RIGHT)
        equation3 = MathTex(r"E = mc^2").next_to(equation1, DOWN)
        equation4 = Tex(r'$\nabla \cdot E = \rho$').next_to(equation2, DOWN)

        group = VGroup(t, t2)
        self.play(group.animate.to_edge(UP))

        self.play(Write(equation1))
        self.play(Write(equation2))
        self.play(Write(equation3))
        self.play(Write(equation4))
        self.wait(1)
        self.play(Indicate(equation1), FadeOut(equation2, equation3, equation4))


class Vectors(VectorScene):
    def construct(self):
        func = lambda pos: pos / (pos[1]**2+ pos[0]**2 + 0.001) #to not /0 at origin
        func2 = lambda pos: - pos / (pos[1]**2+ pos[0]**2 + 0.001)
        p_text = Tex("+")
        e_text = Tex("-")
        vf1 =ArrowVectorField(func)
        vf2 = ArrowVectorField(func2)
        proton = Circle().scale(0.25)
        proton.set_fill(RED, opacity=0.5)

        electron = Circle().scale(0.13)
        electron.set_fill(BLUE, opacity=0.5)
        electron.set_stroke(BLUE)

        self.add(vf1, proton, p_text)

        
        #Change to E_field of electron
        self.wait(2)
        self.play(vf1.animate.become(vf2), proton.animate.become(electron), p_text.animate.become(e_text))


class VectorsMagnet(VectorScene):
    def construct(self):
        func = lambda pos: 0.5*UP* (3*pos[0]*pos[1]) / (np.sqrt((pos[0]**2 + pos[1]**2 +0.000001)**5 )) + 0.5*(2* pos[0]**2 - pos[1]**2)/ np.sqrt(((pos[0]**2 + pos[1]**2 +0.000001)**5)) * RIGHT
        func2 = lambda pos: 3 * pos 
        vf1 =ArrowVectorField(func)
        vf2 = ArrowVectorField(func2)
        self.add(vf1)
        self.wait(1)
        proton = Circle().scale(0.25)
        proton.set_fill(RED, opacity=0.5)

        electron = Circle().scale(0.25)
        electron.set_fill(BLUE, opacity=0.5)


        axes = Axes(x_range=[-7, 7], y_range=[-4, 4], x_length=9, y_length=6)

        stream_lines = StreamLines(
            func,
            x_range=[0.5, 7, 0.2],
            y_range=[0.5, 4, 0.2],
            color=YELLOW,
            stroke_width=3,
            noise_factor = None,
            dt=0.01,
            virtual_time=15,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.add(axes)
        self.play(stream_lines.create(flow_speed=3))
        self.play(Create(proton))
        self.wait(1)
        self.play(vf1.animate.become(vf2))



class CoordinateSystem(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )

        func = lambda pos: np.sin(pos[1] / 2) + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )

        # Create Graph
        graph = axes.plot(lambda x: x**2, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x^{2}')

        graph2 = axes.plot(lambda x: x**3, color=WHITE)
        graph_label2 = axes.get_graph_label(graph2, label='x^{3}')

        # Display graph
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)
        self.add(vector_field)
        self.wait(1)




class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

        
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen