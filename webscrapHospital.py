import requests
from bs4 import BeautifulSoup
import pandas as pd

class Hospital:
    
    def hospital_data(self):
    
        base_url="https://www.mouthshut.com/Hospitals-and-Clinics-ProID-925757"
        h_names=[]
        h_ratings=[]
        h_votes=[]
        h_recommended=[]
        hospital_links=[]
        address=[]
        for page in range(1,5):
            url=base_url+"-page-"+str(page)
            response=requests.get(url,verify=False)
            content=response.text
            soup=BeautifulSoup(content,"html.parser")
            
            for h_details in soup.find_all('div',class_="card-body"):
                for h_name in h_details.find_all('a',class_="text-truncate"):
                    h_names.append(h_name.text.strip('\n\n\r\n                            '))
                for h_rating in h_details.find_all('span',class_="rating-no"):
                    h_ratings.append(h_rating.text)
                for h_vote in h_details.find_all('a',class_="review-no"):
                    h_votes.append(h_vote.text)
                for h_rec in h_details.find_all('span',class_="recommended-no"):
                    h_recommended.append(h_rec.text)
                for h_link in h_details.find_all('a',class_="text-truncate"):
                    link=h_link.get('href')
                    res1=requests.get(link,verify=False)
                    con=res1.text
                    s=BeautifulSoup(con,'html.parser')
                    for data in s.find_all('div',class_="product-info"):
                        for addr in data.find_all('p',class_="info-div"):
                            address.append(addr.text.strip( ))
                    
                    
                    hospital_links.append(link)
                    
        
        dic={'Hospital Name':h_names,'Rating':h_ratings,'Review':h_votes,'Recommended':h_recommended,'Website':hospital_links}   
        
        df=pd.DataFrame(dic) 
        
obj=Hospital()
obj.hospital_data()
#print(df)    
        
    
    
    