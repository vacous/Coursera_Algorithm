# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 01:13:31 2016

@author: Administrator
"""

from collections import deque

FILENAME = 'SCC.txt'
def txt_to_list(filename):
    output = []
    with open(filename) as raw_list:
        for ele in raw_list:
            str_list = ele.split()
            output.append( [int(ele2) for ele2 in str_list])
    return output 



#print TEST_CASE_01

#def input_to_adj_list_tailfirst(input_list):
#    '''
#    convert a list[lists] in to a adj list 
#    to the format [head,[tails]] tails sorted 
#    heads also sorted 
#    '''
#    if input_list == []:
#        return input_list 
#    adj_list = [ [input_list[0][1],[input_list[0][0]]] ]
#    jdx = 0
#    for idx in range(1,len(input_list)):
#        if input_list[idx][0] == input_list[idx-1][0]:
#            adj_list[jdx][1].append(input_list[idx][1])
#        else:
#            adj_list.append( [input_list[idx][0],[input_list[idx][1]]] )
#            jdx += 1 
#    return adj_list

def input_to_dict_head(input_list):
    '''
    convert the input_list in to a head-tail dict
    {head:set(tails)}
    '''
    if input_list == []:
        return {}
        
    sorted_input = sorted(input_list, key=lambda tail_head: tail_head[1]) 
    adj_dict = {sorted_input[0][1]:set([sorted_input[0][0]])}
    for idx in range(1,len(input_list)):
        current_head = sorted_input[idx][1]
        current_tail = sorted_input[idx][0]
        previous_head = sorted_input[idx-1][1]
        if current_head == previous_head:
            adj_dict[current_head].add(current_tail)
        else:
            adj_dict[current_head] = set([current_tail])
    # add those heads with no tails into the dict 
    for ele in input_list:
        if ele[0] not in adj_dict:
            adj_dict[ele[0]] = set()
    return adj_dict 

#def remark(input_list):
#    '''
#    take a dgraph in dict format 
#    head:set(tails)
#    generate a dcit {new_node_num:old_node_num} using dfs
#    '''
#    remark_dict = {}
#    remark_value = 1 
#    input_dict = input_to_dict_head(input_list)
#    print input_dict 
#    visit_order = deque( input_dict.keys() )
#    visit_dict = {}
#    for node in input_dict.keys():
#        visit_dict[node] = False
#    
##    print input_dict 
##    print input_dict[input_list[0][0]]
#    while visit_order != deque():
#        # if no tail node
#         
#        while input_dict[ visit_order[-1] ] == set():
#            remark_dictp[visit_order] =
#            visit_dict[visit_order[-1]] = True 
#            visit_order.pop()
##            print visit_order
#            if visit_order == deque():
#                break 
#        if visit_order == deque():
#            break 
#        # if there is a tail run dfs      
#        stack = deque( [visit_order[-1]] )
#        visit_order.popleft()
#        visit_dict[visit_order[-1]] = True 
#        while stack != deque():
##            print visit_dict, stack 
#            head = stack[-1]
#            print stack
#            next_node_set = input_dict[head]
#            temp_node_list = deque(list(next_node_set))
#            loop_breaker = False
#            while temp_node_list != deque([]) and loop_breaker == False:
#                if visit_dict[temp_node_list[0]] == True: 
#                    next_node_set.remove(temp_node_list[0])
#                    temp_node_list.popleft()
#                else:
#                    loop_breaker = True 
#            if temp_node_list == deque():
#                stack.pop()
#    #            print head, remark_value
#                remark_dict[head] = remark_value 
#                remark_value += 1
#            else:
#                stack.append(temp_node_list[0]) 
#                visit_dict[temp_node_list[0]] = True 
#    return remark_dict 

 
def remark(input_list):
    '''
    use dfs to create a mapping dict based on the dfs run time
    '''
    input_dict = input_to_dict_head(input_list)
    visit_set = set( input_dict.keys() )
    visit_boo = {}
    mapping_dict = {}
    run_time = 0 
    for ele in visit_set:
        visit_boo[ele] = False 

    while visit_set != set():
        ini_node = visit_set.pop()
        stack = deque([ini_node])
        visit_boo[ini_node] = True
        while stack != deque():
#            print stack, visit_set
            head = stack[-1]
            tail_node_set = input_dict[head]
#            print tail_node_set
            # if no tail 
            if tail_node_set == set():
                mapping_dict[ stack.pop() ] = run_time
                run_time += 1 
            else:
                # check if all tails are visited 
                copy_deque = deque( list(tail_node_set) )
                while copy_deque != deque():
                    tail_node = copy_deque[0]
                    if visit_boo[tail_node] == False:
                        visit_boo[tail_node] = True 
                        visit_set.remove(tail_node)
                        stack.append(tail_node)
                        break
                    copy_deque.popleft()
                if copy_deque == deque():
                    mapping_dict[ stack.pop() ] = run_time 
                    run_time += 1
    return mapping_dict 
    
    


   
def remark_dict(input_list):
    '''
    remark the original list 
    '''
    remark_dict = remark(input_list)
#    print remark_dict 
    original_list = list(input_list)
    for pair in original_list:
        temp_pair = list(pair)
        pair[1] =  remark_dict[temp_pair[0]]
        pair[0] = remark_dict[temp_pair[1]]
    output_dict = input_to_dict_head(original_list)
    return output_dict

def dgraph_deque(dgraph_set):
    '''
    covert a dgraph in to head:deque
    '''
    output_graph = {}
    for ele in dgraph_set:
        output_graph[ele] = deque( list(dgraph_set[ele]) )
    return output_graph 


import time
def find_max_cc(input_list):
    '''
    find the size of the scc's
    '''
    ini_time = time.time()
    counter = 0 
    dgraph = dgraph_deque( remark_dict(input_list) ) 
#    print dgraph
    visited_order = deque(dgraph.keys())
    visited_dict = {}
    for node in visited_order:
        visited_dict[node] = False
        
    size_set = set()
    while visited_order != deque(): 
        ini_node = visited_order.pop()
        stack = deque([ ini_node ])
        visited_dict[ini_node] = True
        size = 1
        while stack != deque():
            head = stack[-1]
#            print stack
            tail_node_deque= dgraph[ head ]
            if tail_node_deque == deque():
                size_set.add(1) 
                stack.pop()
            else:
                while tail_node_deque != deque():
#                    print dgraph
                    tail_node = tail_node_deque[0]
                    if visited_dict[tail_node] == False:
                        visited_dict[tail_node] = True 
                        stack.append(tail_node)
                        size += 1 
                        break 
                    tail_node_deque.popleft()
                if tail_node_deque == deque():
                    stack.pop()
        counter += 1 
        if counter == 218471 :
            print '!!!!!!!!!!!!!!!!!'
            print stack 
            print visited_order[-1]
            print '!!!!!!!!!!!!!!!!!!!!'
        print counter 
        print size_set
        print (time.time()-ini_time)/counter 
        print '====================='
        size_set.add(size)           
    return size_set 
  
#test = []
test2 = [[1,10],[10,4],[7,1],[4,7],[9,7],[9,3],[3,6],[6,9],[8,6],[2,8],[8,5],[5,2]] 
#test3 = [[7,1],[4,7],[1,4],[9,7],[9,9]]
test4 = [[1,2],[2,1],[3,1],[1,1]]
test5 = [[1,2],[2,3],[3,1],[3,4],[5,4],[6,4],[8,6],[6,7],[7,8],[4,3],[4,6]]
test6 = [[1,2]]
test7 = [[1,4],[2,1],[3,2],[4,3],[5,2]]
#TEST_CASE_01 = txt_to_list('test_case_01.txt')
CONVERTED_INPUT_LIST = txt_to_list(FILENAME)  
#remark(CONVERTED_INPUT_LIST) 
#remark_dict_test = remark(test2)       
print find_max_cc(CONVERTED_INPUT_LIST)
#print remark_dict(test5)
#print find_max_cc(TEST_CASE_01) 
#print find_max_cc(test2)
#print find_max_cc(test2)
#print input_to_dict_head(test3)
#print input_to_dict_head(test5)
#print remark(test2)