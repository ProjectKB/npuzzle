import math


class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def greedy_search(self):
        # A* but g == 0 for every node
        # It can be really fast, but it can lead to suboptimal solution because of local minimum.
        # Meaning the algorithm doesn't consider the cost of an action but only his short term result,
        # resulting in possibly longer path or even no path at all
        pass

    def uniform_cost(self):
        # A* but h == 0 for every node resulting in BFS algorithm (nodes are explored in width, and EVERY one of them are visited)
        pass

    #  Greedy search:
    #      Pros:
    #          - Can be faster than A* because it requires fewer calculations
    #          - Simple to implement
    #      Cons:
    #          - Can get stuck in local minima and find suboptimal solutions
    #          - May not always find a solution
     
    #  Uniform cost search:
    #      Pros:
    #          - Guaranteed to find the optimal solution if one exists
    #          - Simple to implement
    #      Cons:
    #          - Can be slower than A* because it expands all nodes, even if they are not promising
    #          - May require a lot of memory to store all nodes
     
    #  A* algorithm:                                                                                           
    #      Pros:                                                                                                
    #          - Guaranteed to find the optimal solution if one exists                                          
    #          - Can be more efficient than greedy search or uniform cost search because it uses a heuristic    
    #            function to guide the search                                                                     
    #      Cons:                                                                                                
    #          - More computationally expensive than greedy search or uniform cost search because               
    #            it requires more calculations                                                                  

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

    def euclidean_distance(self, point1, point2):
        # The Euclidean distance or Euclidean metric is the "ordinary" distance between two points that one would
        # measure with a ruler, and is given by the Pythagorean formula.
        # -> (0,0) (3,4) = 5

        x1, y1 = point1
        x2, y2 = point2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def manhattan_distance(self, point1, point2):
        # The Manhattan distance between two points is the sum of the absolute differences of their coordinates.
        # In other words, it is the total distance traveled on a grid to get from one point to the other.
        # -> (0,0) (3,4) = 7

        x1, y1 = point1
        x2, y2 = point2

        return abs(x1 - x2) + abs(y1 - y2)

    def chebyshev_distance(self, point1, point2):
        # The Chebyshev distance between two points is the maximum of the absolute differences of their coordinates.
        # In other words, it is the greatest distance between any two coordinates of the two points.
        # -> (0,0) (3,4) = 4

        x1, y1 = point1
        x2, y2 = point2

        return max([x1 - x2, y1 - y2])

    def resolve(self):
        ### A* algorithm is an algorithm of informed search -> you know what you're looking for

        # open_list = [start_puzzle]
        # closed_list = []

        # while open_list:
            ### find the node with the lowest f-value
            # current_puzzle = min(open_list, [puzzle.get_f() for puzzle in open_list])

            # if current_puzzle == goal
                # return function to reconstruct path

            ### remove current_puzzle from open_list and add it to closed_list
            # open_list.remove(current)
            # closed_list.append(current)

            # current_children = function to calculate current_children
            ### each child could be a puzzle object
            ### in this case we should add a "parent" attribute to puzzle object for reconstructing the path later
            ### the function to calculate children should be in puzzle class too
            ### we could also move f, g and h function to puzzle class and create attribute according to it
            ### this way it should be easier to manipulate them
            ### calculate current children function should create n child, defining their g, h, f and parent at initialization

            # for child in current_children:
                # if child in closed_list:
                    # continue

                # if child not in open_list:
                    # add child to open_list
                # elif child in open list and child.g < old_child.g:
                    # replace old_child by child

        ### No solution found
        # return None

        pass
