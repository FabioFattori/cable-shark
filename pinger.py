import subprocess
import requestError
def ping_ip(ip_address):
    try:
        # Execute ping command
        process = subprocess.Popen(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the process to terminate
        output, error = process.communicate()
        print(output, "\n",error)
        # Check if ping was successful
        if process.returncode == 0:
            return (requestError.res.get(1),output.decode('utf-8'))
        else:
            return (requestError.res.get(0),output.decode('utf-8'))
    except Exception as e:
        return str(e)