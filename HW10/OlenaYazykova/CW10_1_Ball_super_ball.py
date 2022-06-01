class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type=ball_type

my_ball_1=Ball("red")
my_ball_2=Ball()
print(my_ball_1.ball_type)
print(my_ball_2.ball_type)
