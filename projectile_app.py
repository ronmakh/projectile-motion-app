from tkinter import *
import math
from tkinter import messagebox
import random
#import tkFont

main = Tk()
main.title('Projectile Motion')
topframe = Frame(main)
bottomframe = Frame(main)
#main.geometry("800x150")
main.attributes('-fullscreen', True)
main.config(bg='light blue')
topframe.pack()
topframe.config(bg='light blue')
bottomframe.pack()
Button_Disabler = 0

outroimage = PhotoImage(file = 'smilemile.gif')
introimage = PhotoImage(file = 'intro_image.gif')

def refresh():
    for widget in bottomframe.winfo_children():
        widget.destroy()
    for widget in topframe.winfo_children():
        widget.destroy()
    
def abc():
    #cv = Canvas(bottomframe, width = 870, height = 530)
    #yayaya = cv.create_image(0,0, image = introimage, anchor = NW)
    #cv.pack()
    bottomframe.config(bg = "light blue")
  
    

def button_row():
        global Button_Disabler
        button1 = Button(topframe, text="Projectile Motion Theory", command = TheoryPage, state = NORMAL, relief = 'solid', font = (15), bg = 'violet')
        button1.pack(side=LEFT, padx=10, pady=20)

        button2 = Button(topframe, text="Projectile Motion Demonstration", command = DemoPage, state = NORMAL, relief = 'solid', font = (15), bg = 'cyan')
        button2.pack(side=LEFT, padx=10, pady=20)
        
        button3 = Button(topframe, text="Projectile Motion Interactive Game", command = AppPage, state = NORMAL, relief = 'solid', font = (15), bg = 'cyan')
        button3.pack(side=LEFT, padx=10, pady=20)

        button4 = Button(topframe, text="Projectile Motion Summary", command = ConclusionPage, state = NORMAL, relief = 'solid', font = (15), bg = 'violet')
        button4.pack(side=LEFT, padx=10, pady=20)

        if Button_Disabler == 1:
            button1.config(state = DISABLED, relief = 'flat')
        if Button_Disabler == 2:
            button2.config(state = DISABLED, relief = 'flat')
        if Button_Disabler == 3:
            button3.config(state = DISABLED, relief = 'flat')
        if Button_Disabler == 4:
            button4.config(state = DISABLED, relief = 'flat')

def startpage():
    refresh()
    button_row()
    main.geometry('1000x125')
    word = Label(bottomframe,text = "Welcome! Click on any of the above buttons to go to their respective pages", bg = 'light blue', font = (25))
    
    word.grid(row = 1, column =1)
    
def TheoryPage():
    refresh()
    abc()
    main.geometry('1300x800')
    global Button_Disabler
    Button_Disabler = 1
    button_row()
    func_of_TheoryPage()
    
def func_of_TheoryPage():   
    cv = Canvas(bottomframe, width = 870, height = 530)
    yayaya = cv.create_image(0,0, image = introimage, anchor = NW)
    cv.pack()

def guidepopup_demo():
    func_of_guidepopup_demo()

def func_of_guidepopup_demo():
    self = Tk()
    self.title("How to use the Demo")
    self.config(bg = 'light green')
    
    Label(self, text = ' Step 1 : Adjust the sliders for Velocity and Angle respectively to see the expected Projectile Motion', bg = 'light green').grid(row = 0, column = 1)
    Label(self, text = ' Step 2 : Click the \'Show Movement\' button to simulate the ball to undergo the Projectile Motion    ', bg = 'light green').grid(row = 1, column = 1)
    Label(self, text = ' Step 3 : Click the \'Reset\' button to reset the animation and inputted values of Velocity and Angle ', bg = 'light green').grid(row = 2, column = 1)

    def close_window():
        self.destroy()
        
    Button(self, text = 'OK',command = close_window).grid(row = 4, column = 1)
    
    self.mainloop()
        
def DemoPage():
    refresh()
    abc()
    main.geometry('1300x800')
    func_of_DemoPage()

