import psutil

def get_opened_ports():
    # Get a list of TCP connections
    tcp_connections = psutil.net_connections(kind='tcp')

    # Filter the connections that are listening
    listening_connections = [conn for conn in tcp_connections if conn.status == psutil.CONN_LISTEN]

    # Get a list of ports that are open
    opened_ports = [conn.laddr.port for conn in listening_connections]


    return opened_ports