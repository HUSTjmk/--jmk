# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Tue May 12 04:44:38 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=195.439361572266, 
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
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['Job-1'].setValues(description='origin')
#* 作业应当调用一个有效的模型.
mdb.jobs['Job-1'].setValues(description='origin')
#* 作业应当调用一个有效的模型.
mdb.jobs.changeKey(fromName='Job-1', toName='Origin')
mdb.jobs.changeKey(fromName='Job-2', toName='Lower-vireous-yangs')
del mdb.jobs['Origin']
del mdb.jobs['Lower-vireous-yangs']
mdb.Job(name='origin', model='origin', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, numCpus=1)
mdb.Job(name='lower-vitreous-yangs', model='assembly-improved', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=50, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, numCpus=1)
mdb.jobs['lower-vitreous-yangs'].submit(consistencyChecking=OFF)
#: 作业输入文件 "lower-vitreous-yangs.inp" 已提交分析.
mdb.jobs['origin'].submit(consistencyChecking=OFF)
#: 作业输入文件 "origin.inp" 已提交分析.
mdb.jobs['00057Mpa'].submit(consistencyChecking=OFF)
#: 作业输入文件 "00057Mpa.inp" 已提交分析.
mdb.jobs['001Mpa'].submit(consistencyChecking=OFF)
#: 作业输入文件 "001Mpa.inp" 已提交分析.
#: Job lower-vitreous-yangs: Analysis Input File Processor completed successfully.
#: Job origin: Analysis Input File Processor completed successfully.
#: Job 00057Mpa: Analysis Input File Processor completed successfully.
#: Job 001Mpa: Analysis Input File Processor completed successfully.
#: Job lower-vitreous-yangs: Abaqus/Explicit Packager completed successfully.
#: Job origin: Abaqus/Explicit Packager completed successfully.
#: Job 00057Mpa: Abaqus/Explicit Packager completed successfully.
#: Job 001Mpa: Abaqus/Explicit Packager completed successfully.
#: Error in job 00057Mpa: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Error in job 00057Mpa: There is only one excessively distorted element
#: Error in job 00057Mpa: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Job 00057Mpa: Abaqus/Explicit aborted due to errors.
#: Error in job 00057Mpa: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job 00057Mpa aborted due to errors.
#: Job origin: Abaqus/Explicit completed successfully.
#: Job origin completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.1775, 
    farPlane=71.6629, width=57.9768, height=29.3337, viewOffsetX=-2.0037, 
    viewOffsetY=-0.899269)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.8034, 
    farPlane=72.0371, width=57.5907, height=29.1383, viewOffsetX=2.40654, 
    viewOffsetY=-0.807327)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.1757, 
    farPlane=71.6648, width=57.9749, height=29.3327, viewOffsetX=2.35827, 
    viewOffsetY=-0.844626)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.8033, 
    farPlane=72.0371, width=57.5906, height=29.1383, viewOffsetX=0.877009, 
    viewOffsetY=-0.624144)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.1756, 
    farPlane=71.6648, width=64.1135, height=32.4385, viewOffsetX=0.121821, 
    viewOffsetY=-1.10029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.0834, 
    farPlane=72.7571, width=62.8669, height=31.8078, viewOffsetX=0.778233, 
    viewOffsetY=0.328529)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.3311, 
    farPlane=71.5093, width=56.8075, height=28.742, viewOffsetX=2.37898, 
    viewOffsetY=0.952902)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.9653, 
    farPlane=71.8752, width=56.4385, height=28.5554, viewOffsetX=0.420285, 
    viewOffsetY=1.57847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.3325, 
    farPlane=71.508, width=56.8089, height=28.7427, viewOffsetX=0.405489, 
    viewOffsetY=1.63863)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.9653, 
    farPlane=71.8752, width=56.4386, height=28.5554, viewOffsetX=1.92365, 
    viewOffsetY=-1.10966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.3195, 
    farPlane=71.5209, width=56.7959, height=28.7361, viewOffsetX=1.92593, 
    viewOffsetY=-1.13642)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.965, 
    farPlane=71.8754, width=56.4384, height=28.5553, viewOffsetX=1.78707, 
    viewOffsetY=0.765999)
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/origin.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/origin.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          5
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.9988, 
    farPlane=97.8764, width=40.8581, height=20.6723, viewOffsetX=0.455247, 
    viewOffsetY=0.522156)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.0697, 
    farPlane=96.8054, width=44.2827, height=22.405, viewOffsetX=0.411038, 
    viewOffsetY=0.0898142)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.7641, 
    farPlane=97.1111, width=44.0496, height=22.2871, viewOffsetX=0.903441, 
    viewOffsetY=-0.896815)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.3947, 
    farPlane=96.4805, width=41.8586, height=21.1786, viewOffsetX=0.232128, 
    viewOffsetY=-0.37488)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1022, 
    farPlane=96.773, width=41.6489, height=21.0725, viewOffsetX=5.43708, 
    viewOffsetY=1.95802)
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['origin'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['origin'].materials['vitreous'].elastic.setValues(table=((0.01, 
    0.49), ))
p = mdb.models['vitreous-yangs'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/origin.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job lower-vitreous-yangs: Abaqus/Explicit completed successfully.
#: Job lower-vitreous-yangs completed successfully. 
#: Job 001Mpa: Abaqus/Explicit completed successfully.
#: Job 001Mpa completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/001Mpa.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/001Mpa.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.0013, 
    farPlane=95.7709, width=33.016, height=16.7046, viewOffsetX=-0.177271, 
    viewOffsetY=2.46285)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.253, 
    farPlane=95.5192, width=33.1569, height=16.7759, viewOffsetX=3.54468, 
    viewOffsetY=1.65683)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9578, 
    farPlane=95.8144, width=37.3378, height=18.8912, viewOffsetX=3.60242, 
    viewOffsetY=1.16944)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.6909, 
    farPlane=96.0813, width=37.1688, height=18.8057, viewOffsetX=4.61549, 
    viewOffsetY=-0.194974)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.5055, 
    farPlane=96.2666, width=34.8283, height=17.6216, viewOffsetX=1.04458, 
    viewOffsetY=1.80519)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4988, 
    farPlane=95.2734, width=33.2944, height=16.8455, viewOffsetX=1.56347, 
    viewOffsetY=2.19703)
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['001Mpa']
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/001Mpa.odb'].close(
    )
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.1707, 
    farPlane=70.6697, width=46.0657, height=23.3071, viewOffsetX=1.47693, 
    viewOffsetY=1.78801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.3919, 
    farPlane=70.4486, width=46.2439, height=23.3973, viewOffsetX=7.12467, 
    viewOffsetY=4.79724)
