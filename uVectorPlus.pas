unit uVectorPlus;

{$mode ObjFPC}{$H+}

interface

uses
  SysUtils;

const
  MAX_E = 1000; // Capacidad maxima del vector segun el estandar de la materia

type
  { TVectorPlus }
  // Clase que modela un arreglo unidimensional y extiende sus operaciones
  // con tecnicas algoritmicas avanzadas: Cortes de Control, Intercalacion,
  // Division y Purga de elementos.
  TVectorPlus = class
  private
    elem: array[1..MAX_E] of integer;
    dim: integer;

  public
    // Constructor
    constructor Create;

    // Metodos basicos de acceso y dimension
    procedure SetDim(n: integer);
    function GetDim(): integer;
    procedure SetElem(pos: integer; ele: integer);
    function GetElem(pos: integer): integer;

    // Operaciones primitivas
    procedure AddElem(ele: integer);
    procedure InsElem(pos: integer; ele: integer);
    procedure RemElem(pos: integer);
    procedure Clear();

    // Utilidades de ordenamiento y copia
    procedure OrdenarAscendente();
    procedure CopiarDesde(origen: TVectorPlus);
    function Clonar(): TVectorPlus;
    function CargarDesdeTexto(const S: string): integer;
    function ATexto(): string;

    // -------------------------------------------------------------------------
    // 5 OPERACIONES REQUERIDAS POR LA APLICACION U4
    // -------------------------------------------------------------------------

    // 1. Cantidad de Cortes de Control
    function CantidadCortesControl(): integer;

    // 2. Cantidad de Elementos entre Cortes de Control
    procedure CantidadElementosEntreCortes(VValores, VCantidades: TVectorPlus);
    function ResumenElementosEntreCortes(): string;

    // 3. Dividir un Vector en dos (Par e Impar)
    procedure DividirParImpar(VPar, VImpar: TVectorPlus);

    // 4. Intercalar dos Vectores (Un elemento de A y uno de B)
    procedure Intercalar(VB, VResult: TVectorPlus);

    // 5. Purgar los Elementos usando Cortes de Control
    procedure PurgarCorteControl(VPurgado: TVectorPlus);
    procedure PurgarCorteControl(); // Version sobre el mismo vector
  end;

  // Alias para compatibilidad con el enunciado: "Crear una Clase llamada VectorPlus"
  VectorPlus = TVectorPlus;

implementation

{ TVectorPlus }

constructor TVectorPlus.Create;
begin
  dim := 0;
  Clear();
end;

procedure TVectorPlus.SetDim(n: integer);
begin
  if (n >= 0) and (n <= MAX_E) then
    dim := n
  else
    Writeln('Error: Dimension fuera de rango [0..', MAX_E, ']');
end;

function TVectorPlus.GetDim(): integer;
begin
  Result := dim;
end;

procedure TVectorPlus.SetElem(pos: integer; ele: integer);
begin
  if (pos >= 1) and (pos <= dim) then
    elem[pos] := ele
  else
    Writeln('Error: Posicion ', pos, ' fuera de rango [1..', dim, ']');
end;

function TVectorPlus.GetElem(pos: integer): integer;
begin
  if (pos >= 1) and (pos <= dim) then
    Result := elem[pos]
  else
  begin
    Writeln('Error: Posicion ', pos, ' fuera de rango [1..', dim, ']');
    Result := 0;
  end;
end;

procedure TVectorPlus.AddElem(ele: integer);
begin
  if dim < MAX_E then
  begin
    Inc(dim);
    elem[dim] := ele;
  end
  else
    Writeln('Error: Almacenamiento lleno, no se puede adicionar elemento.');
end;

procedure TVectorPlus.InsElem(pos: integer; ele: integer);
var
  i: integer;
begin
  if dim >= MAX_E then
  begin
    Writeln('Error: Almacenamiento lleno al insertar.');
    Exit;
  end;

  if (pos < 1) or (pos > dim + 1) then
  begin
    Writeln('Error: Posicion fuera de rango al insertar.');
    Exit;
  end;

  for i := dim downto pos do
    elem[i + 1] := elem[i];

  elem[pos] := ele;
  Inc(dim);
end;

procedure TVectorPlus.RemElem(pos: integer);
var
  i: integer;
begin
  if (pos < 1) or (pos > dim) then
  begin
    Writeln('Error: Posicion fuera de rango al remover.');
    Exit;
  end;

  for i := pos to dim - 1 do
    elem[i] := elem[i + 1];

  elem[dim] := 0;
  Dec(dim);
end;

procedure TVectorPlus.Clear();
var
  i: integer;