def func_of_DemoPage():
    global Button_Disabler
    Button_Disabler = 2
    refresh()
    button_row()


    topframe2 = Label(bottomframe, text = 'Projectile Motion Demo', bg = 'teal', fg = 'white')
    topframe2.grid(row=0, column = 1)

    btmframe = LabelFrame(bottomframe, text = 'Results:')
        
    midframe = LabelFrame(bottomframe, text = 'Demo', bg = 'red')
    midframe.grid(row=1, column = 1)
    yay = Canvas(midframe, width = 1200, height = 440, bg = 'blue')
    yay.grid(row = 1)

    pjm = Canvas(midframe, width = 500, height = 250)
    pjm.grid(row =0,column=0)

    btmframe.grid(row=2, column = 1)
    rlt = Canvas(btmframe, width = 30, height = 20)
    rlt.grid(row = 2)

    guide_button = Button(midframe, text = 'Help',command = guidepopup_demo, bg = 'brown', fg = 'white', relief = 'solid')
    guide_button.place(relx= 0.97,rely= 0.95,  anchor = 'center')
    
    '.....................................................................................................'

    x0 = 190
    y0 = 410
    xx = 210
    yy = 440
    xb = 210
    yb = 430
    proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')

    '..............................................................................................'

    def pause():
        print ('nothing')

    '............................................................................................................'
            
    def clear():    
        yay.delete('all')
        pjm.delete('all')
        rlt.delete('all')
            
        AirTime = 0
        XMotion = 0
        YMotion = 0
        MaxHeight= 0
        Angle = 0
        Speed = 0
        Range1 = 0

        proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
        yay.create_rectangle(0, 430, 1500, 530, fill = 'black')
        lbEnergy = Label(pjm, text = 'Velocity(m/s)', width = 15)
        lbEnergy.grid(row = 0, column = 1)
        lbAngle = Label(pjm, text='Angle(degrees)', width = 15)
        lbAngle.grid(row=0, column=2)
        btnClear = Button(pjm, text = 'Clear', command=clear, width=10)
        btnClear.grid(row=2, column = 2)


        def results(speed1=0, angle1=0):
            g = 9.81        
            XMotion = float(speed1) * math.cos(math.radians(float(angle1)))
            YMotion = float(speed1) * math.sin(math.radians(float(angle1)))
            AirTime1 = (2*YMotion)/g

            if YMotion > 0:
                
                AirTime1 = (2*YMotion)/g
                Range1 = XMotion*AirTime1
                MaxHeight1 = YMotion*(AirTime1/2) - 0.5*g*(AirTime1/2)**2
                if angle1<90:
                    XMotion = XMotion
                    Range1 = Range1
                
                elif angle1==90:
                    XMotion = 0
                    Range1 = 0
                
                   
            else:        
                AirTime1 = 0
                Range1 = 0
                MaxHeight1 = 0
            

            XMotion = str(XMotion)[0:5]
            YMotion = str(YMotion)[0:5]
            AirTime = str(AirTime1)[0:5]
            Angle = str(angle1)[0:5]
            Speed = str(speed1)[0:5]
            MaxHeight = str(MaxHeight1)[0:5]
            Range1 = str(Range1)[0:5]
            g1 = str(g)
            
            L1.config(text = str(XMotion)+'m/s')
            L2.config(text = str(YMotion)+'m/s')
            L3.config(text = str(AirTime)+'s')
            L4.config(text = str(Angle)+'degrees')
            L5.config(text = str(Speed)+'m/s')
            L6.config(text = str(MaxHeight)+'m')
            L7.config(text = str(Range1)+'m')
            L8.config(text = str(g1)+'m/s^2')
        
        def updatex(value):
            yay.delete(ALL)
            proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
            projectile(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
            results(speed1=float(sldVelocity.get()), angle1 = float(sldAngle.get()))
            yay.create_rectangle(0, 430, 1500, 530, fill = 'black')

            
            
        def updatey(value):
            yay.delete(ALL)
            proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
            projectile(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
            results(speed1=float(sldVelocity.get()), angle1 = float(sldAngle.get()))
            yay.create_rectangle(0, 430, 1500, 530, fill = 'black')

        sldVelocity = Scale(pjm, from_=0, to=100, command = updatex, orient = VERTICAL)
        sldVelocity.grid(row=1, column=1)
        sldAngle = Scale(pjm, from_=0, to=90, command = updatey, orient = VERTICAL)
        sldAngle.grid(row=1, column=2)

        def showmovement():
            x0 = 190
            y0 = 410
            xb = 210
            yb = 430
            proball = yay.create_oval(x0, y0, xb, yb, fill = 'blue')
            priball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
            angle = sldAngle.get()
            speed = sldVelocity.get()
            g = 9.81        
            Vx = float(speed) * math.cos(math.radians(float(angle)))
            Vy = float(speed) * math.sin(math.radians(float(angle)))
            if Vy > 0:
                time = (2*Vy)/g
                Range = Vx*time
                maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
            else:
                time = 0
                Range = 0
                maxheight = 0

            if angle == 0:
                Vx = 0
                
            
            print ('Angle:', str(angle), 'degrees')    
            print ('Velocity:', str(speed)+'m/s')
            print ('X motion:', str(Vx)+'m/s')
            print ('Y motion:', str(Vy)+'m/s')
            print ('Air Time:', str(time)+'s')
            print ('MaxHeight:', str(maxheight)+'m')

            x = 1
            y = 1
            
            while True:
                btnMotion = Button(pjm, text = 'Show Movement', command = pause, width=15, relief = SUNKEN)
                btnMotion.grid(row=2, column = 1)
                btnClear = Button(pjm, text = 'Clear', command=pause, width=10, relief = SUNKEN)
                btnClear.grid(row=2, column = 2)
                sldAngle.config(state = DISABLED)
                sldVelocity.config(state = DISABLED)

                if speed == 0 and angle >= 0:
                    priball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
                    break

                if speed >0 and angle == 0:
                    messagebox.showinfo('Error', 'The ball will move forever!!! \n This is due to zero friction along the horizontal displacement.')
                    break
                    
                else:
                    y2 = -1*(Vy*x+(-0.5*g*x**2))+410
                    x3 = Vx
                    y3 = -1*(Vy*x+(-0.5*g*x**2))- (-1*(Vy*(x-1)+(-0.5*g*(x-1)**2)))
                    yay.move(priball, x3, y3)
                    line = yay.create_line((Vx*(x-1))+200, -1*(Vy*(x-1)+(-0.5*g*(x-1)**2))+420, (Vx*x)+200, -1*(Vy*x+(-0.5*g*x**2))+420, fill= 'yellow')
                    yay.after(100)
                    yay.update()
                    position = yay.coords(line)
                    print (position)

                    yay.create_rectangle(0, 450, 1500, 530, fill = 'black')

                    if y2>=410:
                        break
                    x += 1

            btnMotion = Button(pjm, text = 'Show Movement', command = showmovement, width=15, relief = RAISED)
            btnMotion.grid(row=2, column = 1)
            btnClear = Button(pjm, text = 'Clear', command=clear, width=10, relief = RAISED)
            btnClear.grid(row=2, column = 2)
            sldAngle.config(state = NORMAL)
            sldVelocity.config(state = NORMAL)
        

        btnMotion = Button(pjm, text = 'Show Movement', command = showmovement, width=15)
        btnMotion.grid(row=2, column = 1)

    '..............................................................................................................'    
    def results(speed1=0, angle1=0):
        g = 9.81        
        XMotion = float(speed1) * math.cos(math.radians(float(angle1)))
        YMotion = float(speed1) * math.sin(math.radians(float(angle1)))
        AirTime1 = (2*YMotion)/g

        if YMotion > 0:
            
            AirTime1 = (2*YMotion)/g
            Range1 = XMotion*AirTime1
            MaxHeight1 = YMotion*(AirTime1/2) - 0.5*g*(AirTime1/2)**2
            if angle1<90:
                XMotion = XMotion
                Range1 = Range1
            
            elif angle1==90:
                XMotion = 0
                Range1 = 0
            
               
        else:        
            AirTime1 = 0
            Range1 = 0
            MaxHeight1 = 0
        

        XMotion = str(XMotion)[0:5]
        YMotion = str(YMotion)[0:5]
        AirTime = str(AirTime1)[0:5]
        Angle = str(angle1)[0:5]
        Speed = str(speed1)[0:5]
        MaxHeight = str(MaxHeight1)[0:5]
        Range1 = str(Range1)[0:5]
        g1 = str(g)
        
        L1.config(text = str(XMotion)+'m/s')
        L2.config(text = str(YMotion)+'m/s')
        L3.config(text = str(AirTime)+'s')
        L4.config(text = str(Angle)+'degrees')
        L5.config(text = str(Speed)+'m/s')
        L6.config(text = str(MaxHeight)+'m')
        L7.config(text = str(Range1)+'m')
        L8.config(text = str(g)+'m/s^2')

    '.........................................................................................................'

    def projectile(speed=0, angle=0):
        g = 9.81        
        Vx = float(speed) * math.cos(math.radians(float(angle)))
        Vy = float(speed) * math.sin(math.radians(float(angle)))
           
            
        if Vy > 0:
            time = (2*Vy)/g
            Range = Vx*time
            maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
        else:
            time = 0
            Range = 0
            maxheight = 0
            
        if angle == 0:
            Vx = 0
        
        print ('Angle:', str(angle), 'degrees')    
        print ('Velocity:', str(speed)+'m/s')
        print ('X motion:', str(Vx)+'m/s')
        print ('Y motion:', str(Vy)+'m/s')
        print ('Air Time:', str(time)+'s')
        print ('MaxHeight:', str(maxheight)+'m')
        
        if angle >= 0 and speed == 0:
            for t in range(1, 40):
                x1 = Vx*(t-1)+40
                x2 = (Vx*t)+40
                y1 = -1*(Vy*(t-1)+(-0.5*g*(t-1)**2))+450
                y2 = -1*(Vy*t+(-0.5*g*t**2))+450
                proline = yay.create_line((Vx*(t-1))+200, -1*(Vy*(t-1)+(-0.5*g*(t-1)**2))+420, (Vx*t)+200, -1*(Vy*t+(-0.5*g*t**2))+420, fill = 'yellow')
        elif angle == 0 and speed>0:
            xline = yay.create_line(200, 420, 1500, 420, fill = 'black')
        else:
            for t in range(1, 40):
                x1 = Vx*(t-1)+40
                
                x2 = (Vx*t)+40
                y1 = -1*(Vy*(t-1)+(-0.5*g*(t-1)**2))+450
                y2 = -1*(Vy*t+(-0.5*g*t**2))+450
                proline = yay.create_line((Vx*(t-1))+200, -1*(Vy*(t-1)+(-0.5*g*(t-1)**2))+420, (Vx*t)+200, -1*(Vy*t+(-0.5*g*t**2))+420, fill = 'black')


    '....................................................................................................................'

    def showmovement():
        x0 = 190
        y0 = 410
        xb = 210
        yb = 430
        proball = yay.create_oval(x0, y0, xb, yb, fill = 'blue')
        priball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
        angle = sldAngle.get()
        speed = sldVelocity.get()
        g = 9.81        
        Vx = float(speed) * math.cos(math.radians(float(angle)))
        Vy = float(speed) * math.sin(math.radians(float(angle)))
        if Vy > 0:
            time = (2*Vy)/g
            Range = Vx*time
            maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
        else:
            time = 0
            Range = 0
            maxheight = 0

        if angle == 0:
            Vx = 0
            
        
        print ('Angle:', str(angle), 'degrees')    
        print ('Velocity:', str(speed)+'m/s')
        print ('X motion:', str(Vx)+'m/s')
        print ('Y motion:', str(Vy)+'m/s')
        print ('Air Time:', str(time)+'s')
        print ('MaxHeight:', str(maxheight)+'m')

        x = 1
        y = 1
        
        while True:
            sldAngle.config(state = DISABLED)
            sldVelocity.config(state = DISABLED)
            btnMotion = Button(pjm, text = 'Show Movement', command = pause, width=15, relief = SUNKEN)
            btnMotion.grid(row=2, column = 1)
            btnClear = Button(pjm, text = 'Clear', command=pause, width=10, relief = SUNKEN)
            btnClear.grid(row=2, column = 2)

            if speed == 0 and angle >= 0:
                priball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
                break
                

            if speed >0 and angle == 0:
                messagebox.showinfo('Error', 'The ball will move forever!!! \n This is due to zero friction along the horizontal displacement.')
                break
            
            else:
                y2 = -1*(Vy*x+(-0.5*g*x**2))+410
                x3 = Vx
                y3 = -1*(Vy*x+(-0.5*g*x**2))- (-1*(Vy*(x-1)+(-0.5*g*(x-1)**2)))
                yay.move(priball, x3, y3)
                line = yay.create_line((Vx*(x-1))+200, -1*(Vy*(x-1)+(-0.5*g*(x-1)**2))+420, (Vx*x)+200, -1*(Vy*x+(-0.5*g*x**2))+420, fill= 'yellow')
                yay.after(100)
                
                yay.update()
                position = yay.coords(line)
                print (position)

                yay.create_rectangle(0, 450, 1500, 530, fill = 'black')

                if y2>=410:
                    break
                x += 1

        btnMotion = Button(pjm, text = 'Show Movement', command = showmovement, width=15, relief = RAISED)
        btnMotion.grid(row=2, column = 1)
        btnClear = Button(pjm, text = 'Clear', command=clear, width=10, relief = RAISED)
        btnClear.grid(row=2, column = 2)
        sldAngle.config(state = NORMAL)
        sldVelocity.config(state = NORMAL)
        
                 
            
    '................................................................................................................................................'
    def updatex(value):
        yay.delete(ALL)
        proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
        projectile(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
        results(speed1=float(sldVelocity.get()), angle1 = float(sldAngle.get()))
        yay.create_rectangle(0, 430, 1500, 530, fill = 'black')

        
        
    def updatey(value):
        yay.delete(ALL)
        proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
        projectile(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
        results(speed1=float(sldVelocity.get()), angle1 = float(sldAngle.get()))
        yay.create_rectangle(0, 430, 1500, 530, fill = 'black')

        

    '..............................................................................................................................................'    
    yay.create_rectangle(0, 400, 1500, 440, fill = 'black')
    proballo = yay.create_rectangle(x0, y0, xx, yy, fill = 'black')
    white = yay.create_rectangle(x0, 420, xx, 416, fill = 'white')
    lbEnergy = Label(pjm, text = 'Velocity(m/s)', width = 15)
    lbEnergy.grid(row = 0, column = 1)
    lbAngle = Label(pjm, text='Angle(degrees)', width = 15)
    lbAngle.grid(row=0, column=2)
    btnMotion = Button(pjm, text = 'Show Movement', command = showmovement, width=15)
    btnMotion.grid(row=2, column = 1)
    btnClear = Button(pjm, text = 'Clear', command=clear, width=10)
    btnClear.grid(row=2, column = 2)
    sldVelocity = Scale(pjm, from_=0, to=100, command = updatex, orient = VERTICAL)
    sldVelocity.grid(row=1, column=1)
    sldAngle = Scale(pjm, from_=0, to=90, command = updatey, orient = VERTICAL)
    sldAngle.grid(row=1, column=2)

    '............................................................................................'

    lbXMotion = Label(btmframe, text = 'X Motion:   ')
    lbXMotion.grid(row = 0, column = 1)
    L1 = Label(btmframe, text = '0'+ 'm/s')
    L1.grid(row = 1, column = 1)

    lbYMotion = Label(btmframe, text = 'Y Motion:   ')
    lbYMotion.grid(row = 0, column = 2)
    L2 = Label(btmframe, text = '0' + 'm/s')
    L2.grid(row = 1, column = 2)

    lbAirTime = Label(btmframe, text = 'Air Time:   ')
    lbAirTime.grid(row = 0, column = 3)
    L3 = Label(btmframe, text = '0' + 's')
    L3.grid(row = 1, column = 3)

    lbMaxHeight = Label(btmframe, text = 'Max Height:   ')
    lbMaxHeight.grid(row = 0, column = 4)
    L6 = Label(btmframe, text = '0' + 'm')
    L6.grid(row = 1, column = 4)

    lbSpeed = Label(btmframe, text = 'Resultant speed:   ')
    lbSpeed.grid(row = 0, column = 5)
    L5 = Label(btmframe, text = '0'+ 'm/s')
    L5.grid(row = 1, column = 5)

    lbAngle = Label(btmframe, text = 'Angle:     ')
    lbAngle.grid(row = 0, column =6)
    L4= Label(btmframe, text = '0'+ 'degrees')
    L4.grid(row = 1, column = 6)

    lbRange1 = Label(btmframe, text = 'Range:   ')
    lbRange1.grid (row = 0, column =7)
    L7 = Label(btmframe, text = '0' + 'm')
    L7.grid(row = 1, column = 7)

    lbg = Label(btmframe, text = 'Gravitational Acceleration:')
    lbg.grid (row = 0, column = 8)
    L8 = Label(btmframe, text = '9.81' + 'm/s^2')
    L8.grid(row = 1,column = 8)
    
def guidepopup_game():
    func_of_guidepopup_game()
    
def func_of_guidepopup_game():
    self = Tk()
    self.title("How to Play the Game")
    self.config(bg = 'light green')
    
    Label(self, text = ' Step 1 : Adjust the slider for Velocity and Angle to aim the cannon to the target ', bg = 'light green').grid(row = 0, column = 1)
    Label(self, text = ' Step 2 : Click on the \'Shoot\' button to launch the cannon ball from the cannon  ', bg = 'light green').grid(row = 1, column = 1)
    Label(self, text = ' Step 3 : Using the theory that you have learned, try to hit Target 1 and Target 2 ', bg = 'light green').grid(row = 2, column = 1)
    Label(self, text = ' Extra Step : To change the position of the target, click the \'New Target\' button', bg = 'light green').grid(row = 3, column = 1)
    Label(self, text = ' Special Note : The box next to the sliders displays the horizontal distance of the \n cannon and displacement from ground to the target.', bg = 'light green').grid(row = 4, column = 1)
    Label(self, text = ' Apply these values into the formulas you have learnt in the theory page to estimate a suitable velocity and angle to hit the targets', bg = 'light green').grid(row = 5, column = 1)
    
    def close_window():
        self.destroy()
        
    Button(self, text = 'OK',command = close_window).grid(row = 6, column = 1)
    
    self.mainloop()
    
def AppPage():
    refresh()
    abc()
    main.geometry('1300x800')
    func_of_AppPage()

def func_of_AppPage():
    refresh()
    abc()
    global Button_Disabler, tg
    
    Button_Disabler = 3
    button_row()

    '.........................................................................................'
    
    Label(bottomframe, text = "This page lets you play an interractive game")
    topframe2 = LabelFrame(bottomframe, text = 'Projectile Motion Demo')
    topframe2.grid(row=0, column = 1)
    
    midframe = LabelFrame(bottomframe, text = 'Projectile Motion Game', bg = 'green')
    midframe.grid(row=0, column = 1)
    yay = Canvas(midframe, width = 1200, height = 440, bg ='white')
    yay.grid(row = 1)
    
    pjm = Canvas(midframe, height = 250)
    pjm.grid(row = 2)
    
    guide_button = Button(midframe, text = 'Guide',command = guidepopup_game, bg = 'brown', fg = 'white', relief = 'solid')
    guide_button.place(relx= 0.97,rely= 0.95,  anchor = 'center')

    '.....................................................................................................'
    #for proball
    x0 = 190
    y0 = 420
    xx = 210
    yy = 440

    '.......................................................................................................'
    #background pic

    photo = PhotoImage(file = 'sunnyday.gif')

    '..........................................................................................................'
    #making targets for game
    def ranxy():
        global c, p, d, t
        c = random.randint(490, 640) #xcoord for target 1
        d = random.randint(720, 820) #xcoord for target 2
        p = random.randint(50, 290) #ycoord for target 1
        t = random.randint(50,290) #ycoord for target 2

    def target1():
        global target1_y, target1_x
        tar0 = yay.create_oval(c-53, p-53, c+53, p+53, fill = 'green')
        target1_y = 440 - ((yay.coords(tar0)[1] + yay.coords(tar0)[3])/2)
        target1_x = ((yay.coords(tar0)[0] + yay.coords(tar0)[2])/2) - 200
        tar1 = yay.create_oval(c-50, p-50, c+50, p+50, fill = 'white')
        tar2 = yay.create_polygon(c-28, p-28, c-8, p-40, c+11, p-40, c+11, p+40, c-11, p+40, c-11, p-15, c-28, p-15, fill = 'red')
        tar6 = yay.create_line(c, p-15, c, p+15, fill = 'black')
        tar7 = yay.create_line(c-15, p, c+15, p, fill = 'black')
        #distfromground = pjm.create_text(c, p+75, text = " text = "Perpendicular distance from the Ground: " + str(target1_x) + "  metres"", activefill = 'white')
        #distfromcannon = pjm.create_text(c, p+90, text = "Perpendicular distance from Cannon: " + str(target1_y) + "  metres", activefill = 'white')
        
    def target2():
        tar0 = yay.create_oval(d-53, t-53, d+53, t+53, fill = 'green')
        tar1 = yay.create_oval(d-50, t-50, d+50, t+50, fill = 'white')
        tar2 = yay.create_polygon(d-25, t-40, d+25, t-40, d+25, t+8, d-10, t+8, d-10, t+24, d+25, t+24, d+25, t+40, d-25, t+40, d-25, t-8, d+10, t-8, d+10, t-24, d-25, t-24,  fill = 'red')
        tar6 = yay.create_line(d, t-15, d, t+15, fill = 'black')
        tar7 = yay.create_line(d-15, t, d+15, t, fill = 'black')
        target2_y = 440 - ((yay.coords(tar0)[1] + yay.coords(tar0)[3])/2)
        target2_x = ((yay.coords(tar0)[0] + yay.coords(tar0)[2])/2) - 200
        #distfromground = yay.create_text(d, t+75, text = "Distance from ground: " + str(target2_y) + "  metres", activefill = 'white')
        #distfromcannon = yay.create_text(d, t+90, text = "Perpendicular distance from Cannon: " + str(target2_x) + "  metres", activefill = 'white')
        #Button(pjm, text = "TARGET 2 : \nPerpendicular distance from Cannon: " + str(target2_x) + "  metres \nDistance from the ground: " + str(target2_y) + "  metres", state = DISABLED, relief = 'solid').grid(row = 1, column = 3)
        Button(pjm, text = "TARGET 1 : \nHorizontal distance from Cannon: " + str(target1_x) + "  metres \nDistance from the ground: " + str(target1_y) + "  metres \n \n TARGET 2 : \nHorizontal distance from Cannon: " + str(target2_x) + "  metres \nDistance from the ground: " + str(target2_y) + "  metres", relief = 'solid', state = DISABLED, fg = 'black').grid(row =1, column = 3)
    '..................................................................................................................'
    #making explosions

    def kaboom1():
        #explosions
        bang = 0
        xA = c
        yA = p - 20
        xB = c+ 65*math.cos(math.radians(float(60)))
        yB = p-65*math.sin(math.radians(float(60)))
        xC = c+20*math.cos(math.radians(float(30)))
        yC = p-20*math.sin(math.radians(float(30)))
        xD = c+65
        yD = p
        xE = c+20*math.cos(math.radians(float(30)))
        yE = p+20*math.sin(math.radians(float(30)))
        xF = c+65*math.cos(math.radians(float(60)))
        yF = p+65*math.sin(math.radians(float(60)))
        xG = c + 0
        yG = p + 20
        xH = c-65*math.cos(math.radians(float(60)))
        yH = p+65*math.sin(math.radians(float(60)))
        xI = c-20*math.cos(math.radians(float(30)))
        yI = p+20*math.sin(math.radians(float(30)))
        xJ = c - 65
        yJ = p
        xK = c-20*math.cos(math.radians(float(30)))
        yK = p-20*math.sin(math.radians(float(30)))
        xL = c-65*math.cos(math.radians(float(60)))
        yL = p-65*math.sin(math.radians(float(60)))
    
        xA2 = c
        yA2 = p - 14
        xB2 = c+ 36*math.cos(math.radians(float(60)))
        yB2 = p-36*math.sin(math.radians(float(60)))
        xC2 = c+14*math.cos(math.radians(float(30)))
        yC2 = p-14*math.sin(math.radians(float(30)))
        xD2 = c+36
        yD2 = p
        xE2 = c+14*math.cos(math.radians(float(30)))
        yE2 = p+14*math.sin(math.radians(float(30)))
        xF2 = c+36*math.cos(math.radians(float(60)))
        yF2 = p+36*math.sin(math.radians(float(60)))
        xG2 = c + 0
        yG2 = p + 14
        xH2 = c-36*math.cos(math.radians(float(60)))
        yH2 = p+36*math.sin(math.radians(float(60)))
        xI2 = c-14*math.cos(math.radians(float(30)))
        yI2 = p+14*math.sin(math.radians(float(30)))
        xJ2 = c - 36
        yJ2 = p
        xK2 = c-14*math.cos(math.radians(float(30)))
        yK2 = p-14*math.sin(math.radians(float(30)))
        xL2 = c-36*math.cos(math.radians(float(60)))
        yL2 = p-36*math.sin(math.radians(float(60)))

        xA3 = c
        yA3 = p - 10
        xB3 = c+ 27*math.cos(math.radians(float(60)))
        yB3 = p-27*math.sin(math.radians(float(60)))
        xC3 = c+10*math.cos(math.radians(float(30)))
        yC3 = p-10*math.sin(math.radians(float(30)))
        xD3 = c+27
        yD3 = p
        xE3 = c+10*math.cos(math.radians(float(30)))
        yE3 = p+10*math.sin(math.radians(float(30)))
        xF3 = c+27*math.cos(math.radians(float(60)))
        yF3 = p+27*math.sin(math.radians(float(60)))
        xG3 = c + 0
        yG3 = p + 10
        xH3 = c-27*math.cos(math.radians(float(60)))
        yH3 = p+27*math.sin(math.radians(float(60)))
        xI3 = c-10*math.cos(math.radians(float(30)))
        yI3 = p+10*math.sin(math.radians(float(30)))
        xJ3 = c - 27
        yJ3 = p
        xK3 = c-10*math.cos(math.radians(float(30)))
        yK3 = p-10*math.sin(math.radians(float(30)))
        xL3 = c-27*math.cos(math.radians(float(60)))
        yL3 = p-27*math.sin(math.radians(float(60)))

        yay.create_polygon(xA, yA, xB, yB, xC, yC, xD, yD, xE, yE, xF, yF, xG, yG, xH, yH, xI, yI, xJ, yJ, xK, yK, xL, yL, fill = 'yellow')
        yay.create_polygon(xA2, yA2, xB2, yB2, xC2, yC2, xD2, yD2, xE2, yE2, xF2, yF2, xG2, yG2, xH2, yH2, xI2, yI2, xJ2, yJ2, xK2, yK2, xL2, yL2, fill = 'red')
        yay.create_polygon(xA3, yA3, xB3, yB3, xC3, yC3, xD3, yD3, xE3, yE3, xF3, yF3, xG3, yG3, xH3, yH3, xI3, yI3, xJ3, yJ3, xK3, yK3, xL3, yL3, fill = 'black')

    def kaboom2():
        #explosions
        bang = 0
        xA = d
        yA = t - 20
        xB = d+ 65*math.cos(math.radians(float(60)))
        yB = t-65*math.sin(math.radians(float(60)))
        xC = d+20*math.cos(math.radians(float(30)))
        yC = t-20*math.sin(math.radians(float(30)))
        xD = d+65
        yD = t
        xE = d+20*math.cos(math.radians(float(30)))
        yE = t+20*math.sin(math.radians(float(30)))
        xF = d+65*math.cos(math.radians(float(60)))
        yF = t+65*math.sin(math.radians(float(60)))
        xG = d + 0
        yG = t + 20
        xH = d-65*math.cos(math.radians(float(60)))
        yH = t+65*math.sin(math.radians(float(60)))
        xI = d-20*math.cos(math.radians(float(30)))
        yI = t+20*math.sin(math.radians(float(30)))
        xJ = d - 65
        yJ = t
        xK = d-20*math.cos(math.radians(float(30)))
        yK = t-20*math.sin(math.radians(float(30)))
        xL = d-65*math.cos(math.radians(float(60)))
        yL = t-65*math.sin(math.radians(float(60)))
    
        xA2 = d
        yA2 = t - 14
        xB2 = d+ 36*math.cos(math.radians(float(60)))
        yB2 = t-36*math.sin(math.radians(float(60)))
        xC2 = d+14*math.cos(math.radians(float(30)))
        yC2 = t-14*math.sin(math.radians(float(30)))
        xD2 = d+36
        yD2 = t
        xE2 = d+14*math.cos(math.radians(float(30)))
        yE2 = t+14*math.sin(math.radians(float(30)))
        xF2 = d+36*math.cos(math.radians(float(60)))
        yF2 = t+36*math.sin(math.radians(float(60)))
        xG2 = d + 0
        yG2 = t + 14
        xH2 = d-36*math.cos(math.radians(float(60)))
        yH2 = t+36*math.sin(math.radians(float(60)))
        xI2 = d-14*math.cos(math.radians(float(30)))
        yI2 = t+14*math.sin(math.radians(float(30)))
        xJ2 = d - 36
        yJ2 = t
        xK2 = d-14*math.cos(math.radians(float(30)))
        yK2 = t-14*math.sin(math.radians(float(30)))
        xL2 = d-36*math.cos(math.radians(float(60)))
        yL2 = t-36*math.sin(math.radians(float(60)))
        
        xA3 = d
        yA3 = t - 10
        xB3 = d+ 27*math.cos(math.radians(float(60)))
        yB3 = t-27*math.sin(math.radians(float(60)))
        xC3 = d+10*math.cos(math.radians(float(30)))
        yC3 = t-10*math.sin(math.radians(float(30)))
        xD3 = d+27
        yD3 = t
        xE3 = d+10*math.cos(math.radians(float(30)))
        yE3 = t+10*math.sin(math.radians(float(30)))
        xF3 = d+27*math.cos(math.radians(float(60)))
        yF3 = t+27*math.sin(math.radians(float(60)))
        xG3 = d + 0
        yG3 = t + 10
        xH3 = d-27*math.cos(math.radians(float(60)))
        yH3 = t+27*math.sin(math.radians(float(60)))
        xI3 = d-10*math.cos(math.radians(float(30)))
        yI3 = t+10*math.sin(math.radians(float(30)))
        xJ3 = d - 27
        yJ3 = t
        xK3 = d-10*math.cos(math.radians(float(30)))
        yK3 = t-10*math.sin(math.radians(float(30)))
        xL3 = d-27*math.cos(math.radians(float(60)))
        yL3 = t-27*math.sin(math.radians(float(60)))

        yay.create_polygon(xA, yA, xB, yB, xC, yC, xD, yD, xE, yE, xF, yF, xG, yG, xH, yH, xI, yI, xJ, yJ, xK, yK, xL, yL, fill = 'yellow')
        yay.create_polygon(xA2, yA2, xB2, yB2, xC2, yC2, xD2, yD2, xE2, yE2, xF2, yF2, xG2, yG2, xH2, yH2, xI2, yI2, xJ2, yJ2, xK2, yK2, xL2, yL2, fill = 'red')
        yay.create_polygon(xA3, yA3, xB3, yB3, xC3, yC3, xD3, yD3, xE3, yE3, xF3, yF3, xG3, yG3, xH3, yH3, xI3, yI3, xJ3, yJ3, xK3, yK3, xL3, yL3, fill = 'black')

    '...............................................................................................................'
    #disable shoot button while shooting
    def pause():
        print ('Nothing')

    '............................................................................................................'
    #move nozzle of cannon
    def cannon(angle=0):
        x1 = 10* math.sin(math.radians(float(angle)))
        y1 = 10* math.cos(math.radians(float(angle)))
        x2 = 10* math.sin(math.radians(float(angle)))
        y2 = 10* math.cos(math.radians(float(angle)))
        x3 = 60.828* math.cos(math.radians(float(angle) + 9.46))
        y3 = 60.828* math.sin(math.radians(float(angle) + 9.46))
        x4 = 60.828* math.cos(math.radians(9.46 - float(angle)))
        y4 = 60.828* math.sin(math.radians(9.46 - float(angle)))

        #Cannon = yay.create_polygon(200, 400, 200, 420, 260, 420, 260, 400)
        Cannon = yay.create_polygon(200-x1, 410-y1, 200+x2, 410+y2, 200+x4, 410+y4, 200+x3, 410-y3, fill = 'black')
    '..................................................................................................................'
    #resets game     
    def reset():
        yay.delete('all')
        pjm.delete('all')
        ranxy()
        target1()
        target2()
        photo = PhotoImage(file = 'sunnyday.gif')
        basec = yay.create_rectangle(150, 430, 250, 440)
        ballc = yay.create_oval(170,380 , 230, 440)
        #Cannon = yay.create_polygon(200, 400, 200, 420, 260, 420, 260, 400)
        yay.create_rectangle(0, 440, 1500, 530, fill = 'black')
        lbEnergy = Label(pjm, text = 'Velocity (m/s)', width = 12)
        lbEnergy.grid(row = 0, column = 1)
        lbAngle = Label(pjm, text='Angle (degrees)', width = 15)
        lbAngle.grid(row=0, column=2)
        btnClear = Button(pjm, text = 'New Target', command=reset, width=10)
        btnClear.grid(row=2, column = 2)
       
        def updatex(value):
            yay.delete(ALL)
            aim(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
            yay.create_image(0, 0, image=photo, anchor = NW)
            yay.create_rectangle(0, 440, 1500, 530, fill = 'black')
            ballc = yay.create_oval(170,380 , 230, 440, fill = 'black')
            basec = yay.create_rectangle(150, 430, 250, 440, fill = 'white')
            cannon(angle = sldAngle.get())
            target1()
            target2()
        
        def updatey(value):
            yay.delete(ALL)
            aim(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
            yay.create_image(0, 0, image=photo, anchor = NW)
            yay.create_rectangle(0, 440, 1500, 530, fill = 'black')
            ballc = yay.create_oval(170,380 , 230, 440, fill = 'black')
            basec = yay.create_rectangle(150, 430, 250, 440, fill = 'white')
            cannon(angle = sldAngle.get())
            target1()
            target2()

        sldVelocity = Scale(pjm, from_=0, to=100, command = updatex, orient = VERTICAL)
        sldVelocity.grid(row=1, column=1)
        sldAngle = Scale(pjm, from_=0, to=90, command = updatey, orient = VERTICAL)
        sldAngle.grid(row=1, column=2)

        def shoot(angle = 0):
            angle = sldAngle.get()
            x0 = 190 + 50*math.cos(math.radians(float(angle)))
            y0 = 400 - 50*math.sin(math.radians(float(angle)))
            xb = 210 + 50*math.cos(math.radians(float(angle)))
            yb = 420 - 50*math.sin(math.radians(float(angle)))
            proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
            angle = sldAngle.get()
            speed = sldVelocity.get()
            g = 9.81        
            Vx = float(speed) * math.cos(math.radians(float(angle)))
            Vy = float(speed) * math.sin(math.radians(float(angle)))
            if Vy > 0:
                time = (2*Vy)/g
                Range = Vx*time
                maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
            else:
                time = 0
                Range = 0
                maxheight = 0

            if angle == 0:
                Vx = 0
                
            
            print ('Angle:', str(angle), 'degrees')    
            print ('Velocity:', str(speed)+'m/s')
            print ('X motion:', str(Vx)+'m/s')
            print ('Y motion:', str(Vy)+'m/s')
            print ('Air Time:', str(time)+'s')
            print ('MaxHeight:', str(maxheight)+'m')

            XMotion = str(Vx)[0:7]
            YMotion = str(Vy)[0:7]
            AirTime = str(time)[0:5]
            Angle = str(angle)[0:7]
            Speed = str(speed)[0:7]
            MaxHeight = str(maxheight)[0:7]
            Range1 = str(Range)[0:7]


            x = 1
            counter1 = 0
            counter2 = 0

            while True:
                sldAngle.config(state = DISABLED)
                sldVelocity.config(state = DISABLED)
                btnClear = Button(pjm, text = 'New Target', command = pause, width=10, relief = SUNKEN)
                btnClear.grid(row=2, column = 2)
                btnMotion = Button(pjm, text = 'Shoot', command = pause, width=15, relief = SUNKEN)
                btnMotion.grid(row=2, column = 1)


                if speed == 0 and angle >= 0:
                    break

                if speed >0 and angle == 0:
                    messagebox.showinfo('Error', 'The ball will move forever!!! \n This is due to zero friction along the horizontal displacement.')
                    break
                    
                else:
                    xt = (Vx*x)+ (200 + 50*math.cos(math.radians(float(angle))))
                    yt = -1*(Vy*x+(-0.5*g*x**2))+ (410 - 50*math.sin(math.radians(float(angle))))
                    xball = Vx
                    yball = -1*(Vy*x+(-0.5*g*x**2))- (-1*(Vy*(x-1)+(-0.5*g*(x-1)**2)))
                    yay.move(proball, xball, yball)
                    yay.after(100)
                    yay.update()
                    position = yay.coords(proball)
                    print (position)
                    yay.create_rectangle(0, 450, 1500, 530, fill = 'black')

                    t1 = c-50
                    t2 = c+50
                    t3 = p-50
                    t4 = p+50
                    t5 = d-50
                    t6 = d+50
                    t7 = t-50
                    t8 = t+50
                    
                    if (xt > t1 and xt < t2) and (yt > t3 and yt < t4):
                        counter1 += 1
                        kaboom1()

                    if (xt > t5 and xt < t6) and (yt > t7 and yt < t8):
                        counter2 += 2
                        kaboom2()
     
                    if yt>= 425:
                        if counter1 == 0 and counter2 == 0:
                            messagebox.showinfo('No hit', 'No target hit. Try again! \n \n CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                        if counter1 == 0 and counter2 > 0:
                            messagebox.showinfo('Target 2 hit!!','CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                        if counter1 > 0 and counter2 == 0:
                            messagebox.showinfo('Target 1 hit!!','CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                        if counter1 >0 and counter2>0:
                            messagebox.showinfo('COMBO!!!','Target 1 and Target 2 hit!!! \n \n CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                        break
                    
                    x += 1
                    
            btnMotion = Button(pjm, text = 'Shoot', command = shoot, width=15, relief = RAISED)
            btnMotion.grid(row=2, column = 1)
            sldAngle.config(state = NORMAL)
            sldVelocity.config(state = NORMAL)
            btnClear = Button(pjm, text = 'New Target', command = reset, width=10, relief = RAISED)
            btnClear.grid(row=2, column = 2)

        btnMotion = Button(pjm, text = 'Shoot', command = shoot, width=15)
        btnMotion.grid(row=2, column = 1)

    '.........................................................................................................'
    #targets the ball to the target
    def aim(speed=0, angle=0):
        g = 9.81        
        Vx = float(speed) * math.cos(math.radians(float(angle)))
        Vy = float(speed) * math.sin(math.radians(float(angle)))
        if Vy > 0:
            time = (2*Vy)/g
            Range = Vx*time
            maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
        else:
            time = 0
            Range = 0
            maxheight = 0
        if angle == 0:
            Vx = 0

        
        print ('Angle:', str(angle), 'degrees')    
        print ('Velocity:', str(speed)+'m/s')
        print ('X motion:', str(Vx)+'m/s')
        print ('Y motion:', str(Vy)+'m/s')
        print ('Air Time:', str(time)+'s')
        print ('MaxHeight:', str(maxheight)+'m')


    '....................................................................................................................'
    #runs ball animation aka shoot ball
    def shoot(angle = 0):
        global counter1, counter2
        angle = sldAngle.get()
        x0 = 190 + 50*math.cos(math.radians(float(angle)))
        y0 = 400 - 50*math.sin(math.radians(float(angle)))
        xb = 210 + 50*math.cos(math.radians(float(angle)))
        yb = 420 - 50*math.sin(math.radians(float(angle)))
        proball = yay.create_oval(x0, y0, xb, yb, fill = 'yellow')
        angle = sldAngle.get()
        speed = sldVelocity.get()
        g = 9.81        
        Vx = float(speed) * math.cos(math.radians(float(angle)))
        Vy = float(speed) * math.sin(math.radians(float(angle)))
        if Vy > 0:
            time = (2*Vy)/g
            Range = Vx*time
            maxheight = Vy*(time/2) - 0.5*g*(time/2)**2
        else:
            time = 0
            Range = 0
            maxheight = 0

        if angle == 0:
            Vx = 0
            
        
        print ('Angle:', str(angle), 'degrees')    
        print ('Velocity:', str(speed)+'m/s')
        print ('X motion:', str(Vx)+'m/s')
        print ('Y motion:', str(Vy)+'m/s')
        print ('Air Time:', str(time)+'s')
        print ('MaxHeight:', str(maxheight)+'m')

        XMotion = str(Vx)[0:7]
        YMotion = str(Vy)[0:7]
        AirTime = str(time)[0:5]
        Angle = str(angle)[0:7]
        Speed = str(speed)[0:7]
        MaxHeight = str(maxheight)[0:7]
        Range1 = str(Range)[0:7]

        x = 1
        counter1 = 0
        counter2 = 0
        
        while True:
            sldAngle.config(state = DISABLED)
            sldVelocity.config(state = DISABLED)
            btnClear = Button(pjm, text = 'New Target', command = pause, width=10, relief = SUNKEN)
            btnClear.grid(row=2, column = 2)
            btnMotion = Button(pjm, text = 'Shoot', command = pause, width=15, relief = SUNKEN)
            btnMotion.grid(row=2, column = 1)

            if speed == 0 and angle >= 0:
                break
                

            if speed >0 and angle == 0:
                messagebox.showinfo('Error', 'The ball will move forever!!! \n This is due to zero friction along the horizontal displacement.')
                break
                        
            else:
                xt = (Vx*x)+ (200 + 50*math.cos(math.radians(float(angle))))
                yt = -1*(Vy*x+(-0.5*g*x**2))+ (410 - 50*math.sin(math.radians(float(angle))))
                xball = Vx
                yball = -1*(Vy*x+(-0.5*g*x**2))- (-1*(Vy*(x-1)+(-0.5*g*(x-1)**2)))

                yay.move(proball, xball, yball)
                yay.after(100)
                yay.update()
                position = yay.coords(proball)
                print (position)
                yay.create_rectangle(0, 450, 1500, 530, fill = 'black')

                t1 = c-50
                t2 = c+50
                t3 = p-50
                t4 = p+50
                t5 = d-50
                t6 = d+50
                t7 = t-50
                t8 = t+50

                if (xt > t1 and xt < t2) and (yt > t3 and yt < t4):
                    counter1 += 1
                    kaboom1()

                if (xt > t5 and xt < t6) and (yt > t7 and yt < t8):
                    counter2 += 2
                    kaboom2()
 
                if yt>= 425:
                    if counter1 == 0 and counter2 == 0:
                        messagebox.showinfo('No hit', 'No target hit. Try again! \n \n CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                    if counter1 == 0 and counter2 > 0:
                        messagebox.showinfo('Target 2 hit!!', 'CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                    if counter1 > 0 and counter2 == 0:
                        messagebox.showinfo('Target 1 hit!!','CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                    if counter1 >0 and counter2>0:
                        messagebox.showinfo('COMBO!!!','Target 1 and Target 2 hit!!! \n \n CANNONBALL TRAJECTORY: \n Resultant Speed: %s m/s \n Angle: %s degrees \n X Velocity: %s m/s \n Y Velocity: %s m/s \n Air Time: %s s \n Max Height: %s m \n Range: %s m' %(Speed, Angle, XMotion, YMotion, AirTime, MaxHeight, Range1))
                    break
                
                x += 1
                
                
        btnMotion = Button(pjm, text = 'Shoot', command = shoot, width=15, relief = RAISED)
        btnMotion.grid(row=2, column = 1)
        sldAngle.config(state = NORMAL)
        sldVelocity.config(state = NORMAL)
        btnClear = Button(pjm, text = 'New Target', command = reset, width=10, relief = RAISED)
        btnClear.grid(row=2, column = 2)
 
    '................................................................................................................................................'
    #updates aim 
    def updatex(value):
        yay.delete(ALL)
        yay.create_image(0, 0, image=photo, anchor = NW)
        aim(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
        yay.create_rectangle(0, 440, 1500, 530, fill = 'black')
        ballc = yay.create_oval(170,380 , 230, 440, fill = 'black')
        basec = yay.create_rectangle(150, 430, 250, 440, fill = 'white')
        #Cannon = yay.create_polygon(200, 400, 200, 420, 260, 420, 260, 400)
        cannon(angle = float(sldAngle.get()))
        target1()
        target2()

    #updates aim    
    def updatey(value):
        yay.delete(ALL)
        yay.create_image(0, 0, image=photo, anchor = NW)
        aim(speed=float(sldVelocity.get()), angle = float(sldAngle.get()))
        yay.create_rectangle(0, 440, 1500, 530, fill = 'black')
        ballc = yay.create_oval(170,380 , 230, 440, fill = 'black')
        basec = yay.create_rectangle(150, 430, 250, 440, fill = 'white')
        #Cannon = yay.create_polygon(200, 400, 200, 420, 260, 420, 260, 400)
        cannon(angle = float(sldAngle.get()))
        target1()
        target2()

    '..............................................................................................................................................'
    ranxy()
    yay.create_rectangle(0, 400, 1500, 440, fill = 'black')
    basec = yay.create_rectangle(150, 430, 250, 440, fill = 'white')
    ballc = yay.create_oval(170,380 , 230, 440, fill = 'black')
    #Cannon = yay.create_polygon(200, 400, 200, 420, 260, 420, 260, 400)
    lbEnergy = Label(pjm, text = 'Velocity (m/s)', width = 12)
    lbEnergy.grid(row = 0, column = 1)
    lbAngle = Label(pjm, text='Angle (degrees)', width = 15)
    lbAngle.grid(row=0, column=2)
    btnMotion = Button(pjm, text = 'Shoot', command = shoot, width=15)
    btnMotion.grid(row=2, column = 1)
    btnClear = Button(pjm, text = 'New Target', command=reset, width=10)
    btnClear.grid(row=2, column = 2)
    sldVelocity = Scale(pjm, from_=0, to=100, command = updatex, orient = VERTICAL)
    sldVelocity.grid(row=1, column=1)
    sldAngle = Scale(pjm, from_=0, to=90, command = updatey, orient = VERTICAL)
    sldAngle.grid(row=1, column=2)

    '..................................................................................................'


def ConclusionPage():
    refresh()
    abc()
    main.geometry('1300x800')
    global Button_Disabler
    Button_Disabler = 4
    button_row()
    func_of_ConclusionPage()

def func_of_ConclusionPage():
    kartik = Canvas(bottomframe, width = 870, height = 530)
    nani = kartik.create_image(0,0, image = outroimage, anchor = NW)
    kartik.pack()

    def close_window():
        main.destroy()
        
    Button(bottomframe, text = 'Quit Programme',command = close_window, bg = 'red', fg = 'white', relief = 'solid').place(relx = 0.87, rely = 0.95)
    

startpage()
main.mainloop()     
