#!/usr/bin/env python
#also sorry for the nonpythony format I'm mostly a C/C++ developer

import vtk

filename = "file_pdb/cafeine.pdb" #file path for input 


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
mapp = vtk.vtkPolyDataMapper()


# Setup FileIO
pdbReader.SetFileName(filename); 
renWin.





iren.SetRenderWindow(renWin)
# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