begin
  for i := 1 to MAX_E do
    elem[i] := 0;
  dim := 0;
end;

procedure TVectorPlus.OrdenarAscendente();
var
  i, j, aux: integer;
begin
  if dim <= 1 then
    Exit;

  for i := 1 to dim - 1 do
  begin
    for j := 1 to dim - i do
    begin
      if elem[j] > elem[j + 1] then
      begin
        aux := elem[j];
        elem[j] := elem[j + 1];
        elem[j + 1] := aux;
      end;
    end;
  end;
end;

procedure TVectorPlus.CopiarDesde(origen: TVectorPlus);
var
  i: integer;
begin
  Clear();
  if origen = nil then
    Exit;

  for i := 1 to origen.GetDim() do
    AddElem(origen.GetElem(i));
end;

function TVectorPlus.Clonar(): TVectorPlus;
var
  nuevo: TVectorPlus;
begin
  nuevo := TVectorPlus.Create;
  nuevo.CopiarDesde(Self);
  Result := nuevo;
end;

function TVectorPlus.CargarDesdeTexto(const S: string): integer;
var
  i, len, val, numCount: integer;
  numStr: string;
  enNumero: boolean;
begin
  Clear();
  numCount := 0;
  numStr := '';
  enNumero := False;
  len := System.Length(S);

  for i := 1 to len do
  begin
    if ((S[i] >= '0') and (S[i] <= '9')) or ((S[i] = '-') and (not enNumero)) then
    begin
      numStr := numStr + S[i];
      enNumero := True;
    end
    else
    begin
      if enNumero and (numStr <> '') and (numStr <> '-') then
      begin
        if TryStrToInt(numStr, val) then
        begin
          AddElem(val);
          Inc(numCount);
        end;
        numStr := '';
        enNumero := False;
      end;
    end;
  end;

  if enNumero and (numStr <> '') and (numStr <> '-') then
  begin
    if TryStrToInt(numStr, val) then
    begin
      AddElem(val);
      Inc(numCount);
    end;
  end;

  Result := numCount;
end;

function TVectorPlus.ATexto(): string;
var
  i: integer;
  res: string;
begin
  if dim = 0 then
  begin
    Result := '[]';
    Exit;
  end;

  res := '[';
  for i := 1 to dim do
  begin
    res := res + IntToStr(elem[i]);
    if i < dim then
      res := res + ', ';
  end;
  res := res + ']';
  Result := res;
end;

// =============================================================================
// OPERACION 1: Cantidad de Cortes Control
// =============================================================================
// Precondicion de la tecnica de Corte de Control: los datos deben estar ordenados
// o agrupados por el criterio de corte. Por ello, se genera una copia de trabajo
// ordenada para agrupar elementos identicos y se cuentan las transiciones de corte.
function TVectorPlus.CantidadCortesControl(): integer;
var
  vTemp: TVectorPlus;
  i, cant, clave: integer;
begin
  if dim = 0 then
  begin
    Result := 0;
    Exit;
  end;

  vTemp := Clonar();
  vTemp.OrdenarAscendente();

  cant := 0;
  i := 1;
  while i <= vTemp.GetDim() do
  begin
    clave := vTemp.GetElem(i);
    Inc(cant); // Inicio de un nuevo corte de control

    // Recorrer y consumir todos los elementos pertenecientes a este corte
    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do
      Inc(i);
  end;

  vTemp.Free;
  Result := cant;
end;

// =============================================================================
// OPERACION 2: Cantidad de Elementos entre Cortes de Control
// =============================================================================
// Determina la cantidad de elementos (frecuencia) que contiene cada corte de control.
// Retorna dos vectores sincronizados:
// - VValores: Contiene la clave/valor de cada corte
// - VCantidades: Contiene la cantidad de elementos en dicho corte
procedure TVectorPlus.CantidadElementosEntreCortes(VValores, VCantidades: TVectorPlus);
var
  vTemp: TVectorPlus;
  i, cant, clave: integer;
begin
  if VValores <> nil then
    VValores.Clear();
  if VCantidades <> nil then
    VCantidades.Clear();

  if dim = 0 then
    Exit;

  vTemp := Clonar();
  vTemp.OrdenarAscendente();

  i := 1;
  while i <= vTemp.GetDim() do
  begin
    clave := vTemp.GetElem(i);
    cant := 0;

    // Contar los elementos que comparten la misma clave de corte
    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do
    begin
      Inc(cant);
      Inc(i);
    end;

    if VValores <> nil then
      VValores.AddElem(clave);
    if VCantidades <> nil then
      VCantidades.AddElem(cant);
  end;

  vTemp.Free;
end;

