import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMapNodes = {}

        nodi = DAO.getAllNodes()

        for n in nodi:
            self._idMapNodes[n.ID] = n

    def buildGraph(self, distanza_minima):
        self._graph.clear()

        tratte = DAO.getEdgePeso(distanza_minima)

        for t in tratte:
            nodo_partenza = self._idMapNodes[t.a1]
            nodo_arrivo = self._idMapNodes[t.a2]
            self._graph.add_edge(nodo_partenza, nodo_arrivo, weight=t.peso_medio)

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getArchiDistanza(self):
        return list(self._graph.edges.data('weight'))