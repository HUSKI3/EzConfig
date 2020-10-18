# EzConfig
Easy to use expandable configuration reader in Python

# How to use:
1. Download both ezconf.py and merrors.py and place them into your project folder.
2. Create a new config with basic values given in the `example_config.json`
3. Enjoy!

Example (located in tests.py):
```Python
# Import EzConfig
import ezconf
# Create config object
config = ezconf.config()
# Read the config file
print("\nLoad config")
config.read("example_config.json")
# Get non-nested values
print("\nGet non-nested value\n")
print(config.get("name"))
# Get nested values
print("\nGet nested value\n")
print(config.get("extra-info","packages"))
# Add more nested values
print("\nCreat new main nested value")
config.add("Message Data","")
config.nested("Message Data","message count","30")
print("\nAdding second nested entry")
config.nested("Message Data","last message","14/10/2020")
config.nested("Message Data","last user to send a message","Test")
# Get pretty json
print("\nGet pretty print\n")
print(config.pretty())
# Add object
config.add("Tests","none")
# check results
print(config.pretty())
```

Example of the config.json:
```json
{
"name": "Example Application",
"version": "0.0.1",
"run_script": "tests.py",
"author": "Linkus",
"license": "Apache 2",
"extra-info":{
  "packages": "merrors, ezconfig",
  "desc": "Easier configs for python"
}
}
```

Result
![image](https://media.discordapp.net/attachments/691415466840948777/765940745604562955/unknown.png)