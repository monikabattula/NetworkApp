### **Paramiko (Low-Level SSH for Advanced Control)**

**What is it?**

Paramiko is a **Python SSH library** for **secure connections** to devices, allowing execution of **commands, file transfers (SCP), and tunneling**.

 **Why Use Paramiko?**

- **More control over SSH sessions** than Netmiko.
- Useful for **file transfers, running scripts, and handling SSH keys**.
- Ideal for **non-networking devices (e.g., Linux servers, IoT devices, firewalls).**
The planning of the application:

left side of the 3text files needed for our application:

→ The first file is going to contain the IP addresses of our network devices , namely our three arista VM 

→ The next file holds the username and password used to login to each arista switch written on the same line separed by comma.

→ holds the commands that we want to execute on each of these switches.

So , the final application will read through all of these files, extract the necessary data, then use that data to establish the SSH connection to each device and excute the commands.

right side of the rectangle box have 5python scripts that can be imported to the [networkApp.py](http://networkApp.py) 

So bascially we are creating five modules each with its own functionality and role and then use them inside final porgram.

So, doing like this we can easily do the troubleshooting without checking hundrends of lines code just can check root cause

first, we have the IP_file_vaild.py script→ the final app will ask the user to manually input the name of the file holding the IP addresses.The role of this script is to check whether the file specified by the user exists on local file system and to also read the contents of file if it does exist and extract the IP addresses inside the text file in the form of list.

IP_addr_vaild.py→this script simply checks if each IP address in the first text file is a valid address.

ip_reach.py→ each ip address is reachable or not by performing a ping and evaluating the result.

SSH_connection.py→that performs several importcant tasks for our program:

→ first, it checks if the other two text files, meaning the one holding the username and password and one containing the commands to send are vaild and exist on the local file system or it trhoughs customised errors

create_threads.py → will create a thread for each device and perform the SSH connection command sending and output handling for all the devices simultanerously.
The file created having

10.10.10.2

10.10.10.3

10.10.10.4

Create the file in same folder and save it having admin,python

testing the application in the all three VMs created:(use same commands to check the loopback interface )

admin

pswd:****

enable (or) en

terminal

interface loopback 0

ip address 1.1.1.1 255.255.255.0

copy run start

you will get >> copy completed successfully.

show interfaces loopback 0

configuring the multiple devices 

tacacs-server host 10.10.10.7

tacacs-server key python

tacacs-server timeout 10

ntp server 10.10.10.8

vlan 22

vlan 33

vlan 44
