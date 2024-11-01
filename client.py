import threading
import socket
import argparse
import sys
import tkinter as tk
from tkinter import messagebox

class Send(threading.Thread):
    def __init__(self, sock, name, host, port):
        super().__init__()
        self.sock = sock
        self.name = name
        self.host = host
        self.port = port

    def run(self):
        while True:
            message = input(f'{self.name}: ')
            if message == "QUIT":
                self.sock.sendto(f'{self.name} telah meninggalkan chat.'.encode('ascii'), (self.host, self.port))
                print('\nQuitting...')
                self.sock.close()
                sys.exit(0)
            else:
                self.sock.sendto(f'{self.name}: {message}'.encode('ascii'), (self.host, self.port))

class Receive(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        self.messages = None

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode('ascii')
                print(f'\r{message}\n', end='')
                if self.messages:
                    self.messages.insert(tk.END, message)
            except OSError:
                break

class Client:
    def __init__(self, host, server_port, client_port):
        self.host = host
        self.server_port = server_port
        self.client_port = client_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', client_port))
        self.name = None
        self.messages = None

    def login(self, username, password, login_window):
        self.name = username
        self.sock.sendto(f'LOGIN {username} {password}'.encode('ascii'), (self.host, self.server_port))
        response, _ = self.sock.recvfrom(1024)
        response_message = response.decode('ascii')

        if response_message == 'Username sudah dipakai. Gunakan yang lain.':
            messagebox.showerror("Login gagal", response_message)
        elif response_message == 'Password salah. Silahkan coba lagi.':
            messagebox.showerror("Login gagal", response_message)
        else:
            messagebox.showinfo("Login berhasil", response_message)
            login_window.destroy()
            self.start_chat()

    def start_chat(self):
        print('Getting ready to send and receive messages...')
        
        send = Send(self.sock, self.name, self.host, self.server_port)
        receive = Receive(self.sock)
        send.start()
        receive.start()
        
        self.sock.sendto(f'{self.name} sudah bergabung.'.encode('ascii'), (self.host, self.server_port))
        print("\rReady! Leave the chatroom anytime by typing 'QUIT'\n")
        print(f'{self.name}: ', end='')
        
        self.create_chat_window(receive)

    def send(self, textInput):
        message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, f'{self.name}: {message}')
        if message == "QUIT":
            self.sock.sendto(f'{self.name} has left the chat.'.encode('ascii'), (self.host, self.server_port))
            print('\nQuitting...')
            self.sock.close()
            sys.exit(0)
        else:
            self.sock.sendto(f'{self.name}: {message}'.encode('ascii'), (self.host, self.server_port))

    def create_chat_window(self, receive):
        window = tk.Tk()
        window.title("GAS Chatroom")

        # Frame for messages and scrollbar
        fromMessage = tk.Frame(master=window)
        scrollBar = tk.Scrollbar(master=fromMessage)
        messages = tk.Listbox(master=fromMessage, yscrollcommand=scrollBar.set, font=("Arial", 11))
        scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Store message listbox for reference
        self.messages = messages
        receive.messages = messages

        fromMessage.grid(row=0, column=0, sticky="nsew")

        # Frame for text input and send button
        fromEntry = tk.Frame(master=window)
        textInput = tk.Entry(master=fromEntry)
        textInput.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        textInput.bind("<Return>", lambda x: self.send(textInput))
        textInput.insert(0, "Write your message here.")

        btnSend = tk.Button(master=fromEntry, text='Send', command=lambda: self.send(textInput))
        btnSend.pack(side=tk.RIGHT, padx=5)

        fromEntry.grid(row=1, column=0, padx=10, sticky="ew")

        # Configure window layout
        window.rowconfigure(0, minsize=500, weight=1)
        window.rowconfigure(1, minsize=50)
        window.columnconfigure(0, minsize=500, weight=1)

        window.mainloop()

def main(host, server_port, client_port):
    client = Client(host, server_port, client_port)
    
    # Login window
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(login_window, text="Login", command=lambda: client.login(username_entry.get(), password_entry.get(), login_window))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    login_window.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="UDP Chatroom Client")
    parser.add_argument('host', help='The host IP address')
    parser.add_argument('server_port', type=int, help='Server port number')
    parser.add_argument('client_port', type=int, help='Client port number')
    args = parser.parse_args()
    main(args.host, args.server_port, args.client_port)
