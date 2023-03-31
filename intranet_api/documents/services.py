import mimetypes

import requests

from documents.models import Document


class SilvaSearchService:
    """
    Service to process documents and search in Silva Intranet.
    """

    def __init__(self):
        """
        Initializes the SilvaSearchService based on the loaded configuration.
        """

        # Fetch silva settings
        from intranet_core import settings
        self.process_url = settings.SILVA_SEARCH_PROCESS_URL
        self.search_url = settings.SILVA_SEARCH_URL

    def process(self, _document: Document) -> None:
        """
        Processes the provided content and returns the result.

        :param _document: the document to process.
        :return: Nothing.
        """

        # Check if content was provided
        assert _document is not None

        if self.check_processed(_document):
            return

        # Determine the MIME type of the file
        content_type, encoding = mimetypes.guess_type(_document.fileUrl.path)

        # Prepare the file for the POST request to the FastAPI endpoint
        file_data = {'file': (_document.get_filename(), _document.fileUrl.file, content_type)}

        # Create the request
        request = requests.post(f'{self.process_url}/{_document.id}', files=file_data)

        # Check if the request was successful
        if request.status_code != 201:
            # If not, raise an exception
            raise Exception(f'Failed to process document: {request.text}')

        # Get out of here
        return

    def check_processed(self, _document: Document) -> bool:
        """
        Checks if the provided document has been processed.
        :param _document: the document to check.
        :return: True if the document has been processed, False otherwise.
        """

        # Check if content was provided
        assert _document is not None

        # Create the request
        request = requests.get(self.process_url, params={
            'external_id': _document.id,
        })

        # Check if the request was successful
        if request.status_code != 200:
            # If not, raise an exception
            raise Exception(f'Failed to check document: {request.text}')

        try:
            # Return the result
            return request.json() == _document.get_filename()
        except Exception as e:
            from intranet_core.settings import logger
            logger.error(f'Error: {e}')
            return False

    def search(self, _q: str) -> list[Document]:
        """
        Searches for a given query in the database.
        :param _q: the query to search for.
        :return: the list of documents that match the query.
        """

        # Create the request
        request = requests.get(self.search_url, params={
            'q': _q,
        })

        # Check if the request was successful
        if request.status_code != 200:
            # If not, raise an exception
            raise Exception(f'Failed to search for documents: {request.text}')

        # Process the results
        document_ids = request.json()
        # Return the list of documents
        return list(Document.objects.filter(id__in=document_ids).all())


silva_search_service = SilvaSearchService()
