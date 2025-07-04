import subprocess
import sys
import os
import time
import shutil
import socket
from tqdm import tqdm
from colorama import init, Fore, Style

init(autoreset=True)

REQUIRED_TOOLS = ["whois", "nslookup", "host", "theharvester", "dnsenum", "sublist3r", "nmap"]
RESULTS_DIR = "footprint_results"
os.makedirs(RESULTS_DIR, exist_ok=True)


def show_banner():
    banner = r"""

██╗███╗░░██╗███████╗░█████╗░░██████╗░█████╗░░██████╗░███████╗
██║████╗░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝░██╔════╝
██║██╔██╗██║█████╗░░██║░░██║╚█████╗░███████║██║░░██╗░█████╗░░
██║██║╚████║██╔══╝░░██║░░██║░╚═══██╗██╔══██║██║░░╚██╗██╔══╝░░
██║██║░╚███║██║░░░░░╚█████╔╝██████╔╝██║░░██║╚██████╔╝███████╗
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝
                | Website Footprinting Toolkit | by- Genos
                      by- 𝔾𝕖𝕟𝕠𝕤
    """
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "=" * 60)
    time.sleep(1)


def check_internet():
    print(Fore.YELLOW + "[+] Checking internet connectivity...")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print(Fore.GREEN + "[+] Internet connection confirmed.\n")
    except OSError:
        print(Fore.RED + "[-] No internet connection detected. Please connect and try again.")
        return False
    return True


def check_and_install_tools():
    print(Fore.YELLOW + "[+] Checking required tools...\n")
    missing_tools = []

    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            missing_tools.append(tool)

    if not missing_tools:
        print(Fore.GREEN + "[+] All required tools are installed.\n")
        return True

    print(Fore.RED + "[!] Missing tools detected: " + ", ".join(missing_tools))
    print(Fore.YELLOW + "[+] Installing missing tools...\n")

    install_command = f"sudo apt update && sudo apt install {' '.join(missing_tools)} -y"
    try:
        subprocess.run(install_command, shell=True, check=True)
        print(Fore.GREEN + "\n[+] All missing tools installed successfully!\n")
        return True
    except subprocess.CalledProcessError:
        print(Fore.RED + "\n[-] Error occurred while installing tools.\n")
        return False


def run_command(command, description, filename):
    print(Fore.CYAN + f"\n[+] {description}")
    log_path = os.path.join(RESULTS_DIR, filename)

    for _ in tqdm(range(100), desc=f"Running {description}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=70):
        time.sleep(0.01)

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout + result.stderr

        with open(log_path, "w") as file:
            file.write(output)

        print(Fore.GREEN + f"[+] Results saved to {log_path}")
    except Exception as e:
        print(Fore.RED + f"[-] Error executing {description}: {str(e)}")


def footprint_menu(domain):
    while True:
        print(Fore.YELLOW + "\n=== INFOSAGE Footprinting Menu ===")
        print(f"Target Domain: {domain}")
        print("1. WHOIS Lookup")
        print("2. DNS Lookup")
        print("3. Host IP Resolution")
        print("4. Email Enumeration (theHarvester)")
        print("5. DNS Enumeration (dnsenum)")
        print("6. Subdomain Enumeration (Sublist3r)")
        print("7. Nmap Basic Scan")
        print("8. Run Full Scan")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            run_command(f"whois {domain}", "WHOIS Lookup", "whois.txt")
        elif choice == "2":
            run_command(f"nslookup {domain}", "DNS Lookup", "dns_lookup.txt")
        elif choice == "3":
            run_command(f"host {domain}", "Host IP Resolution", "host_ip.txt")
        elif choice == "4":
            run_command(f"theharvester -d {domain} -b google -l 100", "Email Enumeration", "email_enum.txt")
        elif choice == "5":
            run_command(f"dnsenum {domain}", "DNS Enumeration", "dns_enum.txt")
        elif choice == "6":
            run_command(f"sublist3r -d {domain}", "Subdomain Enumeration", "subdomains.txt")
        elif choice == "7":
            run_command(f"nmap -sP {domain}", "Nmap Basic Scan", "nmap_scan.txt")
        elif choice == "8":
            full_scan(domain)
        elif choice == "9":
            print(Fore.CYAN + "Exiting INFOSAGE. Results are saved in the 'footprint_results' folder.")
            break
        else:
            print(Fore.RED + "Invalid option. Please select a valid choice.")


def full_scan(domain):
    print(Fore.YELLOW + "\n[+] Running Full Footprinting Scan...\n")
    run_command(f"whois {domain}", "WHOIS Lookup", "whois.txt")
    run_command(f"nslookup {domain}", "DNS Lookup", "dns_lookup.txt")
    run_command(f"host {domain}", "Host IP Resolution", "host_ip.txt")
    run_command(f"theharvester -d {domain} -b google -l 100", "Email Enumeration", "email_enum.txt")
    run_command(f"dnsenum {domain}", "DNS Enumeration", "dns_enum.txt")
    run_command(f"sublist3r -d {domain}", "Subdomain Enumeration", "subdomains.txt")
    run_command(f"nmap -sP {domain}", "Nmap Basic Scan", "nmap_scan.txt")
    print(Fore.GREEN + "\n[+] Full scan completed. All results are saved in the 'footprint_results' folder.")


def main():
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Usage: python3 infosage.py <domain>")
        print(Fore.RED + "[-] Domain argument missing. Please rerun the script with the domain as an argument.")
        return

    domain = sys.argv[1]

    show_banner()

    if not check_internet():
        return

    if not check_and_install_tools():
        return

    footprint_menu(domain)


if __name__ == "__main__":
    main()
