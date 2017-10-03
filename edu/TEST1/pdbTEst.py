#!/usr/bin/env python
#also sorry for the nonpythony format I'm mostly a C/C++ developer

import vtk

filename = "file_pdb/cafeine.pdb" #file path for input 
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
mapp = vtk.vtkPolyDataMapper()


# Setup FileIO
pdbReader.SetFileName(filename); #not using just yet but important
#to keep arround considering difficulty of finding docs.
#this reads in a pdb file. Doesn't throw error though not tested for
#actually giving anything useful
 
sphereMap = vtk.vtkPolyDataMapper() #still not sure what it does
sphereMap.SetInputConnection(sphere.GetOutputPort()) #handle to sphere?
sphereActor = vtk.vtkActor() #ok so this is just a prerender pipeline?
sphereActor.SetMapper(sphereMap)



renWin.AddRenderer(ren) #ok so on high level makes sense this puts
#the graphics into the os allocated window
iren.SetRenderWindow(renWin) #and assignes the callback handles

ren.AddActor(sphereActor) #and put in the sphere


# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
