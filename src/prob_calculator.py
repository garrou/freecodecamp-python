import copy
import random
from typing import List

class Hat:
    def __init__(self, **kwargs) -> None:
        self.balls = kwargs
        self.contents = self.__init_contents(kwargs)

    def __init_contents(self, balls_occur) -> List:
        balls = []
        for ball in balls_occur.keys():
            for _ in range(balls_occur.get(ball)):
                balls.append(ball)
            
        return balls

    def draw(self, nb_to_draw) -> List:
        drawn = []
        if nb_to_draw >= len(self.contents):
            return self.contents

        for _ in range(nb_to_draw):
            ball = random.choice(self.contents)
            drawn.append(ball)
            self.contents.remove(ball)

        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    m = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        drawn = h.draw(num_balls_drawn)
        m += count_matches(drawn, expected_balls)
    return m / num_experiments

def count_matches(drawn, expected) -> int:
    for ball in expected.keys():
        if drawn.count(ball) < expected.get(ball):
            return 0
    return 1

def main():
    hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
    probability = experiment(hat=hat, expected_balls={"yellow":2, "blue":3, "test":1}, num_balls_drawn=20, num_experiments=100)
    print(probability)
    # expected: 1.0

    hat = Hat(blue=3, red=2, green=6)
    probability = experiment(hat=hat, expected_balls={"blue":2, "green":1}, num_balls_drawn=4, num_experiments=1000)
    print(probability)
    # expected: 0.272

if __name__ == "__main__":
    main()