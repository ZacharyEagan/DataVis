#!/usr/bin/env python
#also sorry any nonpythony format I'm mostly a C/C++ developer
import sys
import numpy as np
import vtk
import math
from vtk.util import numpy_support


#window and render objects
renWin = vtk.vtkRenderWindow() #window to hold graphics stuff
iren = vtk.vtkRenderWindowInteractor() #adds basic human UI to window
iren.SetRenderWindow(renWin) #and assignes the callback handles


# pdbReader
ren = vtk.vtkRenderer() #link to the graphics pipeline
pdbReader = vtk.vtkPDBReader() 
if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   filename = "files_pdb/test2.pdb" #file path for input 

pdbReader.SetFileName(filename); #not using just yet but important
mapp = vtk.vtkPolyDataMapper() 
mapp.SetInputConnection(pdbReader.GetOutputPort()) 
pdbActor = vtk.vtkActor() 
pdbProp = pdbActor.GetProperty()
pdbActor.SetMapper(mapp) 
ren.AddActor(pdbActor) 




# parse pdb file for number of atoms per acid (count) and types of acids (names)
count  = {}
names = {}
with open(filename, "r") as pdbfile:
   for line in pdbfile:
      if line.find("ATOM") == 0 or line.find("HETAM") == 0:
         listo = line.split()
         count[listo[5]] = count.get(listo[5], 0) + 1
         names[listo[5]] = listo[3]
         
#reorganise data into namecount which is the number of unique instances of each acid
namecount = {}
for acid in names:
   namecount[names[acid]] = namecount.get(names[acid], 0) + 1
print(namecount)

# histogram
table1 = vtk.vtkTable()

arrx = vtk.vtkFloatArray()
arrx.SetName("X-Axis")
table1.AddColumn(arrx)

arrd = vtk.vtkFloatArray()
arrd.SetName("Data")
table1.AddColumn(arrd)

numpoints = 20
table1.SetNumberOfRows(numpoints)
for i in range(numpoints):
   table1.SetValue(i, 0, i)
   table1.SetValue(i, 1, 5)

view1 = vtk.vtkContextView()
chart1 = vtk.vtkChartHistogram2D()

#points1 = chart1.AddPlot(vtk.vtkChart.POINTS)
#points1.SetInput(table1, 0, 1)

view1 = vtk.vtkContextView()
view1.GetRenderer().SetBackground(1.0,1.0,1.0)
#view1.GetScene().AddItem(chart1)
xyrenderer = view1.GetRenderer()


# PieChart
chart = vtk.vtkChartPie()
pie = chart.AddPlot(0)

#pie = vtk.vtkPlotPie()
#chart = vtk.vtkChartHistogram2D()
chart.SetShowLegend(True)
view = vtk.vtkContextView()
view.GetRenderer().SetBackground(0.0,0.0,0.0)
view.GetScene().AddItem(chart)
pieRenderer = view.GetRenderer()
###### Data Section
table = vtk.vtkTable()




#table.SetValue(0,0,1)
#print "a"
#print (table.GetValue(0,0))
#print "b"

#pie.SetInput(table)
#print "c"
#table.SetNumberOfRows(len(namecount))
#print "d"

#table.SetNumberOfColumns(1)
#pie.SetInputArray(0, "Amins")


#pie.SetInputData(table)
 #    
arrC = vtk.vtkFloatArray()
#arrC.SetName('Cosine')
arrS = vtk.vtkFloatArray()
arrS.SetName('Sine')
#table.AddColumn(arrC)





dataLables = vtk.vtkStringArray()
dataPoints = vtk.vtkIntArray()
dataPoints.SetName("Amino Acid Composition")
table.AddColumn(dataPoints)
table.AddColumn(arrS)



for i in namecount:
   dataLables.InsertNextValue(i)
   dataPoints.InsertNextValue(namecount[i]) 

table.SetNumberOfRows(len(namecount))
pie.SetLabels(dataLables)
#print type(pie.GetColorSeries())
srs = pie.GetColorSeries()
srs.SetColorScheme(vtk.vtkColorSeries.COOL)
#srs.SetColorScheme(vtk.vtkColorSeries.SPECTRUM)
#pie.SetColorSeries(vtk.vtkColorSeries().SetColorScheme(16))

#pie.GetLabel().Properties()
#chart.GetAxis(0).GetTitleProperties()
#pie.GetAxis()
print (pie)
points = chart.AddPlot(vtk.vtkChart.POINTS)
points.SetInput(table, 0, 1)

##### end data section


#set viewport sides
ren.SetViewport(0, 0.0, 0.5, 1.0);
pieRenderer.SetViewport(0.5,0.2,1.0,0.8)
#xyrenderer.SetViewport(0.5,0,1.0,1.0)

#add renderers to window
renWin.AddRenderer(ren) #ok so on high level makes sense this puts
renWin.AddRenderer(pieRenderer)
#renWin.AddRenderer(xyrenderer)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
