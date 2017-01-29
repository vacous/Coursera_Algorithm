# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 16:50:05 2016

@author: Administrator
"""

def txt_to_dict(filename):
    output_dict = {}
    with open(filename) as raw_list:
        for ele in raw_list:
            str_list = ele.split()
            for idx in range( len(str_list) ):
                if idx == 0:
                    node = int( str_list[0] )
                else:
                    node_dist = str_list[idx].split(',')
                    other_node = int( node_dist[0] )
                    dist = int( node_dist[1] )
                    node_pair = tuple( sorted( [node, other_node ] ))
                    output_dict[node_pair] = int(dist)
    return output_dict
    
dist_dict = txt_to_dict('dijkstraData.txt')

def txt_to_ungraph(filename):
    output_dict = {}
    with open(filename) as raw_list:
        for ele in raw_list:
            str_list = ele.split()
            for idx in range( len(str_list) ):
                if idx == 0:
                    head_node = int(str_list[0])
                    output_dict[ head_node ] = set()
                else:
                    node_dist = str_list[idx].split(',')
                    other_node = int( node_dist[0] )
                    output_dict[ head_node ].add( other_node )
    return output_dict

ungraph = txt_to_ungraph('dijkstraData.txt')

def if_all_visited(boo_dict):
    output_boo = True 
    for ele in boo_dict:
        output_boo = output_boo and ele
    return output_boo

def find_shorest_path(ungraph,dist_graph,start_node):
    '''
    use ungraph to find the neighbors 
    and use dist_graph to find the shorest distance 
    '''
    visit_boo = {}
    for node in ungraph.keys():
        visit_boo[node] = False
    shortest_path = {}
    shortest_path[start_node] = 0
    visit_boo[start_node] = True
    while len(shortest_path) != len(ungraph):
        print shortest_path
        temp_min_dist = float('inf')
        next_node = None
        visited_nodes = shortest_path.keys()
        for each_node in visited_nodes:
            for each_neighbor in ungraph[each_node]:
#                print ungraph[each_node]
                if visit_boo[each_neighbor] == False:
                    temp_dist = shortest_path[each_node] + dist_graph[tuple(sorted([each_node,each_neighbor]))]
                    if temp_dist < temp_min_dist:
                        temp_min_dist = temp_dist
                        next_node = each_neighbor
        shortest_path[next_node] = temp_min_dist
        visit_boo[next_node] = True 
    return shortest_path
        
result = find_shorest_path(ungraph,dist_dict ,1)           
answer_node = [7,37,59,82,99,115,133,165,188,197]
for ele in answer_node:
    print result[ele]
