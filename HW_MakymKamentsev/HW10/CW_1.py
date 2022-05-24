class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

ball1 = Ball('super')
ball2 = Ball()
print(ball1.ball_type)
print(ball2.ball_type)
