from manim import *
import numpy as np



class Axes3DExample(ThreeDScene):
    def construct(self):
        '''
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],  # X-axis from -1 to 1
            y_range=[-2, 2, 1],  # Y-axis from -1 to 1
            z_range=[-2, 2, 1],  # Z-axis from -1 to 1
            x_length=4,  # Total length of the X-axis (1 unit in each direction)
            y_length=4,  # Total length of the Y-axis
            z_length=4,  # Total length of the Z-axis
        )
        '''
        axis_length = 2
        neg_axes = VGroup(
            Line([0, 0, 0], [0, 0, -axis_length], color=WHITE),  # Negative Z
            Line([0, 0, 0], [-axis_length, 0, 0], color=WHITE),  # Negative X
            Line([0, 0, 0], [0, -axis_length, 0], color=WHITE),  # Negative Y
        )
        neg_axes.set_z_index(0)  # Should be behind the circle

        # Create the positive parts of the axes (foreground)
        pos_axes = VGroup(
            Line([0, 0, 0], [0, 0, axis_length], color=WHITE),  # Positive Z
            Line([0, 0, 0], [axis_length, 0, 0], color=WHITE),  # Positive X
            Line([0, 0, 0], [0, axis_length, 0], color=WHITE),  # Positive Y
        )
        pos_axes.set_z_index(2)  # Should be in front of everything



        t = ValueTracker(0)


        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)

        # 3D variant of the Dot() object

        # zoom out so we see the axes
        self.set_camera_orientation(zoom=0.5)
        sphere = Sphere(
            radius=1,
            resolution=(5, 5)  # Adjust resolution for smoothness
        )

        sphere.set_fill(opacity=0)  # Makes faces invisible


        for submobject in sphere.family_members_with_points():
            points = submobject.get_points()
            if len(points) > 0:
                # Compute color based on the z-coordinate (height)
                colors = [interpolate_color(RED, BLUE, (p[2] + 2) / 4) for p in points]
                submobject.set_stroke(color=colors, width=1)


        self.add(sphere)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=2, run_time=0.2)
        self.add(axes, y_label, x_label)

        self.wait(0.5)  
        self.add(Circle(radius=1).move_to([0,0,0]))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)  

        '''
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array[0,np.cos(t.get_value()),np.sin(t.get_value())],
            resolution=1
        )

        arrow.add_updater(
            lambda mob: mob.become(Arrow3D(start=[0,0,0], end=[0,np.cos(t.get_value()),np.sin(t.get_value())], color=BLUE))
        )

        self.add(arrow)
        # animate the move of the camera to properly see the axes
        #self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)

        # built-in updater which begins camera rotation
        #self.begin_ambient_camera_rotation(rate=0.15)

        self.wait(1)
        self.play(t.animate.set_value(2*np.pi), run_time=2)
        self.wait(2)
        '''
        print("dsa")