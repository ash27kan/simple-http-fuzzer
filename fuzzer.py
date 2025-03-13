import requests

target = "http://example.com/?text="

payloads_file = open("payload_test.txt", "r")

def color_status_code(status_code):
    if status_code == 200:
        return "\033[32m"
    elif status_code == 500:
        return "\033[31m"
    elif status_code == 403:
        return "\033[33m"
    else:
        return "\033[36m"

def fuzz():
    for x, y in enumerate(payloads_file, start=1):
        url = target + y.strip()
        response = requests.get(url) # the HTTP method that can be changed
        color = color_status_code(response.status_code)
        print("[{:02}]sent {} ----> {}Status Code: {}{}".format(x, url, color, response.status_code, "\033[0m"))

if __name__ == "__main__":
    fuzz()