mdb.Job(name='lower-vitreous-yangs-origin', model='origin', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=50, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, numCpus=1)
mdb.jobs['lower-vitreous-yangs-origin'].submit(consistencyChecking=OFF)
#: 作业输入文件 "lower-vitreous-yangs-origin.inp" 已提交分析.
#: Job lower-vitreous-yangs-origin: Analysis Input File Processor completed successfully.
#: Job lower-vitreous-yangs-origin: Abaqus/Explicit Packager completed successfully.
mdb.Job(name='assembly-improved', model='assembly-improved', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=50, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, numCpus=1)
#: Job lower-vitreous-yangs-origin: Abaqus/Explicit completed successfully.
#: Job lower-vitreous-yangs-origin completed successfully. 
mdb.jobs['assembly-improved'].submit(consistencyChecking=OFF)
#: 作业输入文件 "assembly-improved.inp" 已提交分析.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
#: Job assembly-improved: Analysis Input File Processor completed successfully.
#: Job assembly-improved: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].view.setValues(width=31.1581, height=15.7646, 
    viewOffsetX=1.41066, viewOffsetY=2.50342)
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs-origin.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs-origin.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          5
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.1027, 
    farPlane=95.7725, width=31.0927, height=15.7315, viewOffsetX=0.389993, 
    viewOffsetY=3.02271)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.2133, 
    farPlane=93.6618, width=18.4522, height=9.33597, viewOffsetX=0.267928, 
    viewOffsetY=5.17133)
odb = session.mdbData['assembly-improved']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.3756, 
    farPlane=105.659, width=38.7489, height=19.6052, viewOffsetX=0.325997, 
    viewOffsetY=1.99202)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4518, 
    farPlane=102.092, width=40.151, height=20.3146, cameraPosition=(25.4755, 
    6.91909, 78.0314), cameraUpVector=(-0.0370869, 0.903184, -0.427648), 
    cameraTarget=(3.995, -0.925449, -0.212322), viewOffsetX=0.337794, 
    viewOffsetY=2.0641)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#: 警告: Boundary conditions are shown in the local co-ordinate system, in which they were defined.
