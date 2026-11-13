# Aplicación U4: Otras Técnicas Algorítmicas en 1, 2 o más Objetos
**Clase `VectorPlus` con Interfaz Gráfica (GUI) en Lazarus / Free Pascal**

* **Universidad:** Universidad Autónoma Gabriel René Moreno (UAGRM)
* **Facultad:** Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones (FICCT)
* **Materia:** Programación I (INF120) - Grupo SC
* **Docente:** Lic. Evans Balcazar Veizaga
* **Estudiante:** Gustavo Melgar Baldivieso
* **Registro:** 213195623
* **Repositorio GitHub:** [https://github.com/gumebdoc/inf120_app04](https://github.com/gumebdoc/inf120_app04)
* **Fecha:** Noviembre 2026 - Santa Cruz de la Sierra, Bolivia

---

## 📌 1. Descripción del Proyecto

Este proyecto implementa la **Aplicación U4** de la materia Programación I. Siguiendo las directrices del docente y la estructura de la *Implementación 2*, se construyó la clase **`VectorPlus`** (`TVectorPlus`) en **Object Pascal**, acompañada de una completa **Interfaz Gráfica de Usuario (GUI)** en **Lazarus IDE**.

El proyecto se diseñó estrictamente bajo el avance conceptual de la materia:
* Programación Orientada a Objetos estándar (clase, atributos privados, métodos públicos).
* Arreglos estáticos continuos (`array[1..MAX_E] of integer`) con índice base 1.
* Estructuras de control canónicas (`while`, `for`, `if`).
* **Sin funciones avanzadas, sin genéricos, sin punteros complejos ni librerías no cubiertas en el avance.**

---

## 🚀 2. Las 5 Operaciones Implementadas

| N° | Operación | Técnica Algorítmica | Propósito |
|---|---|---|---|
| **1** | **Cantidad de Cortes Control** | Corte de Control canónico | Cuenta los cambios de clave/bloques homogéneos en el vector. |
| **2** | **Cantidad de Elementos entre Cortes de Control** | Frecuencia / Tamaño de bloque | Contabiliza cuántos elementos componen cada corte de control. |
| **3** | **Dividir un Vector en dos (Par e Impar)** | Partición condicional (`mod 2`) | Segrega los números en dos nuevos vectores (Pares e Impares). |
| **4** | **Intercalar dos Vectores (Un elemento de A y uno de B)** | Mezcla alternada (Interleaving) | Alterna un valor de A y uno de B paso a paso con colas remanentes. |
| **5** | **Purgar Elementos usando Cortes de Control** | Deduplicación lineal intra-corte | Elimina todos los duplicados preservando un único representante. |

---

## 📂 3. Estructura del Repositorio

```text
├── uVectorPlus.pas                # Unidad de la clase TVectorPlus con las 5 operaciones
├── main.pas                       # Controlador de eventos de la Interfaz Gráfica (GUI)
├── main.lfm                       # Definición visual del formulario en Lazarus
├── VectorPlusApp.lpr              # Programa principal de Lazarus (GUI)
├── VectorPlusApp.lpi              # Archivo de proyecto de Lazarus
├── VectorPlusApp.res              # Recurso de iconos y manifiesto de Windows
├── TestVectorPlus.pas             # Programa de pruebas unitarias y consola
├── Aplicación U4 - Informe.docx   # INFORME COMPLETO EN WORD (Carátula, marco teórico, pseudocódigos, pruebas de escritorio)
├── Aplicación U4 - Informe.pdf    # Versión PDF del informe formal
├── build_informe_u4_app.py        # Script Python automatizado para compilar los informes
├── ficct_logo.png                 # Logotipo oficial de la FICCT - UAGRM
└── README.md                      # Documentación del proyecto
```

---

## 🛠️ 4. Instrucciones de Compilación y Ejecución

### Opción A: Desde Lazarus IDE (Interfaz Gráfica)
1. Abrir **Lazarus**.
2. Menú **Proyecto** -> **Abrir Proyecto...** y seleccionar `VectorPlusApp.lpi`.
3. Presionar **F9** (o botón verde *Ejecutar*).
4. La ventana interactiva se desplegará mostrando las tablas de vectores (Vector A, Vector B, Resultado, Par, Impar) y los botones de operaciones.

### Opción B: Desde Terminal mediante `lazbuild` (GUI)
```powershell
lazbuild.exe ".\VectorPlusApp.lpi"
.\VectorPlusApp.exe
```

### Opción C: Batería de Pruebas en Consola (`TestVectorPlus.pas`)
```powershell
fpc -MObjFPC -Scghi -O1 TestVectorPlus.pas
.\TestVectorPlus.exe
```

---

## 📊 5. Resultados de la Verificación Experimental

Ejemplo con el vector oficial de la lección:
`VA = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]` (dim = 13)

* **Operación 1 (Cantidad de Cortes):** 7 cortes (Claves: `0, 1, 2, 3, 4, 6, 8`).
* **Operación 2 (Elementos por Corte):**
  * Corte 1 [Clave 0] -> 1 elemento
  * Corte 2 [Clave 1] -> 1 elemento
  * Corte 3 [Clave 2] -> 2 elementos
  * Corte 4 [Clave 3] -> 4 elementos
  * Corte 5 [Clave 4] -> 1 elemento
  * Corte 6 [Clave 6] -> 1 elemento
  * Corte 7 [Clave 8] -> 3 elementos
  * *Total: 13 elementos.*
* **Operación 3 (División Par e Impar):**
  * Pares: `[2, 0, 2, 8, 4, 8, 6, 8]` (dim = 8)
  * Impares: `[1, 3, 3, 3, 3]` (dim = 5)
* **Operación 4 (Intercalación con `VB = [10, 20, 30, 40, 50]`):**
  * Resultado: `[2, 10, 0, 20, 2, 30, 1, 40, 3, 50, 8, 4, 8, 6, 8, 3, 3, 3]` (dim = 18)
* **Operación 5 (Purga usando Cortes de Control):**
  * Resultado: `[0, 1, 2, 3, 4, 6, 8]` (dim = 7 únicos, 6 duplicados eliminados)

---

## 👨‍💻 Autor
* **Estudiante:** Gustavo Melgar Baldivieso
* **Registro:** 213195623
* **Carrera:** Ingeniería en Sistemas / Informática
* **Universidad Autónoma Gabriel René Moreno (UAGRM)**
