"graph search, using paths stack instead of recursion"

def search(start, goal, graph):
    solns = generate(([start], []), goal, graph)
    solns.sort(key=lambda x: len(x))
    return solns
def generate(paths, goal, graph):
    solns = []
    while paths:
        front, paths = paths
        state = front[-1]
        if state == goal:
            solns.append(front)
        else:
            for arc in graph[state]:
                if arc not in front:
                    paths = (front + [arc]), paths
    return solns

if __name__ == '__main__':
    import gtestfunc
    gtestfunc.tests(search)



























