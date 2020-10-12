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
# Get pretty json
print("\nGet pretty print\n")
print(config.pretty())


