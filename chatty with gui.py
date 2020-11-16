import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from general_ques import general_ques
from arithmetic import arithmetic_operations
from voice_access import voice_recognizer, speak
warnings.filterwarnings("ignore")
from tkinter import *
from tkinter import scrolledtext

# Reading traing data and tokenizing it
article_raw = open("training data.txt", "r", errors = "ignore")
article = article_raw.read()
article = article.lower()
sentence_list = nltk.sent_tokenize(article)

# to arrange the index
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

# Create the bot bot response
def bot_response(user_input):
    sentence_list.append(user_input)
    bot_response = ""
    count_matrix = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(count_matrix[-1], count_matrix)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + " " + sentence_list[index[i]]
            response_flag = 1
            break

    if response_flag == 0:
        bot_response = bot_response + "I apologise, I don't understand." + "\n"

    sentence_list.remove(user_input)
    return bot_response

def prototype():
    user_input = messageWindow.get()
    user_input = user_input.lower()
    print("USER: " + user_input)
    if user_input == "exit":
        return ("\nBOT: BBye take care. See you soon :) ","It was nice talking to you. See you soon :)\n")
    else:
        if general_ques(user_input) != None:
            return ("\n BOT: " + general_ques(user_input) + "\n\n")
        elif arithmetic_operations(user_input) != None:
            return ("\n BOT: " + arithmetic_operations(user_input) + "\n\n")
        else:
            return ("\n BOT: " + bot_response(user_input) + "\n\n")



def output():
    chatWindow.insert(END, "USER: " + messageWindow.get())
    output = prototype()
    chatWindow.insert(END, output)
    chatWindow.yview_pickplace("end")
    messageWindow.delete(0, "end")

root = Tk()

root.title("ChatBot")

root.geometry("400x500")

messageWindow = Entry(root, bg = "yellow", width = 30)
messageWindow.place(x = 128, y = 400, height = 88, width = 260)

chatWindow = scrolledtext.ScrolledText(root, bd = 1, bg = "light green", width = 50, height = 8)
chatWindow.place(x = 6, y = 6, height = 385, width = 390)


Button = Button(root, command = output, text = "Send", bg = "blue", activebackground = "light blue", width = 12, height = 5, fg = "white", font = ("Arial", 20))
Button.place(x = 6, y = 400, height = 88, width = 120)


#scrollbar = Scrollbar(root, command = chatWindow.yview)
#scrollbar.place(x = 375, y = 5, height = 385)


root.mainloop()