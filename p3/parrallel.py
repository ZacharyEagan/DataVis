import vtk





ren = vtk.vtkRenderer()
#ren.AddActor()
renwin = vtk.vtkRenderWindow()
renwin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renwin)
renwin.Render()
iren.Start()
