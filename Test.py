import random

class Studierender:
    Name  = ["Tim","Kim","Lin","Jin","Mirco","Nico","David","Remo"]
    Noten = []
    passed = "None"
    i = 0
    
for count in range(len(Studierender.Name)) :
    Studierender.Noten.append(int(random.random()* 6)+1)
    
  
class Teacher:
    
    def study(Studierender):
        Studierender.Noten[Studierender.i] =+ bonus
        return Studierender 
        
      
        
class Test:
    while Studierender.i < len(Studierender.Name):
    
        if Studierender.Noten[Studierender.i] < 4 :
            Studierender.passed = "fail"
        else:
            Studierender.passed = "passed"
    
     
        print(Studierender.Name[Studierender.i],Studierender.Noten[Studierender.i],Studierender.passed)       
        
        #Studierender = Teacher.study()
            
        print(Studierender.Name[Studierender.i],Studierender.Noten[Studierender.i])

        Studierender.i = Studierender.i + 1   
 