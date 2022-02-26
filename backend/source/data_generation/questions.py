import random
import json
from faker import Faker

fake = Faker()
DATA_COUNT = 5


class Questions():
    def __init__(self):
        self.question = fake.name()
        self.options = self.generate_options()
        self.answer = random.randint(10, 50)

    def generate_options(self):
        options = {
            "a": random.randint(10, 50),
            "b": random.randint(10, 50),
            "c": random.randint(10, 50),
            "d": random.randint(10, 50),
        }

        return options


if __name__ == "__main__":
    data_list_v1 = []
    for i in range(DATA_COUNT):
        data_list_v1.append(Questions().__dict__)

    data_list_v2 = []
    for i in range(DATA_COUNT*2):
        data_list_v2.append(Questions().__dict__)

    data_list_v3 = []
    for i in range(DATA_COUNT*3):
        data_list_v3.append(Questions().__dict__)

    with open('../data/questions.json', 'w+') as outfile:
        json.dump({"questions_v1": {"result": data_list_v1},
                  "questions_v2": {"result": data_list_v2},
                   "questions_v3": {"result": data_list_v3}}, outfile)
