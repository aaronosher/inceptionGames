import os.path
import string
import random

class game:
    game_id = None
    host_player = []
    guest_player = []

    # 1,1 is top left
    game_board = {
        (1,1):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (1,2):{
            (1,1): 0,
            (1,2): 0,g
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (1,3):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (2,1):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (2,2):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (2,3):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (3,1):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (3,2):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        },
        (3,3):{
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (2,1): 0,
            (2,2): 0,
            (2,3): 0,
            (3,1): 0,
            (3,2): 0,
            (3,3): 0
        }
    }

    def __init__(self, input):
        if type(input) is dict:
            # Create Game Instance

        if len(input) is 6:
            # Create Game Object

        newId  = self.generateId()
        while os.path.isfile('./games/'+newId+'.incept') is True:
            newId = self.generateId()

        gameFile = open('./games/'+newId+'.incept', 'w')


    def generateId(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
