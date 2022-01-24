import requests

# res = requests.get("https://api.national-holidays.jp/2022/05")
# print(res.json())

def get_list(year, month = 0, day = 0):
  url = "https://api.national-holidays.jp/%d" % year
  if (month > 0):
    url += "/%02d" % month
    if (day > 0):
      url += "/%02d" % day
  req = requests.get(url)
  # print(req.json())
  return req.json()


def get_name(day):
  l = get_list(day.year, day.month, day.day)
  if 'name' in l:
    return l['name']


if __name__ == '__main__':
  from datetime import datetime
  print(get_name(datetime(2022, 5, 2)))
  print(get_name(datetime(2022, 5, 4)))
