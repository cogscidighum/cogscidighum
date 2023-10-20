
class Celsci():
    def __init__(self,**keys):
        #print("this happens")
        self.celscilist = {
        'dd':{'x':{'followers': 1100}},
        'jp':{'x':{'followers': 300}},
        'sh':{'x':{'followers': 200}},
        'gs':{'x':{'followers': 100}}
        }
    celscilist = {
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
    def checkfame(x1):
        person = fame(celscilist[x1]['x']['followers'])
        return person
     
 #def checkfame1(x2):
 #   person = x2 + "-aso"
 #   return person
    
for person in Celsci.celscilist:
    print(person,Celsci.checkfame(person))
