from ufo import *
import turtle as t


t.tracer(0)
t.hideturtle()
t.delay(60)

ufo1 = Ufo('Пришелец-1', 100, 200, 150, 'green', 5, 6)
ufo2 = Ufo('Пришелец-2', -200, -200, 200, 'pink', 3, 4)
ufo2.set_name('Неопознанный объект')
while True:
    ufo1.move()
    ufo2.move()
    t.clear()
    ufo1.show()
    t.update()
    ufo2.show()
    t.update()