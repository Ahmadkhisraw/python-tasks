import re
import urllib.request
import csv

def get_html_content(url):
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

def extract_data(html_content):
    name_pattern = re.compile(r'<h1>(.*?)</h1>')
    address_pattern = re.compile(r'<span itemprop="address">(.*?)</span>')
    phone_pattern = re.compile(r'<a class="tel" href="tel:(.*?)">')
    hours_pattern = re.compile(r'<strong>Часы работы:</strong>(.*?)</div>')

    name = re.search(name_pattern, html_content).group(1)
    address = re.search(address_pattern, html_content)
    phones = re.findall(phone_pattern, html_content)
    hours = re.search(hours_pattern, html_content)

    return name, address, ', '.join(phones), hours

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Address', 'Phones', 'Hours']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerow({'Name': data[0], 'Address': data[1], 'Phones': data[2], 'Hours': data[3]})

filename = "avtoservisy.csv"
url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"

html_content = get_html_content(url)
extracted_data = extract_data(html_content)

save_to_csv(extracted_data, filename)