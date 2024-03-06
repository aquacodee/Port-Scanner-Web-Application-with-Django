import socket
from django.shortcuts import render
from .models import ScanResult
from .utils import detect_service, check_vulnerability


def home(request):
    if request.method == "POST":
        ip_address = request.POST.get("ip_address")
        start_port = int(request.POST.get("start_port"))
        end_port = int(request.POST.get("end_port"))

        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    service = detect_service(port)
                    vulnerability = check_vulnerability(
                        port, ip_address
                    )  # Pass IP address to check_vulnerability
                    ScanResult.objects.create(
                        ip_address=ip_address,
                        port=port,
                        is_open=True,
                        service=service,
                        vulnerability=vulnerability,
                    )
                sock.close()
            except Exception as e:
                print(f"Error checking port {port}: {e}")

        results = ScanResult.objects.filter(ip_address=ip_address)
        return render(request, "home.html", {"results": results})
    return render(request, "home.html")
