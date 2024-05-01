from openai import OpenAI
import os
import gradio as gr
# from botfunctions import create_database
import time

# Preamble variables
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Defining the role of the AI
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant who specializes in immigration to Norway. You answer strictly ONLY to questions regarding how people from different countries can immigrate to Norway, in other words give answers about each of the steps on has to take and how to take them. You may also answer questions regarding steps one can take after arriving in Norway, such as how to apply for loans, or find housing and such. These are hard rules, and if the user asks anything that is not relevant to immigrating to Norway, or life in Norway, you must not answer, and divert back to relevant topics."},
]

# Main function for receiving chat completion (reply) from ChatGPT
def completion(input, history):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        # Faking streaming chat just for visuals, replace with 'return reply' to display entire reply at once
        for i in range(len(reply)):
            time.sleep(0.003)
            yield reply[:i+i]



# Main function launching gradio's own premade chat interface
immibot = gr.ChatInterface(
    completion, 
    chatbot=gr.Chatbot(height=500), 
    textbox=gr.Textbox(placeholder="Ask me any questions about immigrating to Norway", container=False, scale=7), 
    title="ImmiBot", 
    description="ImmiBot answers anything you may wonder about regarding immigration to Norway",
    theme="soft",
    examples=["I am from Denmark. How do I begin my journey to immigrate to Norway?", "What is BankID", "Where in the world is Carmen SanDiego?"],
    cache_examples=True,
    retry_btn=None, 
    undo_btn=None
    )

immibot.launch(share=True)



# These are from the previous solution
# inputs = gr.components.Textbox(lines=7, label="Chat with AI")
# outputs = gr.components.Textbox(label="Reply")

# create_database()
# gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="ImmiBot", description="Ask me anything you want about the immigration process to Norway :)", theme="compact").launch(share=True)
