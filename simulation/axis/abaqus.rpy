# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-21.00.46 RELr427 198590
# Run by Administrator on Thu May  7 20:33:25 2026
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
openMdb('axis.cae')
#: 模型数据库 "E:\study\research\articles\眼睛力学参数\simulation\axis\axis.cae" 已打开.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.5603, 
    farPlane=67.8044, width=43.8055, height=19.9073, viewOffsetX=2.8976, 
    viewOffsetY=2.5399)
mdb.models['porcine-eye'].parts['eye'].setValues(geometryRefinement=EXTRA_FINE)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis\axis.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.506, 
    farPlane=66.8586, width=37.0035, height=16.8161, viewOffsetX=3.89334, 
    viewOffsetY=3.325)
p = mdb.models['porcine-eye'].parts['eye']
s = p.features['Shell planar-1'].sketch
mdb.models['porcine-eye'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['porcine-eye'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.4639, 
    farPlane=60.3544, width=59.9146, height=28.4009, cameraPosition=(4.25356, 
    -2.45207, 52.9091), cameraTarget=(4.25356, -2.45207, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(10.64, 11.2457, 
    52.9091), cameraTarget=(10.64, 11.2457, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(10.8081, 
    16.6913, 52.9091), cameraTarget=(10.8081, 16.6913, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.4638, 
    farPlane=60.3544, width=52.9406, height=25.095, cameraPosition=(10.1873, 
    16.1598, 52.9091), cameraTarget=(10.1873, 16.1598, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(10.9669, 
    10.0896, 52.9091), cameraTarget=(10.9669, 10.0896, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.2558, 
    farPlane=56.5624, width=23.49, height=11.1348, cameraPosition=(6.46464, 
    11.5515, 52.9091), cameraTarget=(6.46464, 11.5515, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(5.7069, 
    11.1409, 52.9091), cameraTarget=(5.7069, 11.1409, 0))
s1.ArcByCenterEnds(center=(0.0, 11.7813968658447), point1=(0.0, 15.0), point2=(
    1.90171480178833, 13.7193098068237), direction=CLOCKWISE)
s1.CoincidentConstraint(entity1=v[20], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[18], entity2=g[2], addUndoState=False)
s1.Line(point1=(0.0, 15.0), point2=(0.0, 14.1791524887085))
s1.VerticalConstraint(entity=g[17], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)
s1.CoincidentConstraint(entity1=v[21], entity2=g[2], addUndoState=False)
s1.Line(point1=(2.25433988439387, 14.0786469220696), point2=(2.25433988439387, 
    13.42369556427))
s1.VerticalConstraint(entity=g[18], addUndoState=False)
s1.ObliqueDimension(vertex1=v[19], vertex2=v[22], textPoint=(3.713707447052, 
    14.1298847198486), value=1.0)
s1.ObliqueDimension(vertex1=v[18], vertex2=v[21], textPoint=(-2.03525114059448, 
    13.9984998703003), value=1.0)
s1.RadialDimension(curve=g[16], textPoint=(2.77476644515991, 15.5586843490601), 
    radius=10.0)
#: 视口 "Viewport: 1" 的内容已复制到剪贴板.
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.8473, 
    farPlane=62.9709, width=71.5455, height=33.9141, cameraPosition=(5.91021, 
    5.2164, 52.9091), cameraTarget=(5.91021, 5.2164, 0))
s1.DistanceDimension(entity1=v[19], entity2=g[2], textPoint=(1.04350852966309, 
    16.9212760925293), value=6.0)
s1.Arc3Points(point1=(0.0, 20.7813968658447), point2=(6.0, 18.7813968658447), 
    point3=(2.5, 20.0))
s1.RadialDimension(curve=g[19], textPoint=(-4.07404899597168, 
    12.2193174362183), radius=10.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.3843, 
    farPlane=59.4339, width=46.3956, height=21.9926, cameraPosition=(5.93259, 
    10.0076, 52.9091), cameraTarget=(5.93259, 10.0076, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6.45315, 
    15.5544, 52.9091), cameraTarget=(6.45315, 15.5544, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.07133, 
    17.8899, 52.9091), cameraTarget=(7.07133, 17.8899, 0))
session.viewports['Viewport: 1'].view.setValues(width=43.6119, height=20.673, 
    cameraPosition=(5.76145, 17.9639, 52.9091), cameraTarget=(5.76145, 17.9639, 
    0))
s1.CoincidentConstraint(entity1=v[21], entity2=v[2])
s1.undo()
session.viewports['Viewport: 1'].view.setValues(width=46.3956, height=21.9926, 
    cameraPosition=(5.46728, 18.2303, 52.9091), cameraTarget=(5.46728, 18.2303, 
    0))
s1.FixedConstraint(entity=v[2])
s1.CoincidentConstraint(entity1=v[2], entity2=v[21])
s1.undo()
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.3947, 
    farPlane=56.4235, width=24.9894, height=11.8455, cameraPosition=(4.1973, 
    16.5046, 52.9091), cameraTarget=(4.1973, 16.5046, 0))
s1.dragEntity(entity=v[21], points=((0.0, 20.7813968658447), (0.0, 
    20.7813968658447), (0.0, 21.25), (0.0, 21.25), (0.0, 21.5189018249512), (
    0.0, 21.6412010192871), (0.0, 21.25), (0.0, 21.25), (0.0, 21.25), (
    0.377045631408691, 21.25), (0.359521865844727, 21.25), (0.27190113067627, 
    20.7326946258545), (0.0, 20.4531536102295), (0.0, 20.4356822967529), (
    0.341997146606445, 20.5754528045654), (0.359521865844727, 
    20.6278667449951)))
s1.dragEntity(entity=v[21], points=((0.0, 20.6278667449951), (0.0, 
    20.6278667449951), (0.0, 20.9074077606201), (0.0, 21.25), (0.0, 21.25), (
    0.0, 20.7676372528076), (0.0, 20.5230388641357), (0.0, 20.4182109832764), (
    0.0, 20.6453380584717), (0.0, 20.8375225067139), (0.0, 21.25), (
    0.306949615478516, 21.25), (0.377045631408691, 21.25), (0.341997146606445, 
    21.25), (0.341997146606445, 20.8200511932373), (0.341997146606445, 
    20.592924118042), (0.341997146606445, 20.4007396697998), (
    0.341997146606445, 20.3832683563232)))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.1551, 
    farPlane=56.6631, width=30.2096, height=14.32, cameraPosition=(4.98697, 
    15.5829, 52.9091), cameraTarget=(4.98697, 15.5829, 0))
s1.dragEntity(entity=v[18], points=((0.0, 21.6278667449951), (0.0, 
    21.6278667449951), (0.0, 22.00364112854), (0.0, 22.5), (0.0, 22.5)))
session.viewports['Viewport: 1'].view.setValues(width=32.1379, height=15.2341, 
    cameraPosition=(5.24127, 15.3239, 52.9091), cameraTarget=(5.24127, 15.3239, 
    0))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.1551, 
    farPlane=56.6631, width=26.6932, height=12.6532, cameraPosition=(5.37865, 
    15.1445, 52.9091), cameraTarget=(5.37865, 15.1445, 0))
s1.delete(objectList=(g[2], g[16], g[17], g[18], g[19], d[1], d[2], d[3], d[4], 
    c[39], c[40], c[41], c[44]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.9782, 
    farPlane=55.84, width=20.8407, height=9.87895, cameraPosition=(4.64979, 
    14.9207, 52.9091), cameraTarget=(4.64979, 14.9207, 0))
s1.ArcByCenterEnds(center=(-0.012336254119873, 14.5272455215454), point1=(
    0.0753521919250488, 18.2864952087402), point2=(2.35526084899902, 
    17.2519721984863), direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.0045, 
    farPlane=53.8137, width=6.43194, height=3.04888, cameraPosition=(1.5766, 
    17.2229, 52.9091), cameraTarget=(1.5766, 17.2229, 0))
s1.delete(objectList=(g[20], ))
session.viewports['Viewport: 1'].view.setValues(width=6.84249, height=3.24349, 
    cameraPosition=(1.59963, 17.2361, 52.9091), cameraTarget=(1.59963, 17.2361, 
    0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(1.13419, 
    15.2555, 52.9091), cameraTarget=(1.13419, 15.2555, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(1.45088, 
    12.7248, 52.9091), cameraTarget=(1.45088, 12.7248, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(1.45568, 
    12.1651, 52.9091), cameraTarget=(1.45568, 12.1651, 0))
s1.rectangle(point1=(0.0, 11.3398206853892), point2=(0.846285939216614, 
    11.8063068389893))
s1.delete(objectList=(g[23], ))
s1.delete(objectList=(g[22], ))
s1.delete(objectList=(g[24], ))
s1.delete(objectList=(g[21], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.9468, 
    farPlane=53.8714, width=7.74387, height=3.67077, cameraPosition=(1.59658, 
    12.2311, 52.9091), cameraTarget=(1.59658, 12.2311, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2.15049, 
    11.1536, 52.9091), cameraTarget=(2.15049, 11.1536, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.0588, 
    farPlane=53.7594, width=6.04602, height=2.86595, cameraPosition=(1.93064, 
    11.3871, 52.9091), cameraTarget=(1.93064, 11.3871, 0))
s1.ArcByCenterEnds(center=(0.00151455402374268, 11.5181884765625), point1=(0.0, 
    12.5), point2=(0.620532035827637, 12.2410163879395), direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.2452, 
    farPlane=53.573, width=4.72042, height=2.23759, cameraPosition=(1.56002, 
    11.5821, 52.9091), cameraTarget=(1.56002, 11.5821, 0))
s1.Line(point1=(0.640143035890557, 12.2639161906627), point2=(
    0.640143035890557, 12.0837144851685))
s1.VerticalConstraint(entity=g[26], addUndoState=False)
s1.Line(point1=(0.0, 12.5), point2=(0.0, 12.3081331253052))
s1.VerticalConstraint(entity=g[27], addUndoState=False)
s1.ObliqueDimension(vertex1=v[31], vertex2=v[33], textPoint=(0.970795392990112, 
    12.17942237854), value=1.0)
s1.ObliqueDimension(vertex1=v[30], vertex2=v[34], textPoint=(
    -0.445994019508362, 12.3444366455078), value=1.0)
s1.RadialDimension(curve=g[25], textPoint=(0.835074901580811, 
    12.5490531921387), radius=10.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.2029, 
    farPlane=53.6153, width=5.02173, height=2.38041, cameraPosition=(1.60277, 
    11.5387, 52.9091), cameraTarget=(1.60277, 11.5387, 0))
s1.DistanceDimension(entity1=v[31], entity2=g[27], textPoint=(
    0.158933281898499, 12.1390733718872), value=6.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.9421, 
    farPlane=55.8761, width=21.0975, height=10.0007, cameraPosition=(3.61271, 
    11.7115, 52.9091), cameraTarget=(3.61271, 11.7115, 0))
s1.dragEntity(entity=v[30], points=((0.0, 12.5), (0.0, 12.5), (0.0, 
    12.9947643280029), (0.0, 13.1570177078247), (0.0, 13.3192710876465), (0.0, 
    13.5110244750977), (0.0, 13.75), (0.0, 14.2337894439697), (0.0, 15.0), (
    -0.233970880508423, 15.4285621643066), (-0.233970880508423, 
    15.7530689239502), (0.0, 15.6793174743652), (0.0, 15.5760650634766), (0.0, 
    15.5760650634766), (0.239466428756714, 15.6498165130615), (0.0, 
    15.5908164978027), (0.0, 15.5318145751953), (0.0, 15.6203155517578), (0.0, 
    15.7973194122314), (0.0, 15.9300727844238)))
session.viewports['Viewport: 1'].view.setValues(width=22.4442, height=10.639, 
    cameraPosition=(3.37662, 11.9713, 52.9091), cameraTarget=(3.37662, 11.9713, 
    0))
s1.dragEntity(entity=v[31], points=((6.0, 7.79862417872368), (6.0, 
    7.79862417872368), (6.25, 8.20531272888184), (6.25, 8.40930557250977), (
    6.25, 8.75), (6.00507354736328, 8.75), (5.97359466552734, 
    9.00559425354004), (5.95785427093506, 9.22527980804443), (5.95785427093506, 
    9.39788913726807), (5.95785427093506, 9.58619117736816), (6.25, 10.0), (
    6.25, 10.0), (6.25, 10.4335479736328), (6.25, 10.6846170425415), (6.25, 
    10.919994354248), (6.25, 11.25), (6.25, 11.25), (6.25, 11.25), (
    6.60316467285156, 11.5319747924805), (6.729079246521, 11.6261253356934), (
    6.88647174835205, 11.7516593933105), (6.96516799926758, 11.8458108901978), 
    (7.01238536834717, 11.9870367050171), (7.05960273742676, 12.0968799591064), 
    (6.68186092376709, 11.9085779190063), (6.25, 11.7830429077148), (6.25, 
    11.7045841217041), (6.25, 11.5476665496826), (6.00507354736328, 11.25), (
    6.25, 11.5633583068848), (6.25, 11.7359676361084), (6.25, 
    11.8458108901978), (5.94211578369141, 11.8771934509277), (5.989333152771, 
    11.8144273757935), (5.989333152771, 11.7359676361084), (5.95785427093506, 
    11.6418170928955)))
s1.dragEntity(entity=v[34], points=((-0.0421457290649396, 15.3359721971318), (
    0.0, 15.3359721971318), (0.0, 15.0), (0.0, 15.0)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.7527, 
    farPlane=56.0655, width=22.4442, height=10.639, cameraPosition=(3.57113, 
    12.5072, 52.9091), cameraTarget=(3.57113, 12.5072, 0))
s1.Arc3Points(point1=(0.0, 15.0), point2=(6.0, 10.3058448957637), point3=(
    3.36651921272278, 13.6056251525879))
s1.RadialDimension(curve=g[28], textPoint=(3.71278214454651, 16.4458427429199), 
    radius=10.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.7527, 
    farPlane=56.0655, width=25.4009, height=12.0406, cameraPosition=(3.69938, 
    13.2507, 52.9091), cameraTarget=(3.69938, 13.2507, 0))
s1.dragEntity(entity=g[28], points=((1.41715991743249, 14.4849729895532), (
    1.25, 14.5293045043945), (1.52623534202576, 15.0), (1.54404902458191, 
    15.0), (1.54404902458191, 15.3106985092163), (1.54404902458191, 
    15.5238056182861), (1.25, 15.70139503479), (1.25, 15.8079490661621), (1.25, 
    15.8257074356079), (0.974043607711792, 15.736912727356), (
    0.724666357040405, 15.6126003265381), (0.564352750778198, 
    15.4705286026001), (0.404038190841675, 15.0), (0.653415441513062, 
    15.3462162017822), (0.867168188095093, 15.3994932174683), (1.25, 
    15.4705286026001), (1.25, 15.3994932174683), (1.25, 15.0), (1.25, 15.0), (
    0.920605421066284, 15.0), (0.84935450553894, 14.4582691192627), (
    0.920605421066284, 14.3517150878906), (0.93841814994812, 14.1563663482666), 
    (1.25, 13.75), (1.25, 13.75), (1.25, 13.4104909896851), (1.25, 
    13.161865234375), (1.25, 12.9132404327393), (1.63311171531677, 12.5), (
    1.82905077934265, 12.5), (1.9537398815155, 12.5), (2.07842898368835, 12.5), 
    (2.5, 12.1318464279175), (2.5, 11.9542570114136), (2.91562342643738, 
    11.7766666412354), (3.07593703269958, 11.7411499023438), (3.21843791007996, 
    11.6523551940918), (3.75, 11.25), (3.75, 11.25), (4.05563449859619, 11.25), 
    (3.75, 11.25), (3.75, 11.25), (3.41437792778015, 11.7056312561035), (
    3.18281435966492, 11.8832206726074), (2.89781069755554, 12.0075340270996), 
    (2.87999892234802, 12.0963287353516), (3.09374976158142, 12.2028818130493), 
    (3.25406336784363, 12.5), (3.43219065666199, 12.5)))
s1.dragEntity(entity=g[27], points=((-0.213277228033456, 13.7123928070068), (
    0.0, 13.75), (0.0, 13.75), (0.0, 14.0853309631348), (0.0, 
    14.2806797027588), (0.0, 14.3161964416504)))
s1.dragEntity(entity=g[28], points=((3.90236641886405, 12.2727879392438), (
    3.75, 12.5), (3.75, 12.0963287353516), (3.75, 11.9187393188477), (3.75, 
    11.8832206726074), (3.75, 12.0785694122314), (3.75, 12.5), (3.75, 12.5), (
    3.75, 12.5), (3.75, 12.8066864013672), (4.07344627380371, 12.966516494751), 
    (4.35844993591309, 13.161865234375), (4.44751262664795, 13.250659942627), (
    4.59001350402832, 13.446008682251), (5.0, 13.75), (5.0, 14.0853309631348), 
    (5.49845886230469, 14.4405097961426), (5.87252521514893, 15.0), (6.25, 
    15.3284568786621), (6.25, 15.5238056182861), (6.25, 15.70139503479), (6.25, 
    15.8257074356079), (6.25, 16.25), (5.94377613067627, 16.25), (
    5.9081506729126, 16.25), (6.25, 16.5893421173096), (6.25, 
    16.7491722106934), (6.62065696716309, 16.8734855651855), (6.76315879821777, 
    16.9445209503174), (6.97691059112549, 16.9800395965576), (7.15503787994385, 
    16.9977989196777), (7.5, 16.9977989196777), (7.5, 16.9977989196777), (7.5, 
    16.9445209503174), (7.5, 16.8379669189453), (7.17284870147705, 
    16.7846908569336), (6.94128513336182, 16.6426200866699), (6.65628242492676, 
    16.25), (6.25, 16.25), (6.25, 16.25), (6.25, 16.25), (6.25, 16.25), (
    6.58503150939941, 16.5183067321777), (6.7275333404541, 16.5893421173096), (
    6.56721878051758, 16.25), (6.25, 16.25), (6.25, 16.25), (5.83689975738525, 
    16.25), (5.73002433776855, 16.25), (5.56971073150635, 15.9677791595459), (
    5.28470706939697, 15.8257074356079), (5.0, 15.7724313735962), (5.0, 
    15.6836357116699), (5.0, 15.6303596496582), (4.59001350402832, 
    15.5770826339722), (4.25157260894775, 15.5593233108521), (3.75, 
    15.6126003265381), (3.75, 15.70139503479), (3.21843791007996, 
    15.8079490661621), (3.02249979972839, 15.9500198364258), (2.77312254905701, 
    16.25), (2.5, 16.25), (2.5, 16.553825378418), (1.98936533927917, 
    16.6958961486816), (1.81123805046082, 16.7491722106934), (1.61529898643494, 
    16.8734855651855), (1.25, 16.9800395965576), (1.25, 17.033317565918), (
    1.25, 17.0688343048096), (1.25, 17.0155563354492), (1.57967448234558, 
    16.9445209503174), (1.73998808860779, 16.7846908569336), (1.88248896598816, 
    16.6603775024414), (1.77561354637146, 16.5893421173096), (1.59748721122742, 
    16.6248607635498), (1.25, 16.7491722106934), (1.61529898643494, 
    16.7136554718018), (1.54404902458191, 16.6603775024414), (1.63311171531677, 
    16.6603775024414)))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.3369, 
    farPlane=56.4813, width=28.747, height=13.6267, cameraPosition=(3.69505, 
    13.7221, 52.9091), cameraTarget=(3.69505, 13.7221, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4.98524, 
    9.86324, 52.9091), cameraTarget=(4.98524, 9.86324, 0))
s1.CoincidentConstraint(entity1=v[32], entity2=g[27])
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.3369, 
    farPlane=56.4813, width=25.4009, height=12.0406, cameraPosition=(4.89516, 
    9.42758, 52.9091), cameraTarget=(4.89516, 9.42758, 0))
s1.dragEntity(entity=g[28], points=((1.13041105394115, 12.7611152310275), (
    1.25, 12.5), (1.68887805938721, 13.1036777496338), (2.00950622558594, 
    13.4410972595215), (2.20544528961182, 13.75), (2.5, 13.75), (2.5, 13.75), (
    2.5, 13.75), (2.5, 13.75), (1.97388172149658, 13.75), (1.70669078826904, 
    13.4410972595215), (1.528564453125, 13.3523025512695), (1.25, 
    13.2812671661377), (1.25, 13.1747131347656), (0.922934532165527, 
    13.1036777496338), (1.25, 13.1747131347656), (0.833870887756348, 
    13.42333984375), (0.816058158874512, 13.75), (0.887309074401855, 13.75), (
    0.976371765136719, 13.75), (0.86949634552002, 13.75), (1.25, 13.75), (1.25, 
    13.75), (1.25, 13.3523025512695), (1.25, 13.2102317810059), (
    0.887309074401855, 13.032642364502), (1.25, 13.1036777496338), (1.25, 
    13.1036777496338)))
s1.dragEntity(entity=g[27], points=((0.11958894605885, 13.4410982131958), (0.0, 
    13.4410972595215), (0.0, 13.75)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3337, 
    farPlane=57.4845, width=36.8198, height=17.4534, cameraPosition=(5.98545, 
    10.9555, 52.9091), cameraTarget=(5.98545, 10.9555, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.30229, 
    5.42083, 52.9091), cameraTarget=(7.30229, 5.42083, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.66377, 
    6.78518, 52.9091), cameraTarget=(7.66377, 6.78518, 0))
s1.dragEntity(entity=v[35], points=((5.29261871334786, 11.6523598971727), (5.0, 
    11.6523598971727), (5.0, 11.8821887969971), (4.53951025009155, 
    11.9851570129395), (4.38458776473999, 12.5), (4.33294725418091, 12.5), (
    3.75, 12.5), (3.75, 12.5), (3.3259539604187, 12.5), (3.09357213973999, 
    12.937629699707), (2.88700914382935, 13.0405988693237), (2.5, 
    13.2722816467285), (2.88700914382935, 13.75), (3.14521169662476, 13.75), (
    3.75, 13.75), (3.75, 13.75), (3.75, 13.1950540542603), (3.75, 
    13.1435689926147), (3.75, 13.0663414001465), (3.75, 13.0405988693237)))
d[8].setValues(textPoint=(0.0, 12.9118871688843))
s1.dragEntity(entity=g[27], points=((0.114944862275509, 14.199010848999), (0.0, 
    14.1990098953247), (0.0, 13.75)))
s1.CoincidentConstraint(entity1=g[27], entity2=g[6])
s1.CoincidentConstraint(entity1=g[25], entity2=v[33])
session.viewports['Viewport: 1'].view.setValues(width=34.6106, height=16.4062, 
    cameraPosition=(7.73813, 7.15433, 52.9091), cameraTarget=(7.73813, 7.15433, 
    0))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.3779, 
    farPlane=58.4403, width=44.5113, height=21.0994, cameraPosition=(7.87005, 
    5.53456, 52.9091), cameraTarget=(7.87005, 5.53456, 0))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.7957, 
    farPlane=60.0225, width=57.2443, height=27.1351, cameraPosition=(9.35092, 
    3.32934, 52.9091), cameraTarget=(9.35092, 3.32934, 0))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0008, 
    farPlane=58.8174, width=42.0118, height=19.9145, cameraPosition=(8.77633, 
    5.49424, 52.9091), cameraTarget=(8.77633, 5.49424, 0))
s1.CoincidentConstraint(entity1=g[27], entity2=g[6])
s1.undo()
s1.CoincidentConstraint(entity1=g[6], entity2=g[27])
s1.undo()
s1.CoincidentConstraint(entity1=g[27], entity2=g[6])
s1.undo()
s1.undo()
s1.undo()
s1.undo()
s1.undo()
s1.undo()
s1.CoincidentConstraint(entity1=v[32], entity2=g[6])
s1.CoincidentConstraint(entity1=g[27], entity2=v[2])
s1.undo()
s1.undo()
s1.undo()
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.2225, 
    farPlane=59.5957, width=47.5462, height=22.538, cameraPosition=(8.92769, 
    4.67007, 52.9091), cameraTarget=(8.92769, 4.67007, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(9.82794, 
    7.89453, 52.9091), cameraTarget=(9.82794, 7.89453, 0))
s1.undo()
#* 没有可撤销的操作.
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0008, 
    farPlane=58.8174, width=47.5462, cameraPosition=(10.3621, 8.50086, 
    52.9091), cameraTarget=(10.3621, 8.50086, 0))
s1.unsetPrimaryObject()
del mdb.models['porcine-eye'].sketches['__edit__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.7901, 
    farPlane=66.5745, width=34.9582, height=15.8866, viewOffsetX=3.90681, 
    viewOffsetY=3.94719)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.0389, 
    farPlane=66.3257, width=35.1114, height=15.9562, viewOffsetX=2.22499, 
    viewOffsetY=2.66344)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.0179, 
    farPlane=66.3467, width=37.3388, height=16.9685, viewOffsetX=1.93667, 
    viewOffsetY=2.75635)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['porcine-eye'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
    point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['porcine-eye'].parts['eye']
a.Instance(name='eye-1', part=p, dependent=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.5122, 
    farPlane=69.8524, width=65.0613, height=29.5668, viewOffsetX=-1.34591, 
    viewOffsetY=-0.487092)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.0262, 
    farPlane=70.3695, width=64.4703, height=29.2983, cameraPosition=(4.93353, 
    -0.278222, 61.6925), cameraUpVector=(-0.0118997, 0.999916, -0.00522259), 
    cameraTarget=(5.66396, -0.591671, 0.0153436), viewOffsetX=-1.33369, 
    viewOffsetY=-0.482668)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.1471, 
    farPlane=70.2202, width=64.6174, height=29.3651, cameraPosition=(5.62436, 
    -0.631723, 61.6836), cameraUpVector=(-0.0100809, 0.999949, 0.00059419), 
    cameraTarget=(5.66529, -0.594658, 0.00136997), viewOffsetX=-1.33673, 
    viewOffsetY=-0.483768)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['porcine-eye'].rootAssembly
partInstances =(a.instances['eye-1'], )
a.seedPartInstance(regions=partInstances, size=0.77, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['porcine-eye'].rootAssembly
partInstances =(a.instances['eye-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.0354, 
    farPlane=69.3318, width=61.7556, height=28.1435, viewOffsetX=0.703741, 
    viewOffsetY=-0.0836256)
a = mdb.models['porcine-eye'].rootAssembly
partInstances =(a.instances['eye-1'], )
a.deleteMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.3279, 
    farPlane=69.0394, width=58.3644, height=26.6168, viewOffsetX=1.1095, 
    viewOffsetY=0.219903)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.2079, 
    farPlane=70.3969, width=57.1612, height=26.0681, cameraPosition=(11.0816, 
    1.18063, 61.539), cameraUpVector=(-0.00729034, 0.999577, -0.0281394), 
    cameraTarget=(5.66954, -0.587861, 0.120128), viewOffsetX=1.08663, 
    viewOffsetY=0.21537)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.4721, 
    farPlane=67.8925, width=49.4977, height=22.5732, viewOffsetX=2.41543, 
    viewOffsetY=3.31426)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
dxf = mdb.openDxf('E:/study/research/touch-len.DXF', scaleFromFile=OFF)
mdb.models['porcine-eye'].ConstrainedSketchFromGeometryFile(name='touch-len', 
    geometryFile=dxf)
#: 警告: 栅格中心被移至草稿中心.
#: sketch "touch-len" 已从 "E:/study/research/touch-len.DXF" 导入.
p1 = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['porcine-eye'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.retrieveSketch(sketch=mdb.models['porcine-eye'].sketches['touch-len'])
session.viewports['Viewport: 1'].view.fitView()
#: 提示: 4 个实体已从 touch-len 复制.
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.0562, 
    farPlane=14.7766, width=10.9385, height=5.18873, cameraPosition=(4.46652, 
    8.3256, 13.4164), cameraTarget=(4.46652, 8.3256, 0))
p = mdb.models['porcine-eye'].Part(name='touch-len', 
    dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = mdb.models['porcine-eye'].parts['touch-len']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['porcine-eye'].parts['touch-len']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['porcine-eye'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.6294, 
    farPlane=15.3591, width=10.918, height=4.96513, viewOffsetX=0.904166, 
    viewOffsetY=0.365993)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.2486, 
    farPlane=70.3561, width=61.0276, height=27.7532, viewOffsetX=-0.477816, 
    viewOffsetY=-0.43923)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.8138, 
    farPlane=73.5412, width=57.091, height=25.963, cameraPosition=(14.7206, 
    12.4193, 59.6024), cameraUpVector=(-0.028173, 0.977528, -0.208913), 
    cameraTarget=(5.66191, -0.581795, -0.00970113), viewOffsetX=-0.446995, 
    viewOffsetY=-0.410897)
