from typing import Dict

from pymongo import MongoClient

from app.core.config import cfg
from app.core.logger import logger


class StoreService:
    """
    Service for storing data into MongoDB data store.
    """

    # The mongo client
    _client: MongoClient = None

    def __init__(self):
        """
        Initializes tje StoreService based on the loaded configuration.
        """

        # Fetch mongo settings
        settings: Dict = cfg.get_mongo()

        # Load settings
        self.mongo_host = settings['host']
        self.mongo_port = settings['port']
        self.mongo_user = settings['user']
        self.mongo_password = settings['password']
        self.database = settings['database']
        self.collection = settings['collection']

    def client(self) -> MongoClient:
        """
        Returns the connected client for MongoDB.
        :return: the mongo client.
        """

        # Check if the client has already been opened
        if self._client is None:
            # If not, just do it
            self._client = MongoClient(
                f'mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/'
                f'?authMechanism=DEFAULT')
            logger.info('Client connected to mongo.')

        return self._client

    def store(self, content: Dict) -> None:
        """
        Stores the provided content into the configured collection.

        :param content: the content to store.
        :return: Nothing.
        """

        try:
            # Check if content was provided
            assert content is not None
            # Fetch the database
            db = self.client().get_database(self.database)
            # Fetch the collection
            collection = db.get_collection(self.collection)
            # And store the content
            collection.insert_one(content)

        except Exception as e:
            logger.error(f'Error: {e}')

    def search(self, q: str):
        """
        Searches for a given query in the database.
        :param q: the query to search for.
        :return: the list of documents that match the query.
        """
        to_return = []
        try:

            # Fetch the database
            db = self.client().get_database(self.database)
            # Fetch the collection
            collection = db.get_collection(self.collection)

            conditions = {'$or': [
                {'file_name': {'$regex': f".*{q}.*", '$options': 'i'}},
                {'content': {'$regex': f".*{q}.*", '$options': 'i'}}
            ]}

            results = collection.find(conditions)

            for result in results:
                to_return.append(result)

        except Exception as e:
            logger.error(f'Error: {e}')

        return to_return

    def get_by_external_id(self, external_id: int):
        """
        Searches for a given external_id in the database.
        :param external_id: the external_id to search for.
        :return: the document that matches the external_id.
        """

        to_return = None
        try:
            # Fetch the database
            db = self.client().get_database(self.database)
            # Fetch the collection
            collection = db.get_collection(self.collection)

            condition = {'file_external_id': {'$eq': external_id}}

            results = collection.find(condition)

            for result in results:
                if to_return is None:
                    to_return = result
                    break

        except Exception as e:
            logger.error(f'Error while searching by external_id [{external_id}]: {e}')

        return to_return


store_service = StoreService()
