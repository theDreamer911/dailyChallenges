import subprocess
import re

command = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()


ssid = (re.findall("All User Profile    : (.*)\r", command))

wifi_list = list()

if len(ssid) != 0:
    for name in ssid:
        wifi_profile = dict()

        profile_info = subprocess.run(
            ["nets", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        if re.search("Security Key      : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name

            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profiles", name, "key=clear"]).stdout.decode()

            password = re.search(
                "Key Content       : (.*)\r", profile_info_pass)

            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
