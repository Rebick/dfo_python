import requests
import datetime
from datetime import timedelta

# Fecha en formato de fecha
date = datetime.datetime(2021, 11, 7)
print('Obteniendo el valor del dolar del dia', date)


# Los sabados y domingos no estan disponibles en el dfo, por lo tanto utilizaremos el ultimo viernes

def api_operation(date):
    # Codigo para hacer la consulta
    response = requests.get(
        "http://sidofqa.segob.gob.mx/dof/sidof/indicadores/" + date.strftime(
            '%d-%m-%Y'))  # Formato de la fecha"30-03-2022"
    json = response.json()
    print('El valor del dolar es:', json['ListaIndicadores'][0]['valor'])


while True:
    if date.weekday() == 5:
        one_days_ago = date - timedelta(days=1)
        print('Este dia cae en fin de semana, usa el viernes anterior')
        print('El ultimo viernes es: ', one_days_ago)
        api_operation(one_days_ago)
        break

    if date.weekday() == 6:
        two_days_ago = date - timedelta(days=2)
        print('Este dia cae en fin de semana, usa el viernes anterior')
        print('El ultimo viernes es: ', two_days_ago)
        api_operation(two_days_ago)
        break

    else:
        api_operation(date)
