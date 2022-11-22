# SRTnumerator
Enumerate SRT information based on Slug and Username
```
                    \`-.                /\                .-'/
                     \   `-.           /  \           .-'   /
                      `-.    `-,      /____\      .-'    .-'
                          `-.   \                /   .-' 
                        \`-. \   \              /   / .-'/
                         \   `    \            /    '   /
                          `-.      \          /      .-'
                              `-.   \        /   .-'
                                  `-.\      /.-'
                             \`-.                .-'/
                              \   `-.        .-'   /
                               `-.    `-,,-'    .-'
                                   `-,      ,-'   
                                   /'  .--.  `\ 
                                  /.-'      `-.\ 
                           
      ____  ____ _____ _   _                                _             
     / ___||  _ \_   _| \ | |_   _ _ __ ___   ___ _ __ __ _| |_ ___  _ __ 
     \___ \| |_) || | |  \| | | | | '_ ` _ \ / _ \ '__/ _` | __/ _ \| '__|
      ___) |  _ < | | | |\  | |_| | | | | | |  __/ | | (_| | || (_) | |   
     |____/|_| \_\|_| |_| \_|\__,_|_| |_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                             
Written by Logue & FNGCrysis

usage: SRTnumerator.py [-h] [-u USERNAME] [-uL USERLIST] [-s SLUG] [-sL SLUGLIST] -k KEY

Enumerate SRT Display IDs

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Lookup ID using Single SRT Username
  -uL USERLIST, --userList USERLIST
                        Lookup ID using SRT Username List
  -s SLUG, --slug SLUG  Lookup ID using Single SRT Slug
  -sL SLUGLIST, --slugList SLUGLIST
                        Lookup ID using SRT Slug List
  -k KEY, --key KEY     Synack API Key

```

Examples:
- Enumerate SLUG based on Username
```
python3 SRTnumerator.py -k <synackAPIKey> -u <username>
```
- Enumerate SLUGs from a list of users
```
python3 SRTnumerator.py -k <synackAPIKey> -uL listofSRTusers.txt
```
- Enumerate Username based on SLUG
```
python3 SRTnumerator.py -k <synackAPIKey> -s <SLUG>
```
- Enumerate Usernames from a list of slugs
```
python3 SRTnumerator.py -k <synackAPIKey> -sL listofSRTslugs.txt
  ```
