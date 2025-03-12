import socket

def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Conectado al servidor en {HOST}:{PORT}")

            while True:
                message = input("Ingresa un mensaje (o 'quit' para terminar): ")
                s.sendall(message.encode('utf-8'))

                if message.lower() == 'quit': # Verifica si se envío 'quit'
                    break # Sale del bucle while si se envió 'quit'

                data = s.recv(1024)
                response = data.decode('utf-8')
                print(f"Respuesta del servidor: {response}")


        except ConnectionRefusedError:
            print("Error: No se pudo conectar al servidor.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()