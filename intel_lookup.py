MOCK_DB = {
    "185.220.101.1": {"risk_score": 92},
    "45.33.32.156": {"risk_score": 78},
    "8.8.8.8": {"risk_score": 5},
}

def lookup_ip(ip):
    return MOCK_DB.get(ip, {"risk_score": 20})
