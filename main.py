from src.apis import apis
from src.prisma import prisma
from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(apis, prefix="/apis")

@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


@app.get("/")
async def read_root():
  return {'hello'}