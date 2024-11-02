from tkinter import *
import time
from datetime import datetime
import os
from PIL import ImageTk, Image
from tkinter.messagebox import *

# ПАРОЛЬ ОТ КАРТЫ 1973
class MainWindow:


    def __init__(self):
        self.im_01 = PhotoImage(file='01.gif')
        self.im_02 = PhotoImage(file='02.gif')
        self.im_03 = PhotoImage(file='03.gif')
        self.im_04 = PhotoImage(file='04.gif')
        self.im_05 = PhotoImage(file='05.gif')
        self.im_06 = PhotoImage(file='06.gif')
        self.im_07 = PhotoImage(file='07.gif')
        self.im_08 = PhotoImage(file='08.gif')
        self.im_09 = PhotoImage(file='09.gif')
        self.im_00 = PhotoImage(file='00.gif')
        self.im_null = PhotoImage(file='null.gif')
        self.im_cancel = PhotoImage(file='cancel.gif')
        self.im_enter = PhotoImage(file='enter.gif')
        self.im_correction = PhotoImage(file='correction.gif')
        self.im_minus = PhotoImage(file='minus.gif')
        self.im_plus = PhotoImage(file='plus.gif')
        self.data = ""

        self.btn01 = Button(root, text='1', image=self.im_01)
        self.btn01.grid(row=6, column=1)
        self.btn02 = Button(root, text='2', image=self.im_02)
        self.btn02.grid(row=6, column=2)
        self.btn03 = Button(root, text='3', image=self.im_03)
        self.btn03.grid(row=6, column=3)
        self.btncancel = Button(root, text='cancel', image=self.im_cancel)
        self.btncancel.grid(row=6, column=4)

        self.btn04 = Button(root, text='4', image=self.im_04)
        self.btn04.grid(row=7, column=1)
        self.btn05 = Button(root, text='5', image=self.im_05)
        self.btn05.grid(row=7, column=2)
        self.btn06 = Button(root, text='6', image=self.im_06)
        self.btn06.grid(row=7, column=3)
        self.btncorrection = Button(root, text='correction', image=self.im_correction)
        self.btncorrection.grid(row=7, column=4)

        self.btn07 = Button(root, text='7', image=self.im_07)
        self.btn07.grid(row=8, column=1)
        self.btn08 = Button(root, text='8', image=self.im_08)
        self.btn08.grid(row=8, column=2)
        self.btn09 = Button(root, text='9', image=self.im_09)
        self.btn09.grid(row=8, column=3)
        self.btnnull = Button(root, text='null', image=self.im_null)
        self.btnnull.grid(row=8, column=4)

        self.btnminus = Button(root, text='-', image=self.im_minus)
        self.btnminus.grid(row=9, column=1)
        self.btn00 = Button(root, text='0', image=self.im_00)
        self.btn00.grid(row=9, column=2)
        self.btnplus = Button(root, text='+', image=self.im_plus)
        self.btnplus.grid(row=9, column=3)
        self.btnenter = Button(root, text='enter', image=self.im_enter)
        self.btnenter.grid(row=9, column=4)

        self.init_widget()

    def init_widget(self):
        self.btn01.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('1'))

        self.btn02.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('2'))

        self.btn03.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('3'))
        self.btncancel.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))
        self.btn04.bind('<ButtonRelease-1>',
                         lambda event: self.change_data('4'))
        self.btn05.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('5'))
        self.btn06.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('6'))
        self.btncorrection.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))
        self.btn07.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('7'))
        self.btn08.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('8'))
        self.btn09.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('9'))
        self.btnnull.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))
        self.btnminus.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))
        self.btn00.bind('<ButtonRelease-1>',
                        lambda event: self.change_data('0'))
        self.btnplus.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))
        self.btnenter.bind('<ButtonRelease-1>',
                        lambda event: self.change_data(''))

    def change_data(self, new_data):
        global a
        self.im_pussword1 = PhotoImage(file='4.png')
        self.im_pussword2 = PhotoImage(file='5.png')
        self.im_pussword3 = PhotoImage(file='6.png')
        self.im_pussword4 = PhotoImage(file='7.png')
        self.im_pussword5 = PhotoImage(file='8.png')
        self.data += new_data
        

        if len(self.data) == 1:
            view1 = Label(root, image=self.im_pussword2)
            view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
            root.mainloop()

        if len(self.data) == 2:
            view1 = Label(root, image=self.im_pussword3)
            view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
            root.mainloop()

        if len(self.data) == 3:
            view1 = Label(root, image=self.im_pussword4)
            view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
            root.mainloop()


        if len(self.data) == 4 and self.data == '1973':
            self.im_pic = PhotoImage(file='1.png')
            view1 = Label(root, image=self.im_pic)
            view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
            root.mainloop()

        if len(self.data) == 4 and self.data != '1973':
            self.m_pussword1 = PhotoImage(file='4.png')
            view1 = Label(root, image=self.m_pussword1)
            view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
            root.mainloop()
            self.__init__()


