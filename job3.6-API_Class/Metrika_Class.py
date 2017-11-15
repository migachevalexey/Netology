from pprint import pprint
from urllib.parse import urlencode, urljoin
import requests

# получение токена, формируем ссылку, печатаем ее и переходим по ней вживую
# щелкаем - "Разрешить" и нам выдают токен!
#     AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
#     APP_ID = 'b428505a1e314f50a72e9236426ced16'
#     auth_data = {
#         'response_type': 'token',
#         'client_id': APP_ID
#     }
#     print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


with open(r'C:\Users\934\PycharmProjects\key\YaMetrik_token.txt') as f:
    TOKEN = f.readline().strip()


class YMBase:
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/x-yametrika+json',
            'User-Agent': 'Chrome'
        }


class YandexMetrika(YMBase):
    def __init__(self, token):
        self.token = token

    def get_counters(self):
        url = urljoin(self.MANAGEMENT_URL, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params={'pretty': 1})
        counters = response.json()['counters']
        return [Counter(self.token, i['id'], i['name'], i['status']) for i in counters]


class Counter(YMBase):
    def __init__(self, token, counter_id, counter_name=None, status=None):
        self.token = token
        self.id = counter_id
        self.name = counter_name
        self.status = status

    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': self.id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response.json()

    @property # тут по сути мы метод превращаем в атрибут
    def views(self):
        headers = self.get_headers()
        params = {
            'id': self.id,
            'metrics': 'ym:s:bounceRate,ym:s:pageDepth,ym:s:robotPercentage',
            'dimensions': 'ym:s:deviceCategory'
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response.json()['data']


def site_metrics_device():

    ys = YandexMetrika(TOKEN)
    counters = ys.get_counters()

    for k, counter in enumerate(counters, start=1):
        if counter.status == 'Active':
            try:
                print('{}. Сайт - {}, ID счетчика: {}'.format(k, counter.name, counter.id))
                for j in counter.views:
                    print('{}: показатель отказов - {:.2f}%; глубина просмотра - {:.2f}стр.; роботы - {:.2f}%'.format(
                        j['dimensions'][0]['name'], *j['metrics']))
                print('-------------------------')
            except:
               continue

site_metrics_device()

# def site_metrics_device():
#
#     ys = YandexMetrika(TOKEN)
#     counters = ys.get_counters()
#
#     for k, counter in enumerate(counters, start=1):
#         try:
#             print('{}. Сайт - {}, ID счетчика: {}'.format(k, counter[1], counter[0].id))
#             i = counter[0].views
#             for j in range(len(i)):
#                 print('{}: показатель отказов - {:.2f}%; глубина просмотра - {:.2f}стр.; роботы - {:.2f}%'.format(
#                     i[j]['dimensions'][0]['name'], *i[j]['metrics']))
#             print('-------------------------')
#         except:
#             continue
#
# site_metrics_device()