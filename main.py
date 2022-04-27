from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.account.domain.model.User import User
from database import db
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from database.models import get_db, start_mappers
from app.account.application.controller.User import router as user_router
from app.catalog.application.controller.Product import router as product_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
import fastapi.openapi.utils as fu
from passlib.context import CryptContext


app = FastAPI(
    title="test"
)

app.include_router(user_router)
app.include_router(product_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fu.validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "detail": {"attribute": "Message", "attribute": "Message"}, 
    },
}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):

    errors = {}
    print( exc.errors())
    for error in exc.errors():
        errors[error['loc'][1]] = error['msg']

    return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": errors}),
        )

def create_first_user():
    session : Session = next(get_db())
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    user = session.query(User).count()

    if not user:
        session.add(User(name="admin", email="admin@admin.com", password=context.encrypt("Qwerty123")))
        session.commit()

@app.on_event("startup")
async def startup():
    await db.connect()
    start_mappers()
    load_dotenv()
    create_first_user()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()