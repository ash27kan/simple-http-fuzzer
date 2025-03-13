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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
