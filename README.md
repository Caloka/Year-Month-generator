# Year-Month-generator
### Gerador de array com o formato 'year-month'.

Na área de ciência de dados, é muito importante se trabalhar com indexes temporais para facilitar o trabalho das análises exploratórias, além da geração de gráficos.

Portanto, quando se não tiver tais valores, é importante haver uma forma de criá-los.

Será utilizado somente a biblioteca 'datetime' para criação da função de gerador.

Como parâmetro único, só será preciso informar a quantidade de meses que será contabilizado.

A função conta a partir do mês atual para trás conforme a quantiade de meses parametrizada.

Tomamos como exemplo o número **48**.

Quero gerar 48 meses para trás a partir do mês atual:

~~~python
from datetime import datetime

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
~~~
Como output, será retornado:
![image](https://github.com/Caloka/Year-Month-generator/assets/75040393/3ce9389d-7c32-4df3-95ae-e092dfae6177)

E assim pode-se manipular o pandas para setar o index do seu dataframe com o array criado.


