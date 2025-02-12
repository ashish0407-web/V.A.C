#voice-operated-calculator
from vosk import Model, KaldiRecognizer
import pyaudio
import time
from tkinter import *
from pygame import mixer
from PIL import Image,ImageTk
import pyttsx3 as pt
from math import *
#from tkvideo import tkvideo


def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

def clear(a):
  for widgets in pradeep.winfo_children():
    widgets.destroy()
  if (a==1):
    form()
  elif(a==2):
    match()
  else:
    Print("sorry")

def clear_intial(b):
   for frame in pradeep.winfo_children():
      frame.destroy()
   if(b==1):
     digital()
   elif(b==2):
     voice()

def match():
  help_dict = { 
  'one':'1', 
  'two':'2', 
  'three': '3', 
  'four': '4', 
  'five': '5', 
  'six': '6', 
  'seven': '7', 
  'eight': '8', 
  'nine': '9', 
  'zero': '0', 
  'minus':'-', 
  'plus':'+', 
  'divide':'/', 
  'multiply':'*', 
  'power':'**', 
  'squareroot':'**1/2', 
  'square':'**2', 
  'log':'log', 
  'percentage':'/100', 
  'sin':'sin',
  'cos':'cos', 
  'tan':'tan', 
  'eleven':'11', 
'twelve':'12', 
'thirteen':'13', 
'fourteen':'14',
'fifteen':'15', 
'sixteen':'16', 
'seventeen':'17', 
'eighteen':'18', 
'nineteen':'19', 
'twenty':'20', 
'twentyone':'21', 
'twentytwo':'22', 
'twentythree':'23', 
'twentyfour':'24', 
'twentyfive':'25', 
'twentysix':'26', 
'twentyseven':'27', 
'twentyeight':'28', 
'twentynine':'29', 
'thirty':'30', 
'thirtyone':'31', 
'thirtytwo':'32', 
'thirtythree':'33', 
'thirtyfour35':'34', 
'thirtyfive':'35', 
'thirtysix':'36', 
'thirtyseven':'37', 
'thirtyeight':'38',
'thirtynine':'39',
'forty':'40',
'fortyone':'41',
'fortytwo':'42',
'fortythree':'43',
'fortyfour':'44',
'fortyfive':'45',
'fortysix':'46',
'fortyseven':'47',
'fortyeight':'48',
'fortynine':'49',
'fifty':'50',
'fiftyone':'51',
'fiftytwo':'52',
'fiftythree':'53',
'fiftyfour':'54',
'fiftyfive':'55',
'fiftysix':'56',
'fiftyseven':'57',
'fiftyeight':'58',
'fiftynine':'59',
'sixty':'60',
'sixtyone':'61',
'sixtytwo':'62',
'sixtythree':'63',
'sixtyfour':'64',
'sixtyfive':'65',
'sixtysix':'66',
'sixtyseven':'67',
'sixtyeight':'68', 
'sixtynine':'69',
'seventy':'70',
'seventyone':'71',
'seventytwo':'72',
'seventythree':'73', 
'seventyfour':'74', 
'seventyfive':'75', 
'seventysix':'76', 
'seventyseven':'77', 
'seventyeight':'78', 
'seventynine':'79', 
'eighty':'80', 
'eightyone':'81', 
'eightytwo':'82', 
'eightythree':'83', 
'eightyfour':'84', 
'eightyfive':'85', 
'eightysix':'86', 
'eightyseven':'87', 
'eightyeight':'88', 
'eightynine':'89', 
'ninety':'90', 
'ninetyone':'91', 
'ninetytwo':'92', 
'ninetythree':'93', 
'ninetyfour':'94', 
'ninetyfive':'95', 
'ninetysix':'96', 
'ninetyseven':'97', 
'ninetyeight':'98', 
'ninetynine':'99', 
'hundred':'100', 
'e':'e', 
'bracket1':'(', 
'space':' ', 
'pie':'π', 
'point':'.', 
'degree':'*π/180', 
'isto':'', 
'by':'/', 
'into':'*', 
'bracket2':')'
}
  
  audio()
  test_str=PYAUDIO
  print("The original string is : " + test_str)
  struct= test_str.split()
  print(struct) 
  res = ''.join(help_dict[ele] for ele in struct) 
  print("The string after performing",res)
  OUTPUT_VOICE.insert(0,res)
  π=22/7-0.00126448927
  OUTPUT_VOICE.delete(0,len(res))
  result=str(eval(res)) 
  text="the result of the above expression if {ans}"
  Speak(text.format(ans=result))
  OUTPUT_VOICE.insert(0,result)

def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    print(Voices) 
    engine.setProperty('voice',Voices[0].id) 
    engine.runAndWait() 
