class Ghost(object):
    
    color = ['white', 'yellow', 'purple', 'red']
    
    def __init__(self):
        
        from random import choice
        
        self.color = choice(Ghost.color)
