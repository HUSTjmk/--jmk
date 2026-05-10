# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Sat May  9 06:23:09 2026
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
p = mdb.models['assembly-improved'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.4473, 
    farPlane=72.3932, width=52.7302, height=24.0474, viewOffsetX=0.295746, 
    viewOffsetY=1.14294)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = session.mdbData['assembly-improved']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.7035, 
    farPlane=107.331, width=48.3103, height=22.9162, viewOffsetX=-0.0964341, 
    viewOffsetY=1.18911)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.3968, 
    farPlane=105.638, width=49.7788, height=23.6128, cameraPosition=(37.1268, 
    21.2291, 72.1885), cameraUpVector=(-0.248158, 0.818143, -0.518709), 
    cameraTarget=(4.95485, -0.719521, 0.576581), viewOffsetX=-0.0993656, 
    viewOffsetY=1.22526)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.7275, 
    farPlane=105.307, width=44.238, height=20.9845, viewOffsetX=-2.33489, 
    viewOffsetY=2.51665)
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.mdbData['assembly-improved'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-3.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-3.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.2032, 
    farPlane=96.569, width=39.3154, height=18.6495, viewOffsetX=3.32386, 
    viewOffsetY=1.78289)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9998, 
    farPlane=95.7724, width=35.2146, height=16.7042, viewOffsetX=2.5148, 
    viewOffsetY=2.69982)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8103, 
    farPlane=93.9618, width=25.039, height=11.8774, viewOffsetX=-3.75911, 
    viewOffsetY=5.26018)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6311, 
    farPlane=94.1411, width=24.9652, height=11.8423, viewOffsetX=0.614301, 
    viewOffsetY=4.03948)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.8087, 
    farPlane=91.9635, width=9.03302, height=4.28485, viewOffsetX=-5.10333, 
    viewOffsetY=8.26116)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.7395, 
    farPlane=92.0327, width=9.02307, height=4.28014, viewOffsetX=-2.72322, 
    viewOffsetY=6.54127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.978, 
    farPlane=93.7942, width=23.6982, height=11.2413, viewOffsetX=-3.9074, 
    viewOffsetY=4.75961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8074, 
    farPlane=93.9648, width=23.6318, height=11.2099, viewOffsetX=-1.67424, 
    viewOffsetY=4.59749)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3138, 
    farPlane=92.4584, width=10.422, height=4.94373, viewOffsetX=-2.86902, 
    viewOffsetY=6.5016)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.5491, 
    farPlane=92.2231, width=10.4614, height=4.9624, viewOffsetX=-2.93858, 
    viewOffsetY=6.93603)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.6667, 
    farPlane=93.1055, width=18.1474, height=8.60831, viewOffsetX=-2.5951, 
    viewOffsetY=6.06318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5377, 
    farPlane=93.2345, width=18.1094, height=8.5903, viewOffsetX=-1.5857, 
    viewOffsetY=6.8107)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.2003, 
    farPlane=93.5719, width=21.8615, height=10.3701, viewOffsetX=-1.65143, 
    viewOffsetY=6.49561)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0486, 
    farPlane=93.7235, width=21.8073, height=10.3444, viewOffsetX=-0.805655, 
    viewOffsetY=3.90104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2725, 
    farPlane=94.4997, width=23.4398, height=11.1188, viewOffsetX=-0.558429, 
    viewOffsetY=3.74277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8035, 
    farPlane=93.9687, width=23.6463, height=11.2167, viewOffsetX=-0.148501, 
    viewOffsetY=6.24078)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8049, 
    farPlane=93.9673, width=23.6469, height=11.217, viewOffsetX=-0.878654, 
    viewOffsetY=5.28136)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.3197, 
    farPlane=93.4525, width=16.836, height=7.98622, viewOffsetX=-1.144, 
    viewOffsetY=5.57474)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.6919, 
    farPlane=93.0803, width=16.9382, height=8.0347, viewOffsetX=-0.88944, 
    viewOffsetY=6.61588)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.animationOptions.setValues(frameRate=56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.3414, 
    farPlane=93.4308, width=16.842, height=7.98907, viewOffsetX=-1.74208, 
    viewOffsetY=7.10452)
session.animationOptions.setValues(frameRate=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.8371, 
    farPlane=92.9351, width=15.0018, height=7.11618, viewOffsetX=-3.18178, 
    viewOffsetY=7.12269)
session.animationOptions.setValues(frameRate=44)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    sweepElem=ON, numSweepSegmentsElem=100)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.185, 
    farPlane=93.5872, width=20.2255, height=9.59408, viewOffsetX=-4.68842, 
    viewOffsetY=6.92584)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0372, 
    farPlane=93.735, width=20.1767, height=9.57091, viewOffsetX=-0.981571, 
    viewOffsetY=6.49974)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.9523, 
    farPlane=92.8199, width=12.4835, height=5.9216, viewOffsetX=-0.206091, 
    viewOffsetY=6.83016)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.3737, 
    farPlane=90.7371, width=16.1574, height=7.66433, viewOffsetX=-0.359249, 
    viewOffsetY=8.27447)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.116, 
    farPlane=90.9949, width=18.2233, height=8.64432, viewOffsetX=0.218796, 
    viewOffsetY=7.92859)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis-parted\project.cae".
