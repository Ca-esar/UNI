#gets current date and time
from datetime import datetime
current_time = datetime.now().time()

#gets the local ip address
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
local_ip = s.getsockname()[0]

s.close()

#imports the netmiko libary
from netmiko import ConnectHandler 

#connects to virtual box
net_connect = ConnectHandler(
device_type="linux",
host="127.0.0.1",
port="5679",
username="davida", 
password="agbarakwe",
secret="agbarakwe",
timeout=30
)
net_connect.enable()

command = "sudo python3 done.py"
command = "mkdir -p /home/lubuntu/Downloads"
output = net_connect.send_command(command)


import requests
import os
# Saving a webpage for whatever reason function (option 5)
def savingawebpageforwhateverreason():
    try:
        # Asks the user for the webpage URL
        webpageurl = input("You can try this site if you do not have one http://httpforever.com\n"
                           "Please input the URL that you want to download from. (Make sure this is a full URL and it has to be http) - ")

        # Validate the URL format
        if not webpageurl.startswith("http://") and not webpageurl.startswith("https://"):
            print("The URL must start with 'http://' or 'https://'. Please try again.\n")
            wait(1.5)
            savingawebpageforwhateverreason()  # Exit the function early to allow the user to try again.

        # Send a GET request to the webpage
        response = requests.get(webpageurl)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the filename from the URL (or provide a default)
            filename = webpageurl.split("/")[-1] if webpageurl.split("/")[-1] else "index.html"
            
            # Ensure the file ends with .html (even if it doesn't appear in the URL)
            if not filename.endswith(".html"):
                filename += ".html"
            
            # Get the path to the user's Downloads folder (for Windows, it will work automatically)
            downloadpath_websave = os.path.join(os.path.expanduser('~'),'Downloads')
            
            # Ensure the Downloads directory exists
            if not os.path.exists(downloadpath_websave):
                print("Error: Downloads directory does not exist.")
            
            # Define the full path where the file will be saved
            save_path = os.path.join(downloadpath_websave, filename)
            
            # Write the webpage content to a file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            
            # Inform the user where the webpage was saved
            print(f"Webpage saved to {save_path}. You can find the page there.")
        else:
            print(f"Failed to retrieve the webpage. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to retrieve the webpage: {e}")
    

         
menu = ["1. Date and time",#defines the menu
        "2. Show IP",
        "3. Remote name directory listing,"
        , "4. Backup remote files",
        "5. Save web page",
        "Q. Quit"
] #what user sees


for item in menu:
        print(item)#presents menu option
        
    
choice = input("Select an item from the menu (1, 2, 3, 4, 5, q): ")#asks user for input


if choice in ['1']:
    print(f"The time is: {current_time}")
    

elif choice in ['2']:
    print(f"Your IP is: {local_ip}")
    
elif choice in ['3']:
    command = "ls "
    output = net_connect.send_command(command)
    print(f"The folders are as listed: {output}")
    
elif choice in ['4']:
    command =  "cp -r /home/lubuntu /home/lubuntu2"
    output = net_connect.send_command(command)
    print(f"remote files has been backed up: {output}")
    
elif choice in ['5']:
    command = "home/lubuntu"
    output = net_connect.send_command(command)
    print(f"Website has been backed up: {savingawebpageforwhateverreason()}")
    
elif choice in ['q']:
    print(f"follow commands to exit: {quit}")
else:
        print("Invalid option")      