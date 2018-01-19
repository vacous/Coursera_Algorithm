# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 16:58:38 2016

@author: Administrator
"""
# import the given text file 
filename = 'D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\QuickSort.txt' 
with open(filename) as raw_list:
    given_list = []    
    for ele in raw_list:
        given_list.append(int(ele))


counter = 0
def quick_sort(list1):
    ''' 
    takes a list and use pivot in the comparisions 
    '''
    global counter 
    if len(list1) <= 1:
        counter += 0 
        return list1
    else:
        counter += len(list1)-1
        pivot = list1[0]
        sep_idx = 1
        end_idx = 0 
        while end_idx < len(list1)-1 : 
            end_idx += 1 
            if list1[end_idx] < pivot:
                temp = int(list1[end_idx])
                list1[end_idx] = int(list1[sep_idx])
                list1[sep_idx] = int(temp)
                sep_idx += 1
    return quick_sort(list1[1:sep_idx])+[pivot]+quick_sort(list1[sep_idx:])     
    
def quick_sort_last(list1):
    '''
    use the last ele as the pivot
    ''' 
    global counter
    if len(list1) <= 1:
        return list1
    else:
        counter += len(list1)-1
        list1[-1],list1[0] = list1[0],list1[-1]
        pivot = list1[0]
        sep_idx = 1
        end_idx = 0 
        while end_idx < len(list1)-1 : 
            end_idx += 1 
            if list1[end_idx] < pivot:
                temp = int(list1[end_idx])
                list1[end_idx] = int(list1[sep_idx])
                list1[sep_idx] = int(temp)
                sep_idx += 1
    return quick_sort(list1[1:sep_idx])+[pivot]+quick_sort(list1[sep_idx:]) 
    
def quick_sort_mid(list1):
    '''
    use the last ele as the pivot
    ''' 
    global counter
    if len(list1) <= 1:
        return list1
    else:
        counter += len(list1)-1
        choice = {list1[0]:0,
                  list1[len(list1)/2]:len(list1)/2,
                        list1[-1]:-1}
        keys = choice.keys()
        keys.remove(max(keys))
        keys.remove(min(keys))
        mid_idx = choice[keys[0]]
        list1[0],list1[mid_idx] = list1[mid_idx],list1[0]
        
        pivot = list1[0]
        sep_idx = 1
        end_idx = 0 
        while end_idx < len(list1)-1 : 
            end_idx += 1 
            if list1[end_idx] < pivot:
                temp = int(list1[end_idx])
                list1[end_idx] = int(list1[sep_idx])
                list1[sep_idx] = int(temp)
                sep_idx += 1
    return quick_sort(list1[1:sep_idx])+[pivot]+quick_sort(list1[sep_idx:])   
    
test1 = [1]
test2 = [8,3]                
test3 = [8,3,7,5]   

counter = 0     
#quick_sort(given_list)
#print counter
#counter = 0
#quick_sort_last(given_list)
#print counter
#counter = 0
#quick_sort_mid(given_list)
#print counter

