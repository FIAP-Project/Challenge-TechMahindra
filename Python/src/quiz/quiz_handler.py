import json
import random

from Python.src.quiz.language_handler import get_quiz_translation, get_translatable
from Python.src.util.print_utils import print_error, print_success
from Python.src.util.constants import ROOT_DIR


def load_quiz(topic: str, language: str) -> dict:
    quiz = get_quiz_by_topic(topic)
    translation = get_quiz_translation(language)
    return translate_quiz(quiz, translation)


def get_quiz_by_topic(topic: str) -> dict:
    with open(f'{ROOT_DIR}/resources/data/quiz/{topic}.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def translate_quiz(quiz: dict, translation: dict):
    if isinstance(quiz, str):
        return translation.get(quiz, quiz)
    elif isinstance(quiz, list):
        return [translate_quiz(item, translation) for item in quiz]
    elif isinstance(quiz, dict):
        return {key: translate_quiz(value, translation) for key, value in quiz.items()}
    else:
        return quiz


def randomize_quiz(quiz: list) -> list:
    random.shuffle(quiz)  # Randomize the order of questions
    for q in quiz:
        random.shuffle(q['options'])  # Randomize the order of options
    return quiz


def print_question(question: dict, index: int) -> None:
    print(f"Q{index + 1}: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"  {i + 1}. {option}")
    print()


def get_user_answer(index: int, language: str) -> int:
    while True:
        try:
            answer = int(input(get_translatable('quiz.question.answer', language).format(f'Q{index + 1}')).strip())
            print()
            if 1 <= answer <= 4:
                return answer
            else:
                print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 1~4')
        except ValueError:
            print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 1~4')


def check_answer(question: dict, user_answer: int) -> bool:
    correct_answer = question['correct_answer']
    correct_option_index = question['options'].index(correct_answer) + 1
    return user_answer == correct_option_index


def print_feedback(is_correct: bool, lives: int, language: str) -> None:
    if is_correct:
        print_success(get_translatable('quiz.answer.correct', language))
    else:
        print_error(get_translatable('quiz.answer.wrong', language))

    print(get_translatable('quiz.lives.remaining', language).format(lives))
    print()