session.viewports['Viewport: 1'].view.setValues(width=54.1566, height=24.6285, 
    viewOffsetX=-0.639086, viewOffsetY=-0.269546)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.1081, 
    farPlane=70.3382, width=55.06, height=25.0393, viewOffsetX=10.4324, 
    viewOffsetY=-7.43476)
a1 = mdb.models['porcine-eye'].rootAssembly
p = mdb.models['porcine-eye'].parts['touch-len']
a1.Instance(name='touch-len-1', part=p, dependent=OFF)
p1 = a1.instances['touch-len-1']
p1.translate(vector=(0.0, 7.38982068537817, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.2251, 
    farPlane=82.0066, width=22.7373, height=10.3401, viewOffsetX=-2.87687, 
    viewOffsetY=5.42901)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.0585, 
    farPlane=82.1732, width=22.6841, height=10.3159, viewOffsetX=-1.78767, 
    viewOffsetY=10.5743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72.6017, 
    farPlane=80.63, width=10.3685, height=4.71522, viewOffsetX=-3.80524, 
    viewOffsetY=11.9637)
a1 = mdb.models['porcine-eye'].rootAssembly
v11 = a1.instances['eye-1'].vertices
v12 = a1.instances['touch-len-1'].vertices
a1.CoincidentPoint(movablePoint=v11[2], fixedPoint=v12[2])
#: 实例 "eye-1"  是完全约束的
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.4602, 
    farPlane=86.4429, width=53.8918, height=24.5081, viewOffsetX=-7.68328, 
    viewOffsetY=8.16328)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9087, 
    farPlane=85.9943, width=54.2555, height=24.6735, viewOffsetX=7.26604, 
    viewOffsetY=2.06898)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.3446, 
    farPlane=85.5585, width=48.2525, height=21.9435, viewOffsetX=6.71341, 
    viewOffsetY=2.92743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.6741, 
    farPlane=85.2289, width=48.4886, height=22.0509, viewOffsetX=3.30953, 
    viewOffsetY=3.11138)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.641, 
    farPlane=85.2621, width=51.5584, height=23.4469, viewOffsetX=2.97837, 
    viewOffsetY=2.86096)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['porcine-eye'].parts['touch-len']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['porcine-eye'].Material(name='cornea')
