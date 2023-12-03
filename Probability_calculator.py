import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **hat):
        self.hat = hat
        self.contents = []

    def make_contents(self):
        for color, number_of_balls in self.hat.items():
            for _ in range(number_of_balls):
                self.contents.append(color)
        return self.contents

    def draw(self, num_balls_drawn):
        self.make_contents()
        if num_balls_drawn > len(self.contents):
            balls_drawn = self.contents
        else:
            balls_drawn = []
            for _ in range(num_balls_drawn):
                ball = random.choice(self.contents)
                balls_drawn.append(ball)
                self.contents.remove(ball)
        return balls_drawn


def expected_balls_looking_for(expected_balls):
    balls = []
    for color, number_of_balls in expected_balls.items():
        for _ in range(number_of_balls):
            balls.append(color)
    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    favorite_balls = expected_balls_looking_for(expected_balls)
    number_of_cucsess = 0
    for _ in range(num_experiments):
        drawed_balls = hat.draw(num_balls_drawn)
        balls_in_hat = copy.deepcopy(favorite_balls)
        for ball in drawed_balls:
            if ball in balls_in_hat:
                balls_in_hat.remove(ball)
        if len(balls_in_hat) == 0:
            number_of_cucsess += 1
    return number_of_cucsess / num_experiments
