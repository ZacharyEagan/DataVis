import vtk

renwin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renwin)
ren = vtk.vtkRenderer()






points = vtk.vtkPoints()
points.InsertNextPoint(0.0,0.0,0.0) #0 0 
points.InsertNextPoint(0.0,0.0,1.0) #1 Z
points.InsertNextPoint(0.0,1.0,0.0) #2 Y
points.InsertNextPoint(0.0,1.0,1.0) #3 YZ
points.InsertNextPoint(1.0,0.0,0.0) #4 X
points.InsertNextPoint(1.0,0.0,1.0) #5 XZ
points.InsertNextPoint(1.0,1.0,0.0) #6 XY
points.InsertNextPoint(1.0,1.0,1.0) #7 XYZ


cells = vtk.vtkCellArray()
cells.InsertNextCell(4, [0, 4, 6, 2])
cells.InsertNextCell(4, [0, 2, 3, 1])
cells.InsertNextCell(4, [0, 1, 5, 4])
cells.InsertNextCell(4, [2, 6, 7, 3])
cells.InsertNextCell(4, [4, 5, 7, 6])
cells.InsertNextCell(4, [5, 1, 3, 7])

scalars = vtk.vtkFloatArray()
for i in range (8):
   scalars.InsertTuple(i, (i,))


cube = vtk.vtkPolyData()
cube.SetPoints(points)
cube.SetPolys(cells)
cube.GetPointData().SetScalars(scalars)



#cube.SetVerts(cells)
#cube.SetLines(cells)



#cube.SetVerts()


mapp = vtk.vtkPolyDataMapper()
mapp.SetInputData(cube)
mapp.SetScalarRange(0,8)
actor = vtk.vtkActor()
actor.SetMapper(mapp)
ren.AddActor(actor)
renwin.AddRenderer(ren)
iren.Initialize()
renwin.Render()
iren.Start()


#topo = vtk.vtkCellArray()
#cube = vtk.vtkPolyData()

#cube.SetPoints()
#cube.SetVerts()
#cube.SetLines()
#cube.SetPolys()
#cube.SetStrips()

#pd = cube.GetCellData() #retrieve cell data
#pd = cube.GetPointData() #retrieve point data

#pd.SetScalars()

