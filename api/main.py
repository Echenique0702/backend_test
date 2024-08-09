from fastapi import FastAPI

from core.config import settings

app = FastAPI()


##################################################################
####################### Users Endpoints ##########################
##################################################################

from routes.users import router as user_router
app.include_router(user_router, tags=['Users'], prefix=f'{settings.API_V1}/users')



##################################################################
####################### Friendship Endpoints ##########################
##################################################################

from routes.friendship import router as friendship_router
app.include_router(friendship_router, tags=['Friendship'], prefix=f'{settings.API_V1}/friendships')
