quiz = {
    "question_1": {
        "question": 'What is the capital of France?',
        "answer": "Paris"
    },
     "question_2": {
        "question": 'What is the capital of Italy?',
        "answer": "Rome"
    },
     "question_3": {
        "question": 'What is the capital of Germany?',
        "answer": "Berlin"
    },
     "question_4": {
        "question": 'What is the capital of USA?',
        "answer": "Washington"
    },
     "question_5": {
        "question": 'What is the capital of Ukraine?',
        "answer": "Kyiv"
    },
     "question_6": {
        "question": 'What is the capital of Poland?',
        "answer": "Warsaw"
    },
     "question_7": {
        "question": 'What is the capital of Spain?',
        "answer": "Madrid"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print(f"Your score is: {str(score)}" )
        print('')

    else:
        print('Wrong')
        print(f"The answer is: {value['answer']} ")
        print(f"Your score is: {str(score)}" )
        print('')