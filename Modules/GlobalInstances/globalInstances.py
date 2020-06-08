import sys
sys.path.append('../CommonWidgets')
import infoDialog

class GlobalInstances:
    __instances={}
    @staticmethod
    def buildInstances():
        for constructor in GlobalInstances.__constructors:
            GlobalInstances.__instances[constructor[0]]=constructor[1]()
    @staticmethod
    def getInstance(key):
        if key in GlobalInstances.__instances:
            return GlobalInstances.__instances[key]
        print 'error'
        return None
    __constructors=[('infoDialog',infoDialog.InfoDialog)]