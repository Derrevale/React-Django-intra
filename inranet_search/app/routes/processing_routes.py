import os

from fastapi import APIRouter, UploadFile, File
from tika import parser

from app.core.logger import logger
from app.services.store_service import store_service

router = APIRouter(
    prefix='/process'
)


def get_processing_folder():
    temp_folder = os.getcwd() + '/processing_folder'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    return temp_folder


@router.post('/{external_id}', status_code=201)
async def process_file(external_id: int, file: UploadFile = File(...)):
    file_to_process = os.path.join(get_processing_folder(), file.filename)

    try:
        with open(file_to_process, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception as e:
        logger.error(f'Error: {e}')
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    logger.info(f'File {file_to_process} : {file.content_type}')

    content = parser.from_file(file_to_process)
    if 'content' in content:
        to_store = {
            'file_external_id': external_id,
            'file_name': file.filename,
            'file_type': file.content_type,
            'content': str(content['content'])
        }
        store_service.store(to_store)

    os.remove(file_to_process)

    return {'message': f'file stored at {file_to_process}'}


@router.get('', status_code=200)
async def check_file_processing(external_id: int):
    return store_service.get_by_external_id(external_id) is not None
