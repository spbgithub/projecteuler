'''BronKerbosch1(R, P, X):
       if P and X are both empty:
           report R as a maximal clique
       for each vertex v in P:
           BronKerbosch1(R union {v}, P intersection N(v), X intersection N(v))
           P := P setminus {v}
           X := X union {v}'''

