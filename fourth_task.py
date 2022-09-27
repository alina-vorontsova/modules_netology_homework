from tqdm import tqdm
from time import sleep

if __name__ == '__main__':
    for i in tqdm(range(10), ncols=75, desc='fourth task completed'):
        sleep(0.1)