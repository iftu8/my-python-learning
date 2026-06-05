import re
from collections import Counter
import json

class AdvancedLogAnalyzer:
    def __init__(self):
        # Regex patterns to extract IP, Timestamp, Request Method, Status Code, and Message
        self.log_pattern = re.compile(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*?)\] "(?P<method>\w+) (?P<url>\S+) .*?" (?P<status>\d{3}) (?P<size>\d+|-)(?: "(?P<message>.*?)")?'
        )
        self.ips = []
        self.failed_logins = 0
        self.status_codes = []

    def parse_log_line(self, line):
        """Extracts deep metadata from a single production log string."""
        match = self.log_pattern.match(line)
        if match:
            data = match.groupdict()
            self.ips.append(data['ip'])
            self.status_codes.append(data['status'])
            
            # Security Threat Detection Logic
            if data['status'] == '401' or 'unauthorized' in (data['message'] or '').lower():
                self.failed_logins += 1
            return data
        return None

    def generate_security_report(self, sample_logs):
        """Processes massive log arrays and mathematically computes server status."""
        parsed_data = [self.parse_log_line(line) for line in sample_logs if self.parse_log_line(line)]
        
        if not parsed_data:
            return "❌ Critical Error: Data structure mismatch or corrupted log syntax."

        # Analytical Aggregations using Counter
        ip_counts = Counter(self.ips)
        status_counts = Counter(self.status_codes)
        
        # Suspected Brute-Force Attackers (IPs making more than 2 requests in this sample)
        threat_ips = {ip: count for ip, count in ip_counts.items() if count > 2}

        # Compiling final high-level telemetry report
        report = {
            "Total_Requests_Analyzed": len(parsed_data),
            "Security_Alerts": {
                "Failed_Login_Attempts": self.failed_logins,
                "Suspected_Brute_Force_Attackers": threat_ips
            },
            "Traffic_Analysis": {
                "Top_Active_IP": ip_counts.most_common(1)[0] if ip_counts else None,
                "HTTP_Status_Distribution": dict(status_counts)
            }
        }
        return json.dumps(report, indent=4)

# --- Complex Enterprise Mock Data (Simulation) ---
production_logs = [
    '192.168.1.105 - - [05/Jun/2026:22:15:00 +0600] "POST /login HTTP/1.1" 401 532 "Unauthorized Login Attempt"',
    '192.168.1.105 - - [05/Jun/2026:22:15:05 +0600] "POST /login HTTP/1.1" 401 532 "Unauthorized Login Attempt"',
    '192.168.1.105 - - [05/Jun/2026:22:15:10 +0600] "POST /login HTTP/1.1" 200 2450 "Login Success"',
    '10.0.0.42 - - [05/Jun/2026:22:16:22 +0600] "GET /index.html HTTP/1.1" 200 4120 ""',
    '172.16.254.1 - - [05/Jun/2026:22:17:45 +0600] "GET /api/data HTTP/1.1" 500 124 "Internal Server Error"'
]

# --- Execution Matrix ---
print("⚙️ Executing Enterprise Core Parser Ver 4.0...")
analyzer = AdvancedLogAnalyzer()
json_security_report = analyzer.generate_security_report(production_logs)

print("\n================= 🛡️ SERVER SECURITY TELEMETRY REPORT =================")
print(json_security_report)
print("=======================================================================")
