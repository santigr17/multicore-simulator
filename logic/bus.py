class bus:
    class __bus:
        def __init__(self):
            self.newData = False
            self.data = 0

        def newMns(self, mns):
            self.locked = True
            self.data = mns
    
    
    instance = None

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __init__(self):
        if(self.instance is None):
            self.instance = bus.__bus()
    

            
    
