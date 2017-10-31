import os
import numpy
import vtk


#path to the .mha file 
filenameSegmentation = "./data/brain_segmentation.mha"

#path to colorfile.txt
filenameColorfile = "./data/colorfile.txt"

#opacity of the different volumes (between 0.0 and 1.0)
volOpacityDef = 0.25

reader = vtk.vtkMetaImageReader()
reader.SetFileName(filenameSegmentation)

castFilter = vtk.vtkImageCast()
castFilter.SetInputConnection(reader.GetOutputPort())
castFilter.SetOutputScalarTypeToUnsignedShort()
castFilter.Update()

imdataBrainSeg = castFilter.GetOutput()

import csv
fid = open(filenameColorfile, "r")
reader = csv.reader(fid)
dictRGB = {}
for line in reader:
   dictRGB[int(line[0])] = [float(line[2])/255.0, float(line[3])/255.0,float(line[4])/255.0]
fid.close()

funcColor = vtk.vtkColorTransferFunction()

for idx in dictRGB.keys():
   funcColor.AddRGBPoint(idx, dictRGB[idx][0], dictRGB[idx][1],dictRGB[idx][2])


funcOpacityScalar = vtk.vtkPiecewiseFunction()

for idx in dictRGB.keys():
   funcOpacityScalar.AddPoint(idx, volOpacityDef if idx<>0 else 0.0)

funcOpacityGradient = vtk.vtkPiecewiseFunction()

funcOpacityGradient.AddPoint(1, 0.0)
funcOpacityGradient.AddPoint(5, 0.1)
funcOpacityGradient.AddPoint(100, 1.0)

propVolume = vtk.vtkVolumeProperty()
propVolume.ShadeOff()
propVolume.SetColor(funcColor)
propVolume.SetScalarOpacity(funcOpacityScalar)
propVolume.SetGradientOpacity(funcOpacityGradient)
propVolume.SetInterpolationTypeToLinear()




#section gets overwritten later on
funcRayCast = vtk.vtkVolumeRayCastCompositeFunction()
funcRayCast.SetCompositeMethodToClassifyFirst()
#mapperVolume = vtk.vtkVolumeRayCastMapper()
mapperVolume = vtk.vtkVolumeTextureMapper2D()
#mapperVolume = vtk.vtkSmartVolumeMapper()
#mapperVolume.SetVolumeRayCastFunction(funcRayCast)

mapperVolume.SetInputData(imdataBrainSeg)

actorVolume = vtk.vtkVolume()
actorVolume.SetMapper(mapperVolume)
actorVolume.SetProperty(propVolume)






#funcRayCast = vtk.vtkVolumeRayCastCompositeFunction()
#funcRayCast.SetCompositeMethodToClassifyFirst()

#mapperVolume = vtk.vtkVolumeRayCastMapper()
#mapperVolume.SetVolumeRayCastFunction(funcRayCast)
#mapperVolume.SetInputData(imdataBrainSeg)


#actorVolume = vtk.vtkVolume()
#actorVolume.SetMapper(mapperVolume)
#actorVolume.SetProperty(propVolume)


##end clipping




renderer = vtk.vtkRenderer()
renderer.AddActor(actorVolume)
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()
renWin.AddRenderer(renderer)
iren.SetRenderWindow(renWin)



###clipping
_origin = numpy.array(imdataBrainSeg.GetOrigin())
_spacing = numpy.array(imdataBrainSeg.GetSpacing())
_dims = numpy.array(imdataBrainSeg.GetDimensions())
_center = numpy.array(_origin+_spacing*(_dims/2.0))
planeClip = vtk.vtkPlane()
#planeClip = vtk.vtkPlane()
planeClip.SetOrigin(_center)
planeClip.SetNormal(0.0,0.0,-1.0)

mapperVolume.AddClippingPlane(planeClip)


iren.Initialize()
renWin.Render()
iren.Start()


