import random

def chatbot():
    responses = {
        'hello': ['Hi there!', 'Hello!', 'Hey!'],
        'how are you': ['I am doing well!', 'Great, thanks!', 'Good!'],
        'what is your name': ['I am a chatbot', 'You can call me Bot', 'I am Bot'],
        'bye': ['Goodbye!', 'See you later!', 'Bye!']
    }
    
    print("Bot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("Bot: Goodbye!")
            break
        
        found_response = False
        for key in responses:
            if key in user_input:
                print(f"Bot: {random.choice(responses[key])}")
                found_response = True
                break
        
        if not found_response:
            print("Bot: I don't understand that. Try asking about my name or saying hello!")

if __name__ == "__main__":
    chatbot()