from project.scripts.xlsx_parser import FileParser
from datetime import datetime
from project.database.functions import save_filedata_to_database, get_file_data_from_db
import os

__all__ = [
    "save_file_data_to_database",
    "get_file_path"
]


async def save_file_data_to_database(file):
    # unix time.
    time_now = int(datetime.now().timestamp())

    # create new file and append data.
    contents = await file.read()
    with open(f'../xlsx_files/{file.filename}_{time_now}.xlsx', "wb") as f:
        f.write(contents)

    # parse file.
    fp = FileParser()
    fp.get_file_data(file=f'../xlsx_files/{file.filename}_{time_now}.xlsx')
    fp.create_file_objects()

    # append data to database
    await save_filedata_to_database(filedata=fp.projects_list,
                                    file_name=f'{file.filename}_{time_now}.xlsx',
                                    loaded_date=time_now
                                    )


async def get_file_path(version: int):
    # get file data from database
    file_data = await get_file_data_from_db(version=version)
    if not file_data:
        return

    path = f'../xlsx_files/{file_data.file_name}'
    # if file not found.
    if not os.path.exists(path):
        return

    return path
