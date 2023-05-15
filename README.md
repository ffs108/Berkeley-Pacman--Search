See the original project instructions here: http://ai.berkeley.edu/search.html

This project, as the name suggests, focuses on search algorithms. Algorithms include: Depth-First Search, Breadth-First Search, Uniform Cost Search, and A* search. The heuristic for the A* is also modified between problems and adjusted for particular map layouts.

Commands of note:

  Depth-First Search: 
                     * python pacman.py -l tinyMaze -p SearchAgent
                     * python pacman.py -l mediumMaze -p SearchAgent
                     * python pacman.py -l bigMaze -z .5 -p SearchAgent
                      
  Breadth-First Search:
                     * python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
                     * python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
                      
  Uniform Cost Search:
                     * python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
                     * python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
                     * python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
                      
  General A* Search:
                     * python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
                      
  A* Search focusing on corners:
                     * python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
                     * python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
                      
  A* Heuristic Modification for Food prioritization:
                     * python pacman.py -l trickySearch -p AStarFoodSearchAgent
