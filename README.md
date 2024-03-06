# Port Scanner Web Application with Django

Port Scanner Web Application with Django is a web-based tool designed to scan for open ports on a specified IP address range. This application allows users to input an IP address, start port, and end port, and then performs port scanning to identify open ports. Additionally, the application detects services running on open ports and checks for potential vulnerabilities using Nmap. The scan results are displayed in a user-friendly interface, providing information about the port number, associated service, and vulnerability status.

## Features

- Scan for open ports within a specified IP address range.
- Identify services running on open ports.
- Check for potential vulnerabilities using Nmap.
- User-friendly interface to view scan results.

## Requirements

- Python 3.x
- Django
- Nmap

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/port-scanner-web-app.git
cd port-scanner-web-app
```

2. Install Dependencies:

```
pip install -r requirements.txt
```
3.  Install Nmap. Follow the instructions provided in the Nmap website for your specific operating system.

## Usage
### Run the Django development server:
```
python manage.py runserver
```
1.Open a web browser and navigate to `http://127.0.0.1:8000/`.

2. Input the IP address, start port, and end port in the form provided.

3. Click on the "Scan Ports" button to initiate the port scanning process.

4. View the scan results displayed on the web page.


## Cotributing
### Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.










