# mysql-selfmanaged
# VM used was Google Cloud
log on to GCP account and select "Compute engine > VM Instances"
Click on "Create Instance" 

## Create GCP VM
When creating the Instance, you choose a name
Choose the image type "Ubuntu 19.04 x86/64"
Select the size you need to run the virtual environment (I selected e2 medium).
Turn on the firewalls for http as well as https
Click on the create instance button at the bottom of the page once everything is set up.

## Setting up newly created VM
Once the instance is created, click on "ssh" and connect to the vm via a pop up browser
Once inside, run "Sudo apt-get update" to update the packages within the terminal.
Then run "Sudo apt-get install mysql-server mysql-client" to install mysql.
Then log into mysql with "Sudo mysql"

## Open ports
To open the ports to allow mysql instance available to external computers, go back to GCP, search "firewall" and create a firewall rule that allows the mysql port 3386 to connect to through the VM 
Back in the VM terminal, run "sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf" to open the text editor, scroll down to find the "bind address" and change the bind address to "0.0.0.0" to allow connections from all IP addresses.