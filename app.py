from typing import Union


from pymongo import MongoClient

app=FastAPI()

conn=MongoClient("mongodb+srv://kritirajsingh585_db_user:iOo91VnwmHWl0QGC@cluster0.wymh9kr.mongodb.net/notes")





if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)