import threading
import time
from types import SimpleNamespace

# This makes data thread local, unlike if SimpleNamespace or any other similar object was used
local_data = threading.local()
# local_data = SimpleNamespace(value=None)

def worker(name):
    local_data.value = name
    time.sleep(1)
    print(f"{threading.current_thread().name}: {local_data.value}")

threads = [
    threading.Thread(target=worker, args=("A",)),
    threading.Thread(target=worker, args=("B",)),
]

for t in threads:
    t.start()

for t in threads:
    t.join()