function TVectorPlus.ResumenElementosEntreCortes(): string;
var
  VValores, VCantidades: TVectorPlus;
  i: integer;
  res: string;
begin
  if dim = 0 then
  begin
    Result := 'El vector esta vacio (0 cortes de control).';
    Exit;
  end;

  VValores := TVectorPlus.Create;
  VCantidades := TVectorPlus.Create;
  CantidadElementosEntreCortes(VValores, VCantidades);

  res := 'CORTES DE CONTROL Y CANTIDAD DE ELEMENTOS:' + LineEnding;
  res := res + 'Total de cortes detectados: ' + IntToStr(VValores.GetDim()) + LineEnding;
  res := res + '-----------------------------------------' + LineEnding;

  for i := 1 to VValores.GetDim() do
  begin
    res := res + 'Corte #' + IntToStr(i) + ': Clave = ' + IntToStr(VValores.GetElem(i)) +
      '  -->  Cantidad de elementos: ' + IntToStr(VCantidades.GetElem(i)) + LineEnding;
  end;

  VValores.Free;
  VCantidades.Free;
  Result := res;
end;

// =============================================================================
// OPERACION 3: Dividir un Vector en dos (Par e Impar)
// =============================================================================
// Recorre el vector original evaluando la paridad de cada elemento (elem mod 2).
// Los valores pares se dirigen a VPar y los impares a VImpar.
procedure TVectorPlus.DividirParImpar(VPar, VImpar: TVectorPlus);
var
  i, valor: integer;
begin
  if VPar <> nil then
    VPar.Clear();
  if VImpar <> nil then
    VImpar.Clear();

  for i := 1 to dim do
  begin
    valor := elem[i];
    if (valor mod 2 = 0) then
    begin
      if VPar <> nil then
        VPar.AddElem(valor);
    end
    else
    begin
      if VImpar <> nil then
        VImpar.AddElem(valor);
    end;
  end;
end;

// =============================================================================
// OPERACION 4: Intercalar dos Vectores (Un elemento de A y uno de B)
// =============================================================================
// Toma alternadamente un elemento de Self (Vector A) y un elemento de VB (Vector B)
// colocandolos en VResult. Si un vector tiene mayor dimension, los elementos
// sobrantes se anaden al final de VResult.
procedure TVectorPlus.Intercalar(VB, VResult: TVectorPlus);
var
  i, j: integer;
begin
  if VResult = nil then
    Exit;

  VResult.Clear();
  i := 1;
  j := 1;

  // Intercalar 1 elemento de A y 1 elemento de B mientras ambos tengan datos
  while (i <= dim) and ((VB <> nil) and (j <= VB.GetDim())) do
  begin
    VResult.AddElem(elem[i]);
    VResult.AddElem(VB.GetElem(j));
    Inc(i);
    Inc(j);
  end;

  // Si quedan elementos en Vector A (Self), se agregan consecutivamente
  while i <= dim do
  begin
    VResult.AddElem(elem[i]);
    Inc(i);
  end;

  // Si quedan elementos en Vector B, se agregan consecutivamente
  if VB <> nil then
  begin
    while j <= VB.GetDim() do
    begin
      VResult.AddElem(VB.GetElem(j));
      Inc(j);
    end;
  end;
end;

// =============================================================================
// OPERACION 5: Purgar los Elementos usando Cortes de Control
// =============================================================================
// 1) Se ordenan los elementos para garantizar la contiguidad de claves iguales.
// 2) Se aplica la estructura canonica de corte de control:
//    Se selecciona el primer elemento de cada bloque (clave) y se omiten
//    todos los duplicados subsiguientes del mismo corte.
procedure TVectorPlus.PurgarCorteControl(VPurgado: TVectorPlus);
var
  vTemp: TVectorPlus;
  i, clave: integer;
begin
  if VPurgado = nil then
    Exit;

  VPurgado.Clear();
  if dim = 0 then
    Exit;

  vTemp := Clonar();
  vTemp.OrdenarAscendente();

  i := 1;
  while i <= vTemp.GetDim() do
  begin
    clave := vTemp.GetElem(i);
    VPurgado.AddElem(clave); // Solo se anade el representante unico del corte

    // Se salta el resto de elementos repetidos dentro del corte
    while (i <= vTemp.GetDim()) and (vTemp.GetElem(i) = clave) do
      Inc(i);
  end;

  vTemp.Free;
end;

procedure TVectorPlus.PurgarCorteControl();
var
  vTemp: TVectorPlus;
begin
  vTemp := TVectorPlus.Create;
  PurgarCorteControl(vTemp);
  CopiarDesde(vTemp);
  vTemp.Free;
end;

end.
