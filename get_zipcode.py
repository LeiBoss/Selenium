from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('http://www.ip138.com/post/')

a=driver.find_elements_by_css_selector('div#newAlexa a')

url_dic={}
fo = open("zipcode.txt", "w",encoding='utf-8')
for url in a:
    url_dic[url.text]=url.get_attribute('href')
    #print(url.text)
    #print(url.get_attribute('href'))
    #driver.get(url.get_attribute('href'))
    #tr_list= driver.find_elements_by_css_selector('table.t12 tr')
    #driver.quit()

for item in url_dic:
    print(item+':'+url_dic[item])
    fo.writelines(item+':'+url_dic[item]+'\n')
    driver.get(url_dic[item])
    tr_list= driver.find_elements_by_css_selector('table.t12 tr[bgcolor="#ffffff"]')
    for tr in tr_list:
        td_list=tr.find_elements_by_tag_name('td')
        i=0
        while i < len(td_list):
            if(i+1<len(td_list)):
                if(td_list[i].text.strip()):
                    print(td_list[i].text+':'+td_list[i+1].text)
                    fo.writelines(td_list[i].text+':'+td_list[i+1].text+'\n')
                    
            i=i+3        
    print('-------------------------------------------------')
    fo.writelines('-------------------------------------------- \n')
    

fo.close()
'''
driver.get('http://www.ip138.com/65/')
tr_list= driver.find_elements_by_css_selector('table.t12 tr[bgcolor="#ffffff"]')
for tr in tr_list:
     td_list=tr.find_elements_by_tag_name('td')
     i=0
     
     while i < len(td_list):
        if(i+1<len(td_list)):
            if(td_list[i].text.strip()):
                print(td_list[i].text+':'+td_list[i+1].text)
                fo.writelines(td_list[i].text+':'+td_list[i+1].text+'\n')
        i=i+3
'''

#print(type(a))
#print(a)

driver.quit()