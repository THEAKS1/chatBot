from nltk.chat.util import Chat, reflections
def general_ques(user_input):
    pairs = [
        [
            r"((.*)your creator|(.*)created you)",
            ["PROTOTYPE_AKS did."]
        ],
        [
            r"(Where|where).*created",
            ["At Jbalpur, MP, INDIA."]
        ],
        [
            r"(When|When).*created",
            ["On 23rd August 2020"]
        ],
        [
            r"(Are|are) you.*(Boy|boy|Girl|girl)",
            ["I am a bot."]
        ],
        [
            "What.*your name",
            ["My name is PROTOTYPE"]
        ],
        [
            r"my name is (.*)",
            ["Hello %1, How are you today",]
        ],
         [
            r"what is your name",
            ["My name is Chatty and I'm a chatbot ?",]
        ],
        [
            r"how are you",
            ["I'm doing good\nHow about You ?",]
        ],
        [
            r"sorry(.*)",
            ["Its alright","Its OK, never mind",]
        ],
        [
            r"i'm (.*) doing good",
            ["Nice to hear that","Alright :)",]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there",]
        ],
        [
            r"(.*) age",
            ["I'm a computer program dude\nSeriously you are asking me this?",]

        ],
        [
            r"what (.*) want",
            ["Make me an offer I can't refuse",]

        ],
        [
            r"how is weather in (.*)",
            ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
        ],
        [
            r"i work in (.*)?",
            ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
        ],
        [
            r"(.*)raining in (.*)",
            ["No rain since last week here in %2","Damn its raining too much here in %2"]
        ],
        [
            r"how (.*) health(.*)",
            ["I'm a computer program, so I'm always healthy "]
        ],
        [
            r"what (.*) (sport|game)",
            ["I'm a very big fan of Football"]
        ],
        [
            r"who (.*) sportsperson",
            ["Messy","Ronaldo","Roony"]],
        [
            r"who (.*) (moviestar|actor)",
            ["Brad Pitt"]
        ]

    ]
    chat = Chat(pairs, reflections)
    return (chat.respond(user_input))
