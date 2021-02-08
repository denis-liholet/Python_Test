from logic import answer_and_questions, score_return


file_path_questions = "questions.txt"
file_path_result = "result.txt"


with open(file_path_questions, "r", encoding="UTF-8") as my_file:
    with open(file_path_result, "w", encoding="UTF-8") as result_file:
        answer_and_questions(my_file, result_file)


print("Number of correct answers: " + str(score_return()))
