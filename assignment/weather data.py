import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.weather.gov.hk/tc/cis/normal/1991_2020/seatemp.htm"
x_vals = []
y_vals = []

response = requests.get(url)
response.encoding = 'utf-8'  
soup = BeautifulSoup(response.text, 'html.parser')


tables = soup.find_all('table')

table = tables[0] if tables else None

if table is None:
    print("没有找到表格，请检查网页结构。")
else:
    month_mapping = {
        "一月": "January",
        "二月": "February",
        "三月": "March",
        "四月": "April",
        "五月": "May",
        "六月": "June",
        "七月": "July",
        "八月": "August",
        "九月": "September",
        "十月": "October",
        "十一月": "November",
        "十二月": "December"
    }

    for tr in table.find_all('tr')[1:]:  
        tds = tr.find_all('td')
        if len(tds) >= 2:  
            month = tds[0].text.strip()  
            mean_temp = tds[1].text.strip()  
            if month and mean_temp:
                x_vals.append(month_mapping.get(month, month)) 
                y_vals.append(float(mean_temp))  

    print("Months:", x_vals)
    print("Mean Temperatures:", y_vals)

    plt.figure(figsize=(10, 5))
    plt.bar(x_vals, y_vals, color='skyblue')
    plt.title('Monthly Mean Sea Surface Temperature (1991-2020)')
    plt.xlabel('Month')
    plt.ylabel('Mean Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()