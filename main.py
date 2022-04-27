import random
from time import sleep
from multiprocessing import Pool


def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

if __name__ == "__main__":
    urls = ["a.com", "b.com", "c.com", "d.com"]

    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)

output = []
for url in urls:
    result = scrape(url)
    output.append(result)