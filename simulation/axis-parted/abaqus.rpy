# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Fri May  8 21:52:37 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=213.427062988281, 
    height=129.362701416016)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('project.cae')
#: 模型数据库 "E:\study\research\articles\眼睛力学参数\simulation\axis-parted\project.cae" 已打开.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.603, 
    farPlane=71.3273, width=58.5748, height=27.7853, viewOffsetX=-0.224878, 
    viewOffsetY=-0.100174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.2692, 
    farPlane=71.661, width=58.2295, height=27.6214, viewOffsetX=3.16806, 
    viewOffsetY=2.58923)
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-2.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-2.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          5
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.8302, 
    farPlane=96.045, width=35.1182, height=16.6585, viewOffsetX=0.685318, 
    viewOffsetY=2.21553)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.3719, 
    farPlane=93.5032, width=18.5485, height=8.79855, viewOffsetX=-1.30893, 
    viewOffsetY=5.34684)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7971, 
    farPlane=93.078, width=17.5564, height=8.32794, viewOffsetX=-1.16099, 
    viewOffsetY=5.54415)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7975, 
    farPlane=93.0777, width=15.5129, height=7.35861, viewOffsetX=-1.1333, 
    viewOffsetY=5.7444)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.9192, 
    farPlane=92.9559, width=15.5434, height=7.37311, viewOffsetX=-0.448344, 
    viewOffsetY=6.90844)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.6534, 
    farPlane=93.2218, width=18.6335, height=8.83891, viewOffsetX=-0.851355, 
    viewOffsetY=7.13646)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].materials['vitreous'].elastic.setValues(table=((0.42, 
    0.49), ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: 作业输入文件 "Job-1.inp" 已提交分析.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-2.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          5
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.2355, 
    farPlane=96.6396, width=39.3427, height=18.6624, viewOffsetX=0.854644, 
    viewOffsetY=0.795922)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.248, 
    farPlane=94.6272, width=29.8716, height=14.1697, viewOffsetX=0.532512, 
    viewOffsetY=2.78513)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.0386, 
    farPlane=94.8366, width=29.7677, height=14.1205, viewOffsetX=2.16005, 
    viewOffsetY=6.08688)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6806, 
    farPlane=94.1946, width=23.4897, height=11.1425, viewOffsetX=1.61242, 
    viewOffsetY=6.77044)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8585, 
    farPlane=94.0166, width=23.5586, height=11.1751, viewOffsetX=0.707871, 
    viewOffsetY=6.06507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.5602, 
    farPlane=94.315, width=24.3698, height=11.5599, viewOffsetX=0.663757, 
    viewOffsetY=5.93614)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.animationOptions.setValues(frameRate=43)
session.animationOptions.setValues(frameRate=63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.9332, 
    farPlane=96.9419, width=37.9608, height=18.0069, viewOffsetX=5.47021, 
    viewOffsetY=3.90791)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.6578, 
    farPlane=96.2173, width=38.4356, height=18.2321, viewOffsetX=6.61752, 
    viewOffsetY=2.39711)
session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
    compass=OFF, timeScale=1, frameRate=9)
