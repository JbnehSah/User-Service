from fastapi.testclient import TestClient
import pytest
import asyncio
from prisma import Prisma, register

from main import app

prisma = Prisma()
prisma.connect()
register(prisma)
client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
async def test_init(request):
  await prisma.connect()
  yield
  await prisma.disconnect()


@pytest.mark.asyncio
async def test_find_users():
  response = client.get("/apis/users")
  assert response.status_code == 200


@pytest.mark.asyncio
async def test_find_user():
  response = client.get("/apis/users/1")
  assert response.status_code == 200

@pytest.mark.asyncio
async def test_create_user():
     payload = {
      "email": "string7",
      "contacts": [
        {
        "email": "string8",
        },
        {
        "email": "string9",
        }
      ]
     }
     
     response = client.post("/apis/users", payload)
     assert response.status_code == 201

