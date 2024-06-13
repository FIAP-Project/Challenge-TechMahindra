from quiz.language_handler import get_language, get_translatable
from quiz.topic_handler import get_topic
from quiz.quiz_handler import (
    load_quiz,
    randomize_quiz,
    print_question,
    get_user_answer,
    check_answer
)


def run_quiz():
    language = get_language()
    topic = get_topic(language)

    quiz_data = load_quiz(topic, language)
    quiz_questions = randomize_quiz(quiz_data['quiz'])

    correct_answers = conduct_quiz(quiz_questions, language)

    print_result(correct_answers, len(quiz_questions), language)


def conduct_quiz(quiz_questions, language):
    correct_answers = 0
    for index, question in enumerate(quiz_questions):
        print_question(question, index)
        user_answer = get_user_answer(index, language)

        if check_answer(question, user_answer):
            correct_answers += 1

    return correct_answers


def print_result(correct_answers, total_questions, language):
    result_message = get_translatable('quiz.correct.answers.amount', language)
    print(result_message.format(correct_answers, total_questions))


if __name__ == "__main__":
    run_quiz()
