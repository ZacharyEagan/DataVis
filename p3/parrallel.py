import vtk



########### Iris data exctraction from lab6
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
iris_species = []

with  open("iris.csv", "r") as iris_file:
   for line in iris_file:
      data = line.split(",")
#      print len(data)
      if len(data) == 5:
#      print data
         sepal_length.append(float(data[0]))
         sepal_width.append(float(data[1]))
         petal_length.append(float(data[2]))
         petal_width.append(float(data[3]))
         iris_species.append(data[4])

width_sum = 0;
for petal in petal_width:
   width_sum += petal;
width_av = width_sum / len(petal_width)

petal_dict = {}
for iris in iris_species:
   petal_dict[iris] = petal_dict.get(iris,0) + 1
print (petal_dict)


scale = 0.01
################end Iris Data Extraction




reader = vtk.vtkDelimitedTextReader()
reader.DetectNumericColumnsOn()
reader.SetFieldDelimiterCharacters(",")
#reader.SetHaveHeaders(True)
reader.SetHaveHeaders(False)
reader.SetMaxRecords(100)
reader.SetFileName("iris.csv")
reader.Update()
#table = reader.GetOutput()
rep = vtk.vtkParallelCoordinatesRepresentation()
rep.SetInputConnection(reader.GetOutputPort())


view = vtk.vtkContextView()
view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
view.GetRenderWindow().SetSize(600,300)

chart = vtk.vtkChartParallelCoordinates()
view.GetScene().AddItem(chart)

print chart.GetPlot(0)
print " "
print type(chart.GetPlot(0))
print " "


chart.GetPlot(0).SetInputData(reader.GetOutput())

view.ResetCamera()
view.Render()

# Start interaction event loop
view.GetInteractor().Start()







#parRep = vtk.vtkParallelCoordinatesRepresentation()
#parRep.SetInputConnection(data.GetOutputPort())
#parRep.SetInputConnection(reader.GetOutputPort())
#parRep.SetInputArrayToProcess(0,0,0,0,'petal')

#parView = vtk.vtkParallelCoordinatesView()
#parView.SetRepresentation(parRep)
#parView.SetInspectMode(1)
#parView.SetBrushOperatorToReplace()
#parView.SetBrushModeToLasso()



#ren = vtk.vtkRenderer()
#ren.AddActor()
#renwin = vtk.vtkRenderWindow()
#renwin.AddRenderer(ren)
#iren = vtk.vtkRenderWindowInteractor()
#iren.SetRenderWindow(renwin)
#renwin.Render()

#parView.GetRenderWindow().SetSize(600,300)
#parView.ResetCamera()
#parView.Render()
#parView.GetInteractor().Start()

#iren.Start()