mdb.models['porcine-eye'].materials['cornea'].Elastic(table=((0.25, 0.49), ))
mdb.models['porcine-eye'].Material(name='front-sclera')
mdb.models['porcine-eye'].materials['front-sclera'].Elastic(table=((4.3, 0.49), 
    ))
mdb.models['porcine-eye'].Material(name='back-sclera')
mdb.models['porcine-eye'].materials['back-sclera'].Elastic(table=((8.2, 0.49), 
    ))
mdb.models['porcine-eye'].Material(name='crystalline')
mdb.models['porcine-eye'].materials['crystalline'].Elastic(table=((0.16, 0.49), 
    ))
mdb.models['porcine-eye'].Material(name='vitreous')
mdb.models['porcine-eye'].materials['vitreous'].Elastic(table=((0.42, 0.49), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.2228, 
    farPlane=15.7658, width=12.7217, height=5.78539, viewOffsetX=1.01242, 
    viewOffsetY=0.551285)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
del mdb.models['porcine-eye'].parts['touch-len']
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['porcine-eye'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#* FeatureError: 重生成失败
a1 = mdb.models['porcine-eye'].rootAssembly
a1.regenerate()
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['porcine-eye'].rootAssembly
del a.features['touch-len-1']
p1 = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s1 = mdb.models['porcine-eye'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(viewStyle=AXISYM)
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s1.FixedConstraint(entity=g[2])
s1.retrieveSketch(sketch=mdb.models['porcine-eye'].sketches['touch-len'])
session.viewports['Viewport: 1'].view.fitView()
#: 提示: 4 个实体已从 touch-len 复制.
p = mdb.models['porcine-eye'].Part(name='Part-2', dimensionality=AXISYMMETRIC, 
    type=DISCRETE_RIGID_SURFACE)
p = mdb.models['porcine-eye'].parts['Part-2']
p.BaseWire(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['porcine-eye'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['porcine-eye'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.9915, 
    farPlane=14.9971, width=7.71635, height=3.50912, viewOffsetY=-0.00161961)
mdb.models['porcine-eye'].parts['Part-2'].setValues(
    geometryRefinement=EXTRA_FINE)
mdb.models['porcine-eye'].parts.changeKey(fromName='Part-2', 
    toName='touch-len')
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.1877, 
    farPlane=15.8009, width=14.415, height=6.55545, viewOffsetX=1.4875, 
    viewOffsetY=0.992995)
p1 = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['porcine-eye'].parts['touch-len']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.7167, 
    farPlane=15.2719, width=9.13096, height=4.15244, viewOffsetX=0.65802, 
    viewOffsetY=-0.0053525)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['porcine-eye'].rootAssembly
p = mdb.models['porcine-eye'].parts['touch-len']
a1.Instance(name='touch-len-1', part=p, dependent=OFF)
p1 = a1.instances['touch-len-1']
p1.translate(vector=(0.0, 7.38982068537817, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.3828, 
    farPlane=84.8489, width=40.5297, height=18.4315, viewOffsetX=-0.534015, 
    viewOffsetY=3.56467)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.6728, 
    farPlane=84.559, width=40.7016, height=18.5097, viewOffsetX=0.463408, 
    viewOffsetY=5.03208)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.3266, 
    farPlane=83.6548, width=41.0892, height=18.6859, cameraPosition=(16.0373, 
    7.03874, 75.6445), cameraUpVector=(-0.00781826, 0.979437, -0.201598), 
    cameraTarget=(5.65284, 2.72855, -0.141912), viewOffsetX=0.46782, 
    viewOffsetY=5.07999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.2795, 
    farPlane=83.702, width=41.0613, height=18.6732, viewOffsetX=1.44721, 
    viewOffsetY=6.51294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.8889, 
    farPlane=83.0925, width=34.4049, height=15.6461, viewOffsetX=0.295259, 
    viewOffsetY=7.56692)
a1 = mdb.models['porcine-eye'].rootAssembly
v11 = a1.instances['touch-len-1'].vertices
v12 = a1.instances['eye-1'].vertices
a1.CoincidentPoint(movablePoint=v11[3], fixedPoint=v12[2])
#: 实例 "touch-len-1"  是完全约束的
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.4206, 
    farPlane=82.8449, width=36.8794, height=16.7715, viewOffsetX=0.373447, 
    viewOffsetY=7.55118)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.164, 
    farPlane=83.1015, width=36.745, height=16.7103, viewOffsetX=2.28025, 
    viewOffsetY=1.0452)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.1628, 
    farPlane=83.1028, width=36.7444, height=16.7101, viewOffsetX=3.28585, 
    viewOffsetY=2.48482)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.1628, 
    farPlane=83.1028, width=36.7445, height=16.7101, viewOffsetX=1.27457, 
    viewOffsetY=4.28437)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.4207, 
    farPlane=82.8448, width=36.8796, height=16.7715, viewOffsetX=1.81548, 
    viewOffsetY=4.46531)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.164, 
    farPlane=83.1015, width=36.7451, height=16.7104, viewOffsetX=2.29879, 
    viewOffsetY=2.31524)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.453, 
    farPlane=82.8125, width=32.6017, height=14.8261, viewOffsetX=1.65033, 
    viewOffsetY=3.19499)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.695, 
    farPlane=82.5705, width=32.7137, height=14.8771, viewOffsetX=1.3346, 
    viewOffsetY=3.06863)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis\axis.cae".
