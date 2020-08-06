import pymel.core as pm

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaGeneralLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaGeneralLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=("BoolPin", False), nodeType=NodeTypes.Pure, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def objExists(DagPath=("StringPin", "")):
        return pm.objExists(DagPath)

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def SetTranslation(dag=('StringPin', ""), vector=('MayaVectorPin', pm.datatypes.Vector())):
        """Sets node translation if node exists"""
        if pm.objExists(dag):
            node = pm.PyNode(dag)
            node.t.set(vector)
            return True
        return False

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def SetRotation(dag=('StringPin', ""), vector=('MayaVectorPin', pm.datatypes.Vector())):
        """Sets node rotation if node exists"""
        if pm.objExists(dag):
            node = pm.PyNode(dag)
            node.r.set(vector)
            return True
        return False

    @staticmethod
    @IMPLEMENT_NODE(returns=("BoolPin", False), nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def setTransform(DagPath=("StringPin", ""),
                     Location=("MayaVectorPin", pm.datatypes.Vector()),
                     Rotation=("MayaVectorPin", pm.datatypes.Vector()),
                     Scale=("MayaVectorPin", pm.datatypes.Vector(1.0, 1.0, 1.0))):
        """
        Sets transform to PyNode
        """
        if pm.objExists(DagPath):
            node = pm.PyNode(DagPath)
            node.t.set(Location.x, Location.y, Location.z)
            node.r.set(Rotation.x, Rotation.y, Rotation.z)
            node.s.set(Scale.x, Scale.y, Scale.z)
            return True
        else:
            return False

    @staticmethod
    @IMPLEMENT_NODE(returns=("BoolPin", False), nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def setKeyFrame(DagPath=("StringPin", ''),
                    AttributeName=("StringPin", '')):

        if not pm.objExists(DagPath):
            return False

        if AttributeName == '':
            pm.setKeyframe(DagPath)
            return True
        else:
            try:
                pm.setKeyframe(DagPath, at=AttributeName)
                return True
            except:
                return False

    @staticmethod
    @IMPLEMENT_NODE(returns=None, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def frameRange(Min=("Reference", ("IntPin", 0)),
                   Max=("Reference", ("IntPin", 0))):
        """
        Returns time slader min and max.
        """
        Min(pm.playbackOptions(q=True, min=True))
        Max(pm.playbackOptions(q=True, max=True))

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def setCurrentFrame(CurrentFrame=("IntPin", 0)):
        pm.setCurrentTime(CurrentFrame)

    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0), meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def currentFrame():
        return pm.currentTime(q=True)

    @staticmethod
    @IMPLEMENT_NODE(returns=("BoolPin", False), nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def parent(parentObj=("StringPin", ""), childObj=("StringPin", ""),
               absolute=("BoolPin", False),
               addObject=("BoolPin", False),
               noConnections=("BoolPin", False),
               noInvScale=("BoolPin", False),
               relative=("BoolPin", False),
               removeObject=("BoolPin", False),
               shape=("BoolPin", False),
               world=("BoolPin", False)):
        """Wrapper for **pm.parent**"""
        try:
            pm.parent(childObj, parentObj,
                      a=absolute,
                      add=addObject,
                      nc=noConnections,
                      nis=noInvScale,
                      r=relative,
                      rm=removeObject,
                      s=shape,
                      w=world)
        except:
            pass

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'General', 'Keywords': []})
    def align(alignToLead=("BoolPin", False),
              coordinateSystem=("StringPin", ""),
              xAxis=("StringPin", "none", {"ValueList": ["min", "mid", "max", "dist", "stack", "none"]}),
              yAxis=("StringPin", "none", {"ValueList": ["min", "mid", "max", "dist", "stack", "none"]}),
              zAxis=("StringPin", "none", {"ValueList": ["min", "mid", "max", "dist", "stack", "none"]})):
        try:
            pm.align(atl=alignToLead, cs=coordinateSystem, x=xAxis, y=yAxis, z=zAxis)
        except:
            pm.align(atl=alignToLead, x=xAxis, y=yAxis, z=zAxis)
