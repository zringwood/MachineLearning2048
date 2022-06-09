import neat, random, os
from game import *


def train_ai(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    game = Game(3)
    while game.haspossiblemoves():
        output = net.activate((game.board[0][0],game.board[0][1],game.board[0][2],game.board[1][0],game.board[1][1],game.board[1][2],game.board[2][0],game.board[2][1],game.board[2][2]))
        decision = output.index(max(output))
        if decision == 0:
            nextboard = game.updateright()
        elif decision == 1:
            nextboard = game.updateleft()
        elif decision == 2:
            nextboard = game.updatedown()   
        else:
            nextboard = game.updateup()
        if nextboard == game.board :
            break
        game.board = nextboard
        game.addnewtile()
    #for now, fitness is just going to be the sum of the values on the board.
    total = 0
    for line in game.board :
        for cell in line:
            total += cell
    genome.fitness = total
def eval_genomes(genomes, config):
    for gen in genomes :
        #These are tuples and we don't care about the first value
        train_ai(gen[1], config)
#In the config file, the number of inputs changes based on the length of the board
def run_neat():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    net = neat.nn.FeedForwardNetwork.create(winner, config)
    game = Game(3)
    while game.haspossiblemoves():
        output = net.activate((game.board[0][0],game.board[0][1],game.board[0][2],game.board[1][0],game.board[1][1],game.board[1][2],game.board[2][0],game.board[2][1],game.board[2][2]))
        decision = output.index(max(output))
        if decision == 0:
            nextboard = game.updateright()
        elif decision == 1:
            nextboard = game.updateleft()
        elif decision == 2:
            nextboard = game.updatedown()   
        else:
            nextboard = game.updateup()
        if nextboard == game.board :
            break
        game.board = nextboard
        game.addnewtile()
        print(str(game))
run_neat()
