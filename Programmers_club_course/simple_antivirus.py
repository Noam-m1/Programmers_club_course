import hashlib       # Used to calculate the SHA256 hash of the file
import requests      # Used to send HTTP requests to VirusTotal API
import os            # Used to work with file paths and check if files exist
import time          # Used to add delays (wait for scan results)

# VirusTotal API key (needed to authenticate with the VirusTotal API)
API_KEY = 'af59c7723fd396bf8a99d3f1e18d7e15c1e810273ac23288740bfa62ac14cc02'

# Ask the user to type the full path of the file to scan
file_path = input("please type your wanted full filepath:")

# Base URLs used to make API requests to VirusTotal
FILE_REPORT_URL = 'https://www.virustotal.com/api/v3/files/'
UPLOAD_URL = 'https://www.virustotal.com/api/v3/files'
ANALYSIS_URL = 'https://www.virustotal.com/api/v3/analyses/'

# Function to calculate the SHA256 hash of the file
def get_file_hash(filepath):
    sha256 = hashlib.sha256()  # Creates a new SHA256 hash object
    try:
        with open(filepath, 'rb') as f:  # Open the file in binary mode (rb = read binary)
            while chunk := f.read(8192):  # Read the file in chunks of 8192 bytes (helps with large files)
                sha256.update(chunk)  # Feed each chunk into the SHA256 algorithm
        return sha256.hexdigest()  # Return the final hash as a hexadecimal string
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None

# Function to check if the file hash already exists in VirusTotal
def check_virustotal(file_hash):
    headers = {'x-apikey': API_KEY}  # This sets your API key in the request headers for authentication

    # Send a GET request to VirusTotal to check if this file hash is already known
    response = requests.get(FILE_REPORT_URL + file_hash, headers=headers)
    
    if response.status_code == 200:  # If the file hash was found and is known to VirusTotal
        print("✅ File already exists in VirusTotal.")
        data = response.json()  # Convert the JSON response from the server into a Python dictionary
        stats = data['data']['attributes']['last_analysis_stats']  # Get the scan result statistics
        print("📊 Scan Results:")
        print(f"✔️ Harmless: {stats['harmless']}")
        print(f"⚠️ Suspicious: {stats['suspicious']}")
        print(f"❌ Malicious: {stats['malicious']}")
        return True
    elif response.status_code == 404:
        # File hash not found in VirusTotal
        print("📁 File not found in VirusTotal. Will upload.")
        return False
    else:
        # Some other error occurred (like invalid API key or network issue)
        print(f"❌ Error checking file hash: {response.status_code}")
        print(response.text)
        return None

# Function to upload the file to VirusTotal for scanning
def upload_file(filepath):
    headers = {'x-apikey': API_KEY}  # Set your API key in the headers

    # Open the file in binary mode and prepare it for upload
    with open(filepath, 'rb') as f:
        # os.path.basename(filepath) gets just the file name from the full path
        # 'files' is a dictionary that matches what VirusTotal expects for file uploads
        files = {'file': (os.path.basename(filepath), f)}

        # Send a POST request to upload the file to VirusTotal
        response = requests.post(UPLOAD_URL, headers=headers, files=files)

    if response.status_code == 200:
        data = response.json()  # Get the response data
        analysis_id = data['data']['id']  # This ID is used to check the scan results later
        print(f"✅ File uploaded. Analysis ID: {analysis_id}")
        return analysis_id
    else:
        print(f"❌ Upload failed: {response.status_code}")
        print(response.text)
        return None

# Function to check the scan results using the analysis ID
def get_scan_result(analysis_id):
    headers = {'x-apikey': API_KEY}  # Set your API key again
    response = requests.get(ANALYSIS_URL + analysis_id, headers=headers)  # Ask VirusTotal for the scan result

    if response.status_code == 200:
        data = response.json()  # Convert JSON to Python dictionary
        status = data['data']['attributes']['status']  # Check if the scan is still running or done
        print(f"⏳ Scan status: {status}")
        if status == 'completed':
            stats = data['data']['attributes']['stats']  # Get the stats once completed
            print("📊 Final Scan Results:")
            print(f"✔️ Harmless: {stats['harmless']}")
            print(f"⚠️ Suspicious: {stats['suspicious']}")
            print(f"❌ Malicious: {stats['malicious']}")
        else:
            print("⌛ Scan is still in progress. Try again later.")
    else:
        print(f"❌ Could not retrieve scan result: {response.status_code}")
        print(response.text)

# === Main Program Starts Here ===
if os.path.exists(file_path):  # Check if the user-specified file actually exists
    file_hash = get_file_hash(file_path)  # Get the SHA256 hash of the file
    print(f"\n🔑 SHA256: {file_hash}")

    found = check_virustotal(file_hash)  # Check if this file is already known to VirusTotal

    if found is False:
        analysis_id = upload_file(file_path)  # If not, upload the file
        if analysis_id:
            print("⏱ Waiting 60 seconds for scan to complete...")
            time.sleep(60)  # Wait for the scan to be processed
            get_scan_result(analysis_id)  # Get the results
else:
    print(f"❌ File does not exist: {file_path}")

#got help from chat.GPT, API VirusTotal, GitHub and more genral sites for coding during the creation of this project