def audio():
    model = Model("C:/Users/Administrator/PycharmProjects/pythonProject2/vosk/vosk-model-small-en-in-0.4")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    speak("your audio is being captured")
    print("your voice is recorded")
    time.sleep(1.5)
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    clear_frame()
 #   Framemohit=Frame(pradeep)
  #  Framemohit.pack()
   # player = tkvideo.tkvideo("C:\\path\\to\\video.mp4", Framemohit, loop = 3, size = (1280,720))
  #  player.play()
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            speak("unable to recognizze your voice")
            speak("please try again")

        elif recognizer.AcceptWaveform(data):
            PYAUDIO1 = recognizer.Result()
            PYAUDIO= PYAUDIO1[14:-3]
            print(PYAUDIO)
            break
def form():
    vishal.maxsize(650,350)
    root = Frame(pradeep)

    entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=32)
    entryField.grid(row=0, column=0, columnspan=10)

    # micImage = PhotoImage(file='download.png')
    # micButton = Button(root, image=micImage, bd=20, bg='blue', activebackground='dodgerblue3')
    # micButton.grid(row=0, column=7)
    mixer.init()

    def click(value):
        ex = entryField.get()  # 789 ex[0:len(ex)-1]
        answer = ''

        try:

            if value == 'C':
                ex = ex[0:len(ex) - 1]  # 78
                entryField.delete(0, END)
                entryField.insert(0, ex)
                return

            elif value == 'CE':
                entryField.delete(0, END)

            elif value == '√':
                answer = math.sqrt(eval(ex))

            elif value == 'π':
                answer = math.pi

            elif value == 'cosθ':
                answer = math.cos(math.radians(eval(ex)))

            elif value == 'tanθ':
                answer = math.tan(math.radians(eval(ex)))

            elif value == 'sinθ':
                answer = math.sin(math.radians(eval(ex)))

            elif value == '2π':
                answer = 2 * math.pi

            elif value == 'cosh':
                answer = math.cosh(eval(ex))

            elif value == 'tanh':
                answer = math.tanh(eval(ex))

            elif value == 'sinh':
                answer = math.sinh(eval(ex))

            elif value == chr(8731):
                answer = eval(ex) ** (1 / 3)

            elif value == 'x\u02b8':  # 7**2
                entryField.insert(END, '**')
                return

            elif value == 'x\u00B3':
                answer = eval(ex) ** 3

            elif value == 'x\u00B2':
                answer = eval(ex) ** 2

            elif value == 'ln':
                answer = math.log2(eval(ex))

            elif value == 'deg':
                answer = math.degrees(eval(ex))

            elif value == "rad":
                answer = math.radians(eval(ex))

            elif value == 'e':
                answer = math.e

            elif value == 'log₁₀':
                answer = math.log10(eval(ex))

            elif value == 'x!':
                answer = math.factorial(eval(ex))

            elif value == chr(247):  # 7/2=3.5
                entryField.insert(END, "/")
                return

            elif value == '=':
                answer = eval(ex)

            else:
                entryField.insert(END, value)
                return

            entryField.delete(0, END)
            entryField.insert(0, answer)

        except SyntaxError:
            pass

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    def mod(a, b):
        return a % b

    def lcm(a, b):
        l = math.lcm(a, b)
        return l

    def hcf(a, b):
        h = math.gcd(a, b)
        return h

    button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                        "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                        "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                        "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                        "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
    rowvalue = 1
    columnvalue = 0
    for i in button_text_list:
        button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='yellow',
                        font=('arial', 12, 'bold'), activebackground='blue', cursor="hand2",
                        command=lambda button=i: click(button))
        button.grid(row=rowvalue, column=columnvalue, pady=0.5, padx=0.5)
        columnvalue += 1
        if columnvalue > 7:
            rowvalue += 1
            columnvalue = 0
    root.pack()
    root.configure(height=400, width=500)
    root.pack_propagate(False)
#defining command 2 over here
def command2():
    speak("you have chosen digit method to input using typing or clicking")
    time.sleep(1.5)
    speak("our only job is to make calculation a enjoyable")
#click mode for calculation
def digital():
    command2()
    #initialising the labels
    lab2=Label(pradeep,text='please wait while loading ....',bg="red",width=35,height=5)
    #packing labels
    lab2.pack(side='bottom', anchor='center')
    time.sleep(2)
    clear(1)
    
def voice():
    speak("thanks for selecting voice input")
    time.sleep(2.5)
    #taking the data from user
    speak("please speak the expression")
    OUTPUT_VOICE=Entry(pradeep,font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=50)
    OUTPUT_VOICE.place(x=150,y=100)
    clear(2)
   
    
def get_audio():
    speak("do you want to select the voice input reply in yes or no")
    audio()
    choice=PYAUDIO
    if choice=='yes':
        voice()
    elif choice=="no":
        speak("please while loading the digital calculator")
        digital()
    else:
        speak("please reply in yes or no")
        get_audio()

