unit main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Grids, ExtCtrls,
  uVectorPlus;

type

  { TFormMain }

  TFormMain = class(TForm)
    // Titulo y encabezado
    LabelTitulo: TLabel;
    LabelSubtitulo: TLabel;
    LabelAutor: TLabel;

    // Grupo Vector A
    GroupBoxA: TGroupBox;
    LabelGridA: TLabel;
    StringGridA: TStringGrid;
    LabelElemA: TLabel;
    EditElemA: TEdit;
    LabelPosA: TLabel;
    EditPosA: TEdit;
    ButtonAddA: TButton;
    ButtonInsA: TButton;
    ButtonRemA: TButton;
    ButtonClearA: TButton;
    LabelTextoA: TLabel;
    EditTextoA: TEdit;
    ButtonCargarTextoA: TButton;
    ButtonEjemploA: TButton;

    // Grupo Vector B
    GroupBoxB: TGroupBox;
    LabelGridB: TLabel;
    StringGridB: TStringGrid;
    LabelElemB: TLabel;
    EditElemB: TEdit;
    ButtonAddB: TButton;
    ButtonClearB: TButton;
    LabelTextoB: TLabel;
    EditTextoB: TEdit;
    ButtonCargarTextoB: TButton;
    ButtonEjemploB: TButton;

    // Grupo Operaciones
    GroupBoxOperaciones: TGroupBox;
    ButtonOp1: TButton;
    EditCortesA: TEdit;
    ButtonOp2: TButton;
    ButtonOp3: TButton;
    ButtonOp4: TButton;
    ButtonOp5: TButton;
    ButtonDemo: TButton;
    ButtonLimpiarTodo: TButton;

    // Grupo Resultados
    GroupBoxResultados: TGroupBox;
    LabelGridResultado: TLabel;
    StringGridResultado: TStringGrid;
    LabelGridPar: TLabel;
    StringGridPar: TStringGrid;
    LabelGridImpar: TLabel;
    StringGridImpar: TStringGrid;
    LabelReporte: TLabel;
    MemoReporte: TMemo;

    // Eventos
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);

    // Eventos Vector A
    procedure ButtonAddAClick(Sender: TObject);
    procedure ButtonInsAClick(Sender: TObject);
    procedure ButtonRemAClick(Sender: TObject);
    procedure ButtonClearAClick(Sender: TObject);
    procedure ButtonCargarTextoAClick(Sender: TObject);
    procedure ButtonEjemploAClick(Sender: TObject);

    // Eventos Vector B
    procedure ButtonAddBClick(Sender: TObject);
    procedure ButtonClearBClick(Sender: TObject);
    procedure ButtonCargarTextoBClick(Sender: TObject);
    procedure ButtonEjemploBClick(Sender: TObject);

    // Eventos de Operaciones
    procedure ButtonOp1Click(Sender: TObject);
    procedure ButtonOp2Click(Sender: TObject);
    procedure ButtonOp3Click(Sender: TObject);
    procedure ButtonOp4Click(Sender: TObject);
    procedure ButtonOp5Click(Sender: TObject);
    procedure ButtonDemoClick(Sender: TObject);
    procedure ButtonLimpiarTodoClick(Sender: TObject);

  private
    VA: TVectorPlus;
    VB: TVectorPlus;
    VRes: TVectorPlus;
    VPar: TVectorPlus;
    VImpar: TVectorPlus;

    procedure ActualizarGrid(Grid: TStringGrid; V: TVectorPlus);
    procedure ActualizarTodasLasTablas();
    procedure Log(const Mensaje: string);

  public

  end;

var
  FormMain: TFormMain;

implementation

{$R *.lfm}

{ TFormMain }

procedure TFormMain.FormCreate(Sender: TObject);
begin
  VA := TVectorPlus.Create;
  VB := TVectorPlus.Create;
  VRes := TVectorPlus.Create;
  VPar := TVectorPlus.Create;
  VImpar := TVectorPlus.Create;

  // Cargar ejemplo inicial por defecto
  VA.CargarDesdeTexto('2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3');
  EditTextoA.Text := '2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3';

  VB.CargarDesdeTexto('10, 20, 30, 40, 50');
  EditTextoB.Text := '10, 20, 30, 40, 50';

  ActualizarTodasLasTablas();
  Log('Sistema inicializado. Se cargaron los vectores de ejemplo de la leccion.');
end;

procedure TFormMain.FormDestroy(Sender: TObject);
begin
  VA.Free;
  VB.Free;
  VRes.Free;
  VPar.Free;
  VImpar.Free;
end;

procedure TFormMain.ActualizarGrid(Grid: TStringGrid; V: TVectorPlus);
var
  i, dim: integer;
