import vtk

reader = vtk.vtkDelimitedTextReader()
#reader = vtk.vtkCSVTextReader()
reader.DetectNumericColumnsOn()
reader.SetFieldDelimiterCharacters(",")
reader.SetHaveHeaders(True)
#reader.SetHaveHeaders(False)
reader.SetMaxRecords(300)
#print reader.GetHeaders()
#reader.SetFileName("iris.csv")
#reader.SetFileName("data/banklist.csv")
#reader.SetFileName("data/bikepghmembers.csv")
reader.SetFileName("data/2012_SAT_Results.csv")
#reader.SetFileName("postscndryunivsrvy2013dirinfo.csv")
reader.Update()

print "data read"

rep = vtk.vtkParallelCoordinatesRepresentation()
rep.SetInputConnection(reader.GetOutputPort())
rep.SetUseCurves(1)
#rep.SelectColorArray(1)

view = vtk.vtkContextView()
view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
view.GetRenderWindow().SetSize(600,300)

size = 57
table = vtk.vtkLookupTable()
table.SetNumberOfTableValues(size)
table.SetRange(2,5)
table.SetNumberOfColors(size)
#table.Build()

for i in range(57): 
   table.SetTableValue(i,i,0,0)
   print table.GetTableValue(i)
   print i


chart = vtk.vtkChartParallelCoordinates()
chart.GetPlot(0).SetInputData(reader.GetOutput())
view.GetScene().AddItem(chart)
chart.GetPlot(0).SetLookupTable(table)
#chart.GetPlot(0).SetLookupTable(table)
chart.GetPlot(0).SelectColorArray("Sepal_Length")
chart.GetPlot(0).SetScalarVisibility(1)
#chart.GetPlot(0).GetPen().SetOpacityF(0.8)



chart.SetColumnVisibility("School Name", False)
chart.SetColumnVisibility("Purchaser", False)
chart.SetColumnVisibility("Purchased", False)
#chart.SetRowVisibility(0, False)

view.ResetCamera()
view.Render()

# Start interaction event loop
view.GetInteractor().Start()

