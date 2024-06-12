from Python.src.util import print_utils
from quiz import language_handler
from quiz import topic_handler
from quiz import quiz_handler


def main():
    language: str = language_handler.get_language()
    topic: str = topic_handler.get_topic(language)

    quiz: dict = quiz_handler.load_quiz(topic, language)


if __name__ == "__main__":
    main()
