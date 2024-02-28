import yaml

data={
    'different_images': [{'name':'ausfniddau','replica':2},{'name':'ausfueauth','replica':3}]

}

with open('charts/values.yaml','r') as yamlfile:
    cur_yaml = yaml.safe_load(yamlfile) # Note the safe_load
    cur_yaml.update(data)

if cur_yaml:
    with open('charts/values.yaml','w') as yamlfile:
        yaml.safe_dump(cur_yaml, yamlfile), # Also note the safe_dump

print('done')