##My life
##I went Namilyanga College 
##Namilyango SS
##Different Guys
##5 GUYS PROBABLY

class Paul:
    def write_letter(self):
        return  "Favour....I am Paul...My favorite song is Master of Puppets"
    
##The scammers    
class Marvin(Paul):
    def write_letter(self):
        return "Dear Favour.. My Favourite song is Dance for me"
    
class Dan(Paul):
    def write_letter(self):
        return "Dear Favour.. My Favourite song is Staying Alive" 

class James(Paul):
    def write_letter(self):
        return "Dear Favour.. My Favourite song is Smooth Criminal" 

class Mark(Paul):
    def write_letter(self):
        return "Dear Favour.. My Favourite song is I am the warlus"     
          
class James(Mark, James):
    pass

letter_writing_boy = Paul()
print(letter_writing_boy.write_letter())       