session.viewports['Viewport: 1'].view.setValues(width=30.7514, height=13.9847, 
    viewOffsetX=0.709948, viewOffsetY=3.10026)
p1 = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.1991, 
    farPlane=68.1656, width=46.2662, height=21.0403, viewOffsetX=0.893827, 
    viewOffsetY=0.898355)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['porcine-eye'].HomogeneousSolidSection(name='cornea-section', 
    material='cornea', thickness=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.1283, 
    farPlane=68.2363, width=52.294, height=23.7815, viewOffsetX=2.46676, 
    viewOffsetY=1.35289)
p = mdb.models['porcine-eye'].parts['eye']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='cornea-sec')
p = mdb.models['porcine-eye'].parts['eye']
p.SectionAssignment(region=region, sectionName='cornea-section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.5592, 
    farPlane=67.8054, width=43.774, height=19.9069, viewOffsetX=3.3379, 
    viewOffsetY=2.28447)
mdb.models['porcine-eye'].HomogeneousSolidSection(name='front-sclera-section', 
    material='front-sclera', thickness=None)
mdb.models['porcine-eye'].HomogeneousSolidSection(name='back-sclera-section', 
    material='back-sclera', thickness=None)
mdb.models['porcine-eye'].HomogeneousSolidSection(name='crystalline-section', 
    material='crystalline', thickness=None)
