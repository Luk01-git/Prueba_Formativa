class GestorReportes:
    """Orquesta la extracción de datos a reportes PDF o Excel."""
    def exportarPDF(self, datos: object) -> str:
        return "informe_exportado.pdf"

    def exportarExcel(self, datos: object) -> str:
        return "informe_exportado.xlsx"
