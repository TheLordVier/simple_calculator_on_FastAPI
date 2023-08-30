# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# import os
#
# app = FastAPI()
# templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "templates"))
#
#
# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request})
#
#
# @app.post("/", response_class=HTMLResponse)
# async def calculate(request: Request, expression: str = Form(...)):
#     try:
#         result = eval(expression)
#         return templates.TemplateResponse("result.html", {"result": result})
#     except Exception as e:
#         return templates.TemplateResponse("error.html", {"error_message": str(e)})

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def calculate(request: Request, expression: str = Form(...)):
    try:
        result = eval(expression)
        return templates.TemplateResponse("result.html", {"result": result, "request": request})
    except Exception as e:
        return templates.TemplateResponse("error.html", {"error_message": str(e), "request": request})