mdb.models['porcine-eye'].HomogeneousSolidSection(name='vitreous', 
    material='vitreous', thickness=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.8303, 
    farPlane=67.5343, width=46.7953, height=21.2809, viewOffsetX=3.58999, 
    viewOffsetY=2.12551)
a = mdb.models['porcine-eye'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['porcine-eye'].parts['eye']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
region = p.Set(faces=faces, name='front-sclera-set')
p = mdb.models['porcine-eye'].parts['eye']
p.SectionAssignment(region=region, sectionName='front-sclera-section', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.4842, 
    farPlane=67.8804, width=49.4737, height=22.4989, viewOffsetX=3.85791, 
    viewOffsetY=2.53443)
p = mdb.models['porcine-eye'].parts['eye']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(faces=faces, name='back-sclera-set')
p = mdb.models['porcine-eye'].parts['eye']
p.SectionAssignment(region=region, sectionName='back-sclera-section', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['porcine-eye'].parts['eye']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
region = p.Set(faces=faces, name='crystalline')
p = mdb.models['porcine-eye'].parts['eye']
p.SectionAssignment(region=region, sectionName='crystalline-section', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
mdb.models['porcine-eye'].sections.changeKey(fromName='vitreous', 
    toName='vitreous-section')
p = mdb.models['porcine-eye'].parts['eye']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#10 ]', ), )
region = p.Set(faces=faces, name='vitreous-set')
p = mdb.models['porcine-eye'].parts['eye']
p.SectionAssignment(region=region, sectionName='vitreous-section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.7632, 
    farPlane=68.6014, width=55.2634, height=25.1319, viewOffsetX=2.73094, 
    viewOffsetY=3.12412)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.4238, 
    farPlane=68.9408, width=54.9209, height=24.9761, viewOffsetX=6.41395, 
    viewOffsetY=0.376594)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.373, 
    farPlane=68.9916, width=51.5774, height=23.4556, viewOffsetX=6.92436, 
    viewOffsetY=-0.540502)
a1 = mdb.models['porcine-eye'].rootAssembly
a1.regenerate()
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['porcine-eye'].ExplicitDynamicsStep(name='Press', 
    previous='Initial', timePeriod=0.01, scaleFactor=1.0, improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Press')
session.viewports['Viewport: 1'].view.setValues(width=29.0125, height=13.1939, 
    viewOffsetX=0.524769, viewOffsetY=2.98726)
mdb.models['porcine-eye'].ExplicitDynamicsStep(name='Resume', previous='Press', 
    timePeriod=1e-05, improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Resume')
mdb.models['porcine-eye'].steps['Resume'].setValues(timePeriod=0.001, 
    improvedDtMethod=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.1449, 
    farPlane=83.1207, width=39.08, height=17.7722, viewOffsetX=2.75117, 
    viewOffsetY=2.356)
mdb.models['porcine-eye'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'SVAVG', 'E', 'LE', 'UT', 'RF', 'CSTRESS', 'CDISP'), 
    timeMarks=ON)
mdb.models['porcine-eye'].historyOutputRequests['H-Output-1'].setValues(
    variables=('ALLAE', 'ALLCD', 'ALLDC', 'ALLDMD', 'ALLFD', 'ALLIE', 'ALLKE', 
    'ALLPD', 'ALLSE', 'ALLVD', 'ALLWK', 'ALLCW', 'ALLMW', 'ALLPW', 'ETOTAL'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.2533, 
    farPlane=83.4894, width=38.5833, height=17.5463, cameraPosition=(1.611, 
    11.3902, 75.4488), cameraUpVector=(0.0473941, 0.966206, -0.253377), 
    cameraTarget=(5.55526, 2.78646, -0.580251), viewOffsetX=2.7162, 
    viewOffsetY=2.32605)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.1246, 
    farPlane=82.6181, width=30.5029, height=13.8716, viewOffsetX=2.326, 
    viewOffsetY=2.52874)
mdb.models['porcine-eye'].ContactProperty('global')
mdb.models['porcine-eye'].interactionProperties['global'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['porcine-eye'].interactionProperties['global'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
#: 相互作用属性 "global" 已创建.
mdb.models['porcine-eye'].interactionProperties.changeKey(fromName='global', 
    toName='eye-inside')
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.3526, 
    farPlane=82.3901, width=30.602, height=13.9167, cameraPosition=(1.72207, 
    11.2851, 75.4665), cameraUpVector=(0.00674983, 0.966772, -0.25555), 
    cameraTarget=(5.66633, 2.68133, -0.562592), viewOffsetX=2.33356, 
    viewOffsetY=2.53697)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Press')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Resume')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Press')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Resume')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Press')
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.2747, 
    farPlane=83.4681, width=41.0587, height=18.6721, viewOffsetX=1.91829, 
    viewOffsetY=3.42302)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.994, 
    farPlane=83.7488, width=40.8923, height=18.5964, viewOffsetX=6.64541, 
    viewOffsetY=-1.99811)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.5956, 
    farPlane=82.1472, width=27.1333, height=12.3393, viewOffsetX=6.18757, 
    viewOffsetY=-2.12972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.8013, 
    farPlane=81.9415, width=27.2124, height=12.3752, viewOffsetX=3.16928, 
    viewOffsetY=1.55761)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.2111, 
    farPlane=81.5317, width=25.7277, height=11.7001, viewOffsetX=3.05337, 
    viewOffsetY=1.31002)
