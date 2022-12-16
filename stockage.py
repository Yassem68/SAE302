import os
response = os.system("ping -c 4 " + "127.0.0.1")
if response == 0:
    pingstatus = "Network Active"
    print("Le ping a fonctionné")
else:
    pingstatus = "Network Error"
    print("Le ping n'a pas fonctionné")


