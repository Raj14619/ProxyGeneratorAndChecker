import random
import ipaddress

# Function to generate and write 1 million random IPv4 addresses to a text file
def generate_and_write_random_ips():
    # Specify the file path
    file_path = "random_ips.txt"

    with open(file_path, 'w') as file:
        for _ in range(50000):
            random_ip_int = random.randint(0, 2**32 - 1)
            random_ip = ipaddress.IPv4Address(random_ip_int)
            file.write(f"{random_ip}\n")

    print("1 million random IPv4 addresses generated and saved to random_ips.txt")