begin
  Grid.Clean([]);
  if (V = nil) or (V.GetDim() = 0) then
  begin
    Grid.ColCount := 1;
    Grid.Cells[0, 0] := 'Pos';
    Grid.Cells[0, 1] := '-';
    Exit;
  end;

  dim := V.GetDim();
  Grid.ColCount := dim;
  for i := 1 to dim do
  begin
    Grid.Cells[i - 1, 0] := IntToStr(i);
    Grid.Cells[i - 1, 1] := IntToStr(V.GetElem(i));
  end;
end;

procedure TFormMain.ActualizarTodasLasTablas();
begin
  ActualizarGrid(StringGridA, VA);
  ActualizarGrid(StringGridB, VB);
  ActualizarGrid(StringGridResultado, VRes);
  ActualizarGrid(StringGridPar, VPar);
  ActualizarGrid(StringGridImpar, VImpar);
end;

procedure TFormMain.Log(const Mensaje: string);
begin
  MemoReporte.Lines.Add(Mensaje);
end;

// =============================================================================
// GESTION VECTOR A
// =============================================================================

procedure TFormMain.ButtonAddAClick(Sender: TObject);
var
  val: integer;
begin
  if TryStrToInt(Trim(EditElemA.Text), val) then
  begin
    VA.AddElem(val);
    ActualizarGrid(StringGridA, VA);
    Log('Vector A: Se adiciono el elemento ' + IntToStr(val));
    EditElemA.Text := '';
  end
  else
    ShowMessage('Por favor ingrese un numero entero valido en Elemento.');
end;

procedure TFormMain.ButtonInsAClick(Sender: TObject);
var
  val, pos: integer;
begin
  if not TryStrToInt(Trim(EditElemA.Text), val) then
  begin
    ShowMessage('Por favor ingrese un elemento entero valido.');
    Exit;
  end;
  if not TryStrToInt(Trim(EditPosA.Text), pos) then
  begin
    ShowMessage('Por favor ingrese una posicion valida (1..' + IntToStr(VA.GetDim() + 1) + ').');
    Exit;
  end;

  if (pos < 1) or (pos > VA.GetDim() + 1) then
  begin
    ShowMessage('Posicion fuera de rango [1..' + IntToStr(VA.GetDim() + 1) + '].');
    Exit;
  end;

  VA.InsElem(pos, val);
  ActualizarGrid(StringGridA, VA);
  Log('Vector A: Se inserto ' + IntToStr(val) + ' en la posicion ' + IntToStr(pos));
end;

procedure TFormMain.ButtonRemAClick(Sender: TObject);
var
  pos: integer;
begin
  if not TryStrToInt(Trim(EditPosA.Text), pos) then
  begin
    ShowMessage('Por favor ingrese una posicion a remover (1..' + IntToStr(VA.GetDim()) + ').');
    Exit;
  end;

  if (pos < 1) or (pos > VA.GetDim()) then
  begin
    ShowMessage('Posicion fuera de rango [1..' + IntToStr(VA.GetDim()) + '].');
    Exit;
  end;

  VA.RemElem(pos);
  ActualizarGrid(StringGridA, VA);
  Log('Vector A: Se removio el elemento de la posicion ' + IntToStr(pos));
end;

procedure TFormMain.ButtonClearAClick(Sender: TObject);
begin
  VA.Clear();
  ActualizarGrid(StringGridA, VA);
  EditCortesA.Text := '';
  Log('Vector A: Ha sido vaciado.');
end;

procedure TFormMain.ButtonCargarTextoAClick(Sender: TObject);
var
  c: integer;
begin
  c := VA.CargarDesdeTexto(EditTextoA.Text);
  ActualizarGrid(StringGridA, VA);
  Log('Vector A: Se cargaron ' + IntToStr(c) + ' elementos desde texto.');
end;

procedure TFormMain.ButtonEjemploAClick(Sender: TObject);
begin
  EditTextoA.Text := '2, 0, 2, 1, 3, 8, 4, 8, 6, 8, 3, 3, 3';
  VA.CargarDesdeTexto(EditTextoA.Text);
  ActualizarGrid(StringGridA, VA);
  Log('Vector A: Cargado con ejemplo oficial de la leccion.');
end;

// =============================================================================
// GESTION VECTOR B
// =============================================================================

procedure TFormMain.ButtonAddBClick(Sender: TObject);
var
  val: integer;
begin
  if TryStrToInt(Trim(EditElemB.Text), val) then
  begin
    VB.AddElem(val);
    ActualizarGrid(StringGridB, VB);
    Log('Vector B: Se adiciono el elemento ' + IntToStr(val));
    EditElemB.Text := '';
  end
  else
    ShowMessage('Por favor ingrese un numero entero valido para Vector B.');
end;