def EXIT():
    exIT = Toplevel()
    exIT.geometry("350x125")
    exIT.minsize(350, 125)
    exIT.maxsize(350, 125)
    exIT.configure(bg="white")
    label1 = Label(exIT, text="Do You Want To EXIT ??? ", font={'bold', 'ariel'},fg="White")
    but1 = Button(exIT, text="YES", width=10,fg="Yellow",activebackground="blue",bg="Black", cursor="hand2",command=vishal.destroy)
    but2 = Button(exIT, text="NO", width=10,fg="Yellow",activebackground="blue",bg="Black", cursor="hand2",command=exIT.destroy)
    label1.grid(row=0, column=0, padx=50, pady=25, columnspan=4)
    but1.grid(row=2, column=1)
    but2.grid(row=2, column=2)
    exIT.mainloop()


def contact():
    filemenu = Toplevel(menu)
    filemenu.title('ABOUT')
    Label_filemenu1=label(filemenu,text='')
    Label_filemenu2=label(filemenu,text='contact :')
    Label_filemenu3=label(filemenu,text='vishalsharma@gmail.com')
    Label_filemenu4=label(filemenu,text='Do you want to report the issue ')
    Label_filemenu5=Button(filemenu,text='Ok')
    Label_filemenu1.grid(row=0,column=0)
    Label_filemenu2.grid(row=2,column=1)
    Label_filemenu3.grid(row=2,column=2)
    Label_filemenu4.grid(row=3,column=1,columnspan=3)
    Label_filemenu5.grid(row=4,column=2)
    filemenu.mainloop()

def framevishal():
    speak("welcome to main window ")


#main frame code
def mainframe():
    vishal.minsize(650,400)
    #vishal.maxsize(650,400)
    option_frame=Frame(vishal,bg='#c3c3c3')
    
    #side options
    Home_menu=Button(option_frame,text='HOME',cursor="hand2",command=framevishal,width=15,activebackground="black",activeforeground='white')
    Home_menu.place(x=10,y=95)

    digital_menu=Button(option_frame,text='DIGITAL',cursor="hand2",command=lambda:clear_intial(1),width=15,activebackground="black",activeforeground='white')
    digital_menu.place(x=10,y=140)
    
    voice_menu=Button(option_frame,text='VOICE',cursor="hand2",command=lambda:clear_intial(2),width=15,activebackground="red",activeforeground='white')
    voice_menu.place(x=10,y=185)

    report_menu=Button(option_frame,text='REPORT',cursor="hand2",command=contact,width=15,activebackground="red",activeforeground='white')
    report_menu.place(x=10,y=225)

    
    option_frame.pack(side=LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=150,height=400)

    menu = Menu(vishal)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=EXIT)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=contact)
    vishal.config(menu=menu)
    global pradeep
    pradeep=Frame(vishal,highlightbackground='black',highlightthickness=3)
    gif4 = Image.open("images - 2022-10-29T120216.392.jpeg")
    resize5 = gif4.resize((450, 300), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(resize5)
    lab7 = Label(pradeep, image=image5)
    lab7.pack()
    pradeep.pack_propagate(False)
    pradeep.configure(height=400, width=500)

    speak("you have sucessfully loaded the application")
    pradeep.after(ms=3000,func=get_audio)
    pradeep.pack(side=LEFT)
#defining th speak commands
def command1():
    speak("starting up")
    time.sleep(1.5)
    speak("please wait while loading the required files")

def destro():
    for widgets in vishal.winfo_children():
        widgets.destroy()
    mainframe()



vishal=Tk()
vishal.title('Voice Age Calculator --> V.A.C')
vishal.geometry('400x285')
#JPEG=Image.open("vac.ico")
#JPEG1=ImageTk.PhotoImage(JPEG)
vishal.iconbitmap("vac.ico")
vishal.configure(bg='black')
image6=None
def nam():
    global lab8
    gif5 = Image.open('vac.jpg')
    resize6 = gif5.resize((150, 150), Image.ANTIALIAS)
    image6 = ImageTk.PhotoImage(resize6)
    lab8 = Label(vishal, image=image6)
nam()
lab8.pack()
time.sleep(1.5) 

#inserting image
gif2=Image.open("vac.jpg")
resize2=gif2.resize((300,250),Image.ANTIALIAS)
image2=ImageTk.PhotoImage(resize2) 

lab5=Label(vishal,image=image2)

lab4=Label(vishal,text="Starting up ...",width=150,cursor="watch",fg='white',bg='black', font={"arial",28,"bold"},relief=SUNKEN)

lab5.place(x=50,y=0)
lab4.pack(side='bottom',anchor='center')
vishal.after(ms=50,func=destro)
vishal.after(ms=200,func=command1)
vishal.mainloop()
