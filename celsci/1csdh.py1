class Celsci:
    celscilist = {
    'dd':{'x':{'followers': 400}},
    'jp':{'x':{'followers': 300}},
    'sh':{'x':{'followers': 200}},
    'gs':{'x':{'followers': 100}}
    }
    asname="aso"
    def fame(x):
        y="low"
        if x>300:
            y= 'high'
        return y
 
def checkfame(x):
    person = Celsci.fame(Celsci.celscilist[x]['x']['followers'])
    return person
    
for person in Celsci.celscilist:
    #dh=ic(person,checkfame(person))
    print(person,checkfame(person))
