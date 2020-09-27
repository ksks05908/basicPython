import random
class Card:
    def __init__(self, name):
        self.number = 15
        self.master = name
        self.values = [sorted(random.sample(range(1, 91), 5)) for _ in range(0, 3)]
        for list in self.values:
            for _ in range(0, 5):
                list.insert(random.randint(0, len(list)), ' ')

    def __str__(self):
        output = ''
        output += f'{self.master}:\n' + '-' * 30 + '\n'
        for list in self.values:
            output += ' '.join(map(lambda x: ' ' + str(x) if len(str(x)) == 1 else str(x), list)) + '\n'
        return f'{output}'

    def exclude(self, this):
        for one_list in self.values:
            if this in one_list:
                one_list[one_list.index(this)] = 'X'
                self.number -= 1
                return True
        return False

class Player():
    def __init__(self, name):
        self.name = name
        self.card = Card(self.name)

class Game():
    def __init__(self, *args):
        self.player1, self.player2 = args

    def generation_kegs(self):
        kegs = list(range(1, 91))
        random.shuffle(kegs)
        for keg in kegs:
            print(self.player1.card, self.player2.card)
            answer = input(f'Новый бочонок: {keg}\nХотите зачеркнуть?(y/n)')
            result = self.player1.card.exclude(keg)
            if (answer == 'y' and result == False) or (answer == 'n' and result == True) or answer != 'y' and answer != 'n':
                print('Конец игры! Вы ошиблись')
                break
            self.player2.card.exclude(keg)
            if self.player2.card.number == 0 or self.player1.card.number == 0:
                print('Игра окончена!')
                print(f'Победил {player1.name}') if self.player2.card.number > self.player1.card.number else print(f'Победил {player2.name}')
                break

player1 = Player('Human')
player2 = Player('Computer')
game = Game(player1, player2)
game.generation_kegs()
