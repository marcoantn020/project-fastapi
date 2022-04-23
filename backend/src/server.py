from fastapi import FastAPI, Depends, Request, BackgroundTasks
from src.jobs.write_notification import write_notification
from fastapi.middleware.cors import CORSMiddleware
from src.routes import (
    product_routes,
    user_routes,
    order_routes
)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("chegada.....")

    response = await call_next(request)

    print('volta....')

    return response

app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="notificação enviada")
    return {"message": "ok"}
