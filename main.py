from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.user.router import user_router
from api.auth.router import login_router 


import uvicorn

app = FastAPI(title='auth-app')

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/register", tags=['user'])
main_api_router.include_router(login_router, prefix="/login", tags=['login'])


app.include_router(main_api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",  # Разрешить все источники (можно указать конкретные домены)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
 
if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False, access_log=True)