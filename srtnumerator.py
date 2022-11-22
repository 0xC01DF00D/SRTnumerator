import requests
import argparse
import sys
import urllib3
import json

#Add Colors
class bcolors:
    RED = '\033[1;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[94m'
    LIGREEN = '\033[92m'
    GREEN = '\033[0;32m'
    NORMAL = '\033[0m'
    ORANGE = '\033[33m'

title = (bcolors.RED + """
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
"""+ bcolors.NORMAL + """                           
      ____  ____ _____ _   _                                _             
     / ___||  _ \_   _| \ | |_   _ _ __ ___   ___ _ __ __ _| |_ ___  _ __ 
     \___ \| |_) || | |  \| | | | | '_ ` _ \ / _ \ '__/ _` | __/ _ \| '__|
      ___) |  _ < | | | |\  | |_| | | | | | |  __/ | | (_| | || (_) | |   
     |____/|_| \_\|_| |_| \_|\__,_|_| |_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                             
"""+ bcolors.NORMAL)
print (title)

#Tricks to disable pesky SSL warnings
requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

prox = {"http":"http://127.0.0.1:8080", "https":"https://127.0.0.1:8080"}

#Functions
# parse the arguments
parser = argparse.ArgumentParser(description='Enumerate SRT Display IDs')
parser.add_argument('-u','--username', help='Lookup ID using Single SRT Username',required=False)
parser.add_argument('-uL','--userList', help='Lookup ID using SRT Username List',required=False)
parser.add_argument('-s','--slug', help='Lookup ID using Single SRT Slug',required=False)
parser.add_argument('-sL','--slugList', help='Lookup ID using SRT Slug List',required=False)
parser.add_argument('-k','--key', help='Synack API Key',required=True)

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

############################################################## User Functions ##############################################################

def usersToList():
    with open(args.userList) as file:
        users = [line.strip() for line in file]
        return users

def lookupUsersFromFile(users, key):
    for user in users:
        lookupSingleUser(user, key)

def lookupSingleUser(user, key):

    try:
        global outputFile
        query = "https://platform.synack.com/api/targets/scz3994tx0/eligible_collaborators?search=" + user.strip()
        r = requests.get(query, headers={"Authorization":"Bearer " + key}, verify=False, timeout=1)
        print(r.status_code)
        name = json.loads(r.text)
        print("Username: " + str(name[0]['slug']))
        print("Slug: " + str(name[0]['display_name']))

    except:
        print("Error.\n")

############################################################## Slug Functions ##############################################################
def slugsToList():
    with open(args.slugList) as file:
        slugs = [line.strip() for line in file]
        return slugs

def lookupSlugsFromFile(slugs, key):
    for slug in slugs:
        lookupSingleSlug(slug, key)


def lookupSingleSlug(slug, key):

    try:
        global outputFile
        query = "https://platform.synack.com/api/profiles/search?id%5B%5D=" + slug.strip()
        r = requests.get(query, headers={"Authorization":"Bearer " + key}, verify=False, timeout=1)
        print(r.status_code)
        name = json.loads(r.text)
        print("Username: " + str(name[0]['display_name']))
        print("Slug: " + str(name[0]['user_id']))

    except:
        print("Error.\n")




#MAIN
#Flow control for user vs user list
if args.userList:
    lookupUsersFromFile(usersToList(), args.key)
    print ("[*] Done."+ bcolors.NORMAL)
elif args.username:
    lookupSingleUser(args.username, args.key)
    print ("[*] Done."+ bcolors.NORMAL)

#Flow control for slug vs slug list
if args.slugList:
    lookupSlugsFromFile(slugsToList(), args.key)
    print ("[*] Done."+ bcolors.NORMAL)
elif args.slug:
    lookupSingleSlug(args.slug, args.key)
    print ("[*] Done."+ bcolors.NORMAL)
