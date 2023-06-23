from typing import List

import langdetect
from deep_translator import GoogleTranslator

from intranet_core.settings import logger


class TranslatedText:
    def __init__(self, text, language):
        self.text = text
        self.language = language

    def __str__(self):
        return self.text


def _other_language(language: str) -> str:
    if language.lower() == 'fr':
        return 'nl'
    return 'fr'


class TranslationService:
    @staticmethod
    def _translator(src_lang: str, dst_lang: str) -> GoogleTranslator:
        """
        Returns a translator object.
        :param src_lang: the source language.
        :param dst_lang: the destination language.
        :return: a translator object.
        """

        return GoogleTranslator(source=src_lang, target=dst_lang)

    @staticmethod
    def translations_as_dict(translations: List[TranslatedText]) -> dict:
        """
        Returns a dictionary of translations.
        :param translations: the list of translations.
        :return: a dictionary of translations.
        """

        return {translation.language: translation.text for translation in translations}

    def translate(self, text) -> List[TranslatedText]:
        """
        Translate a text into all the languages supported by the system.

        :param text: the text to translate.
        :return: a list of TranslatedText objects.
        """

        try:
            # Detect the language of the text
            text_lang = langdetect.detect(text)
            # If the language is not supported, use French
            if text_lang not in ('fr', 'nl'):
                text_lang = 'fr'
        except Exception as e:
            logger.error(f'Error while detecting the language of the text: {e}')
            raise e

        # Initialize the list of translated texts
        translated_texts = [TranslatedText(text=text, language=text_lang)]

        # Find the other language
        other_language = _other_language(text_lang)
        try:
            # Translate the text
            translated_value = self._translator(text_lang, other_language).translate(text)
        except Exception as e:
            logger.error(f'Error while translating the text: {e}')
            translated_value = text

        # Add the translated text to the list
        translated_texts.append(TranslatedText(text=translated_value, language=other_language))

        return translated_texts
