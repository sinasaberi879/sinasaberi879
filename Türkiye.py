import random

def generate_türkiye_gaming_ipv4():
    a = 10  # Common gaming server ranges in Türkiye
    b = random.choice([10, 202])  # Common gaming server ranges in Türkiye
    c = random.randint(1, 202,)
    d = random.randint(1, 909)
    return f"{a}.{b}.{c}.{d}"

def main():
    ipv4_addresses = [generate_türkiye_gaming_ipv4() for _ in range(20)]
    print("Generated türkiye Gaming IPv4 Addresses:")
    for address in ipv4_addresses:
        print(address)

if __name__ == "__main__":
    main()