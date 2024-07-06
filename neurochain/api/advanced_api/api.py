from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from fastapi.lifespan import Lifespan
from fastapi.tracing.utils import get_distributed_tracing
from fastapi.tracing.middlewares import DistributedTracingMiddleware

app = FastAPI(
    title="NeuroChain API",
    description="API for NeuroChain project",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/healthcheck")
async def healthcheck():
    return {"message": "API is healthy"}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        user.username, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends()):
    return current_user

@app.get("/items/{item_id}")
async def read_item(item_id: int, current_user: User = Depends()):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
async def create_item(item: Item, current_user: User = Depends()):
    item = create_item(item)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, current_user: User = Depends()):
    item = update_item(item_id, item)
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, current_user: User = Depends()):
    delete_item(item_id)
    return {"message": "Item deleted"}
