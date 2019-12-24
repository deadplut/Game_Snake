from tkinter import *

#Создаём окно
root = Tk()
#Ширина экрана
WIDTH = 800
#ВЫсота экрана
HEIGHT = 600
#Размер сегмента змейки
SEG_SIZE = 20
# Переменная отвечающая за состояние игры
IN_GAME = True
#Устанавливаем название окна
root.title('PythonicWay Snake')

#Создаём экземпляр класса Canvas (Его ещё будем использовать) и заливаем всё зелёным
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")

class Snake(object):
    def __init__(self, segments):
        self.segments = segments
        # список доступных направлений движения змейки
        self.mapping = {"Down": (0,1), "Up": (0,-1),
                        "Left":(-1,0), "Right":(1,0)}
        #Изначально змейка двигается вправо
        self.vector= self.mapping["Right"]

    def move(self):
        """Двигает змейку в заданносм направлении"""

        # перебираем все сегмаенты крмое первого
        for index in range(len(self.segments)-1):
            segmnet = self.segments[index].instance
            x1,y1,x2,y2 = c.coords(self.segments[index+1].imstance)
            #задаём каждому сегменту позццию сегмента стоящего после него
            c.coords(segmnet, x1,y1,x2,y2)

        #получаем координаты сегмента перед "головой"
        x1, y1,x2,y2 = c.coords(self.segments[-2].instance)

        #помещаем "голову' в направлении указанном в векторе движения
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE,
                 y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE,
                 y2 + self.vector[1] * SEG_SIZE)

    def change_direction(self,event):
         """ Изменяет направление движения змейки """

        # event передаст нам символ нажатой клавиши
        # и если эта клавиша в доступных направлениях
        # изменяем направление





#Запускаем окно
root.mainloop()