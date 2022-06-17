import socket


def is_running(site):
    """This function attempts to connect to the given server using a socket.
        Returns: Whether or not it was able to connect to the server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except (socket.gaierror, OSError) as err:
        print(err)
        print(err.args)
        return False
