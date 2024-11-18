#Практическое задание по работе в Pycharm - "Переменные".


completed_tasks = 12
hours_spent = 1.5
course_name = 'Python'
time_for_one_task = (60*(hours_spent/completed_tasks)) #Умножил на 60 для получения времени в минутах

print('Курс: ', course_name + ',', ' Выполненных домашних заданий: ', completed_tasks, ',', ' Всего затрачено: ', hours_spent, ' часа' + ',', ' Среднее время выполнения одного задания: ', time_for_one_task, ' минут' + '.', sep='')