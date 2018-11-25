from source.agents.GameAgent import GameAgent

class ConnectFourHumanAgent(GameAgent):
    
    def __init__(self, disc):
        self._disc = disc
    
    def play (self, board, columns):
        while(True):
            try:
                print("Las columnas válidas son las siguientes: ")
                print(columns)
                value =  int(input("> "))
                if value in columns:
                    return value
                else:
                    print("No se puede jugar esa columna, elija otra")
            except ValueError:
                print("Introducir valores numericos!!!")
        
     