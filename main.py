import uvicorn
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
from users.views import router as users_router

app = FastAPI()
app.include_router(users_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
