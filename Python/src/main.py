from Python.src.util import print_utils
from quiz import language_handler
from quiz import topic_handler
from quiz import quiz_handler


def main():
    language: str = language_handler.get_language()
    topic: str = topic_handler.get_topic(language)

    quiz: dict = quiz_handler.load_quiz(topic, language)
    quiz = quiz_handler.randomize_quiz(quiz['quiz'])

    correct_count = 0
    for i, q in enumerate(quiz):
        quiz_handler.print_question(q, i)
        user_answer = quiz_handler.get_user_answer(i)

        if quiz_handler.check_answer(q, user_answer):
            correct_count += 1

    print(language_handler.get_translatable('quiz.correct.answers.amount', language).format(correct_count, len(quiz)))


if __name__ == "__main__":
    main()
