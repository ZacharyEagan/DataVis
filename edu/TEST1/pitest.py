from __future__ import division
import vtk
import math 

view = vtk.vtkContextView()
view.GetRenderer().SetBackground(1.0,1.0,1.0)
view.GetRenderWindow().SetSize(400,300)

chart = vtk.vtkChartPie()
view.GetScene().AddItem(chart)
chart.SetShowLegend(True)

table = vtk.vtkTable()

######
numPoints = 40
arrX = vtk.vtkFloatArray()
arrX.SetName('X Axis')

arrC = vtk.vtkFloatArray()
arrC.SetName('Cosine')

arrS = vtk.vtkFloatArray()
arrS.SetName('Sine')

arrT = vtk.vtkFloatArray()
arrT.SetName('Sine-Cosine')

table.AddColumn(arrC)
table.AddColumn(arrS)
table.AddColumn(arrX)
table.AddColumn(arrT)

inc = 7.5/(numPoints-1)
table.SetNumberOfRows(numPoints)
for i in range(numPoints):
    table.SetValue(i, 0, i*inc)
    table.SetValue(i, 1, math.cos(i*inc))
    table.SetValue(i, 2, math.sin(i*inc))
    table.SetValue(i, 3, math.sin(i*inc)-math.cos(i*inc))
######3

points = chart.AddPlot(vtk.vtkChart.POINTS)
points.SetInput(table, 0, 1)



view.GetRenderWindow().SetMultiSamples(0)
view.GetInteractor().Initialize()
view.GetInteractor().Start()

