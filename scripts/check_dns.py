import socket
from halo import Halo

def check_dns():
    domains = ['google.com', 'github.com']  # List of domains to test
    dns_results = []

    spinner = Halo(text='Testing DNS resolution', spinner='dots')
    spinner.start()

    for domain in domains:
        try:
            ip_addresses = socket.gethostbyname_ex(domain)[-1]  # Resolving DNS
            dns_results.append({'domain': domain, 'resolved_ip': ip_addresses})
        except socket.gaierror as e:
            dns_results.append({'domain': domain, 'resolved_ip': 'Failed to resolve'})

    spinner.stop()
    return dns_results