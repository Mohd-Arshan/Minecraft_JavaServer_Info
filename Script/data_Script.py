import sys
from mcstatus import JavaServer
from mcstatus.server import JavaServer

def get_minecraft_server_data(server_address):
    try:
        # Remove any protocol prefix like sftp://
        if server_address.startswith("sftp://"):
            server_address = server_address.replace("sftp://", "")

        # Create a MinecraftServer object
        server = JavaServer.lookup(server_address)

        # Fetch the server status
        status = server.status()

        # Display server information
        print(f"Server Address: {server_address}")
        print(f"Version: {status.version.name}")
        print(f"Latency: {status.latency} ms")
        print(f"Players Online: {status.players.online}/{status.players.max}")

        if status.players.sample:
            print("Online Players:")
            for player in status.players.sample:
                print(f"- {player.name}")

    except Exception as e:
        print(f"Failed to fetch data from the server: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <server_address>")
        sys.exit(1)

    server_address = sys.argv[1]
    get_minecraft_server_data(server_address)
