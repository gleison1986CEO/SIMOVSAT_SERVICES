import datetime

from extra_classe.boleto import BOLETO
from error.error_data    import ERROR_DATA
error  =  ERROR_DATA()
pay    =  BOLETO()
class WHATSAPP:

    def sendboletopendente(self, data):
        
        return data


    def sendbmensagempago(self, data):
    
        ## BOLETOS COM ERROS
        pay.boletoserrorrequest(data)
   
        return "OK"


    def sendboletoaberto(self, data, whastapp):

        try:

                linha_digitavel = data["linha_digitavel"]
                link_boleto     = data["link_boleto"]
                short_link      = data["short_link"]
                data_vencimento_original = data["data_vencimento_original"]
                data_vencimento = data["data_vencimento"]
                valor_boleto    = data["valor_boleto"]
                nome_associado  = data["nome_associado"]
                valor_boleto    = data["valor_boleto"]
                cpf_associado   = data["cpf_associado"]

                dates    =   data_vencimento
                now      =   datetime.datetime.now().date()
                date     =   datetime.datetime.strptime(dates.replace("-",""), '%Y%m%d').date()
                vencimento  =   date + datetime.timedelta(days=5) 
                
                ## REMOVER SE PRECISAR MDUAR DATA ## REMOVER SE PRECISAR MDUAR DATA
                print(str(vencimento) + ":: VENCIMENTO")

                if now > vencimento:
                    ### VISTORIA
                    pay.boletosencontrado(whastapp, linha_digitavel, link_boleto, short_link, data_vencimento, valor_boleto, nome_associado, cpf_associado, str(vencimento), "VISTORIA")

                elif now < vencimento:
                    ## BOLETO EM ABERTO
                    pay.boletosencontrado(whastapp, linha_digitavel, link_boleto, short_link, data_vencimento, valor_boleto, nome_associado, cpf_associado, str(vencimento), "BOLETO")
                else:
                    ##ERROS NAO ECONTRADO
                    pay.boletoserrorrequest(whastapp)
                return data

        except:
            pay.boletoserrorrequest(whastapp)


    def sendboletobaixado(self, data):
            
        return data    