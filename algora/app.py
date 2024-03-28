import argparse

class DanceSimulation:
        """
        A class that simulates a dance sequence and its effects on a forest.

        Attributes:
                dance_moves (dict): A dictionary mapping dance move sequences to their effects.
                state_art (dict): A dictionary mapping forest states to their corresponding ASCII art.
                forest_state (str): The current state of the forest.

        Methods:
                simulate_dance: Simulates the dance sequence and prints the effects on the forest.
        """

        def __init__(self):
                self.dance_moves = {
                        ("Twirl", "Spin", "Glide"): "Fireflies light up the forest.",
                        ("Leap", "Twirl", "Soar"): "Gentle rain starts falling.",
                        ("Spin", "Leap", "Dive"): "A rainbow appears in the sky.",
                        ("Twirl", "Leap", "Glide"): "A cool breeze blows through the forest.",
                        ("Leap", "Spin", "Soar"): "The forest is filled with a beautiful melody.",
                        ("Glide", "Soar", "Dive"): "The forest is filled with a golden glow.",
                }

                self.state_art = {
                        "Fireflies light up the forest.": """
    *
*   *
    *
""",
                        "Gentle rain starts falling.": """
    .
 . .
    .
""",
                        "A rainbow appears in the sky.": """
    __
-(__)-
    ""
""",
                        "A cool breeze blows through the forest.": """
 ~ ~ ~
""",
                        "The forest is filled with a beautiful melody.": """
♪ ♫ ♪
""",
                        "The forest is filled with a golden glow.": """
☀ ☀ ☀
""",
                }

                self.forest_state = ""

        def simulate_dance(self):
                """
                Simulates the dance sequence and prints the effects on the forest.

                The user is prompted to enter the number of steps in the dance sequence,
                followed by the dance moves for each participant. The effects of the dance
                moves are applied to the forest and the resulting forest state is printed
                along with its corresponding ASCII art representation.
                """
                num_steps = int(input("Enter the number of steps in the sequence: ").strip())

                dance_sequence = []
                for i in range(num_steps):
                        lox_move = input(f"Enter the dance move for Lox in sequence {i+1}: ").strip()
                        drako_move = input(f"Enter the dance move for Drako in sequence {i+1}: ").strip()
                        fenix_move = input(f"Enter the dance move for Fenix in sequence {i+1}: ").strip()
                        dance_sequence.append((lox_move, drako_move, fenix_move))

                for lox_move, drako_move, fenix_move in dance_sequence:
                        effect = self.dance_moves.get((lox_move, drako_move, fenix_move), "Nothing happens.")
                        self.forest_state = effect
                        print(f"After the dance move {lox_move} + {drako_move} + {fenix_move}, the state of the forest is: {self.forest_state}")
                        print(self.state_art.get(self.forest_state, ""))

        def run(self, dance_sequence):
            dance_sequence = tuple(dance_sequence.split(','))
            self.simulate_dance(dance_sequence)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate a dance sequence and its effects on a forest.')
    parser.add_argument('dance_sequence', type=str, help='A comma-separated dance sequence. For example: "Twirl,Spin,Glide"')

    args = parser.parse_args()

    simulation = DanceSimulation()
    simulation.run(args.dance_sequence)