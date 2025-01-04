def chatbot_response(user_input):
    # Convert user input to lowercase and remove extra whitespace for easier matching
    user_input = user_input.lower().strip()
    
    # Define responses based on predefined rules
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How can I help you today?"
    
    elif "your name" in user_input:
        return "I am a simple chatbot. You can call me Bot!"
    
    elif "help" in user_input or "support" in user_input:
        return "I'm here to assist you with your questions. What do you need help with?"
    
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Take care!"
    
    else:
        return "Hmm, I didn't quite catch that. Could you try rephrasing your question?"

# Main function to interact with the chatbot
def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("ME: ")
        
        if user_input.lower().strip() in ["bye", "goodbye"]:
            print("Bot: Goodbye! Take care!")
            break
        
        response = chatbot_response(user_input)
        print(f"Bot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
