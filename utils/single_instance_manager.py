import socket
import threading

class SingleInstanceManager:
    """
    Handles ensuring that only a single instance of the application is running.
    If another instance is opened, it redirects to the running instance.
    """
    def __init__(self, port=65432, address="127.0.0.1"):
        """
        Initializes the SingleInstanceManager with the given port and address.
        
        :param port: The port to use for the socket server.
        :param address: The address to use for the socket server.
        """
        self.port = port
        self.address = address
        self.server_thread = None

    def is_instance_running(self):
        """
        Checks if another instance of the application is already running.
        
        :return: True if another instance is running, False otherwise.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.address, self.port))
                client_socket.sendall(b"Bring to front")
                
                return True
            
        except ConnectionRefusedError:
            return False

    def start_server(self, on_bring_to_front_callback):
        """
        Starts a socket server to listen for messages from new instances.

        :param on_bring_to_front_callback: A function to call when a "Bring to front" message is received.
        """
        def server_loop():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server_socket.bind((self.address, self.port))
                server_socket.listen()

                while True:
                    conn, _ = server_socket.accept()

                    with conn:
                        data = conn.recv(1024)

                        if data == b"Bring to front" and callable(on_bring_to_front_callback):
                            on_bring_to_front_callback()

        self.server_thread = threading.Thread(target=server_loop, daemon=True)
        self.server_thread.start()
