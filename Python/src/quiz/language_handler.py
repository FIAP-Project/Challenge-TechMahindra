import json
import locale

from Python.src.util.constants import ROOT_DIR
from Python.src.util import print_utils

LANGUAGES = {
    0: 'en_us',
    1: 'pt_br'
}

_selected_language: str = ''


def get_language():
    global _selected_language

    if _selected_language == '':
        system_language: str = get_system_language()

        if system_language in LANGUAGES.values():
            _selected_language = system_language
        else:
            _selected_language = 'en_us'

        for k, v in LANGUAGES.items():
            print(f'{k}: {v}')

        _selected_language = _ask_language_to_play()

    return _selected_language


def get_system_language() -> str:
    default_locale, _ = locale.getdefaultlocale()
    return default_locale.lower()


def _ask_language_to_play():
    while True:
        answer: str = input(get_translatable('quiz.language.select'))
        print()

        if _valid_answer(answer):
            return LANGUAGES[int(answer)]


def _valid_answer(answer: str) -> bool:
    try:
        num_answer = int(answer)
        if num_answer > len(LANGUAGES) - 1:
            print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection")} 0~{len(LANGUAGES) - 1}')

        return num_answer in LANGUAGES

    except ValueError:
        print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection")} 0~{len(LANGUAGES) - 1}')
        return False


def get_translatable(key: str, language: str = '') -> str:
    if language != '':
        return get_quiz_translation(language)[key]

    return get_quiz_translation(_selected_language)[key]


def get_quiz_translation(language: str) -> dict:
    with open(f'{ROOT_DIR}/resources/assets/lang/{language}.json', 'r', encoding='utf-8') as file:
        return json.load(file)
