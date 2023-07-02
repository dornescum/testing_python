import subprocess

def ufw_status():
    command = ['ufw', 'status']
    result = subprocess.run(command, capture_output=True, text=True)
    # return result.stdout
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr

print('test')

print(ufw_status())


