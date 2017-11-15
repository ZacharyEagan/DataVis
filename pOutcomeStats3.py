import vtk
import numpy as np
import scipy.io as sio
import glob
import os
from vtk.util.numpy_support import vtk_to_numpy
from vtk.util.numpy_support import numpy_to_vtk




MIN = 0.0
MAX = 0.0
MEAN = 0.0

#Generates a renderer ready volume from a mat file
def readAvgChangeMatrices(filename):
   mat = sio.loadmat(filename)
   arr = mat['curStack']
   return arr
 
def arrNULLS_AV(arr):
   arp = np.ma.masked_less_equal(arr, np.min(arr))
   aved = np.mean(arp, axis=1)

   return aved

def arrtoImg(data_matrix):
   img = vtk.vtkImageData()
        
   img.SetDimensions(120, 120, 120)
   img.AllocateScalars(vtk.VTK_FLOAT, 1)
   img.SetOrigin(-30.000000, -15.000000, -30.000000)
   img.SetSpacing(.252101, .252101, .252101)
    
   #arr is a vtk.vtkFloatArray()
   data_matrix.filled(-255)
   arr = numpy_to_vtk(num_array=data_matrix.reshape(120*120*120, order='C'), \
            deep=True, array_type=vtk.VTK_FLOAT)
   arr.SetName('ImageScalars')
   img.GetPointData().AddArray(arr)   
   return img

def transferFunc(img, minn,maxx,mean, funcColor, funcOpacityGradient):
   #funcColor = vtk.vtkColorTransferFunction()
   #funcColor.AddRGBPoint(0, 0, 0, 0)
   #funcColor.AddRGBPoint(1, 255, 0, 0)
   #funcColor.AddRGBPoint(2, 0, 255, 0)
   #funcColor.AddRGBPoint(3, 0, 0, 255)
   
   #funcColor.AddRGBPoint(0, 0, 0, 0)
   funcColor.AddRGBPoint(minn, 255, 0, 0)
   funcColor.AddRGBPoint(mean, 0, 255, 0)
   funcColor.AddRGBPoint(maxx, 0, 0, 255)
 
   funcOpacityScalar = vtk.vtkPiecewiseFunction()
   funcOpacityScalar.AddPoint(0, 0)
   funcOpacityScalar.AddPoint(1, 0.25)
   funcOpacityScalar.AddPoint(2, 0.25)
   funcOpacityScalar.AddPoint(3, 0.25)

#   funcOpacityGradient = vtk.vtkPiecewiseFunction() 
   funcOpacityGradient.AddPoint(minn - 1, 0.0)
   funcOpacityGradient.AddPoint(minn, 0.0)
   funcOpacityGradient.AddPoint(mean, 0.1)
   funcOpacityGradient.AddPoint(maxx, 0.2)
	
   propVolume = vtk.vtkVolumeProperty()
   propVolume.ShadeOff()
   propVolume.SetColor(funcColor)
   propVolume.SetScalarOpacity(funcOpacityScalar)
   propVolume.SetGradientOpacity(funcOpacityGradient)
   propVolume.SetInterpolationTypeToLinear()

   funcRayCast = vtk.vtkVolumeRayCastCompositeFunction()
   funcRayCast.SetCompositeMethodToClassifyFirst()
   mapperVolume = vtk.vtkSmartVolumeMapper()
   mapperVolume.SetInputData(img)

   actorVolume = vtk.vtkVolume()
   actorVolume.SetMapper(mapperVolume)
   actorVolume.SetProperty(propVolume)


   return actorVolume

#numpy mask => NULL; AVg on 4th axis, NULLS not invisible, MIN MAX MEAN
#NULL => -wjhatevs some constant, color function, opacity function: numpy array.filled(filled_value = whatevs) else to 1 to sliders 
def mapVolume(img):
   mapperVolume = vtk.vtkSmartVolumeMapper()
   mapperVolume.SetInputData(img)
   actorVolume = vtk.vtkVolume()
   actorVolume.SetMapper(mapperVolume)
   renderer = vtk.vtkRenderer()
   renderer.AddActor(actorVolume)
   return renderer

#Grabs all mat type files in a directory and adds them to a renderer
def allMat(dirName, ren):
   for files in os.listdir(dirName):
      if (files.endswith(".mat")):
         print ("Loading: " + files)
         volume = readAvgChangeMatrices(dirName + "/" + files)
         ren.AddVolume(volume)
         
