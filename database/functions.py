import asyncio
import datetime

import sqlalchemy.exc
from project.database.connector import get_session
from sqlalchemy import select, insert, update
from project.database.models import Version, Value, Project
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from project.schemes.schemes import ProjectScheme


def database_connector(func):
    # Get session before function
    # commit + close session after function.
    async def wrapper(*args, **kwargs):
        if not asyncio.iscoroutinefunction(func):
            # if function not async.
            raise ValueError("Decorator must be used for async functions!")

        session = await get_session()
        func_ = await func(session=session, *args, **kwargs)
        await session.commit()
        await session.close()
        return func_

    return wrapper


@database_connector
async def save_filedata_to_database(session: AsyncSession, filedata: List[ProjectScheme], file_name: str, loaded_date: int):
    await session.execute(insert(Version).values(file_name=file_name,
                                                 loaded_date_unix=loaded_date))
    for project in filedata:
        await session.execute(
            insert(Project).values(code=project.code,
                                   project_name=project.project_name)
        )
        for date, value in project.project_data.items():
            await session.execute(insert(Value).values(
                project_code=project.code,
                date=datetime.datetime.strptime(date, '%Y-%m-%d'),
                plan=value['plan'],
                fact=value['fact']
            ))

    return True


@database_connector
async def get_file_data_from_db(session: AsyncSession, version: int):
    result = await session.execute(select(Version).where(Version.id == version))
    return result.scalar()
