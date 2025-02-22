from manim import *
import numpy as np



class Axes3DExample(ThreeDScene):
    def construct(self):
        
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],  # X-axis from -1 to 1
            y_range=[-2, 2, 1],  # Y-axis from -1 to 1
            z_range=[-2, 2, 1],  # Z-axis from -1 to 1
            x_length=4,  # Total length of the X-axis (1 unit in each direction)
            y_length=4,  # Total length of the Y-axis
            z_length=4,  # Total length of the Z-axis
        )
        
        axis_length = 2

        '''
        neg_axes = VGroup(
            Line([0, 0, 0], [0, 0, -axis_length], color=WHITE),  # Negative Z
            Line([0, 0, 0], [-axis_length, 0, 0], color=WHITE),  # Negative X
            Line([0, 0, 0], [0, -axis_length, 0], color=WHITE),  # Negative Y
        )
        neg_axes.set_z_index(0)  # Should be behind the circle
        ''' 
        # This is so that the circle is not 'above' the top axis
        pos_axes = VGroup(
            Line([0, 0, 0], [0, 0, axis_length], color=WHITE), 
            Line([0, 0, 0], [axis_length, 0, 0], color=WHITE),  
            Line([0, 0, 0], [0, axis_length, 0], color=WHITE),
        )
        pos_axes.set_z_index(2) 
        self.add(pos_axes)


        t = ValueTracker(0)


        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))


        sphere = Sphere(
            radius=1,
            resolution=(5, 5)  # Adjust resolution for smoothness
        )
        sphere.set_fill(opacity=0) 

        #This is to get the gradient in color of the sphere
        for submobject in sphere.family_members_with_points():
            points = submobject.get_points()
            if len(points) > 0:
                colors = [interpolate_color(RED, BLUE, (p[2] + 2) / 4) for p in points]
                submobject.set_stroke(color=colors, width=1)


        self.add(sphere,axes, y_label, x_label)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=2.5)
        self.add(Circle(radius=1).move_to([0,0,0]))
        #self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(1)  
        
        
        
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([0,np.cos(t.get_value()),np.sin(t.get_value())]),
            resolution=1
        )
        arrow.add_updater(
            lambda mob: mob.become(Arrow3D(start=[0,0,0], end=[0,np.cos(t.get_value()),np.sin(t.get_value())], color=BLUE))
        )
        self.add(arrow)
        self.play(t.animate.set_value(2*np.pi), run_time=2)
        self.wait(2)
        

class Axes3DExample2(ThreeDScene):
    def construct(self):
        
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],  # X-axis from -1 to 1
            y_range=[-2, 2, 1],  # Y-axis from -1 to 1
            z_range=[-2, 2, 1],  # Z-axis from -1 to 1
            x_length=4,  # Total length of the X-axis (1 unit in each direction)
            y_length=4,  # Total length of the Y-axis
            z_length=4,  # Total length of the Z-axis
        )

        sphere = Sphere(
            radius=1,
            resolution=(5, 5)  # Adjust resolution for smoothness
        )
        sphere.set_fill(opacity=0) 
        circ = Circle(radius=1).move_to([0,0,0])   
        circ.set_fill(opacity=0.1)

        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([1/np.sqrt(3),1/np.sqrt(3),1/np.sqrt(3)]),
            resolution=20
        )

        xyproj = DashedLine([0, 0, 0], [1/np.sqrt(3), 1/np.sqrt(3), 0], color=WHITE,stroke_width=2)
        zproj = DashedLine([1/np.sqrt(3), 1/np.sqrt(3), 0], [1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3)], color=WHITE,stroke_width=2)



        self.add(circ,sphere, arrow,xyproj,zproj)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=2)
        self.add(axes)
        self.wait(3)