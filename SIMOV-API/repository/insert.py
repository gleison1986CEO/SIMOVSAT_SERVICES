import pyodbc
import time

from classes.conn   import CONN
SQLSERVER  = CONN()
cursor     = SQLSERVER.sqlserver()



class SQLSERVER:
    def USERS(self,tipo, codigo_associado, cpf, rg_associado, email, whastapp, cnh, out):
        
        
        sql = "INSERT INTO dbo.Users (codigo_associado, tipo, rg, email, whastapp, cnh, descricao, Ativo ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        params = (codigo_associado, tipo, rg_associado, email, whastapp, cnh, out, 1)
        print(params)
        cursor.execute(sql, params)
        cursor.commit()
        time.sleep(3)

        query   = cursor.execute("select * from dbo.Users")
        results = query.fetchall()
        time.sleep(5)
        return  results





    def CONEXA(self, situacao, name, date, cpf, agenda, especialidade, telefone, email):
        
        print("SALVANDO" + cpf)
        try:

            sql = "INSERT INTO dbo.ConexaUser (situacao, name, date, cpf, agenda, email, especialidade, telefone,  Ativo ) VALUES (?, ?, ?, ?, ?, ?, ?, ? , ?)"
            params = (situacao, name, date, cpf, agenda, email, especialidade, telefone, 1)
            cursor.execute(sql, params)
            cursor.commit()
                
        except:
            pass    


        return  "Ok" 




    def CLUBE(self, situacao, name, date, cpf, agenda, especialidade, telefone, email):
        
        print("SALVANDO" + cpf)
        try:
            sql = "INSERT INTO dbo.ClubeUser (situacao, name, date, cpf, agenda, email, especialidade, telefone,  Ativo ) VALUES (?, ?, ?, ?, ?, ?, ?, ? , ?)"
            params = (situacao, name, date, cpf, agenda, email, especialidade, telefone, 1)
            cursor.execute(sql, params)
            cursor.commit()
                
        except:
            pass    


        return  "Ok"     

    def VEICULOS(self, data):
    
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results


    def LOCATION(self, data):
        
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results       

    def COOPERATIVAS(self, data):
        
        # sql = "INSERT INTO dbo.cooperativas (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results            


    def PRODUTO(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results           



    def REGIONAIS(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results          



    def SITUACAO(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results          



    def VOLUNTARIOS(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results           



    def INFORNET(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results        


    def PACIENTES(self, data):
            
        # sql = "INSERT INTO dbo.laudos (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # params = (hashcode, laudo, arquivo, cnpj, estado, cidade, description, keywords, Ativo)
        # cursor.execute(sql, params)
        # cursor.commit()
        # time.sleep(3)

        # query   = cursor.execute("select * from dbo.laudos")
        # results = query.fetchall()
        # print(results)
        return  results               


    def KEY(self, data):
            
        sql = "INSERT INTO dbo.Tokens (Token, Ativo) VALUES (?,?)"
        params = (data, 1)
        cursor.execute(sql, params)
        cursor.commit()
        time.sleep(3)

        query   = cursor.execute("select * from dbo.Tokens")
        results = query.fetchall()
        time.sleep(3)
        return  results         


    def HISTORICO(self, nome, tipo, descricao, data, Ativo):
            
        sql = "INSERT INTO dbo.Historico (nome, tipo, descricao, data, Ativo) VALUES (?, ?, ?, ?, ?)"
        params = (nome, tipo, descricao, data, Ativo)

        cursor.execute(sql, params)
        cursor.commit()
        time.sleep(3)

        query   = cursor.execute("select * from dbo.Historico")
        results = query.fetchall()
        time.sleep(3)
        return  results           

       



 