import json

from Python.src.quiz.language_handler import get_quiz_translation
from Python.src.util.constants import ROOT_DIR


def load_quiz(topic: str, language: str) -> dict:
    quiz: dict = _get_quiz_by_topic(topic)
    translation: dict = get_quiz_translation(language)

    return _translate_quiz(quiz, translation)


def _get_quiz_by_topic(topic: str) -> dict:
    with open(f'{ROOT_DIR}/resources/data/quiz/{topic}.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def _translate_quiz(quiz: dict, translation: dict):
    if isinstance(quiz, str):
        return translation.get(quiz, quiz)

    elif isinstance(quiz, list):
        return [_translate_quiz(item, translation) for item in quiz]

    elif isinstance(quiz, dict):
        return {key: _translate_quiz(value, translation) for key, value in quiz.items()}

    else:
        return quiz
