import threading
import time

servers = ["Server 1", "Server 2", "Server 3"]
index = 0

def process_request(server, request):
    print(f"Request {request} diproses oleh {server}")
    time.sleep(1)

def load_balancer(request):
    global index

    server = servers[index]

    t = threading.Thread(
        target=process_request,
        args=(server, request)
    )

    t.start()

    index = (index + 1) % len(servers)

for i in range(1, 11):
    load_balancer(i)