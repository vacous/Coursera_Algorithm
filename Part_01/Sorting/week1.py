# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 00:08:42 2016

@author: Administrator
"""
test = [1,8,3,2,9,7,20,13]
def merge_sort(list1):
    '''
    takes a list of nums and sort the num in order 
    '''
    if len(list1) == 1:
        return list1
    else:    
        sorted_list = []
        list_len = len(list1)
        first_half = merge_sort(list1[:list_len/2])
        second_half = merge_sort(list1[list_len/2:])
        # define and initialize the pointers 
        while first_half != [] and second_half != []:
            print first_half, second_half, sorted_list
            if first_half[0] < second_half[0]:
                sorted_list.append(first_half[0])
                first_half.pop(0)
            else:
                sorted_list.append(second_half[0])
                second_half.pop(0)
        sorted_list.extend(first_half + second_half)        
        return sorted_list


def inversion_counter(list1,ini_counter = 0):
    '''
    takes a list of nums and sort the num in order 
    '''
    if len(list1) == 1:
        return [list1,ini_counter]
    else:
        sorted_list = []
        list_len = len(list1)
        [first_half, first_counter] = inversion_counter(list1[:list_len/2])
        [second_half, second_counter] = inversion_counter(list1[list_len/2:])
        counter = first_counter + second_counter
        # define and initialize the pointers 
        while first_half != [] and second_half != []:
            if first_half[0] < second_half[0]:
                sorted_list.append(first_half[0])
                first_half.pop(0)
            else:
                sorted_list.append(second_half[0])
                if first_half != []:
                    counter += len(first_half) 
                second_half.pop(0)
#            print first_half, second_half, sorted_list, first_counter, second_counter, counter   
        sorted_list.extend(first_half + second_half) 
        return [sorted_list, counter]
test2 = [1,8,5,2,3,6,4]  

# import the given text file 
filename = 'D:\NetDrive\OneDrive\Coursera\Algorithm Design and Analysis-Stanford\Homework\IntergerArray.txt' 
with open(filename) as raw_list:
    given_list = []    
    for ele in raw_list:
        given_list.append(int(ele))
#print given_list        
        

print inversion_counter(given_list)[1]                
        
    