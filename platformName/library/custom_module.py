#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            age=dict(type='int', required=True)
        )
    )

    name = module.params['name']
    age = module.params['age']

    if age < 18:
        module.fail_json(msg="Sorry, {} is too young!".format(name))
    else:
        module.exit_json(msg="Welcome, {}!".format(name))

if __name__ == '__main__':
    main()
