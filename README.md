# Year-Month-generator
### Gerador de array com o formato 'year-month'.

Na área de ciência de dados, é muito importante se trabalhar com indexes temporais para facilitar o trabalho das análises exploratórias, além da geração de gráficos.

Portanto, quando se não tiver tais valores, é importante haver uma forma de criá-los.

Será utilizado somente as bibliotecas 'datetime' e 'numpy' para criação da função geradora.

Como parâmetro único, só será preciso informar a quantidade de meses que será contabilizado.

A função conta a partir do mês atual para trás conforme a quantiade de meses parametrizada.

Tomamos como exemplo o número **48**.

Quero gerar 48 meses para trás a partir do mês atual:

~~~python
from datetime import datetime
import numpy as np

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
 return np.array(year_month)

print(generator_month_year(48))
~~~
Como output, será retornado:
![image](https://github.com/Caloka/Year-Month-generator/assets/75040393/432c80bb-c7a1-4a52-943a-27972f6a4c1e)


E assim, pode-se declarar a biblioteca 'pandas' para transformar esse array em uma série timestamp e setá-lo como index.


