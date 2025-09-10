import copy
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def getAllLocalizations(self):
        return DAO.getAllLocalizations()

    def buildGraph(self, localization):
        self._graph.clear()
        nodes = DAO.getAllNodes(localization)
        for n in nodes:
            self._idMap[n.GeneID] = n

        self._graph.add_nodes_from(nodes)

        archi = DAO.getAllEdges(localization, self._idMap)
        for a in archi:
            if a.gene1 in self._graph and a.gene2 in self._graph:
                self._graph.add_edge(a.gene1, a.gene2, weight=a.peso)


    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()


    def getEdges(self):
        #sortedEdges = sorted(self._graph.edges(data= True), key=lambda edge:edge[2]['weight'], reverse= False)
        #non da ordinare perchè già fatto nella query
        return self._graph.edges(data= True) #data=True --> senza avrei solo i due nodi, così ho anche il peso
        # [('A', 'B', {'weight': 3, 'color': 'red'})]


    def getConnesse(self):
        componentiConnesse = nx.connected_components(self._graph)
        ccSorted = sorted(componentiConnesse, key=lambda connessa: len(connessa), reverse=True)
        # x: len(x) --> ordino ogni componente per la sua lunghezza
        # reverse=True --> ordine crescente
        return ccSorted
