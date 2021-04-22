# Import EzConfig
import ezconf
# Create config object
config = ezconf.config()
# Read the config file
config.read("test.json")
# Get nested values
print("\nHeard:",config.get("alternative")[0]["transcript"])
# Get pretty json
print("\nResponse from recognition\n")
print(config.pretty())
