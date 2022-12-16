# https://www.youtube.com/watch?v=xNJAm3D18s0&ab_channel=inputJT
import src.puzzle as p

class Solver:
    puzzle: p.Puzzle

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def expand_state(self):
        # return every state possible for the current state
        pass

    def get_f(self):
        # f = g + h
        pass

    def get_g(self):
        # the number of nodes traversed from the start node to current node
        pass

    def get_h(self):
        # choose heuristic according to strategy (euclidian, manhattan...)
        pass

    def euclidian_distance(self):
        # https://en.wikipedia.org/wiki/Euclidean_distance
        # https://www.javatpoint.com/euclidian-distance-using-numpy#:~:text=General%20Method%20without%20using%20NumPy%3A&text=sqrs%20%3D%20(point1%20%5B0%5D,and%20point2%3A%20%22%2C%20euc_dist)
        pass

    def manhattan_distance(self):
        # https://fr.wikipedia.org/wiki/Distance_de_Manhattan
        # https://datagy.io/manhattan-distance-python/
        pass

    def chebyshev_distance(self):
        # https://fr.wikipedia.org/wiki/Distance_de_Tchebychev#:~:text=La%20distance%20de%20Tchebychev%2C%20distance,leurs%20coordonn%C3%A9es%20sur%20une%20dimension.
        # https://leetcode.com/problems/maximum-of-absolute-value-expression/solutions/347046/python-manhattanchebyshev-distance/
        pass

    def resolve(self):
        open_list = [self.puzzle]
        closed_list = []

        print(self.puzzle.puzzle)
        print(self.puzzle.control)

        # while open_list:
        #     current_state = select best state in open_list

        #     if current_state == goal
        #         return "Finished"

        #     expanded_state = expand(current_state)

        #     foreach expanded_state:
        #         calcul f_score

        #     move current state from open_list to closed_list
        #     add expanded_state to open_list            

        # implement A* algorithm
        # A* algorithm is an algorithm of informed search -> you know what you're looking for

        #   * open_list = [current_state]
        #   * closed_list = []
        #
        #   while opened_list:
        #       current_state = select best state in open_list
        #
        #       if current_state == goal
        #           return "Finished"
        #
        #       expanded_state = expand(current_state)
        #       foreach expanded_state:
        #           calcul f_score
        #
        #       move current state from open_list to closed_list
        #       add expanded_state to open_list
        #
        pass
