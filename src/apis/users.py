from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.prisma import prisma
import json

router = APIRouter()

class Contact(BaseModel):
    email: str
    name: str      | None = None
    phone: str     | None = None
    role: str      | None = None
    notes: str     | None = None
    contactId: int | None = None

class User(BaseModel):
    email: str
    name: str      | None = None
    phone: str     | None = None
    contacts: List[Contact] #email is unique key


@router.get("/users", tags=["users"])
async def read_users():
  result = await prisma.user.find_many(
        include= {
    'contacts': True,
  })
  return result


@router.get("/users/{userId}", tags=["users"])
async def find_user_by_id(userId: int):
    user = await prisma.user.find_unique(
    where= {
        'id': userId
  },
  include= {
    'contacts': True,
  }
)
    return user

    
@router.get("/users/mail/{email}", tags=["users"])
async def find_user(email: str):
    user = await prisma.user.find_unique(
    where= {
        'email': email
    },
    include= {
    'contacts': True,
  }
)
    return user


@router.post("/users/create", tags=["users"])
async def user_and_contact(user:User):

  list_of_contacts = user.contacts

  contact_list = []
  for i in range(len(list_of_contacts)):
    temp = list_of_contacts[i]
    create = {'email': temp.email,'role': temp.role, 'notes': temp.notes, 'contactId': temp.contactId}
    where =  {'email': temp.email}
    contact_list.append({'where': where, 'create': create})  
  print(contact_list)
  
  created_user = await prisma.user.create(
  data = {
    'email': user.email,
    'name':  user.name,
    'phone': user.phone,
    'contacts': {
      'connectOrCreate': 
      contact_list,
    },
  },
  ),

  for i in range(len(list_of_contacts)):
    temp = list_of_contacts[i]
    from_email = await find_user(temp.email)
    if from_email == None:

      created_user_from_contact = await prisma.user.create(
      data= {
        'email': temp.email,
        'name' : temp.name,
        'phone': temp.phone,
        },
      )

      await prisma.contact.update(
      where= {'email': temp.email},
      data= { 'contactId':  created_user_from_contact.id}
      )
       
    else:
      await prisma.contact.update(
      where= {'email': temp.email},
      data= { 'contactId': from_email.id}
      )
    
  return await find_user(user.email)