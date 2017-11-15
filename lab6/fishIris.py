#Credit: this program is largly the creation of Chris Conlan
#url: https://chrisconlan.com/visualizing-data-blender-python/

#I wont be coppying directly from the site, rather I will use it as a reference when I am stuck without instruction on how to proceded. However since the requirements for this project are in essence "copy this site" the results will likely be very very similar.  

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
         sepal_length.append(data[0])
         sepal_width.append(data[1])
         petal_length.append(data[2])  
         petal_width.append(data[3])
         iris_species.append(data[4])
   for flower in iris_species:
      print (flower)
