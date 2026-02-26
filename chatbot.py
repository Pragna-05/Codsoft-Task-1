def chatbot():
    print("🤖 SmartBot Activated!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["good morning", "good afternoon", "good evening"]:
            print("Chatbot: Hello! Hope you're having a wonderful day!")

        elif "what can you do" in user_input:
            print("Chatbot: I can answer basic questions and chat with you.")

        elif "tell me a joke" in user_input:
            print("Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!")

        elif "motivate me" in user_input:
            print("Chatbot: Believe in yourself! You are capable of amazing things.")

        elif "python" in user_input:
            print("Chatbot: Python is a powerful and beginner-friendly programming language.")

        elif "ai" in user_input:
            print("Chatbot: Artificial Intelligence enables machines to think and learn like humans.")

        elif "your purpose" in user_input:
            print("Chatbot: My purpose is to assist and interact with you.")

        elif "hobby" in user_input:
            print("Chatbot: I enjoy answering questions and learning from conversations!")

        elif "favorite color" in user_input:
            print("Chatbot: I like blue because it represents intelligence and calmness.")

        elif "exam tips" in user_input:
            print("Chatbot: Revise important topics, practice questions, and stay confident.")

        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day ahead!")
            break

        else:
            print("Chatbot: I'm not sure about that. Can you ask something else?")


# Run the chatbot
chatbot()
