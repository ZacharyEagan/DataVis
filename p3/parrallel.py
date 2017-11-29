import vtk

reader = vtk.vtkDelimitedTextReader()
reader.DetectNumericColumnsOn()
reader.SetFieldDelimiterCharacters(",")
reader.SetHaveHeaders(True)
#reader.SetHaveHeaders(False)
reader.SetMaxRecords(20)
#print reader.GetHeaders()
#reader.SetFileName("iris.csv")
reader.SetFileName("postscndryunivsrvy2013dirinfo.csv")
reader.Update()

print "data read"

rep = vtk.vtkParallelCoordinatesRepresentation()
rep.SetInputConnection(reader.GetOutputPort())
rep.SetUseCurves(1)
#rep.SelectColorArray(1)

view = vtk.vtkContextView()
view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
view.GetRenderWindow().SetSize(600,300)

chart = vtk.vtkChartParallelCoordinates()
view.GetScene().AddItem(chart)


chart.GetPlot(0).SetInputData(reader.GetOutput())
view.ResetCamera()
view.Render()

# Start interaction event loop
view.GetInteractor().Start()

