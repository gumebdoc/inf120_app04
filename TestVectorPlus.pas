program TestVectorPlus;

{$mode ObjFPC}{$H+}

uses
  SysUtils, uVectorPlus;

var
  VA, VB, VPar, VImpar, VInter, VPurgado, VVal, VCant: TVectorPlus;
  i: integer;

begin
  Writeln('================================================================');
  Writeln('     PRUEBAS UNITARIAS Y DEMOSTRACION - CLASE TVectorPlus       ');
  Writeln('     Materia: Programacion I (INF120) - Evans Balcazar          ');
  Writeln('     Estudiante: Gustavo Melgar Baldivieso - Reg: 213195623     ');
  Writeln('================================================================');
  Writeln;

  VA := TVectorPlus.Create;
  VB := TVectorPlus.Create;
  VPar := TVectorPlus.Create;
  VImpar := TVectorPlus.Create;
  VInter := TVectorPlus.Create;
  VPurgado := TVectorPlus.Create;
  VVal := TVectorPlus.Create;
  VCant := TVectorPlus.Create;

  // Cargar Vector A con el ejemplo canonico de la leccion:
  // V = [2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3]
  VA.CargarDesdeTexto('2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3');
  Writeln('1. VECTOR A ORIGINAL (Dim = ', VA.GetDim(), '):');
  Writeln('   ', VA.ATexto());
  Writeln;

  // OPERACION 1: Cantidad de Cortes Control
  Writeln('----------------------------------------------------------------');
  Writeln('OPERACION 1: Cantidad de Cortes de Control');
  Writeln('----------------------------------------------------------------');
  Writeln('Cantidad de cortes en Vector A: ', VA.CantidadCortesControl());
  Writeln('(Explicacion: Ordenado queda [0, 1, 2, 2, 3, 3, 3, 3, 4, 6, 8, 8, 8],');
  Writeln(' correspondiendo a los 7 cortes con claves: 0, 1, 2, 3, 4, 6, 8)');
  Writeln;

  // OPERACION 2: Cantidad de Elementos entre Cortes de Control
  Writeln('----------------------------------------------------------------');
  Writeln('OPERACION 2: Cantidad de Elementos entre Cortes de Control');
  Writeln('----------------------------------------------------------------');
  VA.CantidadElementosEntreCortes(VVal, VCant);
  Writeln(VA.ResumenElementosEntreCortes());
  Writeln;

  // OPERACION 3: Dividir un Vector en dos (Par e Impar)
  Writeln('----------------------------------------------------------------');
  Writeln('OPERACION 3: Dividir un Vector en dos (Par e Impar)');
  Writeln('----------------------------------------------------------------');
  VA.DividirParImpar(VPar, VImpar);
  Writeln('Vector Pares   (Dim = ', VPar.GetDim(), '): ', VPar.ATexto());
  Writeln('Vector Impares (Dim = ', VImpar.GetDim(), '): ', VImpar.ATexto());
  Writeln;

  // OPERACION 4: Intercalar dos Vectores (Un elemento de A y uno de B)
  Writeln('----------------------------------------------------------------');
  Writeln('OPERACION 4: Intercalar dos Vectores (Un elemento de A y uno de B)');
  Writeln('----------------------------------------------------------------');
  // Vector B para la prueba
  VB.CargarDesdeTexto('10, 20, 30, 40, 50');
  Writeln('Vector A: ', VA.ATexto());
  Writeln('Vector B: ', VB.ATexto());
  VA.Intercalar(VB, VInter);
  Writeln('Vector Intercalado (A y B): (Dim = ', VInter.GetDim(), ')');
  Writeln('   ', VInter.ATexto());
  Writeln;

  // OPERACION 5: Purgar los Elementos usando Cortes de Control
  Writeln('----------------------------------------------------------------');
  Writeln('OPERACION 5: Purgar los Elementos usando Cortes de Control');
  Writeln('----------------------------------------------------------------');
  Writeln('Vector A con duplicados: ', VA.ATexto());
  VA.PurgarCorteControl(VPurgado);
  Writeln('Vector Purgado (sin duplicados, por corte): ', VPurgado.ATexto());
  Writeln('Dimension original: ', VA.GetDim(), ' -> Dimension purgada: ', VPurgado.GetDim());
  Writeln;

  Writeln('================================================================');
  Writeln('     FIN DE LAS PRUEBAS - TODAS LAS OPERACIONES EXITOSAS        ');
  Writeln('================================================================');

  VA.Free;
  VB.Free;
  VPar.Free;
  VImpar.Free;
  VInter.Free;
  VPurgado.Free;
  VVal.Free;
  VCant.Free;
end.