#: 警告: 选中的主变量在当前帧中对当前显示组中所有单元均不可用.
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5682, 
    farPlane=95.204, width=27.6861, height=14.0079, viewOffsetX=1.32577, 
    viewOffsetY=3.20336)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7302, 
    farPlane=93.042, width=16.5746, height=8.38598, viewOffsetX=-2.80836, 
    viewOffsetY=6.51417)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5996, 
    farPlane=93.1726, width=16.5395, height=8.36824, viewOffsetX=-0.586427, 
    viewOffsetY=5.59938)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.2984, 
    farPlane=93.4738, width=19.8157, height=10.0259, viewOffsetX=-0.985761, 
    viewOffsetY=5.2842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.1445, 
    farPlane=93.6277, width=19.766, height=10.0007, viewOffsetX=-0.199157, 
    viewOffsetY=4.29742)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.9665, 
    farPlane=93.8057, width=22.3047, height=11.2852, viewOffsetX=-0.0625451, 
    viewOffsetY=4.03885)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.7952, 
    farPlane=93.9769, width=22.2421, height=11.2535, viewOffsetX=0.886582, 
    viewOffsetY=5.43834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.2816, 
    farPlane=97.4906, width=49.8347, height=25.2141, viewOffsetX=-3.28213, 
    viewOffsetY=4.2391)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.9481, 
    farPlane=97.8241, width=49.5445, height=25.0673, viewOffsetX=1.37251, 
    viewOffsetY=1.55241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2393, 
    farPlane=95.5329, width=31.4159, height=15.895, viewOffsetX=2.43684, 
    viewOffsetY=3.77716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4808, 
    farPlane=95.2914, width=31.544, height=15.9598, viewOffsetX=1.50235, 
    viewOffsetY=1.36799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.9826, 
    farPlane=94.7896, width=26.421, height=13.3678, viewOffsetX=1.78529, 
    viewOffsetY=2.0994)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.1913, 
    farPlane=94.5809, width=26.5129, height=13.4143, viewOffsetX=1.59305, 
    viewOffsetY=4.36221)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9296, 
    farPlane=95.8477, width=35.3686, height=17.8949, cameraPosition=(8.42034, 
    -0.485438, 77.3394), cameraUpVector=(0.0135222, 0.999881, 0.00745175), 
    cameraTarget=(5.6022, 0.129004, 0.00711268), viewOffsetX=0.869428, 
    viewOffsetY=3.76573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.6747, 
    farPlane=96.1026, width=35.2156, height=17.8175, viewOffsetX=2.02547, 
    viewOffsetY=1.43685)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.695, 
    farPlane=96.0823, width=33.1141, height=16.7542, viewOffsetX=2.11182, 
    viewOffsetY=1.73723)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4756, 
    farPlane=95.3017, width=27.8698, height=14.1009, viewOffsetX=1.77823, 
    viewOffsetY=2.56635)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6938, 
    farPlane=95.0835, width=27.9721, height=14.1526, viewOffsetX=1.74288, 
    viewOffsetY=2.51314)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4536, 
    farPlane=95.1973, width=27.8595, height=14.0957, cameraPosition=(8.20701, 
    -1.7507, 77.2674), cameraUpVector=(0.00724595, 0.999689, 0.0238697), 
    cameraTarget=(5.62226, 0.114226, -0.0530552), viewOffsetX=1.73587, 
    viewOffsetY=2.50303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1366, 
    farPlane=96.5144, width=39.4893, height=19.9798, viewOffsetX=0.641623, 
    viewOffsetY=1.92702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.8581, 
    farPlane=96.7929, width=39.3001, height=19.8841, viewOffsetX=2.22703, 
    viewOffsetY=0.275441)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.483, 
    farPlane=95.168, width=26.201, height=13.2565, viewOffsetX=3.34875, 
    viewOffsetY=1.17711)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6899, 
    farPlane=94.9611, width=26.2921, height=13.3026, viewOffsetX=2.21898, 
    viewOffsetY=3.20211)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.371, 
    farPlane=94.455, width=22.2681, height=11.2666, cameraPosition=(10.189, 
    -1.79853, 77.2639), cameraUpVector=(0.0326649, 0.999189, 0.0235253), 
    cameraTarget=(5.47068, 0.173746, 0.046962), viewOffsetX=1.99599, 
    viewOffsetY=4.84525)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2002, 
    farPlane=94.6258, width=22.2051, height=11.2348, viewOffsetX=1.49173, 
    viewOffsetY=4.18529)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.1997, 
    farPlane=94.6263, width=22.205, height=11.2347, viewOffsetX=1.49172, 
    viewOffsetY=4.18526)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.35876, 
    viewOffsetY=4.06927)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3278, 
    farPlane=95.3568, width=22.2523, height=11.2586, cameraPosition=(9.38385, 
    4.52036, 77.6145), cameraUpVector=(-0.00668099, 0.998373, -0.0566208), 
    cameraTarget=(5.67408, 0.118886, 0.442724), viewOffsetX=1.36165, 
    viewOffsetY=4.07793)
