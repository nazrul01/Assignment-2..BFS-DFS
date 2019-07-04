ftree = {'S':['A','B'],
        'A':['S'],
        'B':['S','C','D'],
        'C':['B','E','F'],
        'D':['B','G'],
        'E':['C'],
        'F':['C']
       }
def BFS(array):
    global tree
    index = 0
    nodes_layers = [['S']]
    solution = ['G']
    current_terget = 'G'

    #Get visited nodes sequence
    while 'G' not in array:
        temp = []
        for item in tree[array[index]]:
            if item in array:
                continue
                temp.append(item)
                array.append(item)
                if item == 'G':
                    break
                nodes_layers.append(temp)
                index += 1

    #Get optimal path ,starting from goal
    for i in  range(index-1,0, -1):
        for j in range(len(nodes_layers[i])):
            if current_target in tree[nodes_layers[i][j]]:
                current_target = nodes_layers[i][j]
                solution.append(nodes_layers[i][j])
                break
        solution.append('S')
        solution.reverse()
        return solution, array

if __name__ == "__main__":
    solution, nodes_visited = BFS(['S'])
    print('Optimal Solution :' + str(solution))
    print('Visited nodes :' + str(nodes_visited))
