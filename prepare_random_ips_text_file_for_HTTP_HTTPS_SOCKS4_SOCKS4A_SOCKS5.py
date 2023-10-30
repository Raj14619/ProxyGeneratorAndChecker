def prepare_random_ips_text_file_for_http(ports):
    with open('random_ips.txt', 'r') as input_f, open('http_to_test.txt', 'w') as output_f:
        for line in input_f:
            ip = line.strip()  # Remove any leading/trailing whitespace
            results = [f"{ip}:{port}" for port in ports]  # Create a list of IP:port strings
            output_f.write("\n".join(results) + '\n')  # Write the results to the output file, including a newline