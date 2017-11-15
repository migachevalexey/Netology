import osa


def convert_Temperature(file):
    temp_C, counter = 0, 0
    with open(file) as f:
        for line in f:
            i = line.split()
            client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
            result = client.service.ConvertTemp(
                Temperature=i[0],
                FromUnit='degreeFahrenheit',
                ToUnit='degreeCelsius')
            temp_C += result
            counter += 1
    avg_temp_C = temp_C / counter
    return round(avg_temp_C, 2)


def convert_Distance(file):
    Distance_km = 0
    with open(file) as f:
        for line in f:
            i = line.split()
            i[1] = float(i[1].replace(',', ''))
            client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
            result = client.service.ChangeLengthUnit(
                LengthValue=i[1],
                fromLengthUnit='Miles',
                toLengthUnit='Kilometers')
            Distance_km += result
    return round(Distance_km, 2)


def convert_currency(file):
    amount_sum = 0
    with open(file) as f:
        for line in f:
            i = line.split()
            client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
            result = client.service.ConvertToNum(
                fromCurrency=i[-1],
                toCurrency='RUB',
                amount=i[1],
                rounding=True)
            amount_sum += result
    return round(amount_sum)


print('Средняя температура по Цельсию - {}°C'.format(convert_Temperature(input('Имя и путь к файлу: '))))
print('Путь в километрах - {}км'.format(convert_Distance(input('Имя и путь к файлу: '))))
print('Стоимость авиабилетов - {}руб.'.format(convert_currency(input('Имя и путь к файлу: '))))
