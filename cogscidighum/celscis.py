celscilist = {
'dd':{'x':{'followers': 1000}},
'jp':{'x':{'followers': 300}},
'sh':{'x':{'followers': 200}},
'gs':{'x':{'followers': 100}}
}
class Celsci():

    asname="aso"
    def fame(x):
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
    
for person in celscilist:
    #dh=ic(person,checkfame(person))
    print(person,checkfame(person))
