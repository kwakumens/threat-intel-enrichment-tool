import ipaddress

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private

def classify_severity(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    return "Low"
