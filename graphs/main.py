from manim import *
import random
from manim_ml.neural_network import NeuralNetwork,FeedForwardLayer
# A customizable Sequential Neural Network


class Creating_beamm_network(Scene):
    def construct(self):
        

        icon = SVGMobject("/home/victor/OneDrive/Thesis/animations/graphs/media/images/main/logo-animation.svg")

        icon.set_color(WHITE)
        self.play(DrawBorderThenFill(icon))


        self.play(FadeOut(icon))

 

        self.wait()


        vertices = [1, 2, 3, 4, 5, 6, 7, 8]

        edges = [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 6), (2, 7), (3, 8), (4, 5)
        ]
        # Define node types
        type_a = [1, 2, 3]      # e.g., blue, represent the households
        type_b = [4, 5, 6 ,7, 8]         # e.g., red, represent the individuals
        
        vertex_config = {}
        for v in type_a:
            vertex_config[v] = {"fill_color": BLUE}
        for v in type_b:
            vertex_config[v] = {"fill_color": RED}
        
        g = Graph(
            vertices, edges, layout_scale=3,
            labels=True, vertex_config=vertex_config
        )
        self.play(Create(g))
        self.wait()

        text = Text("Economic Network", font_size=72)

        text.set_color(WHITE)
        text.to_edge(UP, buff=0.5)

        self.play(Write(text))


        self.play(FadeOut(text))
        self.wait()

        coordinates_plane = NumberPlane()

        self.play(FadeIn(coordinates_plane))
               # STEP 3: Create arrows from graph edges

        num_arrows = 3
        radius = 3
        center = ORIGIN

        arrows = VGroup()
        for i in range(num_arrows):
            angle = i * TAU / num_arrows  # TAU = 2 * PI
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            end_point = center + radius * direction
            arrow = Line(start=center, end=end_point).add_tip()
            arrows.add(arrow)

        # STEP 4: Transform edges into arrows
        self.play(
            Transform(g, arrows)
        )





        self.wait()

        self.clear()

        nn = NeuralNetwork([
    FeedForwardLayer(num_nodes=5),
    FeedForwardLayer(num_nodes=10),
    FeedForwardLayer(num_nodes=5)
])
        nn.move_to(ORIGIN)

        self.play(Create(nn))   
        










