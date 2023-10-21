class Celsci:
    celscilist = {
    'dd':{'x':{'followers': 1200}},
    'jp':{'x':{'followers': 300}},
    'sh':{'x':{'followers': 200}},
    'gs':{'x':{'followers': 100}}
    }
    #ax1="dd"
    def fame(x):
        y="low"
        if x>300:
            y= 'high'
        return y
    asname2= fame(Celsci.celscilist["dd"]['x']['followers'])
def checkfame(x1):
    xy=Celsci.celscilist[x1]['x']['followers']
    person = Celsci.fame(xy)
    return person
     
 #def checkfame1(x2):
 #   person = x2 + "-aso"
 #   return person
    
#for person in Celsci.celscilist:
#    print(person,checkfame(person))
