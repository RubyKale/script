# Trivy Installation Script
## This script is written to install Trivy for AMAZON or Debian based Linux OS on ARM or 64bit Architecture.
## Assumptions

1. **Trivy is not installed**: The script assumes that Trivy is not currently installed on the system.
2. **Python is installed**: Python is required to run this script.
3. **User Permissions**: The user running the script has the necessary permissions to install packages.
4. **Version Specific**: The script is designed for version 0.53.0 of Trivy. The version can be modified in the script.

## How to Run

1. **Download the Script**: Save the script as `install_trivy.py` on your local machine.
2. **Make the Script Executable**: Ensure the script has executable permissions by running:
   ```sh
   chmod +x install_trivy.py
   ```
3. **Run the Script**: Execute the script using Python:
   ```sh
   python install_trivy.py
   ```

## Versions Installed

The script supports the following Trivy package formats based on the operating system and architecture:

- **Debian/Ubuntu**:
  - `trivy_0.53.0_Linux-64bit.deb` for x86 and x86_64 architectures.
  - `trivy_0.53.0_Linux-ARM.deb` for ARM architecture.

- **Amazon Linux**:
  - `trivy_0.53.0_Linux-64bit.rpm` for x86 and x86_64 architectures.
  - `trivy_0.53.0_Linux-ARM.rpm` for ARM architecture.

## How to Change the Version of Trivy Package

To change the version of Trivy:

1. **Update the `version` Variable**: Modify the version in the URL and filename to the desired version.

   ```python
   url = f'https://github.com/aquasecurity/trivy/releases/download/v0.53.0/'
   ```

   Change `v0.53.0` to the desired version, e.g., `v0.54.0`.

2. **Update the Filename**: Ensure the `filename` variable matches the new version format.

   ```python
   filename = f'trivy_{version}_Linux-64bit.deb'
   ```

   Replace `{version}` with the new version number, e.g., `0.54.0`.

## Script Details

### Functions

- **`get_architecture_info()`**: Retrieves the system architecture (e.g., x86_64, ARM).
- **`get_osName_info()`**: Determines the operating system (e.g., Ubuntu, Amazon Linux).
- **`download_file_with_curl(url, filename)`**: Downloads the file from the specified URL using `curl`.
- **`install_package(filename, os)`**: Installs the downloaded package using appropriate package managers (`dpkg` for Debian-based systems, `yum` for Amazon Linux).
- ** `run_trivy_scan()` **: runs the scan on whole filesystem sudo trivy filesystem / --scanners vuln -q --ignore-unfixed”

## Post-Installation
After successfully installing Trivy, the script will automatically run a Trivy scan on the entire filesystem using the following command:

sh
Copy code
sudo trivy filesystem / --scanners vuln -q --ignore-unfixed
Purpose: This command scans the filesystem for vulnerabilities.
Flags:
--scanners vuln: Use the vulnerability scanner.
-q: Quiet mode, reducing output to essential information.
--ignore-unfixed: Ignore vulnerabilities that do not have available fixes.


### Example Usage

The script dynamically constructs the download URL based on the system's architecture and OS, downloads the package, and installs it. It handles both Debian-based and RPM-based package formats.

**Note**: Ensure you have the necessary permissions to run `sudo` commands for package installation.

---



