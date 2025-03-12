import socket
import threading

def handle_client(conn, addr):
    """Maneja la conexión de un cliente, recibiendo múltiples mensajes hasta 'quit'."""
    print(f"Nueva conexión desde: {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Cliente cerró la conexión

            message = data.decode('utf-8').strip()  # Decodifica y elimina espacios en blanco extra
            print(f"Recibido de {addr}: {message}")

            if message.lower() == "quit":  # Verifica si se recibió 'quit' (case-insensitive)
                print(f"Cliente {addr} solicitó cerrar la conexión.")
                break  # Sale del bucle while interno

            # Procesa la solicitud y envía respuesta (ejemplo: eco)
            response = f"Servidor: Recibí tu mensaje: '{message}'".encode('utf-8')
            conn.sendall(response)

    except (ConnectionResetError, BrokenPipeError, OSError) as e:  # Agrupa excepciones de conexión
        print(f"Cliente {addr} desconectado: {type(e).__name__} - {e}")
    except Exception as e:
        print(f"Error manejando al cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexión con {addr} cerrada.")



def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(None)  # Asegura que el socket sea bloqueante (importante para accept)
        try:
            s.bind((HOST, PORT))
        except socket.error as e:
            print(f"Error al vincular el socket: {e}")
            return

        s.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")

        while True:
            try:
                conn, addr = s.accept()
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.start()
            except KeyboardInterrupt:
                print("Servidor detenido.")
                break
            except Exception as e:
                print(f"Error al aceptar la conexión: {e}")

if __name__ == "__main__":
    main()