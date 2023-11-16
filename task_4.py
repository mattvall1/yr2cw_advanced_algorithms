"""
    Author: Matthew Vallance 001225832
    Purpose: Task 4
    Date: 14/11/23
"""
from clrs_library_slim import mst
import read_data

# Get graph and vertices
underground_graph, vertices = read_data.get_data()

# Return MST of underground_graph
underground_graph_mst = mst.kruskal(underground_graph)

# Get edge lists for both graphs
underground_graph_edges = AdjacencyListGraph.get_edge_list(underground_graph)
underground_graph_mst_edges = AdjacencyListGraph.get_edge_list(underground_graph_mst)

# Get removed edges
removed_edges = [x for x in underground_graph_edges if x not in underground_graph_mst_edges]

# Reassign station names to removed edges
removed_edges_names = []
for edge in removed_edges:
    removed_edges_names.append((vertices[edge[0]], vertices[edge[1]]))
    print(vertices[edge[0]] + ' -- ' + vertices[edge[1]])

"""
Observations: 
    1. cannot find where the "read_data.get_data()" is coming from, did you mean data_processing.get_data()?
        same for "AdjacencyListGraph", how is that you dont have to import it in your local machine?
            -> so the code doesnt run in my case and ill analyze it by reading it

    2. "underground_graph_mst_edges" is a list
            then, you get "removed_edges" by  comparing the values from "underground_graph_edges" to "underground_graph_mst_edges"
                that means for each value you look up in all the array
                tahts a O(n^2) time complexity
        HOW TO IMPROVE TO O(n):
        1. put "underground_graph_mst_edges" in a set
        2. thats it 
        this is because whenever you check a value of "x" in set(underground_graph_mst_edges), the calculation of the hashing is considered O(1) 
        
    3. the rest looks clean and good, but try to make a few tests to confirm it
    
    -------------------------------
    with MST
        1. You closed all the possible edges possible allowing all the nodes to be connected
        
    Your question from messaging: 
        1. whats infeasibility
            my def of infeasability is: is NOT POSSIBLE TO DO or it is NOT PRACTICAL
        2. how
            its infeasible if IT IS NOT POSSIBLE TO GO TO THE STATION
        3. when its infeasible
            e.g: lets say that you are in cutty sark and you need to go to lewisham
                the only possible path is using the DLR (lewisham train)
                there are no other lines that you can use
                now, if you close greenwich dlr,
                    you can only go to Mudchute 
                thism eans that its infeasible to close the greenwich dlr because you wont be able to go to lewisham

        you are asked: 
        1. If it's infeasible to meet the closure conditions, provide a reasoned justification
            think what did you get from the MST
            if you close one station, is the graph still FULLY CONNECTED?
                check this link: https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#/media/File:UndirectedDegrees.svg
            thats how you justify if its infeasible, if you get a unconnected graph then ...
            
        # TODO: Ask user to input two stations, so we can check feasibility of removing the link between them
        2. If the closure can be executed, list the affected routes by naming the adjacent stations on each line; for instance, if the segment between Piccadilly Circus and Green Park is shut down, specify it as "Piccadilly Circus -- Green Park"
            afteer checking the feasability of the graph,
            return the nodes in between
            1. run dijkstra
            2. name the nodes

            i am not sure what this question is asking but if its what i wrote above then that should work 

"""