# переменная отвечающая за статус работы банкомата
status = 0
# переменная для анимации
ind = 0
# функция проверяющая вставленна или вытащена карта
def stat():
    global status
    if status == 0:
        card_out()
        status += 1

        im_pussword1 = PhotoImage(file='4.png')
        view1 = Label(root, image=im_pussword1)
        view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
        window = MainWindow()
        root.mainloop()

    else:
        card_in()
        status -= 1

        im_pic3 = PhotoImage(file='14.png')
        view1 = Label(root, image=im_pic3)
        view1.grid(row=0, rowspan=4, column=1, columnspan=4, sticky='nsew', padx=1, pady=1)
        root.mainloop()





date = 'Дата/время: '+datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")+'  '+'Выполненные операции: '
# анимация вытаскивания карты
def card_out():
    global ind, after_id
    after_id = root.after(40,card_out)
    ind += 1
    if ind<34:
        card = cards[ind]
        label['image']=card
        label.grid(row = 0, rowspan=4, column=7, sticky='nsew', padx =1, pady=1)
    else:
        ind = 0
        root.after_cancel(after_id)
    

# анимация засовывания карты
def card_in():
    global ind, after_id
    after_id = root.after(40,card_in)
    ind += 1
    if ind<34:
        card = cards[33-ind]
        label['image']=card
        label.grid(row = 0, rowspan=4, column=7, sticky='nsew', padx =1, pady=1)
    else:
        ind = 0
        root.after_cancel(after_id)
    
# анимация высовывания карты
def money_out():
    global ind, after_id,date
    after_id = root.after(40,money_out)
    ind += 1
    date+="Снято "
    
    date+='рублей'
    if ind<24:
        money = moneys[ind]
        label['image']=money
        label.grid(row = 5,column = 0, columnspan=6,sticky='nsew', padx =1,pady=1)
    else:
        ind = 0
        root.after_cancel(after_id)

# смена картинки на экране по нажатию боковой кнопки
def pic_2():
    im_pic2 = PhotoImage(file='113.png')
    view1 = Label(root, image=im_pic2)
    view1.grid(row = 0, rowspan = 4, column = 1, columnspan=4, sticky='nsew', padx =1, pady=1)
    root.mainloop()
def pic_3():
    im_pic2 = PhotoImage(file='9.png')
    view1 = Label(root, image=im_pic2)
    view1.grid(row = 0, rowspan = 4, column = 1, columnspan=4, sticky='nsew', padx =1, pady=1)
    root.mainloop()

root = Tk()

# анимация карты и денег
cards = []
moneys = []
for i in range (34):
    cards.append(PhotoImage(file='cardin-v-3.gif',format = 'gif -index %i' %(i)))

for i in range (24):
    moneys.append(PhotoImage(file='money.gif',format = 'gif -index %i' %(i)))

# присваивание переменым картинок
im_1 = PhotoImage(file = '1.png' )
im_right = PhotoImage(file = 'right.gif' )
im_left = PhotoImage(file = 'left.gif' )
im_pic1 = PhotoImage(file = '12.png' )

# стартовая картинка экрана
view1 = Label(root, image = im_pic1)
view1.grid( row = 0, rowspan = 4,column = 1, columnspan=4,sticky='nsew', padx =1,pady=1)


# правые боковые кнопки
btn11 = Button(root, text = '', image = im_right, command = money_out)
btn11.grid(row=0, column=0)
btn12 = Button(root, text = '', image = im_right)
btn12.grid(row=1, column=0)
btn13 = Button(root, text = '', image = im_right)
btn13.grid(row=2, column=0)
btn14 = Button(root, text = '', image = im_right)
btn14.grid(row=3, column=0)

# левые боковые кнопки (две из них с прописанной командой для смены картинки (функция pic_2))
btn15 = Button(root, text = '', image = im_left)
btn15.grid(row=0, column=5)
btn16 = Button(root, text = '', image = im_left,  command = pic_2)
btn16.grid(row=1, column=5)
btn17 = Button(root, text = '', image = im_left)
btn17.grid(row=2, column=5)
btn18 = Button(root, text = '', image = im_left, command = pic_3)
btn18.grid(row=3, column=5)



# картинка отсека для выдачи денег
im_mo = PhotoImage(file = 'выдача.png' )
view = Label(root, image = im_mo)
view.grid(row = 4, columnspan=6)

# статичная картинка картоприемника
im_lol = PhotoImage(file = 'картоприемник.png')
view2 = Label(root, image = im_lol)
view2.grid(row = 0, rowspan=4, column=7, sticky='nsew', padx =1, pady=1)




# кнопка вставки\изьятия карты из банкомата
btn19 = Button(root, text='Вставить\Вытащить', font =('Ariel', 10), command = stat)
btn19.grid(row = 4, column=7, sticky='nsew', padx =1, pady=1)
btn20 = Button(root, text='Напечатать чек', font =('Ariel', 10), command = lambda: showinfo('Чек',date))
btn20.grid(row = 5, column=7, sticky='nsew', padx =1, pady=1)
label = Label(root)

window = MainWindow()
root.mainloop()
