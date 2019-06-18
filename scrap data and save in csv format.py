from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.programmableweb.com/apis/directory"
api_no = 0
api={}

while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    row = soup.find('tr',{'class':'odd views-row-first'})
    api_name = row.find('td',{'class':'views-field views-field-title col-md-3'}).text
    api_link = row.find('a').get('href')
    api_category_tag = row.find('td',{'class':'views-field views-field-field-article-primary-category'})
    api_category = api_category_tag.text if api_category_tag else "N/A"
    api_description = row.find('td',{'class':'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'}).text
    api_no = api_no +1
    api[api_no] = [api_name,api_link,api_category,api_description]
    row_even = soup.find_all('tr',{'class':'even'})

    for i in row_even:
        api_name = i.find('td',{'class':'views-field views-field-title col-md-3'}).text
        api_link = i.find('a').get('href')
        api_category_tag = i.find('td',{'class':'views-field views-field-field-article-primary-category'})
        api_category = api_category_tag.text if api_category_tag else "N/A"
        api_description = i.find('td',{'class':'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'}).text
        api_no = api_no +1
        api[api_no] = [api_name,api_link,api_category,api_description]


    row_odd = soup.find_all('tr',{'class':'odd'})

    for j in row_even:
        api_name = j.find('td',{'class':'views-field views-field-title col-md-3'}).text
        api_link = j.find('a').get('href')
        api_category_tag = i.find('td',{'class':'views-field views-field-field-article-primary-category'})
        api_category = api_category_tag.text if api_category_tag else "N/A"
        api_description = j.find('td',{'class':'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'}).text
        api_no = api_no +1
        api[api_no] = [api_name,api_link,api_category,api_description]

    url_tag = soup.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
            url= 'https://www.programmableweb.com' + url_tag.get('href')
            print(url)
    else:
            break

print("Total API's", api_no)

api_df = pd.DataFrame.from_dict(api, orient = 'index', columns = ['API Name','API link','API Category', 'API Description'])
api_df.head()
api_df.to_csv('api.csv')
