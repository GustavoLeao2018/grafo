"""
Grafo = (Vertices, Aresta) 

G = (V, E)

Árvore == DAG (GAD portugues) -> Grafo Aciclico Direcionado

características
não direcionado vs direcionado
cicilo vs acíclico
conectados vs desconexos
ponderados vs não ponderados
esparço vs denso

operações
    - adicionar vertices = add_vertex(G, v)
    - remover vertices = remove_vertex(G, v)
    - adicionar aresta = add_edge(G, u, v, funcao_custo)
    - remover aresta = ramove_aresta(G, u, v)

    - vizinhos = neigbors(G, v) : lista
    - são ou não vizinhos (adjascentes)= adjacent(G, u, v):bool

    - get edge/vertex value
    - set edge/vertex value

Represemtação de grafo:
    Matriz de incidencias custo -> |V| * |E|
            a   b   c   d   e
        1 | 1 | -1 | 0 | 0 | 0
        2 | 1 | 0 | 1 | 1 | 0
        3 | 0 | 1 | 1 | 0 | 1
        4 | 0 | 0 | 0 | 1 | 1 

        01101 and 00011 = 0001


    Matriz de adjascencias custo -> |V| ^ 2
            1   2   3   4   
        1 | 0 | 1 | 1 | 0  
        2 | 1 | 1* | 1 | 1  
        3 | 1 | 1 | 0 | 1  
        4 | 0 | 1 | 1 | 0   



    Lista de adjagencias custo -> |V| + |E|
        | 1 |->{2,1}->{3,1}
        | 2 |->{1,1}->{3,1}->{4,1}
        | 3 |->{1,1}->{2,1}->{4,1}
        | 4 |->{2,1}->{3,1}




    fifo - fila
    lifo - pilha


    busca(G, v):
        l = [] |-> stack --> profundidade
               |-> queue -> largura
        l.push(v)
        G.remove_vertex(v)

        while !l.is_emptu():
            u - l.pop()

            for v in neighbors(G, u):
                l.push(v)
                G.remove_vertex(G)
            * do something(u)


    ALTENATIVA  CORRETA
    busca(G, v):
        l = [] |-> stack --> profundidade
               |-> queue -> largura
        l.push(v)
        G.remove_vertex(v)

        while not l.is_empty():
            u  = l.pop()
            fot v in g.negour(u):
            l.push(v)
        visited(u)

criar uma busca
quantos vertices+' '+ quantas arestas
links+' '+peso
1 2 1
1 3 1
2 2 1
2 3 1
2 4 1
3 4 1


"""



