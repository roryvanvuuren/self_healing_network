from pythonping import ping
import json
from halo import Halo

def check_ping():
    with open('self_healing_network/scripts/inventory.json', 'r') as file:
        inventory = json.load(file)

    # Initializing the Halo spinner
    spinner = Halo(text='Pinging devices', spinner='dots')

    ping_results = []
    spinner.start()  # Starting the spinner
    for device in inventory['devices']:
        response = ping(device['ip'], count=4)
        success = response.success()
        output = str(response)
        ping_results.append({'device': device['name'], 'success': success})

    spinner.stop()  # Stopping the spinner once ping is complete
    return ping_results

# Calling the function to perform ping operations with the Halo spinner
result = check_ping()
print(result)  # You can use or process the ping results further as needed

