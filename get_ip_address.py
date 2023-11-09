import subprocess

def get_ip_address(interface_name):
    try:
        cmd = f"ip addr show {interface_name} | grep 'inet ' | awk '{{print $2}}' | cut -d/ -f1"
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        ip_address = result.strip()
        return ip_address
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
