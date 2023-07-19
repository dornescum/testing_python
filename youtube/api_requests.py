from pandas.io.formats.style_render import format_table_styles
import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint, x):
      r =  requests.get(baseurl + endpoint + f'?page={x}')
      return r.json()


def get_pages(response):
      pages = response['info']['pages']
      return pages


def parse_json(response):
     charlist = []
     for item in response['results']:
          # print(item)
      # name = response['results'][0]['name']
      # episodes = response['results'][0]['episode']
          char = {
          'id' : item['id'],
          'name': item['name'],
          'no_ep': len(item['episode'])
          # 'no_ep': item['episode']
          }
          charlist.append(char)
     return charlist


# print(r.json())
mainlist = []
data = main_request(baseurl, endpoint, 1)
for x in range(1, get_pages(data)+1):
      # print(x)
      mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))


df = pd.DataFrame(mainlist)

df.to_csv('charlist.csv', index=format_table_styles)

# print(df)
# print(df.head(), df.tail())

# print(len(mainlist))

# print(get_pages(data))
# parse_json(data)

# info{pagination}
# print(data['info'])
# pages = data['info']['pages']

# name = data['results'][0]['name']
# episodes = data['results'][0]['episode']

# print(parse_json(data))

