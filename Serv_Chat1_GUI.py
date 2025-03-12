import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ServidorChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Servidor de Chat Mejorado")

        # Configuración de la GUI
        self.host_label = tk.Label(root, text="Dirección IP:")
        self.host_label.pack()

        self.host_entry = tk.Entry(root)
        self.host_entry.pack()
        self.host_entry.insert(0, '127.0.0.1')

        self.listen_button = tk.Button(root, text="Escuchar", command=self.iniciar_servidor)
        self.listen_button.pack()

        self.close_button = tk.Button(root, text="Cerrar Servidor", command=self.cerrar_servidor, state=tk.DISABLED)
        self.close_button.pack()

        self.message_label = tk.Label(root, text="Mensaje:")
        self.message_label.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Enviar", command=self.enviar_mensaje)
        self.send_button.pack()

        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.log_text.pack()

        self.client_listbox = tk.Listbox(root)
        self.client_listbox.pack()

        # Configuración del servidor
        self.socket_servidor = None
        self.clientes = []

    def iniciar_servidor(self):
        host = self.host_entry.get()
        puerto = 12345
        try:
            self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_servidor.bind((host, puerto))
            self.socket_servidor.listen()
            self.log_text.insert(tk.END, f"Servidor escuchando en {host}:{puerto}\n")
            self.listen_button.config(state=tk.DISABLED)
            self.close_button.config(state=tk.NORMAL)
            thread = threading.Thread(target=self.aceptar_conexiones)
            thread.daemon = True
            thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el servidor: {e}")

    def aceptar_conexiones(self):
        while True:
            try:
                conn, addr = self.socket_servidor.accept()
                self.clientes.append((conn, addr))
                self.actualizar_lista_clientes()
                self.log_text.insert(tk.END, f"Conexión establecida desde {addr}\n")

                thread = threading.Thread(target=self.manejar_cliente, args=(conn,))
                thread.daemon = True
                thread.start()
            except OSError:
                break

    def manejar_cliente(self, conn):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                mensaje = data.decode('utf-8')
                self.log_text.insert(tk.END, f"Cliente: {mensaje}\n")
            except (ConnectionResetError, OSError):
                break
        self.remover_cliente(conn)

    def remover_cliente(self, conn):
        for c, addr in self.clientes:
            if c == conn:
                self.clientes.remove((c, addr))
                self.actualizar_lista_clientes()
                self.log_text.insert(tk.END, f"Conexión cerrada con {addr}\n")
                break
        conn.close()

    def enviar_mensaje(self):
        mensaje = self.message_entry.get()
        self.log_text.insert(tk.END, f"Servidor: {mensaje}\n")
        for cliente, addr in self.clientes:
            try:
                cliente.sendall(mensaje.encode('utf-8'))
            except (ConnectionResetError, OSError):
                self.remover_cliente(cliente)
        self.message_entry.delete(0, tk.END)

    def actualizar_lista_clientes(self):
        self.client_listbox.delete(0, tk.END)
        for _, addr in self.clientes:
            self.client_listbox.insert(tk.END, f"{addr[0]}:{addr[1]}")

    def cerrar_servidor(self):
        if self.socket_servidor:
            for cliente, _ in self.clientes:
                try:
                    cliente.close()
                except OSError:
                    pass
            self.socket_servidor.close()
            self.log_text.insert(tk.END, "Servidor cerrado.\n")
            self.listen_button.config(state=tk.NORMAL)
            self.close_button.config(state=tk.DISABLED)
            self.clientes.clear()
            self.actualizar_lista_clientes()

if __name__ == "__main__":
    root = tk.Tk()
    app = ServidorChatGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_servidor)
    root.mainloop()