from dartbot import DartBot
from dartboard import DartBoard
import statistics

class Game:
    def __init__(self, skill=20):
        # game parameters
        self.starting_score = 501
        self.double_out = True

        # intialize dartbot and board
        self.dartbot = DartBot(aim_skill=[skill, skill])
        self.dartboard = DartBoard()
        self.dartbot_score = self.starting_score
    
    def dartbot_turn(self):
        """Dartbot throws three darts."""
        previous_score = self.dartbot_score
        darts_thrown = 0
        for _ in range(3):
            darts_thrown += 1
            aim_at, score, segment_type, segment_number = self.dartbot.turn(remaining_score=self.dartbot_score)
            #print("")
            #print(f"Aiming at {aim_at}, Score: {score}, Type: {segment_type}, Segment: {segment_number}")
            new_score = self.dartbot_score - score

            if new_score == 0 and segment_type == "double":
                # checkout, end game
                self.dartbot_score = 0
                return "Checkout", darts_thrown
            elif new_score <= 1:
                # bust, end turn
                self.dartbot_score = previous_score
                return "Bust", darts_thrown
            else:
                # keep going
                self.dartbot_score = new_score
        return "No outcome", darts_thrown

    def new_game(self):
        number_of_visits = 0
        darts_needed = 0
        self.dartbot_score = self.starting_score
        while self.dartbot_score > 0:
            outcome, darts_thrown = self.dartbot_turn()
            darts_needed += darts_thrown
            #print(f"Remaining Score: {self.dartbot_score}")
            number_of_visits += 1
        #print(f"Number of visits: {number_of_visits}")
        #print(f"Darts thrown: {darts_needed}")
        return darts_needed


if __name__ == "__main__":
    averages = []
    skills = [i for i in range(1, 41)]
    for skill in skills:
        games = []
        for _ in range(1000):
            game = Game(skill=skill)
            darts_thrown = game.new_game()
            games.append(darts_thrown)

        avg_darts = statistics.mean(games)
        averages.append(avg_darts)
        print("----------------------------------------")
        print(f"Average number of darts needed: {avg_darts}")
        print(f"Max leg: {max(games)}, Min leg: {min(games)}, Median: {statistics.median(games)}")
        print(f"Three dart average: {501 / avg_darts * 3}")
        print("----------------------------------------")

    



