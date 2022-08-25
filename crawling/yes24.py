
import requests
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

client =  MongoClient('mongodb://localhost:27017/')
db = client.local
collection = db.yes24
#collection = db.yes24 (오류)   #새로운 collection 추가 하고 싶을 땐 
                        #컬렉션이 이미 있는 것처럼 키로 접근하여 사용하면자동으로 생성 됨

rows = collection.find()
for row in rows:
    print(row)
# res = requests.get("http://www.yes24.com/24/Category/BestSeller")
# soup = BeautifulSoup(res.text, "html.parser")

# for i in range(40):
#     idx = str(i+1)
#     if idx == "19":
#         idx = "19_line"  #19와 20은 숫자가 아닌 19_line으로 됨
#     elif idx == "20":
#         idx = "20_line"
        
#     sstr = "#bestList > ol > li.num" + idx +" > p:nth-child(3) > a"
#     ts = soup.select_one(sstr)

#     db.yes24.insert_one({
#         'Title' : ts.text
#     })
