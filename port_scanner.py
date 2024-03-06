import socket
import threading
import logging

# Configure logging
logging.basicConfig(
    filename="port_scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# function to check if the port is open
def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            logging.info(f"Port {port} is open")
            print(f"Port {port} is open")
        else:
            logging.info(f"Port {port} is closed")
            print(f"Port {port} is closed")
        sock.close()
    except Exception as e:
        logging.error(f"Error checking port {port}: {e}")
        print(f"Error checking port {port}: {e}")


# func to perform port scanning
def port_scan(ip, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=check_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    target_ip = "ghanacodeclub.org"
    target_ports = range(1, 25)
    try:
        port_scan(target_ip, target_ports)
    except KeyboardInterrupt:
        print("\nPort scan interrupted by user.")
        logging.info("Port scan interrupted by user.")
    except Exception as e:
        print(f"An error occurred during port scanning: {e}")
        logging.error(f"An error occurred during port scanning: {e}")
