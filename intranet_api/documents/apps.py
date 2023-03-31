from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'documents'

    def ready(self):
        """
        This method is called when the app is ready to be used.
        """

        # Import here to avoid circular imports (and runtime insults)
        import documents.models as models
        import documents.services as services
        from intranet_core.settings import logger

        # Initialize some working variables
        counter = 0
        errors = 0

        # Loop on the unprocessed documents
        for document in models.Document.objects.filter(processed=False).all():
            try:
                # Process the document
                services.silva_search_service.process(document)
                # Mark the document as processed
                document.processed = True
                # Save the document
                document.save()
                # Increment the counter
                counter += 1
            except Exception as e:
                logger.error(f'Error while processing document {document.name}: {e}')
                errors += 1

        logger.info(f'Processed {counter} documents with {errors} errors.')
