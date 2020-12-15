import sys
sys.path.append('../CommonWidgets')
import infoDialog

class GlobalInstances:
    __instances={}
    __app=None
    @staticmethod
    def buildInstances(app):
        GlobalInstances.__app=app
        for constructor in GlobalInstances.__constructors:
            GlobalInstances.__instances[constructor[0]]=constructor[1]()
    @staticmethod
    def getInstance(key):
        if key in GlobalInstances.__instances:
            return GlobalInstances.__instances[key]
        #print 'error'
        return None
    @staticmethod
    def getApp():
        return GlobalInstances.__app


    __constructors=[('infoDialog',infoDialog.InfoDialog)]