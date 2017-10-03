#!/usr/bin/env python
#also sorry for the nonpythony format I'm mostly a C/C++ developer

import vtk

filename = "test.pdb"


#Declare objects
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()
sphere = vtk.vtkSphereSource()
pdbReader = vtk.vtkPDBReader()
mapp = vtk.vtkPolyDataMapper()



# Setup FileIO
pdbReader.SetFileName("cafeine.pdb");

iren.SetRenderWindow(renWin)





# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
