
from vtk import*
 
 
#Create a sphere
sphereSource =vtkSphereSource();
sphereSource.SetCenter(0.0, 0.0, 0.0);
sphereSource.SetRadius(10);
sphereSource.Update();
 
#Create a mapper and actor
mapper =vtkPolyDataMapper ();
mapper.SetInputConnection(sphereSource.GetOutputPort());
 
actor =vtkActor();
actor.SetMapper(mapper);
 
camera =vtkCamera ();
camera.SetPosition(0, 100,100);
camera.SetFocalPoint(0, 0, 0);
 
#Create a renderer, render window, and interactor
renderer =vtkRenderer();
renderer.SetActiveCamera(camera);
 
renderWindow =vtkRenderWindow();
renderWindow.AddRenderer(renderer);
renderWindowInteractor =vtkRenderWindowInteractor();
renderWindowInteractor.SetRenderWindow(renderWindow);
 
#Add the actor to the scene
renderer.AddActor(actor);
renderer.SetBackground(0.5,0.5,1); # Background color white
 
#Render and interact
renderWindow.Render();
renderWindowInteractor.Start();
