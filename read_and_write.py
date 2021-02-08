from decorators import test_duration, logger

counter = 0
DIV = "----------------------"


@logger
@test_duration
def answer_and_questions(input_file_name, output_file_name):
    for line in input_file_name:
        user_answer = ''
        print(f"question: {line.strip()}")
        write_to_file(output_file_name, str(line.strip()))
        for _ in range(3):
            print(f"option {input_file_name.readline().strip()}")
        answer = int(input_file_name.readline().split(":")[1].strip())
        try:
            while True:
                user_answer = input("\nPlease, input your choice and press Enter: ")
                user_answer = int(user_answer.strip())
                if 1 <= user_answer <= 3:
                    break
                else:
                    print("Please, enter option from 1 to 3")
        except ValueError:
            print("Oops! You should enter numbers only! Be careful next time!!!")
        score_counter_and_answer_result_printing(user_answer, answer, output_file_name)


def write_to_file(file_name, value: str):
    file_name.write(value)


def score_counter_and_answer_result_printing(entered_answer, correct_answer, file_name_for_logging):
    if entered_answer == correct_answer:
        print("Correct!" + "\n" + DIV)
        global counter
        counter += 1
        write_to_file(file_name_for_logging, " --> Correct" + "\n")
    else:
        print("Wrong!" + "\n" + DIV)
        write_to_file(file_name_for_logging, " --> Wrong" + "\n")


def score_return():
    return counter
