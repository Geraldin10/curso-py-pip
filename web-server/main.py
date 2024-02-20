import uvicorn
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def getList():
    return[1,2,3]

@app.get("/contacts", response_class=HTMLResponse)
def getContacts():
    return """ <h1> Soy una paginaWeb</h1>
    <p>Soy un parrafo </p>
    """

def run():
    uvicorn.run("main:app", reload=True)



if __name__ == '__main__':
    run()