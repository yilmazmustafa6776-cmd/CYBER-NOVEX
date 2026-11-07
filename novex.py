import os
import socket
import platform
import subprocess

GREEN = "\033[92m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(GREEN + """
          C Y B E R  N O V E X
""" + RESET)

def system_info():
    print("System:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())

def network_info():
    print("Hostname:", socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("1.1.1.1", 53))
        print("Local IP:", s.getsockname()[0])
    except OSError:
        print("Local IP: Unavailable")
    finally:
        s.close()

def device_scanner():
    print(GREEN + "\n[ NOVEX DEVICE SCANNER ]" + RESET)
    result = subprocess.run(
        ["nmap", "-sn", "-oN", "devices.txt", "192.168.0.0/24"],
        capture_output=True,
        text=True
    )
    print(result.stdout if result.returncode == 0 else result.stderr)

def dashboard():
    print(GREEN + "\n[ SECURITY DASHBOARD ]")
    print("Project: CYBER NOVEX")
    print("Status: Operational" + RESET)

def vulnerability_scanner():
    print(GREEN + "\n[ NOVEX VULNERABILITY SCANNER ]" + RESET)
    if subprocess.run(["which", "lynis"], capture_output=True).returncode != 0:
        print("Lynis is not installed.")
        return
    print("Starting Lynis security audit...\n")
    command = ["lynis", "audit", "system"]
    if os.geteuid() != 0:
        command.insert(0, "sudo")
    subprocess.run(command)

def main():
    while True:
        banner()
        print(GREEN + """
[1] System Information
[2] Network Information
[3] Security Dashboard
[4] NOVEX DEVICE SCANNER
[5] NOVEX VULNERABILITY SCANNER
[6] Exit
""" + RESET)

        choice = input("NOVEX >> ")

        if choice == "1":
            system_info()
        elif choice == "2":
            network_info()
        elif choice == "3":
            dashboard()
        elif choice == "4":
            device_scanner()
        elif choice == "5":
            vulnerability_scanner()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
