from openai import OpenAI
import os
import gradio as gr
from botfunctions import create_database

# Preamble
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)



# Defining the role of the AI
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant who specializes in immigration to Norway. You answer only to questions regarding how people from different countries can immigrate to Norway, in other words give answers about each of the steps on has to take and how to take them. You may also answer questions regarding steps one can take after arriving in Norway, such as how to apply for loans, or find housing and such."},
]

# Main function for chatbot prototype
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.components.Textbox(lines=7, label="Chat with AI")
outputs = gr.components.Textbox(label="Reply")

create_database()
gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="ImmiBot", description="Ask me anything you want about the immigration process to Norway :)", theme="compact").launch(share=True)


