
class Celsci(self):
    def __init__(self,log=None,**keys):
        #print("this happens")
        self.celscilist = {
        'dd':{'x':{'followers': 1100}},
        'jp':{'x':{'followers': 300}},
        'sh':{'x':{'followers': 200}},
        'gs':{'x':{'followers': 100}}
        }
    self.celscilist = {
    'dd':{'x':{'followers': 1200}},
    'jp':{'x':{'followers': 300}},
    'sh':{'x':{'followers': 200}},
    'gs':{'x':{'followers': 100}}
    }
    asname="aso1"
    def fame(self,x):
        y="low"
        if x>300:
            y= 'high'
        return y
"def checkfame(x1):
"    person = fame(celscilist[x1]['x']['followers'])
"    return person
     
 #def checkfame1(x2):
 #   person = x2 + "-aso"
 #   return person
    
"for person in celscilist:
"    #dh=ic(person,checkfame(person))
"    print(person,checkfame(person))
