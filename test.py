import re
import json
import time
import hashlib 

def findFirstMatchInText(filename, pattern):
    with open(filename, 'r') as f:
        content = f.read()
    match = re.search(pattern, content)
    return match.group(0) if match else None

def findFirstMatchInJSON(filename, search_str):
    with open(filename, 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                if search_str in json.dumps(data):
                    return data
            except json.JSONDecodeError:
                continue
    return None

def processHashes(x):
    d = {i: hashlib.sha256(str(i).encode()).hexdigest() for i in range(1, x)}
    h_str = "".join(d.values())
    b = list(d.values())[-1]

    with open('hashes.txt', 'w') as f:
        f.write(h_str)

    with open('hashes.json', 'w') as f:
        json.dump(d, f)

    a = 'hashes.txt'
    t1 = time.time()
    findFirstMatchInText(a, b)
    t2 = time.time()
    findFirstMatchInJSON('hashes.json', b)
    t3 = time.time()

    return t2 - t1, t3 - t2

i = 12
x = 256

while True:
    x *= 2
    print(x, processHashes(x))
    if i <= 0: break
    i -= 1
