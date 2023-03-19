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
        {"role":"system", "content": "You are a helpful assistant"},
        {"role":"user", "content":"Tyler is going through a breakup. identify and validate their emotions. What are some things that I can say to comfort them? And give me rationale to why I should say each response?"},
        {"role":"assistant", "content": "Sure, here are some responses that you can use to identify and validate Tyler's emotions:\n\n1. \"It's totally understandable that you're feeling upset and hurt right now. Breakups can be really hard.\"\n\nRationale: By acknowledging Tyler's feelings as normal and understandable, you're communicating that you're not judging them for how they're feeling. This can create a safe space for them to talk about their emotions and feel heard.\n\n2. \"I can imagine that this is a really difficult time for you. I'm here to listen if you want to talk about it.\"\n\nRationale: By expressing empathy, you're letting Tyler know that you're trying to put yourself in their shoes and understand what they might be going through. This can help Tyler feel less alone and more supported.\n\n3. \"It's okay to feel however you're feeling. You don't have to pretend that everything is fine.\"\n\nRationale: Sometimes people feel pressure to put on a brave face or push down their emotions during a difficult time. By giving Tyler permission to feel whatever emotions they're experiencing, you're communicating that their feelings are valid and important to you.\n\n4. \"Breakups can bring up a lot of complicated emotions - anger, sadness, confusion. It's okay to feel all of those things.\"\n\nRationale: By naming specific emotions that Tyler might be experiencing, you're showing that you understand how multifaceted the grieving process can be. This can help Tyler feel seen and heard, and can normalize the fact that feeling multiple emotions at once is completely normal.\n\n5. \"I want you to know that you're not alone. I'm here for you.\"\n\nRationale: By offering support and being there for Tyler, you're communicating that they don't have to go through this difficult time alone. Knowing that they have someone who cares about them can be incredibly comforting during the grieving process."}]

    my_message = user_input + ". identify and validate their emotions. What are some things that I can say to comfort them? And give me rationale to why I should say each response?";
    messages.append({"role":"user", "content":my_message})
    response = openai.ChatCompletion.create(model = MODEL, messages = messages)

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    user_input = input("Input the context:")
    text = empathic_message(user_input)
    print(text)




