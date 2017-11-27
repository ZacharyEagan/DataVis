import vtk




parRep = vtk.vtkParallelCoordinatesRepresentation()
#parRep.SetInputConnection(data.GetOutputPort())

parView = vtk.vtkParallelCoordinatesView()
parView.SetRepresentation(parRep)
parView.SetInspectMode(1)
parView.SetBrushOperatorToReplace()
parView.SetBrushModeToLasso()



#ren = vtk.vtkRenderer()
#ren.AddActor()
#renwin = vtk.vtkRenderWindow()
#renwin.AddRenderer(ren)
#iren = vtk.vtkRenderWindowInteractor()
#iren.SetRenderWindow(renwin)
#renwin.Render()

parView.GetRenderWindow().SetSize(600,300)
parView.ResetCamera()
parView.Render()
parView.GetInteractor().Start()

#iren.Start()
