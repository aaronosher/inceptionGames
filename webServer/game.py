from pathlib import Path
import string
import random
import json
import operator
import os

class game:
    game_id = None
    host_player = { "name": "", "id": None }
    guest_player = { "name": "", "id": None }
    current_turn = 1
    current_grid = None

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
            (1,2): 0,
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

    large_score = {
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

    def __init__(self, input):
        if type(input) is dict:
            self.createGameInstance(input)

        elif len(input) is 6:
            if self.loadGame(input) is False:
                raise ValueError("Invalid Game ID")

        else:
            raise ValueError("Input must be host_player dictionary or a Valid Game ID")

    def generateId(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def createGameInstance(self, host):
        newId  = self.generateId()
        fileToCheck = Path('./games/'+newId+'.incept')
        if fileToCheck.is_file():
            while fileToCheck.is_file():
                newId = self.generateId()
                fileToCheck = Path(os.getcwd()+'/webserver/games/'+newId+'.incept')

        gameFile = open(os.getcwd()+'/webserver/games/'+str(newId)+'.incept', 'w')

        self.game_id = newId
        self.host_player['id'] = host['id']
        self.host_player['name'] = host['name']

        game = {
            "game_id": self.game_id,
            "host_player": self.host_player,
            "guest_player": self.guest_player,
            "current_turn": self.current_turn,
            "current_grid": self.current_grid,
            "game_board": self.game_board
        }



        game['game_board'] = self.boardToJson(game['game_board'])

        if gameFile.write(json.dumps(game)):
            return True

        return False

    def loadGame(self, game_id):
        fileToCheck = Path(os.getcwd()+'/webserver/games/'+game_id+'.incept')
        if fileToCheck.is_file():
            gameFile = open(os.getcwd()+'/webserver/games/'+game_id+'.incept', 'r')
            game = json.loads(gameFile.read())
            self.game_id = game_id
            self.host_player = game['host_player']
            self.guest_player = game['guest_player']
            newBoard = game['game_board']
            self.game_board = self.jsonToBoard(newBoard)

            return True

        return False

    def boardToJson(self, game_board):
        newBoard = []

        for board in game_board:
            newBoard.append({'key': list(board), 'board': []})
            i = len(newBoard)-1
            for board2 in game_board[board]:
                newBoard[i]['board'].append({
                    'key': list(board2),
                    'state': game_board[board][board2]
                })

        return newBoard

    def jsonToBoard(self, newBoard):
        game_board = {}
        for board in newBoard:
            new_top_key = tuple(board['key'])
            game_board[new_top_key] = {}
            for board2 in board['board']:
                new_b_key = tuple(board2['key'])
                game_board[new_top_key][new_b_key] = board2['state']

        return game_board

    def move(self, move, player=None):
        if player is None:
            player = self.current_turn
        if player is "host" or 1:
            played = 1
            nextPlayer = 2
        elif player is "guest" or 2:
            played = 2
            nextPlayer = 1

        self.game_board[move['big']][move['small']] = played
        self.current_turn = nextPlayer
        self.current_grid = move['small']
        self.updateFile()

        response = 'continue'
        # check for section win
        if self.testForWin(player, move['big']):
            response = "won "+move['big']

        if self.finalWinCheck(player):
            reponse = "won game"

    def updateFile(self):
        gameFile = open(os.getcwd()+'/webserver/games/'+str(self.game_id)+'.incept', 'w')

        game = {
            "game_id": self.game_id,
            "host_player": self.host_player,
            "guest_player": self.guest_player,
            "current_turn": self.current_turn,
            "current_grid": self.current_grid,
            "game_board": self.game_board
        }



        game['game_board'] = self.boardToJson(game['game_board'])

        if gameFile.write(json.dumps(game)):
            return True

    def testForWin(self, player, section):
        # Vertical if common x
        # Horizontal if common y
        # Diagonal at (1,1), (2,2), (3,3) and (1,3), (2,2), (3,1)

        board = self.game_board[section]
        if player is "host":
            player = 1

        elif player is "guest":
            player = 2

        else:
            return False

        win = False

        # Test Vertical
        if board[(1,1)] is player and board[(1,2)] is player and board[(1,3)] is player:
            win = True
        if board[(2,1)] == player and board[(2,2)] == player and board[(2,3)] == player:
            win = True
        if board[(3,1)] is player and board[(3,2)] is player and board[(3,3)] is player:
            win = True

        # Test Horizontal
        if board[(1,1)] is player and board[(2,1)] is player and board[(3,1)] is player:
            win = True
        if board[(1,2)] is player and board[(2,2)] is player and board[(3,2)] is player:
            win = True
        if board[(1,3)] is player and board[(2,3)] is player and board[(3,3)] is player:
            win = True

        # Test Diagonal
        if board[(1,1)] is player and board[(2,2)] is player and board[(3,3)] is player:
            win = True
        if board[(1,3)] is player and board[(2,2)] is player and board[(3,1)] is player:
            win = True

        if win is True:
            self.large_score[section] = player
            return True

        return False

    def scoreStatusCheck(self):
        for section in self.large_score:
            self.testForWin(1, section)
            self.testForWin(2, section)

    def finalWinCheck(self, player):
        board = self.large_score
        win = False
        # Test Vertical
        if board[(1,1)] is player and board[(1,2)] is player and board[(1,3)] is player:
            win = True
        if board[(2,1)] == player and board[(2,2)] == player and board[(2,3)] == player:
            win = True
        if board[(3,1)] is player and board[(3,2)] is player and board[(3,3)] is player:
            win = True

        # Test Horizontal
        if board[(1,1)] is player and board[(2,1)] is player and board[(3,1)] is player:
            win = True
        if board[(1,2)] is player and board[(2,2)] is player and board[(3,2)] is player:
            win = True
        if board[(1,3)] is player and board[(2,3)] is player and board[(3,3)] is player:
            win = True

        # Test Diagonal
        if board[(1,1)] is player and board[(2,2)] is player and board[(3,3)] is player:
            win = True
        if board[(1,3)] is player and board[(2,2)] is player and board[(3,1)] is player:
            win = True

        return win
