import os

from fastapi import APIRouter, UploadFile, File
from tika import parser

from app.core.logger import logger
from app.services.store_service import store_service

# Create the router for processing
router = APIRouter(
    prefix='/process'
)


def get_processing_folder() -> str:
    """
    Returns the folder where the files are processed.
    :return: the folder where the files are processed.
    """

    temp_folder = os.getcwd() + '/processing_folder'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    return temp_folder


@router.post('/{external_id}', status_code=201)
async def process_file(external_id: int, file: UploadFile = File(...)):
    """
    Processes a file and stores it in the database.
    :param external_id: the external id of the file.
    :param file: the file to process.
    :return: the result of the processing.
    """

    # Create the file to process
    file_to_process = os.path.join(get_processing_folder(), file.filename)

    try:
        # Write it to the file system
        with open(file_to_process, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception as e:
        # If there was an error, log it and return an error message
        logger.error(f'Error: {e}')
        return {"message": "There was an error uploading the file"}
    finally:
        # Close the file
        file.file.close()

    logger.info(f'File {file_to_process} : {file.content_type}')

    # Parse the file
    content = parser.from_file(file_to_process)

    # Check if the file was parsed successfully
    if 'content' in content:
        # If so, build the object to store
        to_store = {
            'file_external_id': external_id,
            'file_name': file.filename,
            'file_type': file.content_type,
            'content': str(content['content'])
        }
        # Store the object
        store_service.store(to_store)

    # Remove the file from the file system
    os.remove(file_to_process)

    # Return the result
    return {'message': f'file stored at {file_to_process}'}


@router.get('', status_code=200)
async def check_file_processing(external_id: int):
    """
    Checks if a file has been processed.
    """

    # Fetch the related file
    related_file: dict = store_service.get_by_external_id(external_id)

    # Check if the file was found
    if related_file is not None:
        # If so, return the file name
        return related_file.get('file_name', '').replace('"', '')

    # Otherwise, return None
    return None
