from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot =ChatBot("My Bot")

dataset =[
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot ',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Indore',
    'In which language you talk?',
    ' I mostly talk in english'
]

trainer =ListTrainer(bot)

#now training the bot using trainer :
trainer.train(dataset)



# answer=bot.get_response("what is your name?")
# print(answer)

# print(" This is ChatBot :")
# while 1:
#     string =input()
#     if string == 'exit':
#         break
#     else:
#         ans = bot.get_response("what is your name?")
#         print("bot : ",ans)
main = Tk()

# giving dimensions to out window of application
main.geometry("500x700")

# giving title to window
main.title("My Chat Bot")

# storing image in variable named img
img = PhotoImage(file = "bot.png")
# taking image to photoL
photoL = Label(main, image=img)
# displaying image with padding y-axis =10
photoL.pack(pady = 10)


# functin ask_from_bot:
def ask_from_bot():
    que = textF.get()
    ans = bot.get_response(que)
    msgs.insert(END, " You : " +que)
    msgs.insert(END, " Bot : " + str(ans))
    textF.delete(0, END)


# creating a frame inside main
frame = Frame(main)

# creating scrollBrollbar inside frame
scrollB = Scrollbar(frame)
msgs = Listbox(frame, width = 80, height = 21)

scrollB.pack(side=RIGHT, fill=Y)
msgs.pack(side = LEFT, fill = BOTH, pady = 5)
frame.pack(padx=10)

# creating text field :
textF = Entry(main,font=("verdana", 10))
textF.pack(fill=X, padx=10, pady=10)

# creating button
btn = Button(main,text="SEND",font=("verdana",10), command=ask_from_bot)
btn.pack(pady=3)
main.mainloop()



