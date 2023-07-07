from datetime import datetime

# Obter a data atual
def generator_month_year(size)->list:
 data_atual = datetime.now()
 year = data_atual.year
 mes = data_atual.month
 cont = 0
 year_month = []
 while True:
    if len(year_month) < size:
     while True:
         if len(year_month) < size:
            if (mes - cont) > 0:
                    var = mes - cont
                    check = str(var)
                    if len(check) < 2:
                     str_=f'{year}-0{var}'
                    elif len(check) > 1:
                       str_=f'{year}-{var}'
                    #display(str_)
                    year_month.append(str_)
            else:
                mes = 12
                cont = 0
                year = year - 1
                break
            cont = cont + 1
         else: 
             break
    else:
        break
 return year_month

print(generator_month_year(48))