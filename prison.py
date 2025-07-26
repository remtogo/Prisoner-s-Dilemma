import random
from enum import Enum


class Move(Enum):
    COOPERATE = 'C'
    DEFECT = 'D'


class GamePayoffs:
    BOTH_COOPERATE = (3, 3)
    BOTH_DEFECT = (1, 1)
    COOPERATE_DEFECT = (0, 5)
    DEFECT_COOPERATE = (5, 0)

    @staticmethod
    def get_payoff(player_move, computer_move):
        if player_move == Move.COOPERATE and computer_move == Move.COOPERATE:
            return GamePayoffs.BOTH_COOPERATE
        elif player_move == Move.DEFECT and computer_move == Move.DEFECT:
            return GamePayoffs.BOTH_DEFECT
        elif player_move == Move.COOPERATE and computer_move == Move.DEFECT:
            return GamePayoffs.COOPERATE_DEFECT
        elif player_move == Move.DEFECT and computer_move == Move.COOPERATE:
            return GamePayoffs.DEFECT_COOPERATE
        else:
            raise ValueError("Invalid moves")

    @staticmethod
    def make_player_move() -> Move:
        while True:
            choice = input("Enter your move (C for Cooperate, D for Defect): ").upper()
            if choice in ['C', 'D']:
                return Move(choice)
            print("Invalid move! Please enter C or D.")

    @staticmethod
    def make_computer_move() -> Move:
        return random.choice([Move.COOPERATE, Move.DEFECT])


class PrisonersDilemma:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds = self.generate_random_rounds()
        self.player_history = []  # Keep track of player moves
        self.computer_history = []  # Keep track of computer moves

    def generate_random_rounds(self) -> int:
        return random.randint(1, 25)

    def play_round(self):
        player_move = GamePayoffs.make_player_move()
        computer_move = GamePayoffs.make_computer_move()

        player_payoff, computer_payoff = GamePayoffs.get_payoff(player_move, computer_move)

        self.player_score += player_payoff
        self.computer_score += computer_payoff

        self.player_history.append(player_move)
        self.computer_history.append(computer_move)

        return player_move, computer_move, player_payoff, computer_payoff

    def play_game(self):
        print(f"\nPlaying Prisoner's Dilemma for {self.rounds} rounds:")

        for round_num in range(self.rounds):
            player_move, computer_move, player_payoff, computer_payoff = self.play_round()
            print(f"\nRound {round_num + 1}:")
            print(f"Player chose: {player_move.value}, Computer chose: {computer_move.value}")
            print(f"Payoffs - Player: {player_payoff}, Computer: {computer_payoff}")
            print(f"Current Scores - Player: {self.player_score}, Computer: {self.computer_score}")

        print("\nGame Over!")
        print(f"Final Scores - Player: {self.player_score}, Computer: {self.computer_score}")
        self.analyze_game()

    def analyze_game(self):
        if not self.player_history:
            print("No moves were made.")
            return

        player_cooperation_rate = sum(1 for move in self.player_history if move == Move.COOPERATE) / len(
            self.player_history)
        computer_cooperation_rate = sum(1 for move in self.computer_history if move == Move.COOPERATE) / len(
            self.computer_history)

        print("\nGame Analysis:")
        print(f"Player Cooperation Rate: {player_cooperation_rate:.2%}")
        print(f"Computer Cooperation Rate: {computer_cooperation_rate:.2%}")
        print(
            f"Average Points per Round - Player: {self.player_score / self.rounds:.2f}, Computer: {self.computer_score / self.rounds:.2f}")

        if self.player_score > self.computer_score:
            print("You won! Your strategy was more successful!")
        elif self.computer_score > self.player_score:
            print("Computer won! Its strategy was more successful!")
        else:
            print("The game ended in a tie!")


def main():
    while True:
        game = PrisonersDilemma()
        game.play_game()

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

