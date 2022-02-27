import random
import json
from faker import Faker

fake = Faker()
DATA_COUNT = 5
ANSWER_LIST = ['a', 'b', 'c', 'd']


class Questions():
    def __init__(self):
        self.question = fake.paragraph(
            nb_sentences=5, variable_nb_sentences=False)
        self.options = self.generate_options()
        self.answer = random.choice(ANSWER_LIST)

    def generate_options(self):
        options = {
            "a": fake.text(max_nb_chars=80),
            "b": fake.text(max_nb_chars=80),
            "c": fake.text(max_nb_chars=80),
            "d": fake.text(max_nb_chars=80),
        }

        return options


if __name__ == "__main__":
    data_list_v1 = []
    data_list_v2 = []
    for i in range(DATA_COUNT):
        data_list_v1.append(Questions().__dict__)
        data_list_v2.append(Questions().__dict__)

    data_list_v3 = []
    for i in range(DATA_COUNT-2):
        data_list_v3.append(Questions().__dict__)

    with open('../data/questions.json', 'w+') as outfile:
        json.dump({"questions_v1": {"result": data_list_v1},
                  "questions_v2": {"result": data_list_v2},
                   "questions_v3": {"result": data_list_v3}}, outfile)
