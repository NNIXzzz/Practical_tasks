#Практическое задание по работе в Pycharm - "Переменные".


Completed_tasks = 12
Hours_spent = 1.5
Course_name = 'Python'
Time_for_one_task = (60*(Hours_spent/Completed_tasks)) #Умножил на 60 для получения времени в минутах

print('Курс: ', Course_name + ',', ' Выполненных домашних заданий: ', Completed_tasks, ',', ' Всего затрачено: ', Hours_spent, ' часа' + ',', ' Среднее время выполнения одного задания: ', Time_for_one_task, ' минут' + '.', sep='')