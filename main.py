from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('tenant_production.yaml')

with open('./output/tenant_production.yaml', 'w') as file:
    file.write(template.render(tenant_name="terraform-demo"))