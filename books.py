from bs4 import BeautifulSoup
import requests
import csv 

url= 'http://books.toscrape.com/'
base_url = 'http://books.toscrape.com/catalogue/'
csv_filename = "books_data.csv"
res = requests.get(url)
print(res.status_code)

a= BeautifulSoup(res.text,'html.parser')
print(a)

#
with open(csv_filename,mode="w",newline="",encoding="utf-8")as file:
    writer=csv.writer(file)
    print("Saved")
    #Creating Columns in csv file
    writer.writerow(["title","price","stock_avaliablity","book_url","rating"])
    #Converting rating into integer
    def class_rating(class_list):
        
        ratings={
        "One":"1",
        "Two":"2",
        "Three":"3",
        "Four":"4",
        "Five":"5"
        }
        for cls in class_list:
            if cls in ratings:
                return ratings[cls]
           
        return "0"
    #Loop through all 50 pages
    for page in range(1,51):
        url=f"{base_url}page-{page}.html"
        response=requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod") 

        #Books
        for i in books:
            title=i.h3.a["title"]
            price=i.find("p",class_="price_color").text.strip()
            stock_avaliablity=i.find("p",class_="instock availability").text.strip()
            book_url=i.find("a")["href"]
            rating_tag=i.find("p",class_="star-rating")
            rating =class_rating(rating_tag["class"])if rating_tag else "0"
            

        # Creating rows for job under the each column specified
            writer.writerow([title,price,stock_avaliablity,book_url,rating])
print(f"\n All book data saved to '{csv_filename}'")            
    

    
