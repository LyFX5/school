import json
from random import random


def main():
    # считываем данные
    with open('train.json', 'r') as json_file:
        train = json.load(json_file)

    # посмотрим на информацию, доступную в нулевом эпизоде
    print(train[0].keys())

    # напечатаем возможные действия
    print(set(train[0]['actions']))

    # считываем данные, для которых нужно сделать предсказание
    with open('submit.json', 'r') as json_file:
        submit = json.load(json_file)

    # заполним поле V случайными числами
    for idx, item in enumerate(submit):
        state = item['state']
        item['V'] = random()

    # записываем предсказания в файл
    with open('solution.json', 'w') as json_file:
        json.dump(submit, json_file)


if __name__ == '__main__':
    main()
