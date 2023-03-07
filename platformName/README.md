# Create folder structure
```bash
mkdir -p platformName/{group_vars,host_vars,inventory,library,roles/{common,web,db,load-balancer}}
touch platformName/{site.yml,playbook1.yml,playbook2.yml,README.md}
touch platformName/group_vars/{all.yml,web-servers.yml,db-servers.yml,load-balancers.yml}
touch platformName/host_vars/{web-server-1.yml,web-server-2.yml,db-server-1.yml,db-server-2.yml}
touch platformName/inventory/{production.ini,staging.ini}
touch platformName/library/{custom_module.py,another_custom_module.py}
```

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