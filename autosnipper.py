from tkinter import *
import pyperclip
import pyautogui as pag
import time
import os, sys

ws = Tk()

t_n = "Autosnipper v1.1"  # title name
s_a = '300x420+200+200'  # canvas size of application
bg_c = '#F1F1F5'  # background color of application
fg_c_f = '#C8C7C7'  # foreground color of footer_w
fg_c_l = '#373737'  # foreground color of label
fg_c_e = '#9D9B9B'  # foreground color of entry
i_l = 'icon_7.png'  # icon link


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ws.minsize(300, 420)
ws.maxsize(300, 420)
ws.title(t_n)
ws.geometry(s_a)
ws['bg'] = bg_c
p1 = PhotoImage(file=resource_path(i_l))
ws.iconphoto(False, p1)  # setting of icon

p_f_p = pyperclip.paste()  # pasted file path
pasted = ''


# varriying the croping size basd on the screen size 
def getting_scrn_size():
    if pag.size().height>800:
        return ' 1200, 750'
    else:
        return ' 855, 535'
    
pasted = '345, 85, '+getting_scrn_size()
 
def all_in_one(loc, cordinate):
    # variable declaration
    ss_location = loc
    ss_coordinate = cordinate
    sleep_time = 0.2
    ss_t_c = (10, 50)  # screenshot taking coordinate
    p_t_c = (0, 10)  # program terminate coordinate
    os.chdir(ss_location)

    # screenshot taker function
    def take_ss(count):
        ss = pag.screenshot(region=ss_coordinate)
        ss.save(rf'screenshot{count}.png')
        print(rf'screenshot{count}.png')

    # time decider for the different action
    def time_definer_for_screenshot():
        updator = 0
        insideif = 0
        insideelif_2 = 0
        while True:
            time.sleep(sleep_time)
            x, y = pag.position()
            if x < ss_t_c[0] and y > ss_t_c[1]:
                insideif += 1
                if insideif < 2:
                    take_ss(updator)
                    updator += 1

            elif y < p_t_c[1]:
                return False

            else:
                insideif = 0
                insideelif_2 += 0

    time_definer_for_screenshot()


def two_in_one():
    x = file_path.get()
    k = im_size.get()
    k_tup = tuple(map(int, k.split(', ')))
    all_in_one(x, k_tup)


def position_find():
    while True:
        time.sleep(0.2)
        pag.position()


def set_mechanical():
    if check_fluent.get():
        check_fluent.set(0)
    im_size.delete(0, END)
    im_size.insert(0, f'345, 80,{getting_scrn_size()}')

def set_fluent():
    if check_mechanical.get():
        check_mechanical.set(0)
    im_size.delete(0, END)
    im_size.insert(0, f'355, 130,{getting_scrn_size()}')


Label(ws,
      text="Path *",
      fg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

file_path = Entry(ws,
                  width=33,
                  fg=fg_c_l,
                  font='Arial 11'
                  )
file_path.insert(0, p_f_p)
file_path.pack(ipadx=5, ipady=5)
print(file_path.get())

Label(ws,
      text="Size",
      fg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

im_size = Entry(ws,
                width=33,
                fg=fg_c_e,
                font='Arial 11'
                )
im_size.insert(0, pasted)
im_size.pack(ipadx=5, ipady=5)
print(im_size.get())

# Check buttons
check_mechanical = IntVar()
check_fluent = IntVar()

Checkbutton(ws,
            text="Mechanical",
            variable=check_mechanical,
            onvalue=1,
            offvalue=0,
            command=set_mechanical,
            fg=fg_c_l,
            font='Arial 11',
            anchor="w",
            justify=LEFT).pack(ipadx=23, ipady=5)

Checkbutton(ws,
            text="Fluent",
            variable=check_fluent,
            onvalue=1,
            offvalue=0,
            command=set_fluent,
            fg=fg_c_l,
            font='Arial 11',
            anchor="w",
            justify=LEFT).pack(ipadx=40, ipady=0)

btn = Button(ws,
             text="Start",
             width=20,
             command=lambda: [two_in_one()]
             )
btn.pack(pady=10, padx=10, ipady=5)

Label(ws,
      text="@C2023 Developed by ramesh kr. mahato \n         rameshsingh9813@gmail.com",
      fg=fg_c_f,
      bg=bg_c,
      height=12,
      width=40,
      bd=1,
      anchor="s",
      justify=LEFT).pack()
ws.mainloop()
