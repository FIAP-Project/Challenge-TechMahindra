from quiz.language_handler import get_language, get_translatable
from quiz.topic_handler import get_topic
from quiz.quiz_handler import (
    load_quiz,
    randomize_quiz,
    print_question,
    get_user_answer,
    check_answer,
    print_feedback
)


def run_quiz():
    language = get_language()

    while True:
        topic = get_topic(language)

        quiz_data = load_quiz(topic, language)
        quiz_questions = randomize_quiz(quiz_data['quiz'])

        correct_answers = conduct_quiz(quiz_questions, language)

        print_result(correct_answers, len(quiz_questions), language)

        if play_again(language):
            continue
        else:
            break


def conduct_quiz(quiz_questions, language):
    correct_answers = 0
    lives = 3

    for index, question in enumerate(quiz_questions):
        print_question(question, index)
        user_answer = get_user_answer(index, language)

        if check_answer(question, user_answer):
            correct_answers += 1
            print_feedback(True, lives, language)
        else:
            lives -= 1
            print_feedback(False, lives, language)

            if lives == 0:
                break

    if lives > 0:
        print_result(correct_answers, len(quiz_questions), language)
    else:
        print(game_over_message(language))

    return correct_answers


def print_result(correct_answers, total_questions, language):
    result_message = get_translatable('quiz.correct.answers.amount', language)
    print(result_message.format(correct_answers, total_questions))
    print()


def game_over_message(language):
    return get_translatable('quiz.game.over', language)


def play_again(language: str) -> bool:
    while True:
        answer = input(get_translatable('quiz.play.again', language))

        if answer == '':
            continue
        elif answer in 'Ss':
            print()
            return True
        elif answer in 'Nn':
            return False
        else:
            continue


if __name__ == "__main__":
    run_quiz()