a = mdb.models['vitreous-yangs'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job assembly-improved: Abaqus/Explicit completed successfully.
#: Job assembly-improved completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.064, 
    farPlane=95.7082, width=31.068, height=15.719, viewOffsetX=2.36304, 
    viewOffsetY=3.38119)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2336, 
    farPlane=94.5386, width=24.7367, height=12.5156, viewOffsetX=3.42767, 
    viewOffsetY=4.1242)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4986, 
    farPlane=95.2736, width=33.2943, height=16.8454, viewOffsetX=4.56639, 
    viewOffsetY=3.12524)
p = mdb.models['vitreous-yangs'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['origin'].materials['vitreous'].elastic.setValues(table=((0.42, 
    0.49), ))
a = mdb.models['origin'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['assembly-improved'].submit(consistencyChecking=OFF)
#: 作业输入文件 "assembly-improved.inp" 已提交分析.
#: Job assembly-improved: Analysis Input File Processor completed successfully.
#: Job assembly-improved: Abaqus/Explicit Packager completed successfully.
#: Job assembly-improved: Abaqus/Explicit completed successfully.
#: Job assembly-improved completed successfully. 
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['origin'].materials['vitreous'].elastic.setValues(table=((0.01, 
    0.49), ))
a = mdb.models['origin'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(width=47.9693, height=24.2703, 
    viewOffsetX=0.144385, viewOffsetY=0.431848)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.783, 
    farPlane=96.9892, width=44.058, height=22.2913, viewOffsetX=4.98031, 
    viewOffsetY=-2.29937)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.6903, 
    farPlane=97.0818, width=46.7951, height=23.6762, viewOffsetX=5.776, 
    viewOffsetY=-2.73112)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.3715, 
    farPlane=97.4007, width=46.5364, height=23.5453, viewOffsetX=2.60914, 
    viewOffsetY=-0.0767284)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.026, 
    farPlane=96.7462, width=44.2433, height=22.3851, viewOffsetX=3.9836, 
    viewOffsetY=-0.10837)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs-origin.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.996, 
    farPlane=95.8792, width=37.3672, height=18.9061, viewOffsetX=0.393885, 
    viewOffsetY=4.25331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.7292, 
    farPlane=96.146, width=37.1982, height=18.8206, viewOffsetX=3.06502, 
    viewOffsetY=0.875234)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4528, 
    farPlane=96.2035, width=28.2027, height=14.2693, viewOffsetX=1.4452, 
    viewOffsetY=2.93271)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1322, 
    farPlane=97.5526, width=39.9732, height=20.2246, viewOffsetX=1.16411, 
    viewOffsetY=1.61695)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
o7 = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.7488, 
    farPlane=96.9359, width=31.5401, height=15.9579, viewOffsetX=3.33346, 
    viewOffsetY=3.22613)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.1116, 
    farPlane=98.6606, width=58.5344, height=29.6158, viewOffsetX=5.64066, 
    viewOffsetY=7.633)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.7383, 
    farPlane=99.0339, width=58.145, height=29.4187, viewOffsetX=5.21143, 
    viewOffsetY=-5.43492)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9828, 
    farPlane=95.7894, width=33.1408, height=16.7677, viewOffsetX=2.51368, 
    viewOffsetY=-3.52334)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2352, 
    farPlane=95.537, width=33.2826, height=16.8395, viewOffsetX=3.0725, 
    viewOffsetY=1.7767)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.9874, 
    farPlane=96.7848, width=44.5764, height=22.5537, viewOffsetX=3.21428, 
    viewOffsetY=-0.391098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.6807, 
    farPlane=97.0915, width=44.3406, height=22.4343, viewOffsetX=5.58689, 
    viewOffsetY=-1.21625)
