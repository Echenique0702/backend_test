from fastapi import FastAPI

from core.config import settings

app = FastAPI()


##################################################################
####################### Users Endpoints ##########################
##################################################################

from routes.users import router as user_router
app.include_router(user_router, tags=['Users'], prefix=f'{settings.API_V1}/users')
