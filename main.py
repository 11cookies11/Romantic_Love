import random
import threading
import tkinter as tk
# from PIL import Image,ImageTK

class ROMANTIC_LOVE():
    def __init__(self):
        self.window = tk.Tk()
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        print(self.screen_width/50)
        print(self.screen_height/50)

    def showlove(self):
        window = tk.Tk()
        x_show = random.randrange(0,self.screen_width)
        y_show = random.randrange(0,self.screen_height)
        window.geometry("40x50"+"+"+str(x_show)+"+"+str(y_show))
        #
        # tmp = Image.open(".鲜花.png")
        # img = tk.PhotoImage(window,tmp)
        tk.Label(window, text='LOVE', bg='green', font=('宋体', 17), width=20, height=4).pack()
        window.mainloop()


if __name__ == '__main__':
    love = ROMANTIC_LOVE()
    for i in range(10):
        threading.Thread(target=love.showlove).start()

