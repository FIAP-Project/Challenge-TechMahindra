from Python.src.quiz.language_handler import get_translatable
from Python.src.util import print_utils

TOPICS = {
    0: 'circuit',
    1: 'curiosities',
    2: 'drivers',
    3: 'history',
    4: 'technologies'
}

_selected_topic: str = ''
_language = ''


def get_topic(language: str) -> str:
    global _selected_topic
    global _language

    if _selected_topic == '':
        _language = language

        translatable_topics = {
            0: get_translatable('quiz.topic.circuit', _language),
            1: get_translatable('quiz.topic.curiosities', _language),
            2: get_translatable('quiz.topic.drivers', _language),
            3: get_translatable('quiz.topic.history', _language),
            4: get_translatable('quiz.topic.technologies', _language)
        }

        for k, v in translatable_topics.items():
            print(f'{k}: {v}')

        _selected_topic = ask_topic()

    return _selected_topic


def ask_topic() -> str:
    while True:
        answer: str = input(get_translatable('quiz.topic.select', _language))
        print()

        if _valid_answer(answer):
            return TOPICS[int(answer)]


def _valid_answer(answer: str) -> bool:
    try:
        num_answer = int(answer)
        if num_answer > len(TOPICS) - 1:
            print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection", _language)} 0~{len(TOPICS) - 1}')

        return num_answer in TOPICS

    except ValueError:
        print_utils.print_error(f'{get_translatable("quiz.wrong.number.selection", _language)} 0~{len(TOPICS) - 1}')
        return False
