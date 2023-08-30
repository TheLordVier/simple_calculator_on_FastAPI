from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create a Jinja2Templates instance with the templates directory
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the "form.html" template with the provided context
    """
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def calculate(request: Request, expression: str = Form(...)):
    """
    Evaluate the expression provided by the user
    Render the "result.html" template with the result and context
    Render the "error.html" template with the error message and context
    """
    try:
        result = eval(expression)
        return templates.TemplateResponse("result.html", {"result": result, "request": request})
    except Exception as e:
        return templates.TemplateResponse("error.html", {"error_message": str(e), "request": request})
