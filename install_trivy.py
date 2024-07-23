

import platform
import subprocess


def get_architecture_info():
    architecture = platform.machine()
    return  architecture

def get_osName_info():
    try:
        # Run the command and capture the output
        result = subprocess.run(['cat', '/etc/os-release'], capture_output=True, text=True, check=True)
        print(result.stdout)
        if 'Ubuntu' in result.stdout:
            return('Ubuntu')
        if 'Amazon' in result.stdout:
            return('Amazon')
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("The file /etc/os-release does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def download_file_with_curl(url, filename):
    try:
        # Run the curl command to download the file
        result = subprocess.run(['curl', '-L', '-o', filename, url], capture_output=True, text=True, check=True)

        # Print the output (stdout) and any errors (stderr)
        print("Download output:", result.stdout)
        if result.stderr:
            print("Download errors:", result.stderr)
        print(f"File downloaded successfully as {filename}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running curl: {e}")

def install_package(filename,os):
    try:
        # Run the dpkg command to install the package
        if os in 'Ubuntu':
            result = subprocess.run(['sudo', 'dpkg', '-i', filename], capture_output=True, text=True, check=True)
            # Resolve dependencies if any are missing- sudo apt-get install -f -y  used to fix broken dependencies on a Debian-based system like Ubuntu
           
            result1 = subprocess.run(['sudo', 'apt-get', 'install', '-f', '-y'], capture_output=True, text=True, check=True)
           
            print("Dependency resolution output:", result1.stdout)
            
            if result1.stderr:
                print("Dependency resolution errors:", result1.stderr)

        if os in 'Amazon':
            result = subprocess.run(['sudo', 'yum', 'localinstall', '-y', filename], capture_output=True, text=True, check=True)
            
        # Print the output (stdout) and any errors (stderr)
        print("Installation output:", result.stdout)
       
        if result.stderr:
            print("Installation errors:", result.stderr)
            
        print(f"Package installed successfully from {filename}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing the package: {e}")

def run_trivy_scan():
    try:
        # Running the Trivy scan without capturing output
        print("Running Trivy scan...")
        subprocess.run(
            ["sudo", "trivy", "filesystem", "/", "--scanners", "vuln", "-q", "--ignore-unfixed"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during scan: {e}")
        sys.exit(1)

if __name__ == "__main__":
    architecture = get_architecture_info()
    osName = get_osName_info()
    version = '0.53.0'
    url = f"https://github.com/aquasecurity/trivy/releases/download/v{version}/"
    filename = ''

    if architecture in ('x86', 'x86_64') and osName in ('Ubuntu'):
        filename = f"trivy_{version}_Linux-64bit.deb"
        url += filename

    if  ('ARM' in architecture or 'aarch' in architecture or 'AArch' in architecture) and osName in 'Ubuntu':
        filename = f"trivy_{version}_Linux-ARM.deb"
        url += filename

    if architecture in ('x86', 'x86_64') and osName in ('Amazon'):
        filename = f"trivy_{version}_Linux-64bit.rpm"
        url += filename

    if ('ARM' in architecture or 'aarch' in architecture or 'AArch' in architecture) and osName in ('Amazon'):
        filename = f"trivy_{version}_Linux-ARM.rpm"
        url += filename

    if filename not in '':
        download_file_with_curl(url,filename)
        install_package(filename,osName)
        run_trivy_scan()

    else:
        print("Operating system out of scope of the script")

