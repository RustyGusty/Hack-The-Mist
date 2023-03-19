
import openai

openai.api_key = "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"

MODEL = "gpt-3.5-turbo"

def empathic_message(user_input: str) -> str:
    """
    This function returns many options of empathic message according to the user's
    input
    """
    # messages = [{"role": "system", "content": "Assume you are a helpful mental coach, reply following message in empathetic way:"},]
    # messages.append({"role": "user", "content": user_input})
    # chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    # text = str(chat.choices[0].message.content)
    #
    # return text
    messages = [
        {"role":"system", "content": "You are a coach that provide advice"},
        {"role":"user", "content":"People close to me are going through a hard time. identify and validate their emotions. What are some things that I can say to comfort them? And give me rationale to why I should say each response?"},
        {"role":"assistant", "content": "Sure, here are some responses that you can use to identify and validate their emotions:\n\n1. " } ]



    my_message = user_input + ". identify and validate their emotions. What are some things that I can say to comfort them? And give me rationale to why I should say each response?";
    messages.append({"role":"user", "content":my_message})
    response = openai.ChatCompletion.create(model = MODEL, messages = messages)

    return response['choices'][0]['message']['content']

user_input = input("Input the context:")
text = empathic_message(user_input)
print(text)




