import sys
import time
import requests
from bs4 import BeautifulSoup
try:
    page =  requests.get("https://twitter.com/sachin_rt")
except Exception as e:
    error_type, error_obj,error_info = sys.exc_info()
    print('ERROR FOR LINK:')
    print(error_type,'line:',error_info.tb_lineno)

time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
links = soup.find_all('div',attrs={'class':'css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj'}) 
print(links)
print(soup)
print(page)
for i in links:
    folowing = i.find('div',class_="css-1dbjc4n r-1mf7evn").text
    print(i.links)
    print(i.folowing)
    print("\n") 

#other website scraping


# import requests
# from bs4 import BeautifulSoup
# result = requests.get("https://secure.kelownachamber.org/Pools-Spas/Rocky%27s-Reel-System-Inc-4751")
# src = result.content
# soup = BeautifulSoup(src,'html.parser')
# divs  = soup.find_all("div",attrs={"class":"ListingDetails_Level1_HEADERBOXBOX"})
# for tag in divs:
#   try:
#    title = tag.find("a",attrs={"class":"ListingDetails_Level1_SITELINK"}).text
#    address = tag.find("span",attrs={"itemprop":"street-address"}).text
#    postal = tag.find("span",attrs={"itemprop":"postal-code"}).text
#    maincontact = tag.find("span",attrs={"class":"ListingDetails_Level1_MAINCONTACT"}).text
#    siteTag = tag.find("span",attrs={"class":"ListingDetails_Level1_VISITSITE"})
#    site = siteTag.find("a").attrs['href']
#    print(title)
#    print(address) 
#    print(postal)
#    print(maincontact)
#    print(site)
#   except:
#    pass