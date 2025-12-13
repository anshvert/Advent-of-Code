from typing import *
from math import sqrt

def get_distance(p1: List[int], p2: List[int]) -> float:
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def get_parent(parent_arr: List[int], p: int):
    if parent_arr[p] == -1:
        return p
    parent = get_parent(parent_arr, parent_arr[p])
    parent_arr[p] = parent
    return parent

def merge_boxes(parent: List[int], count_boxes: List[int], p1: int, p2: int):
    parent_p1, parent_p2 = get_parent(parent, p1), get_parent(parent, p2)
    if parent_p1 == parent_p2:
        return
    if count_boxes[parent_p1] < count_boxes[parent_p2]:
        count_boxes[parent_p2] += count_boxes[parent_p1]
        parent[parent_p1] = parent_p2
        count_boxes[parent_p1] = 0
    else:
        count_boxes[parent_p1] += count_boxes[parent_p2]
        parent[parent_p2] = parent_p1
        count_boxes[parent_p2] = 0
    return

def sol2():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        lines = [map(int,i.split(",")) for i in lines]
        coordinates,coordinates_distance = [],[]
        connection_ind = 0
        for x,y,z in lines:
            coordinates.append([x,y,z])
        for i in range(len(coordinates)):
            for j in range(i+1,len(coordinates)):
                distance = get_distance(coordinates[i],coordinates[j])
                coordinates_distance.append([i,j,distance])
        coordinates_distance.sort(key=lambda d:d[2])
        parent,count_boxes = [-1] * len(coordinates_distance),[1] * len(coordinates_distance)
        while 1:
            p1,p2,distance = coordinates_distance[connection_ind]
            merge_boxes(parent,count_boxes,p1,p2)
            if len(coordinates) in count_boxes:
                break
            connection_ind += 1
        print("X Product",coordinates[p1][0] * coordinates[p2][0])

# sol1()
sol2()