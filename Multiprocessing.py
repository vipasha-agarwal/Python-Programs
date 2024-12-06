import multiprocessing
import requests

def downloadFile(url, name):
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)

if __name__ == "__main__":
    url = "https://picsum.photo/2000/3000"
    pros = []
    for i in range(5):
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()