from markov import markov_chain
# import random
from random import randint
from constants import PROJECT_DIR


if __name__ == '__main__':
    mc = markov_chain.MarkovChain()
    # with open('corpus/proverbs', 'r') as c:
    # with open('corpus/bugurt', 'r') as c:
    with open(f'{PROJECT_DIR}/corpus/jokes1', 'r') as c:
        for line in c.readlines():
            if line == "\n":
                continue
            mc.parse_and_add(line.strip())

        # print("Навальный: Алле, Константин Борисович??")
        # print("Кудрявцев: Да да да.")

        for i in range(20):
            print('***')
            print(mc.generate_sentence(150))
            # if i % 2 == 0:
            #     print(f"Навальный: {mc.generate_sentence(randint(20,100))}")
            # else:
            #     print(f"Кудрявцев: {mc.generate_sentence(randint(15,400))}")

        # print("Кудрявцев: На связи тогда.")
        # print("Навальный: Удачи, пока.")
