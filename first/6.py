start = float(input('Результат спортсмена в первый день: '))
goal = int(input('Цель: '))
days = 1
while goal > start:
        start *= 1.1
        days += 1
        print('{}-й день: {:.3} км'.format(days, start))
print(f'На {days}-й день спортсмен достигнет результата')
