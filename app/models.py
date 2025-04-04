from sqlalchemy import Integer, String, Boolean, Column, Date, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional

from app.database import Base

from datetime import datetime, date, timezone

from time import time

class User(Base):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key = True)
    name = Column(String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32), unique=True)
    first_name: Mapped[str] =mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthday: Mapped[date] = mapped_column(Date)
    join_at: Mapped[bool] = mapped_column(DateTime, default=datetime.now(timezone.utc) )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)




class Participation(Base):
    __tablename__="participations"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        type_=Integer,
        nullable=True
    )
    user: Mapped[Optional["User"]] = relationship("User")


    game_id: Mapped[int] = mapped_column()
    start_time: Mapped[time.time]
    end_time: Mapped[time.time] = mapped_column(nullable=True)
    gained_score: Mapped[int] = mapped_column(default=0)
    registered_at: Mapped[datetime]


class Game(Base):
    __tablename__='games'

    id: Mapped[int] = mapped_column(primary_key=True)

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user_id"),
        type_=Integer,
        nullable=True
    )

    owner: Mapped[Optional["User"]] = relationship("User")
    topic_id: Mapped[int] = mapped_column()













































