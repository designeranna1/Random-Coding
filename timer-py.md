![Timer.py](https://github.com/designeranna1/Random-Coding/blob/main/Screenshot%202020-11-23%20at%2010.14.49%20AM.jpg)

## Requirements
Have Python 3.7 or newer installed. You can check the version by typing `python3 --version` in your command line. You can [download the latest Python version from here](https://www.python.org/downloads/).

Below is the code, that you can copy easily.

```py
from tqdm import tqdm, trange
import time
i = input("Set the timer range in seconds: ")
print("Timer started :" + i + "s")
for i in tqdm(range(int(i)),colour='magenta'):
    time.sleep(1.0)

print("Time's up")
```
