import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from general_ques import general_ques
from arithmetic import arithmetic_operations
from voice_access import voice_recognizer, speak
warnings.filterwarnings("ignore")

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

# Start chat
print("Start your chat")
while True:
    user_input = voice_recognizer()
    user_input = user_input.lower()
    print("USER: " + user_input)
    if user_input == "exit":
        print("\nBOT: BBye take care. See you soon :) ","It was nice talking to you. See you soon :)\n")
        speak("BBye take care. See you soon :) It was nice talking to you. See you soon :)")
        break
    else:
        if general_ques(user_input) != None:
            print("\nBOT: " + general_ques(user_input) + "\n")
            speak(general_ques(user_input))
        elif arithmetic_operations(user_input) != None:
            print("\nBOT: " + arithmetic_operations(user_input) + "\n")
            speak(arithmetic_operations(user_input))
        else:
            print("\nBOT: " + bot_response(user_input) + "\n")
            speak(bot_response(user_input))
