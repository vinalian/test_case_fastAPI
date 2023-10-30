from fastapi import APIRouter, HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from project.app.misc.misc import *

router = APIRouter()


@router.post(path='/send_file', name='get file from user')
async def get_file_form_user(file: UploadFile):
    if file.filename.split('.')[-1] != 'xlsx':
        return HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    # save data to database.
    answer = await save_file_data_to_database(file=file)


@router.get(path='/upload_file', name='send file to user')
async def upload_file(version: int):
    file_path = await get_file_path(version=version)

    if not file_path:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return FileResponse(path=file_path, filename=file_path.split('/')[-1], media_type='multipart/form-data')


