import vtk

vol = vtk.vtkImageData()
vol.SetDimensions(2, 3, 4)
vol.SetOrigin(0,0,0)
vol.SetSpacing(1,1,1)


