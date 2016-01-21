from collections import defaultdict
import sys

vertices = {}

class node():

    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def set_adjacent(self,set):
        for item in set:
            # raw_input()
            # print item
            if item[0] in vertices.keys():
                new_node = vertices[item[0]]
            else:
                new_node = node(item[0])
                vertices[new_node.id] = new_node

            if new_node not in self.adjacent.keys():
                self.adjacent[new_node] = item[1]
        # for i in self.adjacent:
        #     print i.id, self.adjacent[i]





def make_node(dict):
    for keys in dict.keys():
        if keys not in vertices.keys():
            curr_node = node(keys)
            vertices[curr_node.id] = curr_node
            curr_node.set_adjacent(dict[curr_node.id])

        else:
            curr_node = vertices[keys]
            curr_node.set_adjacent(dict[curr_node.id])

## Read distance matrix and return a dictionary like {city1:(city2, distance)}

def readfile(link):
    dict = defaultdict(list)
    file = open(link)
    for lines in file.readlines():
        arr = lines.split()
        # raw_input()
        dict[arr[0]].append((arr[1], int(arr[2])))
    file.close()
    return dict


if __name__ == "__main__":
    ar = readfile("distance_matrix.txt")
    print ar
    make_node(ar)
    for k in vertices.keys():
        # print k
        print vertices[k].id
        for items in vertices[k].adjacent.keys():
            raw_input()

            print items.id, vertices[k].adjacent[items]
    # arad = vertices["Arad"]
    # for items in arad.adjacent.keys():
    #     print items.id,arad.adjacent[items]


