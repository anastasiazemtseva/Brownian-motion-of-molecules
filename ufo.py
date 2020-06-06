import turtle as t
import math as m
import random as r


class Ufo:
    def __init__(self, name, x, y, size, color,
                 count_pillars, count_lamps, pillars_down=True,
                 show_name=True, made_in='Russia', engine_grade='Turbo UFO'):
        self.__name = name
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillars_down
        self.show_name = show_name

        self.__made_in = made_in
        self.__engine_grade = engine_grade

    def __str__(self):
        s = 'Сконструировано НЛО под названием' + self.__name + '\n'
        s += 'Координаты (' + str(self.x) + ',' + str(self.y) + ')' + '\n'
        s += 'Размер' + str(self.size) + '\n'
        s += 'Цвет' + str(self.color) + '\n'
        s += 'Количество опор' + str(self.count_pillars) + '\n'
        s += 'Количество ламп' + str(self.count_lamps) + '\n'

        if self.pillars_down:
            s += 'Опоры опущены'
        else:
            s += 'Опоры подняты'

        if self.show_name:
            s += str(self.__name) + '\n'

        return s

    def __repr__(self):
        return self.__str__()

    def show(self, color=True):
        if not color:
            t.color('white')
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                t.up()
                t.goto(self.x, self.y + self.size / 3)
                t.down()
                t.goto(lx, self.y - self.size / 6)

        t.up()
        t.goto(self.x, self.y - self.size / 12)
        t.down()
        if not color:
            t.fillcolor('white')
        else:
            t.fillcolor('blue')
        t.begin_fill()
        t.circle(self.size / 4)
        t.end_fill()

        t.up()
        if not color:
            t.fillcolor('white')
        else:
            t.fillcolor(self.color)
        t.goto(self.x - self.size / 2, self.y + self.size / 4)
        t.down()
        t.begin_fill()
        t.forward(self.size)
        i = m.pi / 2
        while i <= 3 * m.pi / 2:
            sx = (self.size / 2) * m.sin(i)
            sy = (self.size / 3) * m.cos(i)
            t.goto(self.x + sx, self.y + self.size / 4 + sy)
            i += m.pi / self.size
        t.end_fill()

        if not color:
            t.fillcolor('white')
        else:
            t.fillcolor('yellow')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            t.begin_fill()
            t.up()
            t.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            t.down()
            t.circle(dx / 4)
            t.end_fill()

        if self.show_name:
            t.up()
            t.goto(self.x, self.y + self.size / 2)
            t.down()
            t.write(self.__name, align='center')
            t.up()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def move(self):
        self.x = self.x + r.randint(-1, 1) * r.randint(-10, 10)
        self.y = self.y + r.randint(-1, 1) * r.randint(-10, 10)

    @property
    def set_made_in(self, made_in):
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__made_in = made_in
        else:
            self.__made_in = None

    @property
    def get_made_in(self):
        return self.__made_in

    @property
    def engine_grade(self):
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        if new_grade == '':
            print('Марка двигателя не может быть пустой строкой')
        else:
            self.__engine_grade = new_grade

    @engine_grade.getter
    def engine_grade(self):
        if self.__engine_grade == 'Turbo UFO':
            return 'По умолчанию'
        else:
            return self.__engine_grade
