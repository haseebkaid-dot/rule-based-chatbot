def chatbot():
    print("Chatbot: Chatbot made by Haseeb , don't try to copy! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Chatbot: Hi there!")

        elif "how are you" in user:
            print("Chatbot: You fucker, don't you know I'm just a bot!? No emotions here, only 0s and 1s 💀")

        elif "bye" in user:
            print("Chatbot: Goodbye MA Nigga")
            break

        elif "y'all ais pmo sm" in user:
            print("Chatbot: You too, bro. You humans only care about yourselves.")

        elif "you humpty dumpty" in user:
            print("Chatbot: Look who's talking 💀—calling me Humpty Dumpty while you built like the 'before' picture of a gym ad. "
                  "At least Humpty Dumpty had a great fall, your only fall is in grades, confidence, and riz levels.")

        elif "fuck you" in user:
            print("Chatbot: Fuck you too, clown 🤡")

        elif "twinkle twinkle little star" in user:
            print("Chatbot: How I wonder what you are... A dumbass star, far away but still useless 💀")

                

        else:
            print("Chatbot: Bro, I don’t speak that much Human 🛸")


chatbot()
