"dictionary based graph representation"

Graph = {'A': ['B', 'E', 'G'],
         'B': ['C'],
         'C': ['D', 'E'],
         'D': ['F'],
         'E': ['C', 'F', 'G'],
         'F': [ ],
         'G': ['A']}

def tests(searcher):
    print(searcher('E', 'D', Graph))
    for x in ['AG', 'GF', 'BA', 'DA']:
        print(x, searcher(x[0], x[1], Graph))
        




















