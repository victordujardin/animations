from manim import *

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()




class Test(Scene):
    def construct(self):
        cir = Circle(radius =2.4, color=RED )
        self.play(Create(cir))

        


class Pith(Scene):
    def construct(self):
        sq = Square(side_length= 5 , stroke_color=GREEN, fill_color =BLUE, fill_opacity=0.5)


        self.play(Create(sq), running_start=3)

        self.wait()
