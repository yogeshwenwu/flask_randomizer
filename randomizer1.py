import json
import random

# Randomizer Functions

def MCQ_randomizer(tags, lang, mcq_marks):
    with open('mcq_qn.json') as f:
        questions = json.load(f)

    random.shuffle(questions)  # Shuffle the questions

    selected_questions = []
    current_mark = 0

    selected_tag_counts = {tag: 0 for tag in tags}

    for q in questions:
        if lang == q['language']:
            if any(tag in q['topic'] for tag in tags):
                for tag in tags:
                    if tag in q['topic'] and selected_tag_counts[tag] < len(questions) / len(tags):
                        if current_mark + q['mark'] <= mcq_marks:
                            selected_questions.append({
                                'ID': q['id'],
                                'Marks': q['mark'],
                                'Question_Text': q['question'],
                                'Options': q['options']
                            })
                            current_mark += q['mark']
                            selected_tag_counts[tag] += 1
                            break

    return selected_questions, current_mark

def cod_randomizer(lang, tags, dl, cod_marks):
    with open('cod_qn.json') as f:
        questions = json.load(f)

    random.shuffle(questions)  # Shuffle the questions

    cod_questions = []
    current_mark = 0

    selected_tag_counts = {tag: 0 for tag in tags}

    for q in questions:
        if lang == q['language'] and dl == q['difficulty_level']:
            for tag in tags:
                if tag == q['topic'] and selected_tag_counts[tag] < len(questions) / len(tags):
                    if current_mark + q['mark'] <= cod_marks:
                        cod_questions.append({
                            'ID': q['id'],
                            'Marks': q['mark'],
                            'Question_Text': q['question']
                        })
                        current_mark += q['mark']
                        selected_tag_counts[tag] += 1
                        break

    return cod_questions, current_mark

def filler_randomizer(lang, tags, dl, filler_marks):
    with open('filler.json') as f:
        questions = json.load(f)

    random.shuffle(questions)  # Shuffle the questions

    filler_questions = []
    current_mark = 0

    selected_tag_counts = {tag: 0 for tag in tags}

    for q in questions:
        if lang == q['language'] and dl == q['difficulty_level']:
            for tag in tags:
                if tag == q['topic'] and selected_tag_counts[tag] < len(questions) / len(tags):
                    if current_mark + q['mark'] <= filler_marks:
                        filler_questions.append({
                            'ID': q['id'],
                            'Marks': q['mark'],
                            'Question_Text': q['question']
                        })
                        current_mark += q['mark']
                        selected_tag_counts[tag] += 1
                        break

    return filler_questions, current_mark

# Main function

def main(language, cod_per, tags, total_mark, dl):

    mcq_per = 100 - cod_per

    mcq_marks = (mcq_per / 100) * total_mark
    cod_marks = (cod_per / 100) * total_mark

    mcq_quest, m_mark = MCQ_randomizer(tags ,language , mcq_marks)
    cod_quest, c_mark = cod_randomizer(language, tags, dl, cod_marks)

    filler_mark = cod_marks - c_mark

    filler, f_mark = filler_randomizer(language, tags, dl, filler_mark)

    final = [mcq_quest, cod_quest, filler]

    random.shuffle(final)  # Shuffle the final list of questions

    with open('final.json', 'w') as output_file:
        json.dump(final, output_file, indent=4)
    
    print(cod_quest)
    print(mcq_marks)
    print(cod_marks)
    print(total_mark)
    print(m_mark+c_mark+f_mark)
    print("MCQ mark: ",m_mark)
    print("coding mark: ",c_mark)
    print(f_mark)

if __name__ == '__main__':
    main("python", 80, ["Loops and Iteration", "numbers"], 100, "easy")
