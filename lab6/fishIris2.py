#Credit: this program is largly the creation of Chris Conlan
#url: https://chrisconlan.com/visualizing-data-blender-python/

#I wont be coppying directly from the site, rather I will use it as a reference when I am stuck without instruction on how to proceded. However since the requirements for this project are in essence "copy this site" the results will likely be very very similar.  

import bpy  #blender python api

sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
iris_species = []

with  open("iris.csv", "r") as iris_file:
   for line in iris_file:
      data = line.split(",")
#      print len(data)
      if len(data) == 5:
#      print data
         sepal_length.append(float(data[0]))
         sepal_width.append(float(data[1]))
         petal_length.append(float(data[2]))
         petal_width.append(float(data[3]))
         iris_species.append(data[4])

width_sum = 0;
for petal in petal_width:
   width_sum += petal;
width_av = width_sum / len(petal_width)

petal_dict = {}
for iris in iris_species:
   petal_dict[iris] = petal_dict.get(iris,0) + 1
print (petal_dict)
   

scale = 0.01

for i in range(len(iris_species)):
   if iris_species[i] == list(petal_dict.keys())[0 % len(petal_dict)]:
      bpy.ops.mesh.primitive_uv_sphere_add(location=(sepal_length[i], sepal_width[i], petal_length[i]))
   if iris_species[i] == list(petal_dict.keys())[1 % len(petal_dict)]:
      bpy.ops.mesh.primitive_cube_add(location=(sepal_length[i], sepal_width[i], petal_length[i]))
   if iris_species[i] == list(petal_dict.keys())[2 % len(petal_dict)]:
      bpy.ops.mesh.primitive_cone_add(location=(sepal_length[i], sepal_width[i], petal_length[i]))
   if iris_species[i] == list(petal_dict.keys())[3 % len(petal_dict)]:
      bpy.ops.mesh.primitive_torus_add(location=(sepal_length[i], sepal_width[i], petal_length[i]))

   print("math")
   print (petal_width[i] / width_av)
   print ("width")
   print (width_av)
   print ("thiswidth")
   print(petal_width[i])
   bpy.ops.transform.resize(value=(petal_width[i]**0.5*scale,)*3)
   bpy.context.object.name = iris_species[i] + "-at_row-" + str(i)

      




   
