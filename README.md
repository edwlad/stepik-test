# Тест создания коммитов

## Задача

Выполнить [Лирическое отступление про Git](https://stepik.org/lesson/187065/step/11) - сделать несколько коммитов решений задач из [Лекции 2: Полезные методы Selenium](https://stepik.org/lesson/165493/).

## Лекция 2.1 шаг 5

### 2.1.5 Задание

[**Кликаем по checkboxes и radiobuttons**](https://stepik.org/lesson/165493/step/5).  
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.

### 2.1.5 Требования

Ваша программа должна выполнить следующие шаги:

- Открыть страницу <http://suninjuly.github.io/math.html>.
- Считать значение для переменной x.
- Посчитать математическую функцию от x (код для этого приведён ниже).
- Ввести ответ в текстовое поле.
- Отметить checkbox "I'm the robot".
- Выбрать radiobutton "Robots rule!".
- Нажать на кнопку Submit.

### 2.1.5 Решение

[lesson2-1-step5.py](lesson2-1-step5.py)

## Лекция 2.1 шаг 7

### 2.1.7 Задание

[**Поиск сокровища с помощью get_attribute**](https://stepik.org/lesson/165493/step/7).  
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

### 2.1.7 Требования

- Открыть страницу <http://suninjuly.github.io/get_attribute.html>.
- Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
- Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
- Посчитать математическую функцию от x (сама функция остаётся неизменной).
- Ввести ответ в текстовое поле.
- Отметить checkbox "I'm the robot".
- Выбрать radiobutton "Robots rule!".
- Нажать на кнопку "Submit".

### 2.1.7 Решение

[lesson2-1-step7.py](lesson2-1-step7.py)
