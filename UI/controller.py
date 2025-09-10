import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        localization = self._model.getAllLocalizations()
        for l in localization:
            self._view.dd_localization.options.append(ft.dropdown.Option(l))
        self._view.update_page()


    def handle_graph(self, e):
        localization = self._view.dd_localization.value
        if localization is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun valore inserito", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(localization)

        numNodi, numArchi = self._model.graphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Creato grafo con {numNodi} nodi e {numArchi} archi"))



        edges = self._model.getEdges()
        for e in edges:
            self._view.txt_result.controls.append(ft.Text(f"{e[0].GeneID} <--> {e[1].GeneID} : peso {e[2]['weight']}"))

        self._view.update_page()

    def analyze_graph(self, e):
        cc = self._model.getConnesse()
        self._view.txt_result.controls.append(ft.Text("Le componenti connesse sono:"))
        for c in cc:
            if len(c) > 1:
                #self._view.txt_result.controls.append(ft.Text(f"{c} | dimensione: {len(c)}"))
                stringa = ""
                for nodo in c:
                    stringa += f"{nodo.GeneID}, "
                stringa += f" | dimensione componente = {len(c)}"
                self._view.txt_result.controls.append(ft.Text(stringa))

        self._view.update_page()

    def handle_path(self, e):
        pass

