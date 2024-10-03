from fastapi import FastAPI
from src import models, databases, routers

# Создаем таблицы в базе данных (если их нет)
models.Base.metadata.create_all(bind=databases.engine)

app = FastAPI()

# Подключаем маршруты
app.include_router(routers.router)
