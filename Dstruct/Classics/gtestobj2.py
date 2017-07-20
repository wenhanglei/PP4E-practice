from graph import Graph

S = Graph('s')
P = Graph('p')
A = Graph('a')
M = Graph('m')

S.arcs = [P, M]
P.arcs = [S, M, A]
A.arcs = [M]
print(S.search(M))































