import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, distanza_minima):
        self._graph.clear()

        tratte = DAO.getEdgePeso(distanza_minima)

        for t in tratte:
            self._graph.add_edge(t.a1, t.a2, weight=t.peso_medio)

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getArchiDistanza(self):
        return list(self._graph.edges.data('weight'))