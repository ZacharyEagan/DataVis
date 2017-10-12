import vtk

filename = "resources/bunny.obj"
filenameTea = "resources/teapot.obj"


#rendering setup
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()


#Axes
axes = vtk.vtkAxesActor()
ren.AddActor(axes)

#Sphere
sphere = vtk.vtkSphereSource()
sphere.SetCenter(2, 3, 4)
centerS = sphere.GetCenter()
sphereMap = vtk.vtkPolyDataMapper()
#print sphereMap.GetProperty()
sphereMap.SetInputConnection(sphere.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMap)
sprop = sphereActor.GetProperty()
sprop.SetColor(0.1,0.7,0.9)
ren.AddActor(sphereActor)

#objReader
objRead = vtk.vtkOBJReader()
objRead.SetFileName(filename)

teaRead = vtk.vtkOBJReader()
teaRead.SetFileName(filenameTea)

#light objects
light1 = vtk.vtkLight()
light1.PositionalOn()
light1.SetColor(0.2,0.6,0.9)
light1.SetPosition(1, 5, -20)
light1.SetFocalPoint(centerS)
light1.SetConeAngle(2)
ren.AddLight(light1)

#light objects
light3 = vtk.vtkLight()
#light3.PositionalOn()
light3.SetColor(0.1,1.0,0.2)
#light3.SetPosition(1, 5, -20)
#light3.SetFocalPoint(centerS)
#light3.SetConeAngle(2)
ren.AddLight(light3)

#light objects
light2 = vtk.vtkLight()
light2.PositionalOff()
light2.SetColor(1,0.6,0.2)
light2.SetPosition(10, 13, 15)
light2.SetFocalPoint(centerS)
light2.SetConeAngle(20)
ren.AddLight(light2)



#translation objects 
objTran = vtk.vtkTransform()
objTran.Translate(0.7, 0.0, 0.37)
objTran.Scale(10, 10, 10)
#objTran.Rotate(0.7, 0.0, 0.37)




#Note use the translation obj from now on data is read
obj = vtk.vtkTransformPolyDataFilter()
obj.SetInputConnection(objRead.GetOutputPort())
obj.SetTransform(objTran)
obj.Update()
#centerO = obj.GetCenter()

#light objects
#light1 = vtk.vtkLight()
#light1.PositionalOn()
#light1.SetColor(0.2,0.6,0.9)
#light1.SetPosition(1, 5, -20)
#light1.SetFocalPoint(centerO)
#light1.SetConeAngle(2)
#ren.AddLight(light1)



#maping pipeline to prep for rendering
objMap = vtk.vtkPolyDataMapper()
objMap.SetInputConnection(obj.GetOutputPort())
objActor = vtk.vtkActor()
prop = objActor.GetProperty()
print (prop)
#prop.SetRenderPointsAsSpheres(true)
prop.SetColor(1.0, 0.5, 0.1)
objActor.SetMapper(objMap)
ren.AddActor(objActor)


#maping pipeline to prep for rendering (teapot)
teaMap = vtk.vtkPolyDataMapper()
teaMap.SetInputConnection(teaRead.GetOutputPort())
teaActor = vtk.vtkActor()
prop1 = teaActor.GetProperty()
print (prop)
#prop1.SetShadingOn()
#prop.SetRenderPointsAsSpheres(true)
prop1.SetColor(1.0, 1.0, 1.0)
#objActor.SetMapper(teaMap)
#ren.AddActor(teaActor)


#rendering
renWin.AddRenderer(ren)
iren.SetRenderWindow(renWin)


#teacup = 

#axes widget
widg = vtk.vtkOrientationMarkerWidget()
#widg.SetOrientationMarker(teaActor)
widg.SetOrientationMarker(axes)
widg.SetInteractor(iren)
widg.SetEnabled(1)

#rendering start
iren.Initialize()
renWin.Render()
iren.Start()
