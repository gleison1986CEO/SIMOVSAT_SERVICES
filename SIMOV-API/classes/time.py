from datetime import datetime, timedelta

class TIME:

    def timedate25(self):

        current_date = datetime.now()
        end_date     = current_date + timedelta(days=-60)
        out          = end_date.strftime('%d-%m-%Y').replace("-","/")

        return out


    def timedatenow(self):

        current_date = datetime.now()
        out          = current_date.strftime('%d-%m-%Y').replace("-","/")

        return out


    def timedate5(self, data_vencimento_original):
        
        current_date = data_vencimento_original
        end_date     = current_date + timedelta(days=5)
        out          = end_date.strftime('%d-%m-%Y').replace("-","/")
    
        
        return out     