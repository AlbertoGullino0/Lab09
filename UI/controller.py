import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_aereoporti(self, e):

        distanza_minima = self._view.txt_distanzaMinima.value

        if not distanza_minima:
            self._view.create_alert("Inserisci una distanza!")
            return

        try:
            distanza_minima = float(distanza_minima)
        except ValueError:
            self._view.create_alert("Inserisci un valore numerico valido!")
            return

        self._model.buildGraph(distanza_minima)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi.")
        )
        self._view.txt_result.controls.append(ft.Text("Elenco degli archi:"))

        archi = self._model.getArchiDistanza()

        for u, v, peso in archi:
            self._view.txt_result.controls.append(
                ft.Text(f"{u} - {v}: {peso:.0f}")
            )

        self._view.update_page()
