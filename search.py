# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do NOT need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

#TODO
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    "*** YOUR CODE HERE ***"

    explored = dict()
    parent_nodes = dict()
    frontier = util.Stack()
    node = problem.getStartState()
    frontier.push((node, '', 0))
    explored[node] = ''
    solution = []
    if problem.isGoalState(node):
        return solution
    while(frontier.isEmpty() != True):
        node = frontier.pop()
        explored[node[0]] = node[1]
        if problem.isGoalState(node[0]):
            cur_key = node[0] #we found our node and have set it as our current key
            break
        for state in problem.getSuccessors(node[0]):
            if state[0] not in explored.keys():
                parent_nodes[state[0]] = node[0]
                frontier.push(state)
    #here the while goes and uses the our cur key that we set when we got to the goal to back track thru parents
    while (cur_key in parent_nodes.keys()):
        par_node = parent_nodes[cur_key]
        solution.insert(0, explored[cur_key])
        cur_key = par_node

    return solution

    #util.raiseNotDefined()

#TODO
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    explored = dict() #switched from set to dcit to associate states with actions in less confusing manner and to preform check in foreach loop
    parent_nodes = dict() #same as above ^ keep track of the branch cur visited parents
    frontier = util.Queue()
    node = problem.getStartState()
    frontier.push((node, '', 0)) #no direction to move to - new node
    explored[node] = '' #associate the start node with no movement in the explored hashmap
    solution = [] 
    if problem.isGoalState(node):
        return solution 
    while (not frontier.isEmpty()):
        node = frontier.pop()
        explored[node[0]] = node[1] #associating the nodes' state to its string direction
        if problem.isGoalState(node[0]):
            cur_key = node[0] #we found our node and have set it as our current key
            break
        for state in problem.getSuccessors(node[0]):
            if state[0] not in explored.keys() and state[0] not in parent_nodes.keys():
                parent_nodes[state[0]] = node[0]
                frontier.push(state)
    #here the while goes and uses the our cur key that we set when we got to the goal to back track thru parents
    while (cur_key in parent_nodes.keys()):
        par_node = parent_nodes[cur_key]
        solution.insert(0, explored[cur_key])
        cur_key = par_node

    return solution
    #util.raiseNotDefined()

#TODO
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    "*** YOUR CODE HERE ***"
    path_cost = dict() #a state with its cost association
    explored = dict()
    frontier = util.PriorityQueue()
    parent_nodes = dict()
    node = problem.getStartState()
    solution = []
    frontier.push((node, '', 0), 0) #no cost if starting at goal
    explored[node] = ''
    path_cost[node] = 0
    if problem.isGoalState(node):
        return solution
    while (not frontier.isEmpty()):
        node = frontier.pop()
        explored[node[0]] = node[1]
        if problem.isGoalState(node[0]):
            cur_key = node[0]
            break
        for state in problem.getSuccessors(node[0]):
            if state[0] not in explored.keys():
                current_cost = node[2] + state[2] #whats the path cost for movement at this point between nodes
                if state[0] in path_cost.keys():
                    if path_cost[state[0]] <= current_cost: #we've seen this nodes price befo but its cost now its more than previously so we keep goin
                        continue                    
                frontier.push((state[0], state[1], current_cost), current_cost)
                path_cost[state[0]] = current_cost #update cost model in our hashtable
                parent_nodes[state[0]] = node[0] 
    while (cur_key in parent_nodes.keys()):
        par_node = parent_nodes[cur_key]
        solution.insert(0, explored[cur_key])
        cur_key = par_node

    return solution                
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    #manhattan dist = abs(x1 - x2) + abs(y1 - y2)
    #euclidean dist = 2 * sqrt(x**2 + y**2) -> doesnt work for pacman
    return 0

#TODO
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    "*** YOUR CODE HERE ***"
    path_cost = dict()
    explored = dict()
    frontier = util.PriorityQueue()
    parent_nodes = dict()
    node = problem.getStartState()
    solution = []
    frontier.push((node, '', 0), 0) #no path_cost if starting at goal
    explored[node] = ''
    path_cost[node] = 0
    if problem.isGoalState(node):
        return solution
    while(not frontier.isEmpty()):
        node = frontier.pop()
        explored[node[0]] = node[1]
        if problem.isGoalState(node[0]):
            cur_key = node[0]
            break
        for state in problem.getSuccessors(node[0]):
            if state[0] not in explored.keys():
                cur_path_cost = node[2] + state[2] + heuristic(state[0], problem) #include the heuristic
                if state[0] in path_cost.keys():
                    if path_cost[state[0]] <= cur_path_cost:
                        continue
                ncost = node[2] + state[2]
                frontier.push((state[0], state[1], ncost), cur_path_cost)
                path_cost[state[0]] = cur_path_cost #update path_cost model in our hashtable
                parent_nodes[state[0]] = node[0] 

    while (cur_key in parent_nodes.keys()):
        par_node = parent_nodes[cur_key]
        solution.insert(0, explored[cur_key])
        cur_key = par_node

    return solution
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
