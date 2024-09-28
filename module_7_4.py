# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование с использованием %:
formatted_string1 = "В команде Мастера кода участников: %d !" % team1_num
formatted_string2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Форматирование с использованием format():
formatted_string3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
formatted_string4 = "Волшебники данных решили задачи за {} с !".format(team2_time)

# Форматирование с использованием f-строк:
formatted_string5 = f"Команды решили {score_1} и {score_2} задач."
formatted_string6 = f"Результат битвы: {challenge_result}"
formatted_string7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

# Вывод строк
print(formatted_string1)
print(formatted_string2)
print(formatted_string3)
print(formatted_string4)
print(formatted_string5)
print(formatted_string6)
print(formatted_string7)
