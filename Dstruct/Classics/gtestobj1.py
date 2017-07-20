"build class-based graph and run test searches"

from graph import Graph

for name in "ABCDEFG":
    exec("%s = Graph('%s')" % (name, name))

A.arcs = [B, E, G]
B.arcs = [C]
C.arcs = [D, E]
D.arcs = [F]
E.arcs = [C, F, G]
G.arcs = [A]

A.search(G)
for (start, stop) in [(E,D), (A,G), (B,A), (D,A)]:
    print(start.search(stop))
    






























