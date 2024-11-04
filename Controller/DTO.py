from fastapi import FastAPI
from typing import List

def create_routes(app: FastAPI, URLs: List[tuple]):
    for url in URLs:
        if url[0] == 'GET':
            app.get(url[1])(url[2])
        if url[0] == 'POST':
            app.post(url[1])(url[2])
