from datetime import datetime
from typing import Optional, Union
from uuid import UUID
from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import PortalRole, User


import uuid

class UserDAL:
  def __init__(self, db_session: AsyncSession):
    self.db_session = db_session
  
  async def create_user(
      self,
      login: str,
      email: str,
      # first_name: str,
      # middle_name: str,
      # last_name: str,
      hashed_password: str
      ) -> User:
    new_user = User(
      login=login,
      email=email,
      # first_name=first_name,
      # middle_name=middle_name,
      # last_name=last_name,
      hashed_password=hashed_password,
    )

    self.db_session.add(new_user)
    await self.db_session.flush()
    return new_user
  
  # async def delete_user(self, id: UUID) -> Union[UUID, None]:
  #   query = update(User).where(and_(User.id == id, User.is_active == True)).values(is_active = False).returning(User.id)
  #   result = await self.db_session.execute(query)
  #   remote_user_id = result.fetchone()
  #   if remote_user_id is not None:
  #     return remote_user_id[0]
  
  # async def update_user(self, id: UUID, update_user_params: dict) -> Union[UUID, None]:
  #   query = update(User).where(and_(User.id == id, User.is_active == True)).values(update_user_params).returning(User.id)
  #   result = await self.db_session.execute(query)
  #   update_user_id = result.fetchone()
  #   if update_user_id is not None:
  #     return update_user_id[0]

  async def get_user_by_id(self, id: UUID) -> Union[User, None]:
    query = select(User).where(User.id == id)
    result = await self.db_session.execute(query)
    user_row = result.fetchone()
    if user_row is not None:
      return user_row[0]
  
  async def get_user_by_login(self, login: str) -> Union[None, User]:
    query = select(User).where(User.login == login)
    result = await self.db_session.execute(query)
    user_row = result.fetchone()
    if user_row is not None:
      return user_row[0]


