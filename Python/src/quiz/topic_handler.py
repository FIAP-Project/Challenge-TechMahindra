from Python.src.quiz.language_handler import get_translatable
from Python.src.util.constants import ROOT_DIR
from Python.src.util.print_utils import print_error

TOPICS = {}


def load_topics():
    lang_dir = ROOT_DIR / 'resources' / 'data' / 'quiz'
    for index, topic_file in enumerate(lang_dir.glob('*.json')):
        topic_name = topic_file.stem
        TOPICS[index] = topic_name


load_topics()


def get_topic(language: str) -> str:
    translatable_topics = {k: get_translatable(f'quiz.topic.{v}', language) for k, v in TOPICS.items()}

    for k, v in translatable_topics.items():
        print(f'{k}: {v}')

    return ask_topic(language)


def ask_topic(language: str) -> str:
    while True:
        answer = input(get_translatable('quiz.topic.select', language))
        print()

        if valid_answer(answer, language):
            return TOPICS[int(answer)]


def valid_answer(answer: str, language: str) -> bool:
    try:
        num_answer = int(answer)
        if num_answer > len(TOPICS) - 1:
            print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 0~{len(TOPICS) - 1}')
        return num_answer in TOPICS
    except ValueError:
        print_error(f'{get_translatable("quiz.wrong.number.selection", language)} 0~{len(TOPICS) - 1}')
        return False
