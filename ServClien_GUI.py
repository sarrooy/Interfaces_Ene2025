import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ClienteChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente de Chat")

        self.host_label = tk.Label(root, text="Dirección IP del Servidor:")
        self.host_label.pack()

        self.host_entry = tk.Entry(root)
        self.host_entry.pack()
        self.host_entry.insert(0, '127.0.0.1')

        self.connect_button = tk.Button(root, text="Conectar", command=self.conectar_servidor)
        self.connect_button.pack()

        self.message_label = tk.Label(root, text="Mensaje:")
        self.message_label.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Enviar", command=self.enviar_mensaje)
        self.send_button.pack()

        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.log_text.pack()

        self.socket_cliente = None

    def conectar_servidor(self):
        host = self.host_entry.get()
        puerto = 12345
        try:
            self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_cliente.connect((host, puerto))
            self.log_text.insert(tk.END, f"Conectado al servidor en {host}:{puerto}\n")
            self.connect_button.config(state=tk.DISABLED)
            threading.Thread(target=self.recibir_mensajes, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

    def recibir_mensajes(self):
        while True:
            try:
                data = self.socket_cliente.recv(1024)
                if not data:
                    break
                mensaje = data.decode('utf-8')
                self.log_text.insert(tk.END, f"Servidor: {mensaje}\n")
            except (ConnectionResetError, OSError):
                break
        self.log_text.insert(tk.END, "Desconectado del servidor.\n")
        self.connect_button.config(state=tk.NORMAL) #En caso de desconexión, vuelve a habilitar el botón de conectar.

    def enviar_mensaje(self):
        mensaje = self.message_entry.get()
        try:
            self.socket_cliente.sendall(mensaje.encode('utf-8'))
            self.log_text.insert(tk.END, f"Cliente: {mensaje}\n")
        except (ConnectionResetError, AttributeError):
            self.log_text.insert(tk.END, "No se puede enviar el mensaje. No estas conectado a un servidor\n")
        self.message_entry.delete(0, tk.END)

    def cerrar_cliente(self):
        if self.socket_cliente:
            try:
                self.socket_cliente.close()
            except OSError:
                pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteChatGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_cliente)
    root.mainloop()
