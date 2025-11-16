import re
import csv
from urllib.request import urlopen

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
html = urlopen(url).read().decode("utf-8", errors="ignore")

name_pattern = r'class="org-widget-header__title-link">([^<]+)'
names = re.findall(name_pattern, html)

address_pattern = r'org-widget-header__meta org-widget-header__meta--location">\s*([^<]+)'
addresses = re.findall(address_pattern, html)

phone_pattern = r'<dt class="spec__index"><span class="spec__index-inner">Телефон</span></dt>\s*<dd class="spec__value">([^<]+)'
phones = re.findall(phone_pattern, html)

hours_pattern = r'<dt class="spec__index"><span class="spec__index-inner">Часы работы</span></dt>\s*<dd class="spec__value">([^<]+)'
hours = re.findall(hours_pattern, html)


max_len = max(len(names), len(addresses), len(phones), len(hours))

def pad(lst):
    lst = lst[:max_len]
    while len(lst) < max_len:
        lst.append("")
    return lst

names = pad(names)
addresses = pad(addresses)
phones = pad(phones)
hours = pad(hours)

with open("data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Название", "Адрес", "Телефон", "Часы работы"])
    for i in range(max_len):
        writer.writerow([names[i], addresses[i], phones[i], hours[i]])

print("ГОТОВО! Найдено организаций:", max_len)
