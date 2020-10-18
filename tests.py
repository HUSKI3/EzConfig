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
config.add("extra-info","")
config.nested("extra-info","packages","Python")
print(config.get("extra-info")[0])
# Add more nested values
print("\nCreat new main nested value")
config.add("Test Data","")
config.nested("Test Data","line count","27")
print("\nAdding second nested entry")
config.nested("Test Data","Progammer sanity","-100")
config.nested("Test Data","Testing Date","16/10/2020")
# Get pretty json
print("\nGet pretty print\n")
print(config.pretty())
# Add object
config.add("Tests","none")
# check results
print(config.pretty())