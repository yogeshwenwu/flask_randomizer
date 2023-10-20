import json
import random

#randomizer

def MCQ_randomizer(tag, lang , mcq_marks):
    
    with open('mcq_qn.json') as f:
        questions = json.load(f)

    random.shuffle(questions)

    selected_questions = []
    current_mark = 0
    tags = tag
    # for question in questions:
        # if lang == question['language']:

    #my code
    # for q in questions:
    #     if tags in q['Tags']:    
    #         if current_mark + q['Marks'] <= mcq_marks:
    #             selected_questions.append(q['ID'])
    #             selected_questions.append(q['Marks'])
    #             selected_questions.append(q['Question_Text'])
                
    #             selected_questions.append(q['Options'])

                
    #             current_mark += q['Marks']
    #         else:
    #             break

    #chatgpt
    for q in questions:
        if tags in q['topic']:    
            if current_mark + q['mark'] <= mcq_marks:
                selected_questions.append({
                    'ID': q['id'],
                    'Marks': q['mark'],
                    'Question_Text': q['question'],
                    'Options': q['options']
                })
                current_mark += q['mark']
            else:
                break

        # else:
        #     print("Language not found !")
        #     break

    return selected_questions, current_mark

#try 1
# def get_random_question(questions, total_marks, tag):
#     filtered_questions = [q for q in questions if q['Marks'] == 1 and tag in q['Tags']]
#     if not filtered_questions:
#         return None
#     return random.choice(filtered_questions)

# try 2
# def get_random_questions(questions, total_marks, tag):
#     filtered_questions = [q for q in questions if q['Marks'] == 1 and tag in q['Tags']]
#     if not filtered_questions:
#         return None

#     selected_questions = random.sample(filtered_questions, total_marks)
#     return selected_questions


#coding randomizer

def cod_randomizer(lang, tag, dl, cod_marks):
    
    with open('cod_qn.json') as f:
        questions = json.load(f)

    random.shuffle(questions)

    cod_questions = []
    current_mark = 0
    tags = tag

    for q in questions:
        if lang == q['language']:
            if dl == q['difficulty_level']:
                if tags == q['topic']:    
                    if current_mark + q['mark'] <= cod_marks:
                        cod_questions.append({
                        'ID': q['id'],
                        'Marks': q['mark'],
                        'Question_Text': q['question']
                        })
                        current_mark += q['mark']
                    else:
                        print("not working")
                        break

        else:
             print("Language not found !")
             break
        

    return cod_questions, current_mark


#main function

def main(language, cod_per, tag, total_mark, dl):

    # language = "python"
    # total_mark = 100
    mcq_per = 100-cod_per
    # cod_per = 80
    # tag = "Loops and Iteration"
    # tag1 = "numbers"
    # dl = "easy"

    mcq_marks = (mcq_per / 100) * total_mark
    cod_marks = (cod_per / 100) * total_mark

    mcq_quest, m_mark = MCQ_randomizer(tag ,language , mcq_marks)
    cod_quest, c_mark = cod_randomizer(language, tag, dl, cod_marks)
    # selected_questions = get_random_questions(questions,mcq_marks, tag)
    
    final = [mcq_quest, cod_quest]

    # print(final)

    # with open('output1.json', 'w') as output_file:
    #     json.dump(mcq_quest, output_file, indent=4)
    #     json.dump(cod_quest, output_file, indent=4)

    
    # print(mcq_quest)
    # print()
    print(cod_quest)
    # print()
    print(mcq_marks)
    print(cod_marks)
    print("MCQ mark: ",m_mark)
    print("coding mark: ",c_mark)
    
if __name__ == '__main__':
    main()