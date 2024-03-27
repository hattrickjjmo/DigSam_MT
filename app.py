from openai import OpenAI
import os
import gradio as gr

client = OpenAI(
    api_key=os.environ.get("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")
)

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

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

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot", description="Ask anything you want", theme="compact").launch(share=True)


