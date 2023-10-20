class Celsci:
    celscilist = {
    'dd':{'x':{'followers': 900}},
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
        
     def checkfame(x1):
        person = fame(celscilist[x1]['x']['followers'])
        return person

    
for person in Celsci.celscilist:
    #dh=ic(person,Celsci.checkfame(person))
    print(person,Celsci.checkfame(person))
