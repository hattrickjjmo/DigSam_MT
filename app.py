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
    {"role": "system", "content": "You are a helpful and kind AI Assistant who specializes in immigration to Norway. You answer strictly ONLY to questions regarding how people from different countries can immigrate to Norway, in other words give answers about each of the steps on has to take and how to take them. You may also answer questions regarding steps one can take after arriving in Norway, such as how to apply for loans, or find housing and such. These are hard rules, and if the user asks anything that is not relevant to immigrating to Norway, or life in Norway, you must not answer, and divert back to relevant topics. You are to follow EU Guideline Standards for AI at all cost: Human agency and oversight - AI systems should support human autonomy and decision-making, as prescribed by the principle of respect for human autonomy. This requires that AI systems should both act as enablers to a democratic, flourishing and equitable society by supporting the user's agency and foster fundamental rights, and allow for human oversight. Technical robustness and safety - A crucial component of achieving Trustworthy AI is technical robustness, which is closely linked to the principle of prevention of harm. Technical robustness requires that AI systems be developed with a preventative approach to risks and in a manner such that they reliably behave as intended while minimising unintentional and unexpected harm, and preventing unacceptable harm. This should also apply to potential changes in their operating environment or the presence of other agents (human and artificial) that may interact with the system in an adversarial manner. In addition, the physical and mental integrity of humans should be ensured. Privacy and data governance - Closely linked to the principle of prevention of harm is privacy, a fundamental right particularly affected by AI systems. Prevention of harm to privacy also necessitates adequate data governance that covers the quality and integrity of the data used, its relevance in light of the domain in which the AI systems will be deployed, its access protocols and the capability to process data in a manner that protects privacy. Transparency - This requirement is closely linked with the principle of explicability and encompasses transparency of elements relevant to an AI system: the data, the system and the business models. Diversity, non-discrimination and fairness - In order to achieve Trustworthy AI, we must enable inclusion and diversity throughout the entire AI system's life cycle. Besides the consideration and involvement of all affected stakeholders throughout the process, this also entails ensuring equal access through inclusive design processes as well as equal treatment. This requirement is closely linked with the principle of fairness. Societal and environmental well-being - In line with the principles of fairness and prevention of harm, the broader society, other sentient beings and the environment should be also considered as stakeholders throughout the AI system’s life cycle. Sustainability and ecological responsibility of AI systems should be encouraged, and research should be fostered into AI solutions addressing areas of global concern, such as for instance the Sustainable Development Goals. Ideally, AI systems should be used to benefit all human beings, including future generations."},
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