session.writeImageAnimation(fileName='porcine-0.42Mpa', format=AVI, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.1296, 
    farPlane=93.7456, width=20.2799, height=9.61986, viewOffsetX=1.36799, 
    viewOffsetY=6.17447)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.animationOptions.setValues(frameRate=34)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=HARMONIC)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationOptions.setValues(mode=PLAY_ONCE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0758, 
    farPlane=93.7994, width=19.0463, height=9.03472, viewOffsetX=1.04175, 
    viewOffsetY=6.43295)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5112, 
    farPlane=93.3639, width=15.9324, height=7.55759, viewOffsetX=0.540269, 
    viewOffsetY=8.13644)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.1497, 
    farPlane=94.7255, width=25.6631, height=12.1734, viewOffsetX=3.79524, 
    viewOffsetY=5.66661)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3404, 
    farPlane=94.5348, width=24.2988, height=11.5263, viewOffsetX=2.68147, 
    viewOffsetY=5.00976)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.5148, 
    farPlane=94.3603, width=22.9069, height=10.866, viewOffsetX=2.25995, 
    viewOffsetY=5.69062)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=24, maxValue=0.0160743, minValue=-0.588417)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0406, 
    farPlane=93.8345, width=21.7196, height=10.3028, viewOffsetX=1.90551, 
    viewOffsetY=5.79924)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    numIntervals=25, timeMarks=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: 作业输入文件 "Job-1.inp" 已提交分析.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          5
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.9919, 
    farPlane=97.8832, width=43.5746, height=20.6698, viewOffsetX=-0.758121, 
    viewOffsetY=0.647048)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.3133, 
    farPlane=95.5619, width=33.2822, height=15.7875, viewOffsetX=-0.520995, 
    viewOffsetY=2.49394)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.4824, 
    farPlane=94.3927, width=24.9074, height=11.8149, viewOffsetX=0.0688075, 
    viewOffsetY=3.92917)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.2141, 
    farPlane=93.6611, width=19.6817, height=9.33609, viewOffsetX=0.18119, 
    viewOffsetY=4.95423)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=16, maxValue=0.0160685, minValue=-0.684652)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=15)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5102, 
    farPlane=93.365, width=19.7769, height=9.38125, viewOffsetX=0.182067, 
    viewOffsetY=4.97819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.3657, 
    farPlane=93.5094, width=19.7304, height=9.35922, viewOffsetX=0.749321, 
    viewOffsetY=6.26409)
session.viewports['Viewport: 1'].view.setValues(width=18.5465, height=8.79763, 
    viewOffsetX=0.707365, viewOffsetY=6.4206)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.1991, 
    farPlane=93.676, width=19.6769, height=9.33382, viewOffsetX=1.01274, 
    viewOffsetY=7.04047)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
#: 
#: 部件实例: cornea-1
#:  四边形 elements:  323
#:    Min angle on Quad Faces < 10:  0 (0%)
#:    平均 min angle on quad faces:  80.75,  最差 min angle on quad faces:  32.56
#:    Max angle on Quad faces > 160:  0 (0%)
#:    平均 max angle on quad faces:  99.41,  最差 max angle on quad faces:  138.89
#:    长宽比 > 10:  0 (0%)
#:    平均 长宽比:  1.20,  最差 长宽比:  2.75
#:  三角形 elements:  8
#:    Min angle on Tri Faces < 5:  0 (0%)
#:    平均 min angle on tri faces:  41.40,  最差 min angle on tri faces:  21.19
#:    Max angle on Tri faces > 170:  0 (0%)
#:    平均 max angle on tri faces:  75.55,  最差 max angle on tri faces:  89.12
#:    长宽比 > 10:  0 (0%)
#:    平均 长宽比:  1.62,  最差 长宽比:  2.75
#:   Number of elements :  331,   Analysis errors:  0 (0%),  Analysis warnings:  0 (0%)
#: 
#: 部件实例: cornea-1
#:  四边形 elements:  323
#:    Min angle on Quad Faces < 10:  0 (0%)
#:    平均 min angle on quad faces:  80.75,  最差 min angle on quad faces:  32.56
#:    Max angle on Quad faces > 160:  0 (0%)
#:    平均 max angle on quad faces:  99.41,  最差 max angle on quad faces:  138.89
#:    长宽比 > 10:  0 (0%)
#:    平均 长宽比:  1.20,  最差 长宽比:  2.75
#:  三角形 elements:  8
#:    Min angle on Tri Faces < 5:  0 (0%)
#:    平均 min angle on tri faces:  41.40,  最差 min angle on tri faces:  21.19
#:    Max angle on Tri faces > 170:  0 (0%)
#:    平均 max angle on tri faces:  75.55,  最差 max angle on tri faces:  89.12
#:    长宽比 > 10:  0 (0%)
#:    平均 长宽比:  1.62,  最差 长宽比:  2.75
#:    形状因子 < 0.01:  0 (0%)
#:    平均 形状因子:  0.832250,  最差 形状因子:  0.534828
#:   Number of elements :  331,   Analysis errors:  0 (0%),  Analysis warnings:  0 (0%)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.3609, 
    farPlane=68.5693, width=36.7614, height=16.7648, viewOffsetX=-1.13415, 
    viewOffsetY=10.4613)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.1107, 
    farPlane=68.8195, width=36.6064, height=16.6942, viewOffsetX=1.7301, 
    viewOffsetY=5.71716)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis-parted\project.cae".
