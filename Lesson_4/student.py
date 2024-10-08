'''

Реалізувати клас Student, який імітує учня. Клас повинен складатися з наступних полів:
- ім'я;
- рік народження;
- група;
- середній бал.

Створити конструктор, у параметрах якого вказати усі поля класу.
Створити метод __str__(), який як рядки повертає значення всіх полів об'єкта.
Створити метод get_age(), який повертає вік студента, порахований з урахуванням року народження. Поточний рік можна отримати за допомогою модуля datetime. Зробити це можна так:

import datetime
datetime.date.today().year # 2024

'''