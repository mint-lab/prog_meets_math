import tkinter as tk
from fnmatch import fnmatch

class ChatBot:
    def __init__(self):
        self.talk_table = [
            ('*hello*',         'Hello'),
            ('*good morning*',  'Hello'),
            ('*what*you*name*', 'My name is OSS Chatbot.'),
        ]
        self.talk_unknown = "I don't understand your words."

    def reply(self, msg):
        for pattern, response in self.talk_table:
            if fnmatch(msg, pattern):
                return response
        return self.talk_unknown

class SimpleChatBotGUI:
    def __init__(self, chatbot, master):
        self.chatbot = chatbot
        self.master = master
        self.master.title('A Very Simple Chatbot')
        self.label = tk.Label(master, text='Chat Dialog')
        self.label.pack()
        self.text_dialog = tk.Text(master)
        self.text_dialog.pack()
        self.label = tk.Label(master, text='Your Message:')
        self.label.pack()
        self.entry_msg = tk.Entry(master)
        self.entry_msg.pack()
        self.button_send = tk.Button(master, text='Send Your Message', command=self.handle_button)
        self.button_send.pack()

    def handle_button(self):
        msg = self.entry_msg.get()
        self.text_dialog.insert('end', 'You: ' + msg + '\n')
        self.text_dialog.insert('end', 'Bot: ' + self.chatbot.reply(msg) + '\n')
        self.entry_msg.delete(0, tk.END) # Clear 'entry_msg' after reply

if __name__ == '__main__':
    chatbot = ChatBot()
    root = tk.Tk()
    app = SimpleChatBotGUI(chatbot, root)
    root.mainloop()