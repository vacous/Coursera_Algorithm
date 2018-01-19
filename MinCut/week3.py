# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:08:09 2016

@author: Administrator
"""
import random 

def txt_to_list(filename):
    output = []
    with open(filename) as raw_list:
        for ele in raw_list:
            str_list = ele.split()
            output.append( [int(ele2) for ele2 in str_list])
    return output 
    
FINAL_CASE = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\kargerMinCut.txt')    
TEST_CASE_01 = [[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]
TEST_CASE_02 = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\MinCutTest\Test_01.txt')
print TEST_CASE_02
TEST_CASE_03 = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\MinCutTest\Test_02.txt')
TEST_CASE_04 = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\MinCutTest\Test_03.txt')
TEST_CASE_05 = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\MinCutTest\Test_04.txt')
TEST_CASE_06 = txt_to_list('D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\MinCutTest\Test_05.txt')
TEST_CASE_07 = [[1,2,3,4],[2,1,3,4],[3,2,1,5,5],[4,1,2,6],[5,3,3,7,8],[6,4,7,8],[7,5,6,8],[8,5,6,7]]
# define helper functions 
def merge_nodes(list1,list2,node_num):
    '''
    merge two nodes together and the edges connecting those two nodes 
    list1 and list2 are the two nodes arrays 
    '''
    super_node = node_num
    list_combine = list1 + list2 
    while list1[0] in list_combine:
        list_combine.remove(list1[0])
    while list2[0] in list_combine:
        list_combine.remove(list2[0])
    output = [super_node] + list_combine 
    return output, list1[0], list2[0] 


def random_cut(ad_list_ori):
    '''
    find the min cut for a given adjacency list using random nodes merge algo 
    '''
    ad_list = [ list(ele) for ele in ad_list_ori]
    node_num = len(ad_list) + 1 
    while len(ad_list) > 2:
        list1 = random.choice(ad_list)
        ad_list.remove(list1)
        list2_ini_node = random.choice(list1[1:])
        for ele in ad_list:
            if ele[0] == list2_ini_node:
                list2 = ele
        ad_list.remove(list2)
        new_list, node_replace1, node_replace2 = merge_nodes(list1,list2,node_num)
#        print list1, list2, ad_list_ori
#        print new_list
#        print new_list[0], node_replace1, node_replace2
        for array in ad_list:
            for idx in range(len(array)):
                if array[idx] == node_replace1:
                    array[idx] = new_list[0]
                elif array[idx] == node_replace2:
                    array[idx] = new_list[0]
        ad_list.append(new_list)
        node_num += 1             
#        print ad_list             
    return [len(ad_list[0])-1,ad_list]
 
  
def min_cut_value(trial_num,ad_list):
    '''
    run given num of trials and record the min value for 
    the ad_list result
    '''
    min_cut = float('inf')
    for num in range(trial_num):
#        print num, min_cut
        result = random_cut(ad_list)[0]
        if result < min_cut:
            min_cut = result
    return min_cut

for i in range(100):
    print i, min_cut_value(20,FINAL_CASE)     
#print random_cut(TEST_CASE_02)
    