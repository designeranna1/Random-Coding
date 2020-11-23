from tqdm import tqdm, trange
import time
i = input("Set the timer range in seconds: ")
print("Timer started :" + i + "s")
for i in tqdm(range(int(i)),colour='magenta'):
    time.sleep(1.0)

print("Time's up")