import json
import random

from Python.src.quiz.language_handler import get_quiz_translation
from Python.src.quiz.language_handler import get_translatable
from Python.src.util import print_utils
from Python.src.util.constants import ROOT_DIR

_language = ''


def load_quiz(topic: str, language: str) -> dict:
    quiz: dict = _get_quiz_by_topic(topic)
    translation: dict = get_quiz_translation(language)

    global _language
    _language = language

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


def randomize_quiz(quiz) -> dict:
    random.shuffle(quiz)  # Randomize the order of questions
    for q in quiz:
        random.shuffle(q['options'])  # Randomize the order of options
    return quiz


def print_question(q, q_index):
    print(f"Q{q_index + 1}: {q['question']}")
    for i, option in enumerate(q['options']):
        print(f"  {i + 1}. {option}")
    print()


def get_user_answer(q_index):
    while True:
        try:
            answer = int(input(get_translatable('quiz.question.answer', _language).format(f'Q{q_index + 1}')).strip())
            print()
            if 1 <= answer <= 4:
                return answer
            else:
                print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection", _language)} 1~4')
        except ValueError:
            print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection", _language)} 1~4')


def check_answer(q, user_answer):
    correct_answer = q['correct_answer']
    correct_option_index = q['options'].index(correct_answer) + 1
    return user_answer == correct_option_index
