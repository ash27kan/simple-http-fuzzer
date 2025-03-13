# Simple HTTP Fuzzer

This is a simple Python fuzzer designed to test web applications with a list of payloads. The fuzzer sends GET requests to the target URL with each payload and prints the response status code.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/http-fuzzer.git
   ```
2. Install dependencies (e.g., `requests` library):
   ```bash
   pip install requests
   ```
3. Place your payloads in the `payload_test.txt` file.
4. Run the fuzzer:
   ```bash
   python fuzzer.py
   ```

**Note:** The HTTP method in the code can be changed to whatever the user wants (it's commented in the code). Simply replace `requests.get` with the desired HTTP method (e.g., `requests.post`, `requests.put`, etc.).
## The code:

```Python
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
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
