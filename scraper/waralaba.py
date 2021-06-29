import pandas as pd
from selenium import webdriver

# Selenium accesses the Chrome browser driver in incognito mode and
# without actually opening a browser window(headless argument).
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# insert the waralaba's website of one attraction
driver = webdriver.Chrome("path/of/driver", options=options)


def get_page_link(page):
    page = page
    links = []
    # insert the waralaba's website of one attraction
    try:
        driver.get("https://www.waralaba.com/index.html?search_options="
                   "YTo2OntzOjEyOiJzZWFyY2hfbGltaXQiO2k6MTA7czoxNDoic2Vhc"
                   "mNoX29wdGlvbnMiO2E6NTp7czoyMToic2VhcmNoX2NyZWF0ZWRfZmls"
                   "dGVyIjtpOjE7czoxOToic2VhcmNoX3N0YXR1c19saW1pdCI7aToxO3M6"
                   "MTA6InNlYXJjaF9jaWQiO3M6Mzg6IjYsNyw5LDEwLDExLDEyLDEzLDE0LD"
                   "E1LDE2LDE3LDE4LDE5LDIwIjtzOjEzOiJzZWFyY2hfdGFnX2lkIjtzOjMyO"
                   "iIxMDQsMTA1LCAxMDYsMTA3LDEwOCwxMDksMTEwLDExMSI7czoxNDoiZ2VuZX"
                   "JpY19zZWFyY2giO2E6MDp7fX1zOjE0OiJzZWFyY2hfc29ydF9ieSI7czo5OiJv"
                   "cmRlcl9udW0iO3M6MTI6InNlYXJjaF9vcmRlciI7czoxMDoiZGVzY2VuZGluZyI7"
                   "czo2OiJvZmZzZXQiO2k6MDtzOjE4OiJzZWFyY2hfZG9fYWR2YW5jZWQiO2I6MTt9&pg={}".format(page))
        french_link = driver.find_elements_by_id('latest_news')

        if french_link:
            for i in french_link:
                links.append(i.find_elements_by_tag_name('a')[0].get_attribute('href'))
    except:
        raise
    return links


def get_attributes(links):
    list_data = []
    page = 1
    for link in links:
        try:
            driver.get(link)
            dict_data = dict()
            attrs = driver.find_elements_by_class_name('featured_franchise')[0] \
                .find_elements_by_tag_name('p')[0].text.split('\n')
            if attrs:
                for attr in attrs:
                    attr = attr.split(':')
                    dict_data[attr[0]] = attr[1].strip()
            list_data.append(dict_data)
            print('Success process link {} : {}'. format(page, link))
            page = page + 1
        except:
            continue
    return list_data
