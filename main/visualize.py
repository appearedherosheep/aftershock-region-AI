from model import PolyLR, LongMinorAxis
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import folium

경주 = 5.8
포항 = 5.4
# region = PolyLR(경주)[0][0]
model = PolyLR()
region = model.predict([[포항]])
print(region)
a, b = LongMinorAxis(region)
print(a,b)

X = np.array([1, 10])
Y = np.array([1, 10])
plt.plot(X, Y, color='None')
shp = patches.Ellipse((15, 15), a, b, angle=45)
plt.gca().add_patch(shp)
plt.show()

m = folium.Map(location=[129.2247477, 35.8561719])
m
