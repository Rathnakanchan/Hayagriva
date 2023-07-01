class AdLogEntry:
    def __init__(self, ID, serial_number, device_type, platform_id, bid_request_ip, user_platform_uid,
                 user_city, user_zipcode, user_agent, platform_type, channel_type, url, keywords, taxonomy, is_hcp):
        self.ID = ID
        self.serial_number = serial_number
        self.device_type = device_type
        self.platform_id = platform_id
        self.bid_request_ip = bid_request_ip
        self.user_platform_uid = user_platform_uid
        self.user_city = user_city
        self.user_zipcode = user_zipcode
        self.user_agent = user_agent
        self.platform_type = platform_type
        self.channel_type = channel_type
        self.url = url
        self.keywords = keywords
        self.taxonomy = taxonomy
        self.is_hcp = is_hcp

# Example usage
entry1 = AdLogEntry(1001, "123456", "desktop", 12345, "192.168.0.1", "user123", "New York", "12345",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "EHR", "website", "https://example.com", "healthcare, doctor", "cardiology", True)

entry2 = AdLogEntry(1002, "789012", "mobile", "PLATFORM_XYZ", "10.0.0.2", "platform_user_456", "London", "54321",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
                    "telemedicine", "mobile app", "https://example.com", "medicine, patient care", "dermatology", False)

# Accessing the attributes
print(entry1.ID)
print(entry1.device_type)
print(entry1.user_city)
# ...

# Performing operations on the entries
if entry2.is_hcp:
    print("User is a Healthcare Professional")
else:
    print("User is not a Healthcare Professional")

# You can create a list to store multiple log entries
log_entries = [entry1, entry2]
