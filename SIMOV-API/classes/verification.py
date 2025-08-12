

########## VERIFICATION DATA 
class VERIFICATION:


    def cpf(self, data):
        
        out    = data.replace(" ","").replace("-","").replace(".","").replace("/","")
        return out



    def phone(self, data):
        
        out       = data.replace(" ","").replace("-","").replace(".","").replace("/","").replace("(","").replace(")","").replace("_","").replace(" ","").replace("*","")
        phoneOut  = "+55" + str(out)
        return phoneOut        