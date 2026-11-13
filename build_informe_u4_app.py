# -*- coding: utf-8 -*-
"""
Generador del Informe Academico Oficial para la Aplicacion U4: Tecnicas Algoritmicas
Materia: Programacion I (INF120) - Evans Balcazar Veizaga
Estudiante: Gustavo Melgar Baldivieso - Registro: 213195623
Formato: DOCX (Microsoft Word) y PDF de alta calidad
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
from fpdf import FPDF

# ==============================================================================
# METADATOS INSTITUCIONALES
# ==============================================================================

ESTUDIANTE  = "GUSTAVO MELGAR BALDIVIESO"
REGISTRO    = "213195623"
MATERIA     = "PROGRAMACION I"
SIGLA       = "INF120"
GRUPO       = "SC"
DOCENTE     = "LIC. EVANS BALCAZAR VEIZAGA"
UNIVERSIDAD = "UNIVERSIDAD AUTONOMA GABRIEL RENE MORENO"
FACULTAD    = "FACULTAD DE INGENIERIA EN CIENCIAS DE LA COMPUTACION Y TELECOMUNICACIONES"
CARRERA     = "CARRERA DE INGENIERIA EN SISTEMAS / INFORMATICA"
LUGAR_FECHA = "SANTA CRUZ DE LA SIERRA - BOLIVIA, NOVIEMBRE 2026"
TITULO      = "APLICACION U4: OTRAS TECNICAS ALGORITMICAS EN 1, 2 O MAS OBJETOS"
SUBTITULO   = "Implementacion de la Clase VectorPlus y Desarrollo de Interfaz Grafica (GUI) en Lazarus"
GITHUB_REPO = "https://github.com/gumebdoc/inf120_app04"

# ==============================================================================
# FUNCIONES AUXILIARES PARA FORMATO DOCX
# ==============================================================================

def set_cell_background(cell, hex_color):
    """Aplica color de fondo hexadecimal a una celda de tabla en Word."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Establece padding interno en dxa para una celda."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    """Inserta un bloque de codigo sombreado y monoespaciado en el documento Word."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05

    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph()

# ==============================================================================
# DEFINICION DE DATOS DE LAS 5 OPERACIONES
# ==============================================================================

OPERACIONES_DATA = [
    {
        "num": 1,
        "nombre": "Cantidad de Cortes de Control",
        "enunciado": "Determinar y contabilizar la cantidad exacta de cortes de control que presenta el vector.",
        "analisis": (
            "El algoritmo de Corte de Control es una técnica estructurada para procesar conjuntos de datos homogéneos "
            "agrupados por una clave común. La precondición algorítmica fundamental establece que los datos deben encontrarse "
            "rigurosamente ordenados por el criterio de corte para que los elementos iguales ocupen posiciones contiguas.\n\n"
            "Estrategia de solución pedagógica en Programación I:\n"
            "1. Si el vector está vacío (dim = 0), retorna 0 cortes.\n"
            "2. Para preservar la integridad del arreglo original sin alterar el orden original que pudiera requerir el usuario, "
            "se crea una copia temporal del vector y se aplica un ordenamiento ascendente básico (ordenamiento por burbuja).\n"
            "3. Se inicia un contador de cortes en 0 y un puntero de posición i en 1 (indexación base 1 estándar de la materia).\n"
            "4. Se implementa la estructura canónica de corte mediante dos ciclos 'while' anidados:\n"
            "   - El ciclo exterior avanza de corte en corte mientras i <= dim.\n"
            "   - Se toma el elemento en la posición i como la 'clave' del nuevo corte y se incrementa el contador de cortes.\n"
            "   - El ciclo interior consume todos los elementos consecutivos cuyo valor coincide exactamente con dicha clave.\n"
            "5. Al concluir el recorrido completo, se libera la copia y se retorna el total de cortes contabilizados."
        ),
        "pseudocodigo": (
            "ALGORITMO CantidadCortesControl() RETORNA ENTERO\n"
            "    SI dim == 0 ENTONCES\n"
            "        RETORNAR 0\n"
            "    FIN_SI\n"
            "    \n"
            "    // Paso 1: Clonar y ordenar ascendentemente para agrupar claves iguales\n"
            "    Vector vTemp := Clonar(Self)\n"
            "    vTemp.OrdenarAscendente()\n"
            "    \n"
            "    // Paso 2: Recorrido canónico de cortes de control\n"
            "    ENTERO cant := 0\n"
            "    ENTERO i := 1\n"
            "    \n"
            "    MIENTRAS (i <= vTemp.GetDim()) HACER\n"
            "        ENTERO clave := vTemp.GetElem(i)\n"
            "        cant := cant + 1   // Inicio de un nuevo corte de control\n"
            "        \n"
            "        // Avanzar y consumir todos los elementos que compartan la misma clave\n"
            "        MIENTRAS (i <= vTemp.GetDim()) Y (vTemp.GetElem(i) == clave) HACER\n"
            "            i := i + 1\n"
            "        FIN_MIENTRAS\n"
            "    FIN_MIENTRAS\n"
            "    \n"
            "    Liberar(vTemp)\n"
            "    RETORNAR cant\n"
            "FIN_ALGORITMO"
        ),
        "pascal": (
            "function TVectorPlus.CantidadCortesControl(): integer;\n"
            "var\n"
            "  vTemp: TVectorPlus;\n"
            "  i, cant, clave: integer;\n"
            "begin\n"
            "  if dim = 0 then\n"
            "  begin\n"
            "    Result := 0;\n"
            "    Exit;\n"
            "  end;\n"
            "\n"
            "  // 1. Se ordena una copia para asegurar la contiguidad de claves\n"
            "  vTemp := Clonar();\n"
            "  vTemp.OrdenarAscendente();\n"
            "\n"
            "  // 2. Estructura canonica de corte de control\n"
            "  cant := 0;\n"
            "  i := 1;\n"
            "  while i <= vTemp.GetDim() do\n"
            "  begin\n"
            "    clave := vTemp.GetElem(i);\n"
            "    Inc(cant); // Se identifica un nuevo grupo/corte\n"
            "    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do\n"
            "      Inc(i);\n"
            "  end;\n"
            "\n"
            "  vTemp.Free;\n"
            "  Result := cant;\n"
            "end;"
        ),
        "prueba_encabezados": ["Corte #", "i inic.", "Clave", "Condición (vTemp[i] = Clave)", "i final", "cant acumulado"],
        "prueba_filas": [
            ["1", "1", "0", "vTemp[1] = 0 (Verdadero)", "2", "1"],
            ["2", "2", "1", "vTemp[2] = 1 (Verdadero)", "3", "2"],
            ["3", "3", "2", "vTemp[3]=2, vTemp[4]=2 (Verdadero, Verdadero)", "5", "3"],
            ["4", "5", "3", "vTemp[5..8] = 3 (4 elementos iguales)", "9", "4"],
            ["5", "9", "4", "vTemp[9] = 4 (Verdadero)", "10", "5"],
            ["6", "10", "6", "vTemp[10] = 6 (Verdadero)", "11", "6"],
            ["7", "11", "8", "vTemp[11..13] = 8 (3 elementos iguales)", "14", "7"]
        ],
        "prueba_nota": (
            "Vector original de prueba: VA = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3] (dim = 13).\n"
            "Vector ordenado auxiliar:   vTemp = [0, 1, 2, 2, 3, 3, 3, 3, 4, 6, 8, 8, 8].\n"
            "Al finalizar: i = 14 > dim (condición falsa). Total de cortes contabilizados = 7."
        )
    },
    {
        "num": 2,
        "nombre": "Cantidad de Elementos entre Cortes de Control",
        "enunciado": "Calcular la cantidad de elementos (frecuencia) que contiene cada uno de los cortes de control del vector.",
        "analisis": (
            "Esta operación complementa la técnica de cortes de control al cuantificar la profundidad o tamaño de cada bloque. "
            "En aplicaciones reales de procesamiento de información (reportes de ventas, notas de alumnos, inventarios), "
            "el corte de control no solo requiere saber cuántos grupos existen, sino cuántos registros conforman cada subgrupo.\n\n"
            "Estrategia algorítmica:\n"
            "1. Se reciben como parámetros dos objetos TVectorPlus por referencia o destino:\n"
            "   - VValores: Almacenará la clave única correspondiente a cada corte detectado.\n"
            "   - VCantidades: Almacenará el número de elementos pertenecientes a dicho corte.\n"
            "2. Se limpian ambos vectores receptores para asegurar consistencia.\n"
            "3. Se trabaja sobre una copia ordenada del vector original.\n"
            "4. En el ciclo exterior, para cada corte se inicializa un contador local cant := 0 y se almacena la clave.\n"
            "5. En el ciclo interior, por cada elemento consecutivo igual a la clave se incrementa cant y se avanza el puntero i.\n"
            "6. Al finalizar el corte interior, se añade la clave a VValores y la cantidad cant a VCantidades.\n"
            "7. Adicionalmente, se provee la función ResumenElementosEntreCortes() para emitir un reporte legible en la GUI."
        ),
        "pseudocodigo": (
            "ALGORITMO CantidadElementosEntreCortes(SALIDA: Vector VValores, SALIDA: Vector VCantidades)\n"
            "    VValores.Clear()\n"
            "    VCantidades.Clear()\n"
            "    SI dim == 0 ENTONCES\n"
            "        RETORNAR\n"
            "    FIN_SI\n"
            "    \n"
            "    Vector vTemp := Clonar(Self)\n"
            "    vTemp.OrdenarAscendente()\n"
            "    ENTERO i := 1\n"
            "    \n"
            "    MIENTRAS (i <= vTemp.GetDim()) HACER\n"
            "        ENTERO clave := vTemp.GetElem(i)\n"
            "        ENTERO cant := 0\n"
            "        \n"
            "        // Contabilizar todos los elementos dentro de este corte\n"
            "        MIENTRAS (i <= vTemp.GetDim()) Y (vTemp.GetElem(i) == clave) HACER\n"
            "            cant := cant + 1\n"
            "            i := i + 1\n"
            "        FIN_MIENTRAS\n"
            "        \n"
            "        VValores.AddElem(clave)\n"
            "        VCantidades.AddElem(cant)\n"
            "    FIN_MIENTRAS\n"
            "    \n"
            "    Liberar(vTemp)\n"
            "FIN_ALGORITMO"
        ),
        "pascal": (
            "procedure TVectorPlus.CantidadElementosEntreCortes(VValores, VCantidades: TVectorPlus);\n"
            "var\n"
            "  vTemp: TVectorPlus;\n"
            "  i, cant, clave: integer;\n"
            "begin\n"
            "  if VValores <> nil then VValores.Clear();\n"
            "  if VCantidades <> nil then VCantidades.Clear();\n"
            "  if dim = 0 then Exit;\n"
            "\n"
            "  vTemp := Clonar();\n"
            "  vTemp.OrdenarAscendente();\n"
            "  i := 1;\n"
            "  while i <= vTemp.GetDim() do\n"
            "  begin\n"
            "    clave := vTemp.GetElem(i);\n"
            "    cant := 0;\n"
            "    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do\n"
            "    begin\n"
            "      Inc(cant);\n"
            "      Inc(i);\n"
            "    end;\n"
            "    if VValores <> nil then VValores.AddElem(clave);\n"
            "    if VCantidades <> nil then VCantidades.AddElem(cant);\n"
            "  end;\n"
            "  vTemp.Free;\n"
            "end;"
        ),
        "prueba_encabezados": ["Corte #", "Clave", "Rango Índices", "Elementos en el Corte", "cant (frecuencia)", "Estado VCantidades"],
        "prueba_filas": [
            ["1", "0", "vTemp[1]", "0", "1", "[1]"],
            ["2", "1", "vTemp[2]", "1", "1", "[1, 1]"],
            ["3", "2", "vTemp[3..4]", "2, 2", "2", "[1, 1, 2]"],
            ["4", "3", "vTemp[5..8]", "3, 3, 3, 3", "4", "[1, 1, 2, 4]"],
            ["5", "4", "vTemp[9]", "4", "1", "[1, 1, 2, 4, 1]"],
            ["6", "6", "vTemp[10]", "6", "1", "[1, 1, 2, 4, 1, 1]"],
            ["7", "8", "vTemp[11..13]", "8, 8, 8", "3", "[1, 1, 2, 4, 1, 1, 3]"]
        ],
        "prueba_nota": (
            "Comprobación aritmética de consistencia:\n"
            "Suma total de frecuencias = 1 + 1 + 2 + 4 + 1 + 1 + 3 = 13 elementos.\n"
            "Coincide con la dimensión del vector original: dim = 13."
        )
    },
    {
        "num": 3,
        "nombre": "Dividir un Vector en dos (Par e Impar)",
        "enunciado": "Separar y clasificar los elementos del vector en dos nuevos vectores: uno para números pares y otro para impares.",
        "analisis": (
            "La partición o filtrado de arreglos es una de las operaciones fundamentales en algoritmos de clasificación. "
            "El objetivo es discriminar cada valor del arreglo según un predicado lógico de paridad aritmética.\n\n"
            "Estrategia algorítmica:\n"
            "1. Se reciben dos objetos TVectorPlus destinados a almacenar los pares (VPar) e impares (VImpar).\n"
            "2. Se inicializan limpiando cualquier dato previo en ambos contenedores.\n"
            "3. Se ejecuta un recorrido secuencial básico mediante un ciclo 'for' desde la posición 1 hasta dim.\n"
            "4. Para cada elemento elem[i], se evalúa la operación residuo: (elem[i] mod 2 = 0):\n"
            "   - Si la condición es Verdadera, el número es par (incluyendo el 0 según las reglas aritméticas) y se anexa a VPar.\n"
            "   - Si la condición es Falsa, el número es impar y se anexa a VImpar.\n"
            "5. Esta operación no destruye el vector original y mantiene el orden relativo de aparición original de cada elemento."
        ),
        "pseudocodigo": (
            "ALGORITMO DividirParImpar(SALIDA: Vector VPar, SALIDA: Vector VImpar)\n"
            "    VPar.Clear()\n"
            "    VImpar.Clear()\n"
            "    \n"
            "    PARA i DESDE 1 HASTA dim CON PASO 1 HACER\n"
            "        ENTERO valor := elem[i]\n"
            "        SI (valor MOD 2 == 0) ENTONCES\n"
            "            VPar.AddElem(valor)\n"
            "        SINO\n"
            "            VImpar.AddElem(valor)\n"
            "        FIN_SI\n"
            "    FIN_PARA\n"
            "FIN_ALGORITMO"
        ),
        "pascal": (
            "procedure TVectorPlus.DividirParImpar(VPar, VImpar: TVectorPlus);\n"
            "var\n"
            "  i, valor: integer;\n"
            "begin\n"
            "  if VPar <> nil then VPar.Clear();\n"
            "  if VImpar <> nil then VImpar.Clear();\n"
            "\n"
            "  for i := 1 to dim do\n"
            "  begin\n"
            "    valor := elem[i];\n"
            "    if (valor mod 2 = 0) then\n"
            "    begin\n"
            "      if VPar <> nil then VPar.AddElem(valor);\n"
            "    end\n"
            "    else\n"
            "    begin\n"
            "      if VImpar <> nil then VImpar.AddElem(valor);\n"
            "    end;\n"
            "  end;\n"
            "end;"
        ),
        "prueba_encabezados": ["i", "Elemento elem[i]", "elem[i] mod 2", "Clasificación", "VPar acumulado", "VImpar acumulado"],
        "prueba_filas": [
            ["1", "2", "0", "PAR", "[2]", "[]"],
            ["2", "0", "0", "PAR", "[2, 0]", "[]"],
            ["3", "2", "0", "PAR", "[2, 0, 2]", "[]"],
            ["4", "1", "1", "IMPAR", "[2, 0, 2]", "[1]"],
            ["5", "3", "1", "IMPAR", "[2, 0, 2]", "[1, 3]"],
            ["6", "8", "0", "PAR", "[2, 0, 2, 8]", "[1, 3]"],
            ["7", "4", "0", "PAR", "[2, 0, 2, 8, 4]", "[1, 3]"],
            ["8", "8", "0", "PAR", "[2, 0, 2, 8, 4, 8]", "[1, 3]"],
            ["9", "6", "0", "PAR", "[2, 0, 2, 8, 4, 8, 6]", "[1, 3]"],
            ["10", "8", "0", "PAR", "[2, 0, 2, 8, 4, 8, 6, 8]", "[1, 3]"],
            ["11", "3", "1", "IMPAR", "[2, 0, 2, 8, 4, 8, 6, 8]", "[1, 3, 3]"],
            ["12", "3", "1", "IMPAR", "[2, 0, 2, 8, 4, 8, 6, 8]", "[1, 3, 3, 3]"],
            ["13", "3", "1", "IMPAR", "[2, 0, 2, 8, 4, 8, 6, 8]", "[1, 3, 3, 3, 3]"]
        ],
        "prueba_nota": (
            "Resultado de la división de VA = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]:\n"
            "VPar:   [2, 0, 2, 8, 4, 8, 6, 8] (dim = 8 pares).\n"
            "VImpar: [1, 3, 3, 3, 3]          (dim = 5 impares).\n"
            "Total = 8 + 5 = 13 elementos clasificados sin pérdida de información."
        )
    },
    {
        "num": 4,
        "nombre": "Intercalar dos Vectores (Un elemento de A y uno de B)",
        "enunciado": "Combinar de forma alternada los elementos de dos vectores, tomando un elemento del primer vector y uno del segundo consecutivamente.",
        "analisis": (
            "La técnica de intercalación (interleaving / mezcla alternada) combina dos colecciones manteniendo una política "
            "estricta de alternancia uno a uno entre fuentes independientes.\n\n"
            "Estrategia algorítmica:\n"
            "1. Se reciben el vector secundario VB y el vector receptor VResult.\n"
            "2. Se inicializan dos punteros de lectura independientes: i := 1 (para Vector A / Self) y j := 1 (para Vector B).\n"
            "3. En la fase simultánea, mientras ambos punteros sean válidos (i <= dimA y j <= dimB), se agrega elemA[i] a VResult "
            "y de inmediato se agrega elemB[j] a VResult, incrementando ambos punteros.\n"
            "4. En la fase remanente, cuando uno de los vectores se agota antes que el otro por tener menor dimensión:\n"
            "   - Si quedan elementos en Vector A (i <= dimA), se vacían secuencialmente al final de VResult.\n"
            "   - Si quedan elementos en Vector B (j <= dimB), se vacían secuencialmente al final de VResult.\n"
            "5. Esta lógica garantiza que la dimensión de VResult será exactamente igual a dimA + dimB."
        ),
        "pseudocodigo": (
            "ALGORITMO Intercalar(ENTRADA: Vector VB, SALIDA: Vector VResult)\n"
            "    VResult.Clear()\n"
            "    ENTERO i := 1\n"
            "    ENTERO j := 1\n"
            "    \n"
            "    // Fase 1: Intercalación alternada 1 a 1\n"
            "    MIENTRAS (i <= dim) Y (j <= VB.GetDim()) HACER\n"
            "        VResult.AddElem(elem[i])\n"
            "        VResult.AddElem(VB.GetElem(j))\n"
            "        i := i + 1\n"
            "        j := j + 1\n"
            "    FIN_MIENTRAS\n"
            "    \n"
            "    // Fase 2: Descargar remanente de Vector A si es más largo\n"
            "    MIENTRAS (i <= dim) HACER\n"
            "        VResult.AddElem(elem[i])\n"
            "        i := i + 1\n"
            "    FIN_MIENTRAS\n"
            "    \n"
            "    // Fase 3: Descargar remanente de Vector B si es más largo\n"
            "    MIENTRAS (j <= VB.GetDim()) HACER\n"
            "        VResult.AddElem(VB.GetElem(j))\n"
            "        j := j + 1\n"
            "    FIN_MIENTRAS\n"
            "FIN_ALGORITMO"
        ),
        "pascal": (
            "procedure TVectorPlus.Intercalar(VB, VResult: TVectorPlus);\n"
            "var\n"
            "  i, j: integer;\n"
            "begin\n"
            "  if VResult = nil then Exit;\n"
            "  VResult.Clear();\n"
            "  i := 1;\n"
            "  j := 1;\n"
            "\n"
            "  // 1. Alternancia 1 a 1 mientras existan datos en ambos vectores\n"
            "  while (i <= dim) and ((VB <> nil) and (j <= VB.GetDim())) do\n"
            "  begin\n"
            "    VResult.AddElem(elem[i]);\n"
            "    VResult.AddElem(VB.GetElem(j));\n"
            "    Inc(i);\n"
            "    Inc(j);\n"
            "  end;\n"
            "\n"
            "  // 2. Elementos sobrantes de Vector A\n"
            "  while i <= dim do\n"
            "  begin\n"
            "    VResult.AddElem(elem[i]);\n"
            "    Inc(i);\n"
            "  end;\n"
            "\n"
            "  // 3. Elementos sobrantes de Vector B\n"
            "  if VB <> nil then\n"
            "  begin\n"
            "    while j <= VB.GetDim() do\n"
            "    begin\n"
            "      VResult.AddElem(VB.GetElem(j));\n"
            "      Inc(j);\n"
            "    end;\n"
            "  end;\n"
            "end;"
        ),
        "prueba_encabezados": ["Paso", "i", "j", "Elemento A [i]", "Elemento B [j]", "VResult acumulado"],
        "prueba_filas": [
            ["1", "1", "1", "2", "10", "[2, 10]"],
            ["2", "2", "2", "0", "20", "[2, 10, 0, 20]"],
            ["3", "3", "3", "2", "30", "[2, 10, 0, 20, 2, 30]"],
            ["4", "4", "4", "1", "40", "[2, 10, 0, 20, 2, 30, 1, 40]"],
            ["5", "5", "5", "3", "50", "[2, 10, 0, 20, 2, 30, 1, 40, 3, 50]"],
            ["Rem. A", "6", "6 (fin)", "8", "-", "[..., 3, 50, 8]"],
            ["Rem. A", "7", "-", "4", "-", "[..., 8, 4]"],
            ["Rem. A", "8", "-", "8", "-", "[..., 4, 8]"],
            ["Rem. A", "9", "-", "6", "-", "[..., 8, 6]"],
            ["Rem. A", "10", "-", "8", "-", "[..., 6, 8]"],
            ["Rem. A", "11", "-", "3", "-", "[..., 8, 3]"],
            ["Rem. A", "12", "-", "3", "-", "[..., 3, 3]"],
            ["Rem. A", "13", "-", "3", "-", "[..., 3, 3]"]
        ],
        "prueba_nota": (
            "Datos de entrada: VA = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3] (dim = 13) y VB = [10, 20, 30, 40, 50] (dim = 5).\n"
            "Dimensión resultante: dimResult = 13 + 5 = 18 elementos.\n"
            "VResult = [2, 10, 0, 20, 2, 30, 1, 40, 3, 50, 8, 4, 8, 6, 8, 3, 3, 3]."
        )
    },
    {
        "num": 5,
        "nombre": "Purgar los Elementos usando Cortes de Control",
        "enunciado": "Eliminar todos los elementos repetidos de un vector de tal forma que permanezca una única ocurrencia de cada valor, aplicando la técnica de cortes de control.",
        "analisis": (
            "La purga o deduplicación de arreglos busca eliminar elementos redundantes preservando un único representante.\n\n"
            "Tradicionalmente, purgar sin corte de control requiere buscar secuencialmente en el arreglo destino para cada elemento, "
            "lo que demanda tiempo cuadrático O(N²).\n"
            "Por el contrario, la técnica de Corte de Control resuelve la purga de manera elegante y eficiente:\n"
            "1. Se ordena el vector (o una copia auxiliar de trabajo) de manera que todas las instancias repetidas de un valor "
            "queden agrupadas contiguamente formando bloques homogéneos.\n"
            "2. Se recorre la estructura agrupada aplicando la lógica de corte:\n"
            "   - Al ingresar a un nuevo corte en la posición i, se toma elem[i] como la 'clave' y se inserta dicha clave una sola vez "
            "en el vector purgado.\n"
            "   - Seguidamente, un ciclo interior avanza el puntero i mientras elem[i] siga siendo igual a la clave, "
            "descartando automáticamente todas las copias repetidas dentro del corte.\n"
            "3. Cuando el ciclo principal culmina, el vector destino contiene únicamente elementos únicos, sin redundancia alguna."
        ),
        "pseudocodigo": (
            "ALGORITMO PurgarCorteControl(SALIDA: Vector VPurgado)\n"
            "    VPurgado.Clear()\n"
            "    SI dim == 0 ENTONCES\n"
            "        RETORNAR\n"
            "    FIN_SI\n"
            "    \n"
            "    // Paso 1: Ordenar copia para garantizar contigüidad de repetidos\n"
            "    Vector vTemp := Clonar(Self)\n"
            "    vTemp.OrdenarAscendente()\n"
            "    \n"
            "    // Paso 2: Filtrado único por corte de control\n"
            "    ENTERO i := 1\n"
            "    MIENTRAS (i <= vTemp.GetDim()) HACER\n"
            "        ENTERO clave := vTemp.GetElem(i)\n"
            "        VPurgado.AddElem(clave)  // Se almacena una sola vez por corte\n"
            "        \n"
            "        // Saltar y omitir todos los duplicados del mismo corte\n"
            "        MIENTRAS (i <= vTemp.GetDim()) Y (vTemp.GetElem(i) == clave) HACER\n"
            "            i := i + 1\n"
            "        FIN_MIENTRAS\n"
            "    FIN_MIENTRAS\n"
            "    \n"
            "    Liberar(vTemp)\n"
            "FIN_ALGORITMO"
        ),
        "pascal": (
            "procedure TVectorPlus.PurgarCorteControl(VPurgado: TVectorPlus);\n"
            "var\n"
            "  vTemp: TVectorPlus;\n"
            "  i, clave: integer;\n"
            "begin\n"
            "  if VPurgado = nil then Exit;\n"
            "  VPurgado.Clear();\n"
            "  if dim = 0 then Exit;\n"
            "\n"
            "  vTemp := Clonar();\n"
            "  vTemp.OrdenarAscendente();\n"
            "\n"
            "  i := 1;\n"
            "  while i <= vTemp.GetDim() do\n"
            "  begin\n"
            "    clave := vTemp.GetElem(i);\n"
            "    VPurgado.AddElem(clave); // Se inserta solo el representante unico\n"
            "\n"
            "    // Se descartan todas las copias repetidas dentro del corte\n"
            "    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do\n"
            "      Inc(i);\n"
            "  end;\n"
            "\n"
            "  vTemp.Free;\n"
            "end;"
        ),
        "prueba_encabezados": ["Corte #", "i inic.", "Clave insertada", "Duplicados omitidos en el corte", "i final", "VPurgado actual"],
        "prueba_filas": [
            ["1", "1", "0", "Ninguno (vTemp[1] = 0)", "2", "[0]"],
            ["2", "2", "1", "Ninguno (vTemp[2] = 1)", "3", "[0, 1]"],
            ["3", "3", "2", "vTemp[4] = 2 (1 duplicado)", "5", "[0, 1, 2]"],
            ["4", "5", "3", "vTemp[6..8] = 3 (3 duplicados)", "9", "[0, 1, 2, 3]"],
            ["5", "9", "4", "Ninguno (vTemp[9] = 4)", "10", "[0, 1, 2, 3, 4]"],
            ["6", "10", "6", "Ninguno (vTemp[10] = 6)", "11", "[0, 1, 2, 3, 4, 6]"],
            ["7", "11", "8", "vTemp[12..13] = 8 (2 duplicados)", "14", "[0, 1, 2, 3, 4, 6, 8]"]
        ],
        "prueba_nota": (
            "Vector original con redundancia: VA = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3] (dim = 13).\n"
            "Vector resultante purgado:       VPurgado = [0, 1, 2, 3, 4, 6, 8] (dim = 7).\n"
            "Se eliminaron exactamente 6 elementos duplicados garantizando unicidad estricta."
        )
    }
]

# ==============================================================================
# GENERACION DE DOCUMENTO WORD (DOCX)
# ==============================================================================

def generar_docx(ruta_salida):
    print(f"Generando documento Word (DOCX): {ruta_salida}...")
    doc = Document()

    # Configuracion de margenes normales (2.54 cm = 1 pulgada)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # --------------------------------------------------------------------------
    # CARATULA FORMAL
    # --------------------------------------------------------------------------
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_uni.add_run(f"{UNIVERSIDAD}\n{FACULTAD}\n{CARRERA}\n")
    r_uni.bold = True
    r_uni.font.name = 'Arial'
    r_uni.font.size = Pt(11)
    r_uni.font.color.rgb = RGBColor(15, 35, 75)

    if os.path.exists("ficct_logo.png"):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.add_run().add_picture("ficct_logo.png", width=Inches(2.2))

    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tit = p_tit.add_run(f"\n{TITULO}\n")
    r_tit.bold = True
    r_tit.font.name = 'Arial'
    r_tit.font.size = Pt(15)
    r_tit.font.color.rgb = RGBColor(180, 20, 20)

    r_sub = p_tit.add_run(f"{SUBTITULO}\n\n")
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = RGBColor(70, 80, 95)

    # Cuadro institucional de identificacion del estudiante
    t_datos = doc.add_table(rows=1, cols=1)
    t_datos.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_datos = t_datos.cell(0, 0)
    c_datos.width = Inches(5.6)
    set_cell_background(c_datos, "F1F5F9")
    set_cell_margins(c_datos, top=140, bottom=140, left=200, right=200)

    p_d = c_datos.paragraphs[0]
    p_d.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_d = p_d.add_run(
        f"ESTUDIANTE: {ESTUDIANTE}\n"
        f"REGISTRO UNIVERSITARIO: {REGISTRO}\n"
        f"MATERIA: {MATERIA} ({SIGLA}) - GRUPO {GRUPO}\n"
        f"DOCENTE: {DOCENTE}\n"
        f"REPOSITORIO GITHUB: {GITHUB_REPO}\n"
        f"{LUGAR_FECHA}"
    )
    r_d.bold = True
    r_d.font.name = 'Arial'
    r_d.font.size = Pt(9.5)
    r_d.font.color.rgb = RGBColor(15, 35, 75)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # SECCION 1: ENUNCIADO OFICIAL Y OBJETIVOS
    # --------------------------------------------------------------------------
    h1 = doc.add_heading("1. Enunciado Oficial y Requerimientos de la Aplicación", level=1)
    h1.runs[0].font.name = 'Arial'
    h1.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_req = doc.add_paragraph()
    r_req = p_req.add_run(
        "Texto Oficial de la Guía de Aplicación U4:\n"
        "«Crear una Clase llamada VectorPlus, que realice las siguientes operaciones, con Interfaz Gráfica.\n"
        "Operaciones:\n"
        "  1. Cantidad de Cortes Control\n"
        "  2. Cantidad de Elementos entre Cortes de Control\n"
        "  3. Dividir un Vector en dos (Par e Impar)\n"
        "  4. Intercalar dos Vectores (Un elemento de A y uno de B)\n"
        "  5. Purgar los Elementos usando Cortes de Control\n"
        "También debe ser subido en su repositorio Personal de GitHub (Obligatorio) indicando la URL\n"
        "(https://github.com/tu_cuenta/inf120_app04).\n"
        "Descarga el archivo que se encuentra a continuación con el nombre: Implementación 4 (Similar a Implementación 2)\n"
        "donde encontrarás ejemplos de las estructuras para elaborar este trabajo.»\n"
    )
    r_req.font.name = 'Arial'
    r_req.font.size = Pt(9.5)

    # Tabla resumen de operaciones requeridas
    t_ops = doc.add_table(rows=1, cols=3)
    t_ops.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_ops.rows[0].cells
    hdr[0].text = "N°"
    hdr[1].text = "Operación Requerida"
    hdr[2].text = "Técnica Algorítmica y Propósito"
    hdr[0].width = Inches(0.6)
    hdr[1].width = Inches(2.6)
    hdr[2].width = Inches(3.3)
    for c in hdr:
        set_cell_background(c, "1E293B")
        for p in c.paragraphs:
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(9)
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p.runs[0].bold = True

    resumen_ops = [
        ("1", "Cantidad de Cortes Control", "Corte de Control Canónico sobre datos agrupados/ordenados"),
        ("2", "Cantidad de Elementos entre Cortes", "Contabilidad de frecuencia y profundidad de bloque por corte"),
        ("3", "Dividir un Vector en dos (Par e Impar)", "Partición y filtrado condicional por paridad aritmética (mod 2)"),
        ("4", "Intercalar dos Vectores (A y B)", "Mezcla alternada (Interleaving) elemento a elemento con remanentes"),
        ("5", "Purgar Elementos usando Cortes de Control", "Deduplicación lineal agrupada omitiendo duplicados intra-corte")
    ]

    for n_op, nom_op, tec_op in resumen_ops:
        row = t_ops.add_row().cells
        row[0].text = n_op
        row[1].text = nom_op
        row[2].text = tec_op
        row[0].width = Inches(0.6)
        row[1].width = Inches(2.6)
        row[2].width = Inches(3.3)
        set_cell_background(row[0], "F8FAFC")
        set_cell_background(row[1], "FFFFFF")
        set_cell_background(row[2], "FFFFFF")
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.name = 'Arial'
                p.runs[0].font.size = Pt(8.5)
                p.runs[0].font.color.rgb = RGBColor(30, 41, 59)

    doc.add_paragraph()

    # Objetivos del Proyecto
    h_obj = doc.add_heading("Objetivos del Proyecto Académico:", level=2)
    h_obj.runs[0].font.name = 'Arial'
    h_obj.runs[0].font.color.rgb = RGBColor(20, 50, 100)

    p_obj = doc.add_paragraph()
    p_obj.add_run("• Objetivo General:\n").bold = True
    p_obj.add_run(
        "Diseñar, implementar y documentar la clase 'VectorPlus' en Object Pascal bajo el entorno Lazarus / Free Pascal, "
        "incorporando las técnicas algorítmicas avanzadas de la Unidad 4 (Cortes de Control, Partición, Intercalación y Purga), "
        "integrada a una interfaz gráfica de usuario (GUI) intuitiva y funcional, respetando estrictamente el alcance de avance de la materia.\n\n"
    )
    p_obj.add_run("• Objetivos Específicos:\n").bold = True
    p_obj.add_run(
        "1. Extender el modelo canónico de Arreglos Unidimensionales (Vector) con métodos especializados para cortes de control.\n"
        "2. Implementar los algoritmos solicitados empleando exclusivamente sentencias de control primitivas (while, for, if) "
        "sin librerías avanzadas ni estructuras dinámicas ajenas al temario.\n"
        "3. Desarrollar una GUI interactiva con TStringGrid, TButton, TEdit y TMemo para visualización y prueba de los vectores.\n"
        "4. Validar cada operación mediante pruebas de escritorio exhaustivas y comprobación experimental.\n"
        "5. Publicar el código fuente en el repositorio personal de GitHub especificado."
    )

    doc.add_paragraph()

    # --------------------------------------------------------------------------
    # SECCION 2: MARCO TEORICO Y METODOLOGICO
    # --------------------------------------------------------------------------
    h2 = doc.add_heading("2. Marco Teórico y Fundamentos Algorítmicos", level=1)
    h2.runs[0].font.name = 'Arial'
    h2.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_m1 = doc.add_paragraph()
    p_m1.add_run("2.1. Programación Orientada a Objetos en Pascal / Lazarus:\n").bold = True
    p_m1.add_run(
        "La Programación Orientada a Objetos (POO) modela entidades computacionales encapsulando estado (atributos) y "
        "comportamiento (métodos). En Object Pascal, la definición de una clase se estructura en la sección 'type' dividiéndose "
        "en ámbitos de visibilidad: 'private' para restringir el acceso directo a los campos internos (respetando el principio "
        "de ocultamiento de información) y 'public' para exponer la interfaz de comunicación con clientes externos. "
        "En nuestra solución, la clase TVectorPlus administra un arreglo estático elem: array[1..MAX_E] of integer y una "
        "dimensión lógica dim: integer, operados únicamente a través de métodos accesores y transformadores.\n\n"
    )

    p_m1.add_run("2.2. Técnica de Cortes de Control (Control Break):\n").bold = True
    p_m1.add_run(
        "El corte de control es un patrón algorítmico jerárquico diseñado para procesar secuencias de datos agrupándolas según "
        "uno o varios criterios. La precondición ineludible es que los datos deben encontrarse previamente ordenados por el "
        "criterio de corte. Esto garantiza que todos los elementos con valores equivalentes conformen un bloque contiguo.\n"
        "La arquitectura del algoritmo emplea dos ciclos 'while' anidados:\n"
        "• El ciclo exterior itera a lo largo de toda la estructura, reconociendo el inicio de un nuevo grupo y memorizando su valor (clave).\n"
        "• El ciclo interior avanza el puntero de lectura mientras el valor examinado coincida con la clave, permitiendo calcular subtotales, "
        "contar frecuencias o ejecutar filtros dentro del bloque.\n"
        "Cuando el ciclo interior detecta un cambio de valor (transición de clave) o el fin del arreglo, se produce el 'corte', "
        "emitiéndose los resultados parciales antes de pasar al siguiente grupo.\n\n"
    )

    p_m1.add_run("2.3. Partición y Filtrado Condicional de Vectores:\n").bold = True
    p_m1.add_run(
        "Consiste en descomponer un vector fuente en dos o más vectores destino en base a una condición lógica o predicado aritmético. "
        "Para la separación en Par e Impar, se utiliza el operador residuo 'mod': un número 'x' es par si (x mod 2 = 0) e impar en "
        "caso contrario. La operación se efectúa en tiempo lineal O(N), garantizando la conservación íntegra de todos los elementos.\n\n"
    )

    p_m1.add_run("2.4. Intercalación (Interleaving / Alternancia):\n").bold = True
    p_m1.add_run(
        "A diferencia de la mezcla ordenada tradicional (MergeSort), la intercalación simple solicitada alterna estrictamente "
        "un elemento de la fuente A y un elemento de la fuente B (A[1], B[1], A[2], B[2], ...). Cuando los vectores poseen longitudes "
        "distintas, la fase simétrica culmina cuando se agota el arreglo más corto, debiendo vaciarse secuencialmente la cola de elementos "
        "sobrantes del arreglo más extenso.\n\n"
    )

    p_m1.add_run("2.5. Purga mediante Cortes de Control:\n").bold = True
    p_m1.add_run(
        "Purgar un arreglo significa eliminar todas las repeticiones redundantes de manera que solo exista un ejemplar de cada valor. "
        "Mientras que el algoritmo ingenuo de purga compara cada elemento contra todos los demás en tiempo O(N²), la aplicación de cortes "
        "de control optimiza el proceso: tras ordenar la colección en O(N log N) o mediante burbuja básica, cada corte de control "
        "agrupa a todos los duplicados de un valor. Basta con seleccionar el primer elemento del corte (la clave) y saltar con el while "
        "interior todos los duplicados idénticos subsiguientes."
    )

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # SECCION 3: DISENO DE LA CLASE TVectorPlus
    # --------------------------------------------------------------------------
    h3 = doc.add_heading("3. Diseño y Estructura de la Clase VectorPlus", level=1)
    h3.runs[0].font.name = 'Arial'
    h3.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_cd = doc.add_paragraph()
    p_cd.add_run(
        "La clase TVectorPlus extiende el comportamiento clásico del arreglo unidimensional definido en la 'Implementación 2' "
        "proporcionada por la cátedra. A continuación se detalla su especificación formal de atributos y métodos:\n"
    )

    # Tabla de atributos privados
    doc.add_heading("Atributos Privados (Encapsulamiento):", level=2)
    t_atr = doc.add_table(rows=1, cols=3)
    t_atr.alignment = WD_TABLE_ALIGNMENT.CENTER
    h_a = t_atr.rows[0].cells
    h_a[0].text = "Identificador"
    h_a[1].text = "Tipo de Dato"
    h_a[2].text = "Descripción y Propósito"
    h_a[0].width = Inches(1.5)
    h_a[1].width = Inches(1.5)
    h_a[2].width = Inches(3.5)
    for c in h_a:
        set_cell_background(c, "1E293B")
        for p in c.paragraphs:
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(9)
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p.runs[0].bold = True

    atributos = [
        ("elem", "array[1..MAX_E] of integer", "Arreglo estático de memoria continua con capacidad para 1000 enteros."),
        ("dim", "integer", "Dimensión lógica actual (número de elementos efectivamente ocupados en el rango 0..MAX_E).")
    ]
    for n_a, t_a, d_a in atributos:
        row = t_atr.add_row().cells
        row[0].text = n_a
        row[1].text = t_a
        row[2].text = d_a
        row[0].width = Inches(1.5)
        row[1].width = Inches(1.5)
        row[2].width = Inches(3.5)
        set_cell_background(row[0], "F8FAFC")
        set_cell_background(row[1], "FFFFFF")
        set_cell_background(row[2], "FFFFFF")
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.name = 'Arial'
                p.runs[0].font.size = Pt(8.5)

    doc.add_paragraph()

    # Tabla de métodos públicos
    doc.add_heading("Métodos Públicos (Interfaz de la Clase):", level=2)
    t_met = doc.add_table(rows=1, cols=3)
    t_met.alignment = WD_TABLE_ALIGNMENT.CENTER
    h_m = t_met.rows[0].cells
    h_m[0].text = "Firma del Método"
    h_m[1].text = "Categoría"
    h_m[2].text = "Descripción Funcional"
    h_m[0].width = Inches(2.8)
    h_m[1].width = Inches(1.4)
    h_m[2].width = Inches(2.3)
    for c in h_m:
        set_cell_background(c, "1E293B")
        for p in c.paragraphs:
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(9)
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p.runs[0].bold = True

    metodos = [
        ("constructor Create()", "Constructor", "Inicializa la dimensión en 0 y limpia el almacenamiento."),
        ("procedure SetDim(n: integer)", "Acceso", "Asigna la dimensión lógica validando rango [0..MAX_E]."),
        ("function GetDim(): integer", "Acceso", "Retorna la cantidad actual de elementos en el vector."),
        ("procedure SetElem(pos, ele: integer)", "Mutador", "Modifica el valor en la posición indicada [1..dim]."),
        ("function GetElem(pos: integer): integer", "Acceso", "Retorna el valor alojado en la posición [1..dim]."),
        ("procedure AddElem(ele: integer)", "Primitiva", "Inserta un nuevo elemento al final del vector e incrementa dim."),
        ("procedure InsElem(pos, ele: integer)", "Primitiva", "Inserta desplazando elementos hacia la derecha desde pos."),
        ("procedure RemElem(pos: integer)", "Primitiva", "Elimina desplazando elementos hacia la izquierda desde pos."),
        ("procedure Clear()", "Primitiva", "Pone en cero todas las posiciones y reinicia dim a 0."),
        ("procedure OrdenarAscendente()", "Algoritmo", "Ordena los elementos por método burbuja simple."),
        ("procedure CopiarDesde(origen: TVectorPlus)", "Utilidad", "Copia íntegramente los datos de otro objeto TVectorPlus."),
        ("function Clonar(): TVectorPlus", "Utilidad", "Instancia un nuevo objeto duplicado idéntico."),
        ("function CargarDesdeTexto(S: string): integer", "GUI / Parser", "Carga elementos desde texto separado por comas o espacios."),
        ("function ATexto(): string", "GUI / Formato", "Genera representación en cadena con formato '[e1, e2, ...]''."),
        ("function CantidadCortesControl(): integer", "Operación 1", "Determina la cantidad de cortes de control del vector."),
        ("procedure CantidadElementosEntreCortes(...)", "Operación 2", "Calcula la cantidad de elementos agrupados en cada corte."),
        ("procedure DividirParImpar(VPar, VImpar)", "Operación 3", "Segrega los elementos en vectores pares e impares."),
        ("procedure Intercalar(VB, VResult)", "Operación 4", "Combina alternadamente un elemento de A y uno de B."),
        ("procedure PurgarCorteControl(VPurgado)", "Operación 5", "Elimina duplicados aplicando la técnica de cortes de control.")
    ]

    for f_m, c_m, d_m in metodos:
        row = t_met.add_row().cells
        row[0].text = f_m
        row[1].text = c_m
        row[2].text = d_m
        row[0].width = Inches(2.8)
        row[1].width = Inches(1.4)
        row[2].width = Inches(2.3)
        set_cell_background(row[0], "F8FAFC")
        set_cell_background(row[1], "FFFFFF")
        set_cell_background(row[2], "FFFFFF")
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.name = 'Arial'
                p.runs[0].font.size = Pt(8)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # SECCION 4: DESARROLLO DETALLADO DE LAS 5 OPERACIONES
    # --------------------------------------------------------------------------
    h4 = doc.add_heading("4. Desarrollo Algorítmico Detallado de las 5 Operaciones", level=1)
    h4.runs[0].font.name = 'Arial'
    h4.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    for op in OPERACIONES_DATA:
        h_op = doc.add_heading(f"4.{op['num']}. Operación {op['num']}: {op['nombre']}", level=2)
        h_op.runs[0].font.name = 'Arial'
        h_op.runs[0].font.color.rgb = RGBColor(20, 50, 100)

        # Enunciado y Proposito
        p_en = doc.add_paragraph()
        p_en.add_run("• Enunciado Oficial:\n").bold = True
        p_en.add_run(f"{op['enunciado']}\n\n")

        # Analisis
        p_en.add_run("• Análisis y Estrategia de Solución:\n").bold = True
        p_en.add_run(f"{op['analisis']}\n")

        # Pseudocodigo
        doc.add_heading("Pseudocódigo Estructurado:", level=3)
        add_code_block(doc, op["pseudocodigo"])

        # Codigo Pascal
        doc.add_heading("Implementación en Pascal (Lazarus / Free Pascal):", level=3)
        add_code_block(doc, op["pascal"])

        # Prueba de Escritorio
        doc.add_heading("Prueba de Escritorio Exhaustiva:", level=3)
        p_not = doc.add_paragraph()
        p_not.add_run(f"{op['prueba_nota']}\n")
        p_not.runs[0].font.size = Pt(8.5)
        p_not.runs[0].font.color.rgb = RGBColor(70, 80, 95)

        # Tabla de prueba de escritorio
        cols_count = len(op["prueba_encabezados"])
        t_pru = doc.add_table(rows=1, cols=cols_count)
        t_pru.alignment = WD_TABLE_ALIGNMENT.CENTER
        h_p = t_pru.rows[0].cells
        for idx, enc in enumerate(op["prueba_encabezados"]):
            h_p[idx].text = enc
            set_cell_background(h_p[idx], "334155")
            for p in h_p[idx].paragraphs:
                p.runs[0].font.name = 'Arial'
                p.runs[0].font.size = Pt(8)
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
                p.runs[0].bold = True

        for fila in op["prueba_filas"]:
            row = t_pru.add_row().cells
            for idx, val in enumerate(fila):
                row[idx].text = val
                set_cell_background(row[idx], "F8FAFC" if idx == 0 else "FFFFFF")
                for p in row[idx].paragraphs:
                    p.runs[0].font.name = 'Arial'
                    p.runs[0].font.size = Pt(7.8)
                    p.runs[0].font.color.rgb = RGBColor(30, 41, 59)

        doc.add_paragraph()

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # SECCION 5: DISENO DE LA INTERFAZ GRAFICA (GUI) EN LAZARUS
    # --------------------------------------------------------------------------
    h5 = doc.add_heading("5. Diseño e Implementación de la Interfaz Gráfica (GUI)", level=1)
    h5.runs[0].font.name = 'Arial'
    h5.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_gui = doc.add_paragraph()
    p_gui.add_run(
        "Para dar cabal cumplimiento al requerimiento de la práctica («Con Interface Gráfica») y basándonos en la estructura "
        "propuesta en el archivo 'Implementación 2' (donde se visualizaba el vector en componentes de grilla y botones de eventos), "
        "se diseñó un formulario ergonómico y completo en Lazarus llamado TFormMain (alojado en main.pas y main.lfm).\n\n"
    )

    p_gui.add_run("5.1. Componentes Visuales del Formulario:\n").bold = True
    p_gui.add_run(
        "• Panel de Vector A (Principal):\n"
        "  - StringGridA: TStringGrid configurado para desplegar los elementos en dos filas (Fila 0 = Índices 1..dim, Fila 1 = Valores numéricos).\n"
        "  - EditElemA, EditPosA: Cajas de texto para entrada puntual de elementos y posiciones.\n"
        "  - Botones Adicionar, Insertar, Remover y Limpiar A.\n"
        "  - EditTextoA y Botón Cargar: Permite ingresar vectores completos mediante texto separado por comas (ej. el vector oficial de la lección).\n\n"
        "• Panel de Vector B (Secundario para Intercalación):\n"
        "  - StringGridB: TStringGrid con índices y valores para el segundo arreglo.\n"
        "  - Controles de edición y botones para carga manual o en bloque.\n\n"
        "• Panel de Operaciones del Práctico U4:\n"
        "  - Botón '1. Cantidad Cortes Control': Dispara el cálculo y muestra el resultado en la caja EditCortesA.\n"
        "  - Botón '2. Cantidad Elementos entre Cortes': Genera el desglose corte por corte y lo emite en el registro TMemo.\n"
        "  - Botón '3. Dividir un Vector en dos (Par e Impar)': Clasifica Vector A y actualiza StringGridPar y StringGridImpar.\n"
        "  - Botón '4. Intercalar dos Vectores (A y B)': Ejecuta la alternancia simétrica y muestra el resultado en StringGridResultado.\n"
        "  - Botón '5. Purgar Elementos usando Cortes de Control': Aplica deduplicación y actualiza StringGridResultado.\n"
        "  - Botón 'Ejecutar Demostración Completa': Ejecuta en secuencia automatizada las 5 operaciones sobre los vectores activos.\n"
        "  - Botón 'Limpiar Todo': Reinicia los vectores y componentes a su estado inicial.\n\n"
        "• Panel de Resultados:\n"
        "  - StringGridResultado: Visualiza el arreglo producido por Intercalación y Purga.\n"
        "  - StringGridPar / StringGridImpar: Visualizan los arreglos resultantes de la división.\n"
        "  - MemoReporte: TMemo con barra de desplazamiento para bitácora de auditoría y desgloses tabulares de cortes.\n"
    )

    # Código del formulario main.pas
    doc.add_heading("Código Fuente del Manejador de la GUI (main.pas):", level=2)
    if os.path.exists("main.pas"):
        with open("main.pas", "r", encoding="utf-8") as f_main:
            codigo_main = f_main.read()
        add_code_block(doc, codigo_main)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # SECCION 6: VERIFICACION EXPERIMENTAL Y PRUEBAS EN CONSOLA
    # --------------------------------------------------------------------------
    h6 = doc.add_heading("6. Verificación Experimental y Salida del Sistema", level=1)
    h6.runs[0].font.name = 'Arial'
    h6.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_exp = doc.add_paragraph()
    p_exp.add_run(
        "Para validar rigurosamente la corrección lógica y matemática de las 5 operaciones antes de su integración visual, "
        "se implementó una batería de pruebas automatizadas compilada en modo consola bajo Free Pascal (TestVectorPlus.pas). "
        "A continuación se presenta la salida real obtenida tras la compilación y ejecución directa en el entorno de desarrollo:\n"
    )

    salida_consola = (
        "================================================================\n"
        "     PRUEBAS UNITARIAS Y DEMOSTRACION - CLASE TVectorPlus       \n"
        "     Materia: Programacion I (INF120) - Evans Balcazar          \n"
        "     Estudiante: Gustavo Melgar Baldivieso - Reg: 213195623     \n"
        "================================================================\n\n"
        "1. VECTOR A ORIGINAL (Dim = 13):\n"
        "   [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]\n\n"
        "----------------------------------------------------------------\n"
        "OPERACION 1: Cantidad de Cortes de Control\n"
        "----------------------------------------------------------------\n"
        "Cantidad de cortes en Vector A: 7\n"
        "(Explicacion: Ordenado queda [0, 1, 2, 2, 3, 3, 3, 3, 4, 6, 8, 8, 8],\n"
        " correspondiendo a los 7 cortes con claves: 0, 1, 2, 3, 4, 6, 8)\n\n"
        "----------------------------------------------------------------\n"
        "OPERACION 2: Cantidad de Elementos entre Cortes de Control\n"
        "----------------------------------------------------------------\n"
        "CORTES DE CONTROL Y CANTIDAD DE ELEMENTOS:\n"
        "Total de cortes detectados: 7\n"
        "-----------------------------------------\n"
        "Corte #1: Clave = 0  -->  Cantidad de elementos: 1\n"
        "Corte #2: Clave = 1  -->  Cantidad de elementos: 1\n"
        "Corte #3: Clave = 2  -->  Cantidad de elementos: 2\n"
        "Corte #4: Clave = 3  -->  Cantidad de elementos: 4\n"
        "Corte #5: Clave = 4  -->  Cantidad de elementos: 1\n"
        "Corte #6: Clave = 6  -->  Cantidad de elementos: 1\n"
        "Corte #7: Clave = 8  -->  Cantidad de elementos: 3\n\n"
        "----------------------------------------------------------------\n"
        "OPERACION 3: Dividir un Vector en dos (Par e Impar)\n"
        "----------------------------------------------------------------\n"
        "Vector Pares   (Dim = 8): [2, 0, 2, 8, 4, 8, 6, 8]\n"
        "Vector Impares (Dim = 5): [1, 3, 3, 3, 3]\n\n"
        "----------------------------------------------------------------\n"
        "OPERACION 4: Intercalar dos Vectores (Un elemento de A y uno de B)\n"
        "----------------------------------------------------------------\n"
        "Vector A: [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]\n"
        "Vector B: [10, 20, 30, 40, 50]\n"
        "Vector Intercalado (A y B): (Dim = 18)\n"
        "   [2, 10, 0, 20, 2, 30, 1, 40, 3, 50, 8, 4, 8, 6, 8, 3, 3, 3]\n\n"
        "----------------------------------------------------------------\n"
        "OPERACION 5: Purgar los Elementos usando Cortes de Control\n"
        "----------------------------------------------------------------\n"
        "Vector A con duplicados: [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]\n"
        "Vector Purgado (sin duplicados, por corte): [0, 1, 2, 3, 4, 6, 8]\n"
        "Dimension original: 13 -> Dimension purgada: 7\n\n"
        "================================================================\n"
        "     FIN DE LAS PRUEBAS - TODAS LAS OPERACIONES EXITOSAS        \n"
        "================================================================"
    )
    add_code_block(doc, salida_consola)

    # --------------------------------------------------------------------------
    # SECCION 7: GUIA DE COMPILACION Y EJECUCION EN LAZARUS
    # --------------------------------------------------------------------------
    h7 = doc.add_heading("7. Guía de Compilación y Ejecución del Proyecto", level=1)
    h7.runs[0].font.name = 'Arial'
    h7.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_comp = doc.add_paragraph()
    p_comp.add_run("7.1. Apertura y Compilación desde el Entorno Oficial Lazarus IDE:\n").bold = True
    p_comp.add_run(
        "1. Iniciar Lazarus IDE en su estación de trabajo.\n"
        "2. Ir al menú superior: 'Proyecto' -> 'Abrir Proyecto...'.\n"
        "3. Navegar hasta la carpeta del proyecto y seleccionar el archivo 'VectorPlusApp.lpi'.\n"
        "4. En el Inspector de Proyectos se cargarán las unidades 'uVectorPlus.pas', 'main.pas' y el formulario 'main.lfm'.\n"
        "5. Presionar la tecla 'F9' (o hacer clic en el botón verde 'Ejecutar' en la barra de herramientas).\n"
        "6. Lazarus compilará y vinculará automáticamente el ejecutable gráfico interactivo.\n\n"
    )

    p_comp.add_run("7.2. Compilación desde Terminal mediante lazbuild:\n").bold = True
    p_comp.add_run(
        "Para compilar el proyecto de forma desatendida mediante línea de comandos (PowerShell o CMD):\n"
    )
    add_code_block(doc, 'lazbuild.exe ".\\VectorPlusApp.lpi"\n.\\VectorPlusApp.exe')

    p_comp.add_run("7.3. Compilación de la Batería de Pruebas en Consola:\n").bold = True
    add_code_block(doc, 'fpc -MObjFPC -Scghi -O1 TestVectorPlus.pas\n.\\TestVectorPlus.exe')

    # --------------------------------------------------------------------------
    # SECCION 8: CONTROL DE VERSIONES Y REPOSITORIO GITHUB
    # --------------------------------------------------------------------------
    h8 = doc.add_heading("8. Control de Versiones y Repositorio Oficial en GitHub", level=1)
    h8.runs[0].font.name = 'Arial'
    h8.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_git = doc.add_paragraph()
    p_git.add_run(
        "En estricto cumplimiento de la instrucción obligatoria del práctico:\n"
        "«Tambien debe ser subido en su repositorio Personal de GitHub (Obligatorio) indica la URL(https://github.com/tu_cuenta/inf120_app04)»\n\n"
        f"Se ha formalizado el repositorio personal en GitHub bajo el enlace oficial:\n"
        f"URL: {GITHUB_REPO}\n\n"
        "Estructura organizada del repositorio:\n"
        "• uVectorPlus.pas: Implementación completa de la clase TVectorPlus y las 5 operaciones requeridas.\n"
        "• main.pas / main.lfm: Formulario visual interactivo en Lazarus con TStringGrid y TMemo.\n"
        "• VectorPlusApp.lpr / VectorPlusApp.lpi: Archivos maestros de proyecto Lazarus.\n"
        "• TestVectorPlus.pas: Batería de pruebas unitarias y verificación en consola.\n"
        "• Aplicación U4 - Informe.docx: Documento Word formal con la defensa teórica y pruebas de escritorio.\n"
        "• README.md: Documentación de bienvenida e instrucciones de clonación y uso.\n\n"
        "Comandos Git para inicialización y publicación del repositorio:\n"
    )
    comandos_git = (
        "git init\n"
        "git add .\n"
        'git commit -m "Implementacion Aplicacion U4: Clase VectorPlus con GUI en Lazarus"\n'
        "git branch -M main\n"
        f"git remote add origin {GITHUB_REPO}.git\n"
        "git push -u origin main"
    )
    add_code_block(doc, comandos_git)

    # --------------------------------------------------------------------------
    # SECCION 9: CONCLUSIONES Y RECOMENDACIONES
    # --------------------------------------------------------------------------
    h9 = doc.add_heading("9. Conclusiones y Recomendaciones", level=1)
    h9.runs[0].font.name = 'Arial'
    h9.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_conc = doc.add_paragraph()
    p_conc.add_run("Conclusiones:\n").bold = True
    p_conc.add_run(
        "1. Se implementó exitosamente la clase 'VectorPlus' en Object Pascal / Lazarus, cumpliendo con todas las operaciones "
        "requeridas: conteo de cortes de control, cálculo de frecuencias intra-corte, partición par/impar, intercalación alternada "
        "y purga eficiente de repetidos.\n"
        "2. Se demostró la importancia pedagógica de la precondición de ordenamiento en los algoritmos de corte de control: "
        "al agrupar los datos contiguamente, operaciones complejas como la deduplicación (purga) se reducen a un recorrido lineal simple.\n"
        "3. La solución se diseñó respetando estrictamente el alcance de la materia Programación I (INF120), empleando arreglos "
        "estáticos, bucles 'while' y 'for' canónicos y evitando librerías o funciones complejas ajenas al temario.\n"
        "4. La interfaz gráfica (GUI) desarrollada en Lazarus ofrece una herramienta interactiva, visual y pedagógica que facilita "
        "la comprensión de las transformaciones sufridas por los arreglos mediante rejillas sincronizadas.\n\n"
    )
    p_conc.add_run("Recomendaciones:\n").bold = True
    p_conc.add_run(
        "1. Para conjuntos masivos de datos, se recomienda optimizar la etapa previa de ordenamiento sustituyendo el método "
        "de burbuja por algoritmos de mayor rendimiento como QuickSort o MergeSort recursivo.\n"
        "2. Es fundamental validar siempre las entradas numéricas en la interfaz para prevenir desbordamientos o excepciones "
        "por formatos no numéricos.\n"
        "3. Mantener modularizada la capa de lógica algorítmica (uVectorPlus.pas) totalmente desacoplada de la capa visual (main.pas) "
        "para permitir su reutilización en otros entornos como consolas o aplicaciones móviles."
    )

    doc.add_paragraph()

    # --------------------------------------------------------------------------
    # SECCION 10: BIBLIOGRAFIA FORMAL
    # --------------------------------------------------------------------------
    h10 = doc.add_heading("10. Bibliografía Formal", level=1)
    h10.runs[0].font.name = 'Arial'
    h10.runs[0].font.color.rgb = RGBColor(15, 45, 95)

    p_bib = doc.add_paragraph()
    p_bib.add_run(
        "1. Balcazar Veizaga, Evans. «Lección 4: Técnicas Algorítmicas en 1, 2 o más objetos». Universidad Autónoma Gabriel René Moreno (UAGRM), FICCT, 2026.\n"
        "2. Balcazar Veizaga, Evans. «Implementación 2: Clase Vector y Estructuras de Formularios». UAGRM, INF120, 2017-2026.\n"
        "3. Joyanes Aguilar, Luis. «Fundamentos de Programación: Algoritmos, Estructuras de Datos y Objetos». 4ta Edición, McGraw-Hill Interamericana, 2008.\n"
        "4. Cairó Battistutti, Osvaldo. «Metodología de la Programación: Algoritmos, Diagramas de Flujo y Pseudocódigo». 3ra Edición, Alfaomega, 2005.\n"
        "5. Free Pascal Team. «Free Pascal Reference Guide & Lazarus Component Library (LCL) Documentation». Versión 3.2.2 / Lazarus 2.2, 2025.\n"
        "6. Wirth, Niklaus. «Algorithms + Data Structures = Programs». Prentice-Hall Series in Automatic Computation, 1976."
    )
    p_bib.runs[0].font.size = Pt(9)

    doc.save(ruta_salida)
    print(f"Documento DOCX generado exitosamente: {ruta_salida}")

# ==============================================================================
# GENERACION DE DOCUMENTO PDF
# ==============================================================================

class PDFReport(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(100, 110, 120)
            self.cell(0, 6, f'UAGRM - FICCT | INF120 Programacion I | {TITULO}', 0, 0, 'L')
            self.cell(0, 6, f'Pagina {self.page_no()}', 0, 1, 'R')
            self.set_draw_color(200, 210, 220)
            self.line(10, 15, 200, 15)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f'{ESTUDIANTE} (Reg: {REGISTRO}) - Repositorio: {GITHUB_REPO}', 0, 0, 'C')

def generar_pdf(ruta_salida):
    print(f"Generando documento PDF: {ruta_salida}...")
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Caratula
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(15, 35, 75)
    pdf.cell(0, 6, UNIVERSIDAD, 0, 1, 'C')
    pdf.cell(0, 6, FACULTAD, 0, 1, 'C')
    pdf.cell(0, 6, CARRERA, 0, 1, 'C')
    pdf.ln(4)

    if os.path.exists("ficct_logo.png"):
        pdf.image("ficct_logo.png", x=85, y=34, w=40)
        pdf.ln(42)
    else:
        pdf.ln(10)

    pdf.set_font('Helvetica', 'B', 15)
    pdf.set_text_color(180, 20, 20)
    pdf.multi_cell(0, 7, TITULO, 0, 'C')
    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(70, 80, 95)
    pdf.multi_cell(0, 5, SUBTITULO, 0, 'C')
    pdf.ln(6)

    # Cuadro datos
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(25, pdf.get_y(), 160, 40, 'FD')
    pdf.set_xy(25, pdf.get_y() + 3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(15, 35, 75)
    pdf.cell(160, 5, f'ESTUDIANTE: {ESTUDIANTE}', 0, 1, 'C')
    pdf.cell(160, 5, f'REGISTRO UNIVERSITARIO: {REGISTRO}', 0, 1, 'C')
    pdf.cell(160, 5, f'MATERIA: {MATERIA} ({SIGLA}) - GRUPO {GRUPO}', 0, 1, 'C')
    pdf.cell(160, 5, f'DOCENTE: {DOCENTE}', 0, 1, 'C')
    pdf.cell(160, 5, f'REPOSITORIO: {GITHUB_REPO}', 0, 1, 'C')
    pdf.cell(160, 5, f'{LUGAR_FECHA}', 0, 1, 'C')

    pdf.add_page()

    # Contenido resumido del PDF
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(15, 45, 95)
    pdf.cell(0, 8, '1. Enunciado Oficial y Resumen de Operaciones', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 5, 
        "Desarrollo de la clase 'VectorPlus' con interfaz grafica (GUI) en Lazarus incorporando las 5 tecnicas:\n"
        "1. Cantidad de Cortes Control: Identificacion y conteo de transiciones de clave sobre datos agrupados.\n"
        "2. Cantidad de Elementos entre Cortes de Control: Conteo de la profundidad y frecuencia por bloque de corte.\n"
        "3. Dividir un Vector en dos (Par e Impar): Clasificacion condicional basada en el residuo aritmetico (mod 2).\n"
        "4. Intercalar dos Vectores (A y B): Alternancia simetrica elemento a elemento con descarga de colas remanentes.\n"
        "5. Purgar Elementos usando Cortes de Control: Deduplicacion en tiempo lineal omitiendo duplicados contiguos.\n"
    )
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(15, 45, 95)
    pdf.cell(0, 8, '2. Verificacion Experimental y Salida del Sistema', 0, 1, 'L')
    pdf.set_font('Courier', '', 8)
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(226, 232, 240)
    
    salida_corta = (
        "VECTOR A ORIGINAL: [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3] (Dim = 13)\n"
        "OP 1 -> Cantidad de cortes de control: 7 cortes (Claves: 0, 1, 2, 3, 4, 6, 8)\n"
        "OP 2 -> Elementos por corte: 0->1, 1->1, 2->2, 3->4, 4->1, 6->1, 8->3\n"
        "OP 3 -> Pares [2, 0, 2, 8, 4, 8, 6, 8] (Dim=8) | Impares [1, 3, 3, 3, 3] (Dim=5)\n"
        "OP 4 -> Intercalado con B=[10, 20, 30, 40, 50]:\n"
        "        [2, 10, 0, 20, 2, 30, 1, 40, 3, 50, 8, 4, 8, 6, 8, 3, 3, 3] (Dim=18)\n"
        "OP 5 -> Vector Purgado con Cortes: [0, 1, 2, 3, 4, 6, 8] (Dim=7 sin duplicados)\n"
    )
    pdf.multi_cell(0, 4.5, salida_corta, 1, 'L', fill=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(15, 45, 95)
    pdf.cell(0, 8, '3. Conclusiones y Repositorio Oficial', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 5,
        f"El proyecto ha sido completado y verificado en su totalidad. Cumple estrictamente con el avance de la materia "
        f"Programacion I sin recurrir a funciones o complejidades no avanzadas.\n\n"
        f"Repositorio oficial de entrega: {GITHUB_REPO}\n"
        f"El informe completo in extenso con todas las pruebas de escritorio y codigo fuente se encuentra disponible en 'Aplicacion U4 - Informe.docx'."
    )

    pdf.output(ruta_salida)
    print(f"Documento PDF generado exitosamente: {ruta_salida}")

# ==============================================================================
# EJECUCION PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    ruta_docx = "Aplicación U4 - Informe.docx"
    ruta_pdf  = "Aplicación U4 - Informe.pdf"

    generar_docx(ruta_docx)
    generar_pdf(ruta_pdf)
    print("\nProceso de generacion de informes completado exitosamente.")
