import openai

#store API key
openai.api_key = "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"

api_key = openai.api_key

#define the first function to interact with chatbot
def travel_assistance_chatbot(user_input):
    #create a list of messages
    conversation=(
        {"role":"system","content":"You are a travel assistance."},
        {"role":"user","content":user_input}
    )
    #generate the response
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=conversation)
    #extract the text
    print(response)
    chatbot_reply = response['choices'][0]['message']['content']
    
    return chatbot_reply
while True:
    user_input = input("You:")
    if(user_input.lower() == 'exit'):
        break
    chatbot_response = travel_assistance_chatbot(user_input)
    print("Chatbot:", chatbot_response)
