import random

class Studierender:
    Name  = ["Tim","Kim","Lin","Jin","Mirco","Nico","David","Remo","Olav","Sarah"]
    Noten = []
    MeanMarks = []
    passed = "None"
    i = 0
    j = 0
    
    
# Erstellen eines 3 D Array mit Noten   
for count in range(len(Studierender.Name)) :
    for count2 in range(3):
        Studierender.Noten.append(int(random.random()* 6)+1)

for Studierender.j in range(len(Studierender.Noten)/3):
    Studierender.MeanMarks.append(int((Studierender.Noten[0+3*Studierender.j]+Studierender.Noten[1+3*Studierender.j]+Studierender.Noten[2+3*Studierender.j])/3))
# Eigentlich wollte ich def study in class Teacher verschachteln
   
              
class Test:
    
    def study(self,bonus = 1):
        if Studierender.MeanMarks[Studierender.i] in range(6):
            Studierender.MeanMarks[Studierender.i] = Studierender.MeanMarks[Studierender.i] + bonus
            return Studierender 
        else:
            return Studierender
    
    def Check(self): 
        
        if Studierender.MeanMarks[Studierender.i] < 4 :
            Studierender.passed = "fail"
        else:
            Studierender.passed = "passed"
        
    while Studierender.i < len(Studierender.Name):
    
        Check(1)
     
        print(Studierender.Name[Studierender.i],Studierender.MeanMarks[Studierender.i],Studierender.passed)       
        
        study(1)
        Check(1)
            
        print("Study",Studierender.Name[Studierender.i],Studierender.MeanMarks[Studierender.i],Studierender.passed)       
        print("")
        Studierender.i = Studierender.i + 1   
        
        
print("Anzahl noten",len(Studierender.Noten[:]))
print("Notentabelle",Studierender.Noten[:])
print("Durchschnitts Noten" ,Studierender.MeanMarks)


class Teacher:
    Moodlevel = 0
    mood = "sadly"
    i = 0
    
    for i in range(len(Studierender.MeanMarks)):
        if Studierender.MeanMarks[i] >= 4:
            Moodlevel = Moodlevel +1
            
if Teacher.Moodlevel < 4 :
    pass
elif Teacher.Moodlevel == 5:
    Teacher.mood = "ok"
else :
    Teacher.mood = "happy"           
            
print("Students Passed",Teacher.Moodlevel,"Teacher mood",Teacher.mood)    