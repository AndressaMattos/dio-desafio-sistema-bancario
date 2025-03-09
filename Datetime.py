from datetime import date, datetime, timedelta

#data
d = date(2025,7,10)
print(d)
print (date.today())
#data hora
dt = datetime(2025,7,10,10,30,20)
print(dt)
#hora
t = (10,20,30)
print (t)

#manipulação
#Adicionando uma semana
d = d + timedelta(weeks =1)
print(d)


tipo_carro = 'P' # 'M', 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print (f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print (f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print (f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')

print(date.today() - timedelta(days=1))

#print(date.today() - timedelta(hours=1))

resultado = datetime(2023,7,25,10,19,20) - timedelta(hours= 1)

print (resultado.time())
print (datetime.now().date())
print (datetime.now().time())

#formatação 
print(F'---------fORMATAÇÃO--------')
data_hora_atual = datetime.now()
data_hora_str = '2023-7-20 10:20'
mascara_ptbr ='%d/%m/%y %a'
mascara_en ='%Y-%m-%d %H:%M'

print (data_hora_atual)
print (data_hora_atual.strftime(mascara_ptbr))
print(datetime.strptime(data_hora_str, mascara_en))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida.strftime("%Y"))
print(type(data_convertida))

#timezone e pytz

#pytz
print(f'-----------------timezone-------------------')
import pytz
d = datetime.now(pytz.timezone("Europe/Oslo"))
d2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print (d)
print (d2)

#timezone
from datetime import timezone,timedelta, datetime
print(f'-----------------pytz-------------------')
data1 = datetime.now(timezone(timedelta("hours=2")))
data2 = datetime.now(timezone(timedelta("hours=-3")))
print (data1)
print (data2)