#Generates a renderer ready actor from an stl
def setupSTL(filename):
   rdr = vtk.vtkSTLReader()
   rdr.SetFileName(filename);
   mapper = vtk.vtkPolyDataMapper()
   if vtk.VTK_MAJOR_VERSION <= 5:
      mapper.SetInput(rdr.GetOutputPort())
   else:
      mapper.SetInputConnection(rdr.GetOutputPort())
   actor = vtk.vtkActor()
   actor.SetMapper(mapper)
   return actor

#Add Thalimous
def thalSTL():
   renSTL = vtk.vtkRenderer()
   actor = setupSTL("NucleiSurfaces/thalamus2LCenteredAWDiff.stl")
   return actor

   
#Grabs all stl files in a directory and adds them to a renderer
def allSTL(dirName, ren):
   for files in os.listdir(dirName):
      if (files.endswith(".stl")):
         print("Loading: " + files)
         ren.AddActor(setupSTL(dirName +  "/" + files))
 

def vtkSliderCallback2(obj, event):
   sliderRepres = obj.GetRepresentation()
   pos = sliderRepres.GetValue()
   contourFilter.SetValue(0, pos)

def xyChart(color, opac):
   view = vtk.vtkContextView()
   view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
   view.GetRenderWindow().SetSize(400, 300)

   chart = vtk.vtkChartXY()
   view.GetScene().AddItem(chart)
   chart.SetShowLegend(True)
   table = vtk.vtkTable()

   tranItem = vtk.vtkCompositeTransferFunctionItem()
   tranItem.SetOpacityFunction(opac)
   tranItem.SetColorTransferFunction(color)
   tranItem.SetMaskAboveCurve(True) 
   chart.AddPlot(tranItem)
   
   controlItem = vtk.vtkCompositeControlPointsItem()
   controlItem.SetOpacityFunction(opac)
   controlItem.SetColorTransferFunction(color)
   chart.AddPlot(controlItem)

   view.GetRenderWindow().SetMultiSamples(0)
   view.GetInteractor().Initialize()
   return view

    


def setSlider(iren):
   SRep = vtk.vtkSliderRepresentation2D()
   minn = 0
   maxx = 256
   SRep.SetMinimumValue(minn)
   SRep.SetMaximumValue(maxx)
   SRep.SetTitleText("apples")
   SRep.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay() 
   SRep.GetPoint1Coordinate().SetValue(0.2,0.6)
   SRep.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay() 
   SRep.GetPoint2Coordinate().SetValue(0.4,0.6)
   
   SRep.SetSliderLength(0.02)
   SRep.SetSliderWidth(0.03)
   SRep.SetEndCapLength(0.01)
   SRep.SetEndCapLength(0.03)
   SRep.SetTubeWidth(0.03)
   SRep.SetLabelFormat("%3.01f")
   SRep.SetTitleHeight(0.02)
   SRep.SetLabelHeight(0.02) 
       
   SliderWidget = vtk.vtkSliderWidget()
   SliderWidget.SetInteractor(iren)
   SliderWidget.SetRepresentation(SRep)
   SliderWidget.KeyPressActivationOff()
   SliderWidget.SetAnimationModeToAnimate()
   SliderWidget.SetEnabled(True)
   SliderWidget.AddObserver("EndInteractionEvent", vtkSliderCallback2)

if __name__ == '__main__':
   renWin = vtk.vtkRenderWindow()    
   iren = vtk.vtkRenderWindowInteractor()
   iren.SetRenderWindow(renWin)
   ren = vtk.vtkRenderer()
   
   #ren.AddActor(thalSTL())
   allSTL("NucleiSurfaces", ren)
 
   data = readAvgChangeMatrices("AverageChangeMatrices/Bradykinesia.mat")
   data_aved = arrNULLS_AV(data) 
   img = arrtoImg(data_aved)
   MIN = np.min(data_aved)
   MAX = np.max(data_aved)
   MEAN = np.mean(data_aved)
   funcColor = vtk.vtkColorTransferFunction()
   funcOpacityGradient = vtk.vtkPiecewiseFunction() 
   tran = transferFunc(img, MIN,MEAN,MAX,funcColor,funcOpacityGradient)
   ren.AddActor(tran)
 
   view = xyChart(funcColor, funcOpacityGradient)



   renWin.AddRenderer(ren)
   renWin.SetWindowName("Results Refference")

   #view.GetInteractor().Start()
   renWin.Render()
   iren.Initialize()
   iren.Start() 
