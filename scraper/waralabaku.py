import time
from selenium import webdriver

# Selenium accesses the Chrome browser driver in incognito mode and
# without actually opening a browser window(headless argument).
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# insert the waralaba's website of one attraction
driver = webdriver.Chrome("path/of/driver", options=options)


def get_page_link():
    list_data = []
    for s in range(1, 43):
        driver.refresh()
        driver.get('https://waralabaku.com/for_index.php?p={}#jump_head'.format(s))
        french = driver.find_elements_by_class_name('direktori')
        for i in french:
            a_href = i.find_element_by_class_name('direktori_title')
            try:
                link = a_href.find_element_by_tag_name('a').get_attribute('href')
                list_data.append(link)
            except:
                continue
        time.sleep(1)
    return list_data


def get_dict_data(link_param):
    driver.refresh()
    driver.get(link_param)
    product = driver.find_element_by_class_name('tabel_profil').find_elements_by_tag_name('tr')
    dict_product = {}
    for j in product:
        column = j.find_elements_by_tag_name('td')
        for k in column:
            try:
                name = k.find_element_by_tag_name('b').text
                value = k.find_element_by_class_name('tabel_profil_ket').text
                dict_product[name] = value
            except:
                continue
    href_contact = driver.find_element_by_link_text('Kontak').get_attribute('href')
    driver.refresh()
    driver.get(href_contact)
    contact = driver.find_element_by_class_name('table_kontak').find_elements_by_tag_name('tr')
    for l in contact:
        try:
            name = l.find_element_by_class_name('kontak_left').text
            value = l.find_element_by_class_name('kontak_right').text.replace('\n', ' ')
            dict_product[name] = value
        except:
            continue
    # print(dict_product)
    return dict_product
