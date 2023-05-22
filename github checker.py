import requests
import random 
import string
from pystyle import Colorate,Colors,Center

print(Center.XCenter(f'''
 ██████╗ ██╗████████╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
██╔════╝ ██║╚══██╔══╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
██║  ███╗██║   ██║   ██╔██╗ ██║███████║██╔████╔██║█████╗  
██║   ██║██║   ██║   ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                          
'''))

user_lenght = int(input(f"{Colors.blue}[{Colors.white}>{Colors.blue}] {Colors.white}username lenght?: "))

while True:
    user = ''.join(random.choices(string.ascii_letters + string.digits, k=user_lenght))
    r = requests.get(f"https://github.com/{user}")

    if r.status_code == 404:
        print(f"{Colors.green}[{Colors.white}+{Colors.green}] {Colors.white}{user}")
        with open("hits.txt","a") as f:
            f.write(f"{user}\n")
    else:
        print(f"{Colors.red}[{Colors.white}-{Colors.red}] {Colors.white}{user}")