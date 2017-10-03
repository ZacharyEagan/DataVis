#!/usr/bin/env python
#also sorry for the nonpythony format I'm mostly a C/C++ developer
import numpy as np
import vtk
from vtk.util import numpy_support

#filename = "files_pdb/cafeine.pdb" #file path for input 
filename = "files_pdb/test2.pdb" #file path for input 
#found a nice example code that used cafeine so I grabbed the molecule
#seemed like a fiting test considering this will take all night


#Declare objects
ren = vtk.vtkRenderer() #link to the graphics pipeline
renWin = vtk.vtkRenderWindow() #window to hold graphics stuff
iren = vtk.vtkRenderWindowInteractor() #adds basic human UI to window
sphere = vtk.vtkSphereSource() #sphere to test window with
#found an example using this pdb reader
#documentations kinda sucky but might work
#def don't want to parse pdb format by hand, not enough time
#similar to improvement of pcap over fscanf
pdbReader = vtk.vtkPDBReader() 
#the examples also all use this thing. no idea what it is but it
#seems to convert from shape primitives to somthing displayable

#pipeline applied to the pdb molecule
mapp = vtk.vtkPolyDataMapper() # 
mapp.SetInputConnection(pdbReader.GetOutputPort()) #
pdbActor = vtk.vtkActor() #
pdbActor.SetMapper(mapp) #
ren.AddActor(pdbActor) #
#Dang Actually worked!

# Setup FileIO
pdbReader.SetFileName(filename); #not using just yet but important
#to keep arround considering difficulty of finding docs.
#this reads in a pdb file. Doesn't throw error though not tested for
#actually giving anything useful
 
#sphereMap = vtk.vtkPolyDataMapper() #still not sure what it does
#sphereMap.SetInputConnection(sphere.GetOutputPort()) #handle to sphere?
#sphereActor = vtk.vtkActor() #ok so this is just a prerender pipeline?
#sphereActor.SetMapper(sphereMap)
#sphereActor.GetProperty().SetColor(0,0,255)

#table = vtk.vtkTable()
#arrx = vtk.vtkFloatArray()
#arrx.SetName("X Axis")
#table.AddColumn(arrx)
#arrc = vtk.vtkFloatArray()
#arrc.SetName("Cos")
#table.AddColumn(arrc)
#table.SetValue(0,0,0)
#table.SetValue(0,1,1)

#view = vtk.vtkContextView()
#chart = vtk.vtkChartXY()
#chart.SetRenderEmpty(True)



#view.GetScene().AddItem(chart)
#line = chart.AddPlot(0)
#line.SetInputData(table, 0, 1)
#line.SetColor(0,255,0)
#line.SetWidth(1.0)
#view.GetInteractor().Initialize()
#view.GetInteractor().Start()

#here's the data generation
#table = vtk.vtkTable()
#data = np.random.random((3,2))
#data2 = numpy_support.numpy_to_vtk(data, deep=0, array_type=None)
#table.GetRowData().AddArray(data2)

#attempting to add a plot
#chart = vtk.vtkChartPie()
#pie = vtk.vtkPlotPie()
#pie.
#chart.AddPlot(pie)


#ren.AddActor(chart)
#gView = vtk.vtkContextView()
#gView.GetScene().AddItem(chart)
#gView.GetRenderWindow().SetMultiSamples(0)
#pie.Paint(gView)

#gView.AddRepresentationFromInput(pie) #NOPE
#gView.Render()


#ren.AddActor(pie) Nope not this way
renWin.AddRenderer(ren) #ok so on high level makes sense this puts
#the graphics into the os allocated window
iren.SetRenderWindow(renWin) #and assignes the callback handles

#ren.AddActor(sphereActor) #and put in the sphere


# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
