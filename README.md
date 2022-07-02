### Решить задачу математического программирования


Функции 
1) { x1^2 + x2^2; x1,x2 >= 0; x1 + x2 = 4} поиск min и max
2) { cos(x1*x2); 0<= x1 <= pi/4; 0<= x2 <= pi/3  поиск min

Найти: min и max для функции 1) и min для функции 2)

  SLSQP - используемый метод оптимизации


Пример:
- fun: 8.0
- jac: array([4., 4.])
- message: 'Optimization terminated successfully'
- nfev: 7
- nit: 2
- njev: 2
- status: 0
- success: True
- x: array([2., 2.])

Пояснение:
- fun: Значение данной функции в минимуме
- jac: (ndarray)Градиент 
- message: (str)Сообщение: сработала ли оптимизация, если нет то почему
- nfev: (int)Количество найденных значений данной функции
- nit: (int)Количество итераций, выполненных оптимизатором.
- njev: (int)Количество оценок Якоби
- status: (int)С каким кодом завершилась оптимизация.
- success: (bool)Успешно ли завершился оптимизатор.
- x: (ndarray)Точка минимума.
