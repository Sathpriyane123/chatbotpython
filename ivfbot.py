import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create and train the ChatBot
chatbot = ChatBot('IVFChatBot')
trainer = ListTrainer(chatbot)

# Add domain-specific training data
trainer.train([
    "What is IVF?",
    "IVF stands for In-Vitro Fertilization. It is a process by which an egg is fertilized by sperm outside the body.",
    "What are the success rates for IVF?",
    "Success rates for IVF vary depending on several factors, including age, health, and specific conditions. It is best to consult your specialist for personalized information.",
    "What medications are used in IVF?",
    "Common medications include hormone injections to stimulate egg production, such as FSH and LH. Your doctor will provide specific details based on your treatment plan.",
    "How often should I visit the clinic during IVF?",
    "You will need to visit the clinic regularly for monitoring and treatment. The frequency will depend on your specific treatment plan."
])

# Create the GUI
class IVFChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IVF Chatbot")

        self.chat_log = tk.Text(root, bg="white", fg="black", state="disabled")
        self.chat_log.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, bg="lightgrey")
        self.entry.pack(padx=10, pady=10, fill="x")

        self.entry.bind("<Return>", self.get_response)

    def get_response(self, event):
        user_input = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if user_input:
            self.append_chat("You: " + user_input)
            response = chatbot.get_response(user_input)
            self.append_chat("Bot: " + str(response))

    def append_chat(self, text):
        self.chat_log.config(state="normal")
        self.chat_log.insert(tk.END, text + "\n")
        self.chat_log.config(state="disabled")
        self.chat_log.yview(tk.END)

# Run the application
root = tk.Tk()
app = IVFChatbotApp(root)
root.mainloop()
