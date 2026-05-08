# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Fri May  8 13:16:29 2026
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
del mdb.jobs['Job-1']
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, numCpus=1)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF, datacheckJob=True)
#: 作业输入文件 "Job-1.inp" 已提交分析.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: 作业输入文件 "Job-1.inp" 已提交分析.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
#: Error in job Job-1: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Error in job Job-1: There is only one excessively distorted element
#: Error in job Job-1: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-1: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Job Job-1: Abaqus/Explicit aborted due to errors.
#: Error in job Job-1: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.447, 
    farPlane=72.3935, width=52.8784, height=24.0472, viewOffsetX=-2.63378, 
    viewOffsetY=0.817155)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
del a.features['Coincident Point-5']
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.5472, 
    farPlane=70.2932, width=45.5836, height=20.7298, viewOffsetX=-2.53575, 
    viewOffsetY=1.61342)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.8541, 
    farPlane=69.9864, width=45.8266, height=20.8403, viewOffsetX=-0.426776, 
    viewOffsetY=6.27102)
#: 警告: 无法继续--请完成该步骤或取消这一操作.
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6906, 
    farPlane=67.1499, width=25.8931, height=11.7753, viewOffsetX=-0.49314, 
    viewOffsetY=10.4959)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.5059, 
    farPlane=67.3346, width=25.8143, height=11.7394, viewOffsetX=-1.23437, 
    viewOffsetY=0.89182)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0657, 
    farPlane=66.7748, width=20.341, height=9.25035, viewOffsetX=-1.39442, 
    viewOffsetY=1.62652)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.2221, 
    farPlane=66.6183, width=20.3931, height=9.27405, viewOffsetX=0.0474146, 
    viewOffsetY=8.10826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.6896, 
    farPlane=71.1509, width=57.7497, height=26.2626, viewOffsetX=4.68169, 
    viewOffsetY=5.48807)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.3357, 
    farPlane=71.5048, width=57.3892, height=26.0986, viewOffsetX=5.69956, 
    viewOffsetY=13.1228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3422, 
    farPlane=65.4983, width=11.2307, height=5.10735, viewOffsetX=-2.41703, 
    viewOffsetY=10.4402)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('touch-len-1', ), vector=(0.0, 2.2, 0.0))
#: The instance touch-len-1 was translated by 0., 2.2, 0. (相对于装配坐标系)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.5216, 
    farPlane=65.3189, width=9.95204, height=4.52584, viewOffsetX=-2.38765, 
    viewOffsetY=10.6491)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.602, 
    farPlane=65.2385, width=9.96483, height=4.53166, viewOffsetX=-2.45365, 
    viewOffsetY=11.4994)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.3595, 
    farPlane=64.481, width=3.98668, height=1.813, viewOffsetX=-3.96563, 
    viewOffsetY=11.7153)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('touch-len-1', ), vector=(0.0, -0.210173, 0.0))
#: The instance touch-len-1 was translated by 0., -210.173E-03, 0. (相对于装配坐标系)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.1432, 
    farPlane=67.6973, width=24.0009, height=10.9148, viewOffsetX=-0.365914, 
    viewOffsetY=13.4307)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.7134, 
    farPlane=67.1271, width=24.2284, height=11.0182, viewOffsetX=1.6199, 
    viewOffsetY=8.25231)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5026, 
    farPlane=66.3379, width=17.2204, height=7.83124, viewOffsetX=0.52545, 
    viewOffsetY=8.08928)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.637, 
    farPlane=66.2035, width=17.258, height=7.84835, viewOffsetX=0.0784953, 
    viewOffsetY=11.1376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.2314, 
    farPlane=65.6091, width=12.0206, height=5.46655, viewOffsetX=-0.705616, 
    viewOffsetY=11.2131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3275, 
    farPlane=65.5129, width=12.0392, height=5.475, viewOffsetX=-1.97399, 
    viewOffsetY=11.6432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.9408, 
    farPlane=64.8997, width=6.96628, height=3.16802, viewOffsetX=-3.30107, 
    viewOffsetY=11.1979)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.9978, 
    farPlane=64.8426, width=6.97259, height=3.17089, viewOffsetX=-3.1377, 
    viewOffsetY=11.5691)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('touch-len-1', ), vector=(0.0, 0.02, 0.0))
#: The instance touch-len-1 was translated by 0., 20.E-03, 0. (相对于装配坐标系)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.997, 
    farPlane=64.8434, width=7.41756, height=3.37325, viewOffsetX=-3.04069, 
    viewOffsetY=11.5515)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.9399, 
    farPlane=64.9006, width=7.41083, height=3.37019, viewOffsetX=-2.7935, 
    viewOffsetY=11.4114)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.9987, 
    farPlane=64.8418, width=6.55433, height=2.98068, viewOffsetX=-3.21752, 
    viewOffsetY=11.4456)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Press')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: 作业输入文件 "Job-1.inp" 已提交分析.
#: Job Job-1: Analysis Input File Processor completed successfully.
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb')
#* OdbError: 输出数据库 
#* E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb 的 
#* .lck 文件显示 Analysis Input File Processor 目前正在修改数据库. 
#* 这时数据库无法打开.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__edit__', 
    objectToCopy=mdb.models['Model-1'].sketches['back-sclera'])
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.1996, 
    farPlane=34.9917, width=25.6717, height=12.1775, cameraPosition=(5.99702, 
    -7.3122, 31.5956), cameraTarget=(5.99702, -7.3122, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/Job-1.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       2
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.2343, 
    farPlane=96.6379, width=39.3426, height=18.6624, viewOffsetX=1.60414, 
    viewOffsetY=0.742927)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8349, 
    farPlane=95.0373, width=31.561, height=14.9711, viewOffsetX=1.28121, 
    viewOffsetY=2.52077)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6578, 
    farPlane=94.2144, width=24.9801, height=11.8494, viewOffsetX=-0.241683, 
    viewOffsetY=3.72787)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8348, 
    farPlane=95.0374, width=31.5609, height=14.9711, viewOffsetX=2.77396, 
    viewOffsetY=2.68869)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis-parted\project.cae".
