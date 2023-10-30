from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, REAL
from sqlalchemy.ext.asyncio import AsyncAttrs
import datetime


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Version(Base):
    """
    SQLAlchemy model for table version.
    """

    __tablename__ = "Version"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    file_name: Mapped[str] = mapped_column(
        VARCHAR(256)
    )

    loaded_date_unix: Mapped[float] = mapped_column(
        default=datetime.datetime.now()
    )

    def __str__(self) -> str:
        return f"{self.file_name}"


class Project(Base):
    """
    SQLAlchemy model for table project.
    """

    __tablename__ = "project"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    code: Mapped[int] = mapped_column(
        unique=True, index=True
    )

    project_name: Mapped[str] = mapped_column(
        VARCHAR(128), index=True
    )

    def __str__(self) -> str:
        return f"{self.project_name}"


class Value(Base):
    """
    SQLAlchemy model for table value
    """

    __tablename__ = "value"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    project_code: Mapped[int] = mapped_column(
        ForeignKey(
            column="project.code",
            ondelete="CASCADE",
            onupdate="CASCADE",  # category (FK to project table)
        )
    )
    date: Mapped[datetime.datetime] = mapped_column()
    plan: Mapped[float] = mapped_column()
    fact: Mapped[float] = mapped_column()

    def __str__(self) -> str:
        return f"{self.project_code} | {self.date}"
