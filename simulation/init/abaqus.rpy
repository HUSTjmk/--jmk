# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Thu May  7 18:40:59 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=213.629180908203, 
    height=129.362701416016)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('initial.cae')
#: 模型数据库 "E:\study\research\articles\眼睛力学参数\simulation\init\initial.cae" 已打开.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.6576, 
    farPlane=141.445, width=81.595, height=37.0805, cameraPosition=(2.66182, 
    93.0825, 122.637), cameraUpVector=(-0.315498, 0.19873, -0.927883), 
    cameraTarget=(-4.86117, -0.247784, 65.8696))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.8139, 
    farPlane=145.817, width=78.5681, height=35.705, cameraPosition=(87.0275, 
    58.7481, 70.4047), cameraUpVector=(-0.484321, 0.20135, -0.851406), 
    cameraTarget=(-5.20601, -0.107442, 66.0831))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-6', 
    material='back-sclera-material', thickness=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.6088, 
    farPlane=144.315, width=80.4787, height=36.5732, cameraPosition=(93.5715, 
    41.06, 42.8206), cameraUpVector=(-0.625981, 0.18876, -0.756649), 
    cameraTarget=(-5.18706, -0.158665, 66.0032))
session.viewports['Viewport: 1'].view.setValues(nearPlane=78.2523, 
    farPlane=141.988, width=83.2924, height=37.8519, cameraPosition=(70.7208, 
    32.4006, -5.96989), cameraUpVector=(-0.909481, 0.206741, -0.360698), 
    cameraTarget=(-5.28358, -0.195241, 65.7971))
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.0974, 
    farPlane=141.143, width=69.9285, height=31.7787, viewOffsetX=1.10027, 
    viewOffsetY=-1.0072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.9333, 
    farPlane=140.82, width=70.6675, height=32.1146, cameraPosition=(82.9397, 
    24.3964, 5.29713), cameraUpVector=(-0.824655, 0.117516, -0.553294), 
    cameraTarget=(-5.17748, -0.324662, 65.4128), viewOffsetX=1.1119, 
    viewOffsetY=-1.01784)
