"""
TASK 4a 
 shutting down as many tube lines
 Travel between any two stations must remain viable.

return 
 If it's infeasible to meet the closure conditions, provide a reasoned justification
 list the affected routes


Try looking at minimum spaning tree (MST) algorihtm
    (kruskal algorithm, from clrs_library look at the chapter 21 -> mst.py)
    (prims algoirthm may work as well)

An idea would be to: 
1. get all the nodes and edges from the graph
2. use MST (kruskal) and get the minumum spanning tree 
        with this you would shut down as many tube lines as possible 
3. to get the affected routes, 
    use a set and get the diff between
        whole graph
        vs
        MST graph
"""