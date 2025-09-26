
import os
import time
from classes.sendmessagem  import WHATSAPP
from extra_classe.boleto   import BOLETO
from extra_classe.usuarios import USUARIOS
from classes.verification  import VERIFICATION


##################################### INSTANCIAS

usuarios_    =    USUARIOS()
boletos_     =    BOLETO()
whatsapp_    =    WHATSAPP()
verification_=    VERIFICATION()

##################################### INSTANCIAS

################### ALL PAYMENT METHODS HERE
class PAGAMENTOS:

    def boletos(self,cpf, whastapp):
      


      try:  
        

        cpfVerify   = verification_.cpf(cpf)

        time.sleep(10)
        
        params      = usuarios_.cpflist(cpfVerify)

        #### GET DATA FROM USER 
        whastapp_associado = params["telefone_celular"]
        codigo_usuario     = params["codigo_associado"]
        print(codigo_usuario)
        
        phoneVerify    = verification_.phone(whastapp_associado)
        try:
          print("BOLETO DISPONIVEL")
          nosso_numero   = boletos_.boletosdisponivel(codigo_usuario)  ## MUDAR PARA BOLETO DISPONIVEL

          out = boletos_.listar(nosso_numero[0]["nosso_numero"])
          print(out)
          whatsapp_.sendboletoaberto(out, phoneVerify)
          
        except:  
              try:
                print("BOLETO BAIXADO")
                nosso_numero   = boletos_.boletosbaixado(codigo_usuario)  ## MUDAR PARA BOLETO DISPONIVEL
                out = boletos_.listar(nosso_numero[0]["nosso_numero"])
                print(out)
                whatsapp_.sendboletoaberto(out, phoneVerify)
                
              except:  
                    try:
                      print("BOLETO PENDENTE")
                      nosso_numero   = boletos_.boletospendencia(codigo_usuario)  ## MUDAR PARA BOLETO DISPONIVEL
                      out = boletos_.listar(nosso_numero[0]["nosso_numero"])
                      print(out)
                      whatsapp_.sendboletoaberto(out, phoneVerify)
                      
                    except:
                        if whastapp == "MARKETING":
                              whatsapp_.sendbmensagempago(phoneVerify)
                              pass 
                        else:
                           print("ERROR")    
                      
      except:
        if whastapp == "MARKETING":
              try:
                whatsapp_.sendbmensagempago(phoneVerify)
                pass 
              except:
                  pass
              
        else:      
              console.log(whastapp)
              pass 
         

      