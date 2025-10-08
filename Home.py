from tkinter import *
from PIL import Image, ImageTk
import View

class Home_QuanXe:
    def __init__(self):
        self.root = Tk()
        self.root.title("Trang chủ")
        self.root.geometry("900x500")


    def show(self):
        
        image = Image.open("Img/main.png")
        photo = ImageTk.PhotoImage(image)

        background_label = Label(self.root, image=photo)
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = Button(self.root, text="START", font=("Arial", 16, "bold"), 
                         bg="black", fg="white", width=12, command=self.eventStart)
        start_button.place(relx=0.5, rely=0.62, anchor="center")

        self.root.mainloop()

    def eventStart(self):
        self.root.destroy()
        view = View.DatQuanXeView()
        view.showView()


if __name__ == "__main__":
    main = Home_QuanXe()
    main.show()