procedure TFormMain.ButtonClearBClick(Sender: TObject);
begin
  VB.Clear();
  ActualizarGrid(StringGridB, VB);
  Log('Vector B: Ha sido vaciado.');
end;

procedure TFormMain.ButtonCargarTextoBClick(Sender: TObject);
var
  c: integer;
begin
  c := VB.CargarDesdeTexto(EditTextoB.Text);
  ActualizarGrid(StringGridB, VB);
  Log('Vector B: Se cargaron ' + IntToStr(c) + ' elementos desde texto.');
end;

procedure TFormMain.ButtonEjemploBClick(Sender: TObject);
begin
  EditTextoB.Text := '10, 20, 30, 40, 50';
  VB.CargarDesdeTexto(EditTextoB.Text);
  ActualizarGrid(StringGridB, VB);
  Log('Vector B: Cargado con secuencia [10, 20, 30, 40, 50].');
end;

// =============================================================================
// OPERACIONES REQUERIDAS
// =============================================================================

// 1. Cantidad de Cortes Control
procedure TFormMain.ButtonOp1Click(Sender: TObject);
var
  cortes: integer;
begin
  cortes := VA.CantidadCortesControl();
  EditCortesA.Text := IntToStr(cortes) + ' cortes';
  Log('--------------------------------------------------');
  Log('OPERACION 1: Cantidad de Cortes de Control');
  Log('Vector A: ' + VA.ATexto());
  Log('Total de cortes de control detectados: ' + IntToStr(cortes));
end;

// 2. Cantidad de Elementos entre Cortes de Control
procedure TFormMain.ButtonOp2Click(Sender: TObject);
var
  res: string;
begin
  res := VA.ResumenElementosEntreCortes();
  Log('--------------------------------------------------');
  Log('OPERACION 2: Cantidad de Elementos entre Cortes');
  Log('Vector A: ' + VA.ATexto());
  Log(res);
end;

// 3. Dividir un Vector en dos (Par e Impar)
procedure TFormMain.ButtonOp3Click(Sender: TObject);
begin
  VA.DividirParImpar(VPar, VImpar);
  ActualizarGrid(StringGridPar, VPar);
  ActualizarGrid(StringGridImpar, VImpar);
  Log('--------------------------------------------------');
  Log('OPERACION 3: Dividir en Par e Impar');
  Log('Vector A original: ' + VA.ATexto());
  Log('Vector Pares   (Dim=' + IntToStr(VPar.GetDim()) + '): ' + VPar.ATexto());
  Log('Vector Impares (Dim=' + IntToStr(VImpar.GetDim()) + '): ' + VImpar.ATexto());
end;

// 4. Intercalar dos Vectores (Un elemento de A y uno de B)
procedure TFormMain.ButtonOp4Click(Sender: TObject);
begin
  VA.Intercalar(VB, VRes);
  ActualizarGrid(StringGridResultado, VRes);
  Log('--------------------------------------------------');
  Log('OPERACION 4: Intercalar dos Vectores (A y B)');
  Log('Vector A: ' + VA.ATexto());
  Log('Vector B: ' + VB.ATexto());
  Log('Vector Intercalado (Dim=' + IntToStr(VRes.GetDim()) + '): ' + VRes.ATexto());
end;

// 5. Purgar los Elementos usando Cortes de Control
procedure TFormMain.ButtonOp5Click(Sender: TObject);
begin
  VA.PurgarCorteControl(VRes);
  ActualizarGrid(StringGridResultado, VRes);
  Log('--------------------------------------------------');
  Log('OPERACION 5: Purgar Elementos usando Cortes de Control');
  Log('Vector A con duplicados: ' + VA.ATexto());
  Log('Vector Purgado resultante (Dim=' + IntToStr(VRes.GetDim()) + '): ' + VRes.ATexto());
end;

// Demostracion completa paso a paso
procedure TFormMain.ButtonDemoClick(Sender: TObject);
begin
  MemoReporte.Clear();
  Log('==================================================');
  Log('DEMOSTRACION COMPLETA - CLASE TVectorPlus (INF120)');
  Log('==================================================');
  ButtonOp1Click(Sender);
  ButtonOp2Click(Sender);
  ButtonOp3Click(Sender);
  ButtonOp4Click(Sender);
  ButtonOp5Click(Sender);
  Log('Demostracion ejecutada con exito.');
end;

procedure TFormMain.ButtonLimpiarTodoClick(Sender: TObject);
begin
  VA.Clear();
  VB.Clear();
  VRes.Clear();
  VPar.Clear();
  VImpar.Clear();
  EditCortesA.Text := '';
  MemoReporte.Clear();
  ActualizarTodasLasTablas();
  Log('Todos los vectores y resultados han sido limpiados.');
end;

end.