odb = session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.4929, 
    farPlane=98.1919, width=44.7415, height=22.6372, viewOffsetX=2.67212, 
    viewOffsetY=3.10165)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.1858, 
    farPlane=98.499, width=44.5025, height=22.5163, viewOffsetX=5.05619, 
    viewOffsetY=-1.23219)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.8764, 
    farPlane=97.8084, width=37.4095, height=18.9275, viewOffsetX=5.5913, 
    viewOffsetY=-0.324605)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1546, 
    farPlane=97.5302, width=37.5893, height=19.0185, viewOffsetX=5.11173, 
    viewOffsetY=1.94596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2268, 
    farPlane=96.458, width=31.7967, height=16.0877, viewOffsetX=5.28319, 
    viewOffsetY=3.09781)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9936, 
    farPlane=96.6912, width=31.6715, height=16.0244, viewOffsetX=2.89176, 
    viewOffsetY=5.0473)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.3838, 
    farPlane=99.301, width=53.0447, height=26.8382, viewOffsetX=6.08791, 
    viewOffsetY=2.98854)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.0304, 
    farPlane=99.6543, width=52.7122, height=26.67, viewOffsetX=5.3001, 
    viewOffsetY=-0.88515)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.4704, 
    farPlane=99.2144, width=46.9423, height=23.7507, viewOffsetX=5.20749, 
    viewOffsetY=0.266189)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.7944, 
    farPlane=98.8904, width=47.2116, height=23.8869, viewOffsetX=3.85918, 
    viewOffsetY=2.09975)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.1941, 
    farPlane=96.4906, width=32.0398, height=16.2107, viewOffsetX=3.49552, 
    viewOffsetY=5.32181)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9596, 
    farPlane=96.7252, width=31.9128, height=16.1465, viewOffsetX=3.29058, 
    viewOffsetY=-0.510104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.6722, 
    farPlane=97.0125, width=35.9409, height=18.1845, viewOffsetX=1.09645, 
    viewOffsetY=-0.747113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.4141, 
    farPlane=97.2706, width=35.7828, height=18.1045, viewOffsetX=1.89513, 
    viewOffsetY=2.08667)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.3897, 
    farPlane=97.2951, width=38.0509, height=19.2521, viewOffsetX=1.62263, 
    viewOffsetY=2.06706)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1194, 
    farPlane=97.5654, width=37.8748, height=19.1629, viewOffsetX=3.96811, 
    viewOffsetY=3.27283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9769, 
    farPlane=96.7079, width=30.007, height=15.1822, viewOffsetX=4.269, 
    viewOffsetY=3.44065)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.209, 
    farPlane=96.4757, width=30.1251, height=15.242, viewOffsetX=3.13582, 
    viewOffsetY=2.80225)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2102, 
    farPlane=96.4745, width=30.1258, height=15.2423, viewOffsetX=3.65452, 
    viewOffsetY=4.0163)
a = mdb.models['origin'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: 视口 "Viewport: 1" 的内容已复制到剪贴板.
mdb.models['origin'].materials['vitreous'].elastic.setValues(table=((0.42, 
    0.49), ))
a = mdb.models['origin'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['assembly-improved'].submit(consistencyChecking=OFF)
#: 作业输入文件 "assembly-improved.inp" 已提交分析.
mdb.jobs['assembly-improved'].kill()
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: 视口 "Viewport: 1" 的内容已复制到剪贴板.
#: Error in job assembly-improved: Process terminated by external request (SIGTERM or SIGINT received).
#: Job assembly-improved: Analysis Input File Processor was terminated prior to analysis completion.
p = mdb.models['vitreous-yangs'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: Error in job assembly-improved: Analysis Input File Processor exited with an error - Please see the  assembly-improved.dat file for possible error messages if the file exists.
p = mdb.models['vitreous-yangs'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['assembly-improved'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['origin'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['assembly-improved'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['assembly-improved'].materials['vitreous'].elastic.setValues(table=(
    (0.42, 0.49), ))
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['assembly-improved'].submit(consistencyChecking=OFF)
#: 作业输入文件 "assembly-improved.inp" 已提交分析.
p1 = mdb.models['assembly-improved'].parts['back-sclera']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: Job assembly-improved: Analysis Input File Processor completed successfully.
#: Job assembly-improved: Abaqus/Explicit Packager completed successfully.
a = mdb.models['assembly-improved'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job assembly-improved: Abaqus/Explicit completed successfully.
#: Job assembly-improved completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/study/research/articles/眼睛力学参数/simulation/axis-parted/lower-vitreous-yangs.odb'])
o3 = session.openOdb(
    name='E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb')
#: 模型: E:/study/research/articles/眼睛力学参数/simulation/axis-parted/assembly-improved.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     6
#: 网格数:             7
#: 单元集合数:       0
#: 结点集合数:          4
#: 分析步的个数:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(width=41.5131, height=21.0037, 
    viewOffsetX=5.61011, viewOffsetY=-0.983976)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(width=39.4476, height=19.9587, 
    viewOffsetX=5.18501, viewOffsetY=-0.594474)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UT', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.9014, 
    farPlane=97.8708, width=52.6636, height=26.6454, viewOffsetX=7.26019, 
    viewOffsetY=-3.35943)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis-parted\project.cae".