mdb.models['porcine-eye'].interactionProperties.changeKey(
    fromName='eye-inside', toName='global')
mdb.models['porcine-eye'].ContactExp(name='global', createStepName='Press')
mdb.models['porcine-eye'].interactions['global'].includedPairs.setValuesInStep(
    stepName='Press', useAllstar=ON)
mdb.models['porcine-eye'].interactions['global'].contactPropertyAssignments.appendInStep(
    stepName='Press', assignments=((GLOBAL, SELF, ''), ))
mdb.models['porcine-eye'].interactions['global'].wearSurfacePropertyAssignments.appendInStep(
    stepName='Press', assignments=((GLOBAL, ''), ))
#: 相互作用 "global" 已创建.
session.viewports['Viewport: 1'].view.setValues(nearPlane=72.2991, 
    farPlane=80.4436, width=14.9671, height=6.80651, viewOffsetX=2.18307, 
    viewOffsetY=3.22869)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    geometrySilhouetteEdges=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    geometrySilhouetteEdges=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=ALL)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=EXTERIOR)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=FEATURE)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=EXTERIOR)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=ALL)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=EXTERIOR)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    geometrySilhouetteEdges=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    geometryEdgesInShaded=OFF, geometrySilhouetteEdges=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    geometryEdgesInShaded=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.0106, 
    farPlane=65.3541, width=26.1889, height=11.9098, viewOffsetX=4.7917, 
    viewOffsetY=3.31606)
