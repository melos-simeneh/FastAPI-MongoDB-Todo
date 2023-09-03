# Todo using FastAPI and MongoDB
## Prerequisites
1. FastAPI basics
2. Python installed
3. Mongodb Community server installed
## Install Dependencies
1. fastAPI
2. uvicorn
3. pymongo
```
$ pip install fastapi uvicorn pymongo pymongo[srv]
```
## Run server
```
$ uvicorn main:app --reload
```
this will start the app on http://127.0.0.1:8000
