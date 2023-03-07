# Create folder structure
```bash
mkdir -p platformName/{group_vars,host_vars,inventory,library,roles/{common,web,db,load-balancer}}
touch platformName/{site.yml,playbook1.yml,playbook2.yml,README.md}
touch platformName/group_vars/{all.yml,web-servers.yml,db-servers.yml,load-balancers.yml}
touch platformName/host_vars/{web-server-1.yml,web-server-2.yml,db-server-1.yml,db-server-2.yml}
touch platformName/inventory/{production.ini,staging.ini}
touch platformName/library/{custom_module.py,another_custom_module.py}
```

# Project Name

A brief description of your Ansible project.

## Folder Structure

Describe the folder structure of your project, and provide a brief explanation of what each folder contains.

## Configuration

Describe any configuration that needs to be done before running the playbooks, such as setting up SSH keys or installing Ansible dependencies.

## Usage

Provide instructions on how to use the playbooks and roles in your project, including any command-line arguments that need to be provided.



# Project structure

Here's what each of the folders and files does:

- **`platformName/`** is the top-level directory for your Ansible project.
- **`group_vars/`** contains variables that apply to entire groups of hosts. In this example, we have **`all.yml`** which applies to all hosts, and group-specific files for web servers, database servers, and load balancers.
- **`host_vars/`** contains variables that are specific to individual hosts. In this example, we have files for each web server and database server.
- **`inventory/`** contains inventory files that define your hosts and groups. In this example, we have separate inventory files for production and staging environments.
- **`library/`** contains any custom modules that you may have written to extend Ansible.
- **`roles/`** contains your roles, organized by function. In this example, we have roles for common tasks, web servers, database servers, and load balancers.
- **`site.yml`** is the top-level playbook that applies all of your roles to all hosts.
- **`playbook1.yml`** and **`playbook2.yml`** are additional playbooks that you may have created for specific tasks.
- **`README.md`** is a file that provides information about your Ansible project.

This folder structure allows you to organize your code in a logical way and makes it easy to maintain and expand your infrastructure over time.


## Variables

List any variables that need to be defined, and provide a brief explanation of what they do. For example:

### group_vars/all.yml

- `timezone`: The timezone that should be set on all hosts.
- `ntp_server`: The NTP server that should be used to synchronize time on all hosts.
- `http_proxy`: The HTTP proxy server that should be used for outgoing connections.
- `https_proxy`: The HTTPS proxy server that should be used for outgoing connections.

### group_vars/web-servers.yml

- `http_port`: The port number that the web server should listen on for HTTP traffic.
- `https_port`: The port number that the web server should listen on for HTTPS traffic.
- `web_server_user`: The user that the web server process should run as.
- `web_server_group`: The group that the web server process should run as.
- `document_root`: The directory that should be used as the document root for the web server.

### group_vars/db-servers.yml

- `db_server_user`: The user that the database server process should run as.
- `db_server_group`: The group that the database server process should run as.
- `db_name`: The name of the database that should be created.
- `db_user`: The username that should be used to connect to the database.
- `db_password`: The password

### host_vars/web-server-1.yml

- `http_port`: The port number that the web server should listen on for HTTP traffic.
- `https_port`: The port number that the web server should listen on for HTTPS traffic.

### host_vars/web-server-2.yml

- `http_port`: The port number that the web server should listen on for HTTP traffic.
- `https_port`: The port number that the web server should listen on for HTTPS traffic.

### host_vars/db-server-1.yml

- `db_port`: The port number that the database server should listen on.

### host_vars/db-server-2.yml

- `db_port`: The port number

## Inventory

List the contents of your `inventory` directory, including any host groups and variables that are defined. For example:

### inventory/production
```ini
[web_servers]
web-server-1
web-server-2

[db_servers]
db-server-1
db-server-2

[load_balancers]
lb-1
lb-2

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=/path/to/private/key.pem
```

## Custom Modules

List any custom modules that you have defined in your `library` directory, and provide a brief explanation of what each one does. For example:

### library/custom_module.py

This is a custom Ansible module that takes two parameters, `name` and `age`, and checks if the age is greater than or equal to 18. If it is, the module exits with a success message, and if not, it exits with a failure message.

## Roles

List any roles that you have defined in your `roles` directory, and provide a brief explanation of what each one does. For example:

### roles/common

This role contains tasks that apply to all hosts in the inventory, such as setting the timezone.

### roles/web-servers

This role contains tasks that install and start Apache on the web servers in the inventory.

### roles/db-servers

This role contains tasks that install and start MySQL on the database servers in the inventory.

### roles/load-balancers

This role contains tasks that install and configure HAProxy on the load balancers in the inventory.