mdb.save()
#: 模型数据库已保存到 "E:\study\research\articles\眼睛力学参数\simulation\axis\axis.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.5998, 
    farPlane=64.7648, width=21.9731, height=9.99258, viewOffsetX=4.61067, 
    viewOffsetY=4.41191)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.8754, 
    farPlane=80.8673, width=20.2743, height=9.22003, viewOffsetX=3.20213, 
    viewOffsetY=3.51323)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.7193, 
    farPlane=81.0235, width=21.5215, height=9.78723, viewOffsetX=3.43126, 
    viewOffsetY=3.64024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.2181, 
    farPlane=83.7285, width=21.3711, height=9.71884, cameraPosition=(14.8631, 
    16.6925, 75.1132), cameraUpVector=(-0.0785306, 0.9449, -0.3178), 
    cameraTarget=(5.89061, 2.58682, 0.343344), viewOffsetX=3.40728, 
    viewOffsetY=3.6148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.2309, 
    farPlane=83.7157, width=21.375, height=9.72059, cameraPosition=(15.0331, 
    16.5547, 75.1188), cameraUpVector=(-0.1182, 0.942506, -0.312588), 
    cameraTarget=(6.06063, 2.44901, 0.34894), viewOffsetX=3.40789, 
    viewOffsetY=3.61545)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.1756, 
    farPlane=84.4588, width=21.3584, height=9.71305, cameraPosition=(24.8571, 
    15.0392, 73.9219), cameraUpVector=(-0.102254, 0.952251, -0.287685), 
    cameraTarget=(6.10923, 2.59676, 0.684504), viewOffsetX=3.40524, 
    viewOffsetY=3.61264)
p = mdb.models['porcine-eye'].parts['eye']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.7593, 
    farPlane=64.6053, width=23.4392, height=10.6593, viewOffsetX=4.92176, 
    viewOffsetY=4.42294)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshVisibleEdges=ALL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.5807, 
    farPlane=64.784, width=24.8595, height=11.3052, viewOffsetX=5.14128, 
    viewOffsetY=4.49726)
a = mdb.models['porcine-eye'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
