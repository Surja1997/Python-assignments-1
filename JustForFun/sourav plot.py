import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
import numpy as np

df = pd.read_excel('JAVA3_2.xls', 'Sheet1')
xaxis = df['A'].tolist()
yaxis = df['B'].tolist()
zaxis = df['C'].tolist()
print("dff",len(xaxis))

def stringToFloat(string):
    string2 = str(string).strip()
    if ' ' in string2:
        k = string2.split(' ')
        string2 = k[len(k) - 1]
    if 'E' in string2:
        k = string2.split('E')
        if len(k[1]) == 0:
            k[1]='0'
        if k[1][0] == '-':
            k[1] = k[1][1:]
            if len(k[1]) == 0:
                k[1] = '0'
            string2 = str(float(k[0]) / (10 ** float(k[1])))
        else:
            string2 = str(float(k[0]) * (10 ** float(k[1])))

    return string2


for i in range(len(xaxis)):
    xaxis[i] = float(stringToFloat(xaxis[i]))
    yaxis[i] = float(stringToFloat(yaxis[i]))
    zaxis[i] = float(stringToFloat(zaxis[i]))

# print(xaxis[0], yaxis[0], zaxis[0])
# ax.scatter3D(xaxis, yaxis, zaxis)
df2=pd.DataFrame(yaxis,columns=["column"])
df2.to_csv('newJAVA.csv',index=False)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xaxis, yaxis, zaxis, c='r', marker='o')
# ax.contour3D(xaxis, yaxis, zaxis, 50, cmap='binary')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()