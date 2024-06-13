import json
import locale
from Python.src.util.constants import ROOT_DIR
from Python.src.util.print_utils import print_error

LANGUAGES = {
    0: 'en_us',
    1: 'pt_br'
}


def get_language() -> str:
    system_language = get_system_language()
    selected_language = system_language if system_language in LANGUAGES.values() else 'en_us'

    for k, v in LANGUAGES.items():
        print(f'{k}: {v}')

    return ask_language_to_play(selected_language)


def get_system_language() -> str:
    default_locale, _ = locale.getdefaultlocale()
    return default_locale.lower()


def ask_language_to_play(language: str) -> str:
    while True:
        answer = input(get_translatable('quiz.language.select', language))
        print()

        if valid_answer(answer, language):
            return LANGUAGES[int(answer)]


def valid_answer(answer: str, language: str) -> bool:
    try:
        num_answer = int(answer)
        if num_answer > len(LANGUAGES) - 1:
            print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 0~{len(LANGUAGES) - 1}')
        return num_answer in LANGUAGES
    except ValueError:
        print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 0~{len(LANGUAGES) - 1}')
        return False


def get_translatable(key: str, language: str) -> str:
    return get_quiz_translation(language).get(key, '')


def get_quiz_translation(language: str) -> dict:
    with open(f'{ROOT_DIR}/resources/assets/lang/{language}.json', 'r', encoding='utf-8') as file:
        return json.load(file)
