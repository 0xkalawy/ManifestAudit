import xml.etree.ElementTree as ET
from re import findall
import argparse

HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'  # Resets the color to default
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
# print colored text
def print_colored(text, color):
    if text!=None:
        print(f"{color}{text}")
    else:
        print(f"{ENDC}")

# get the AndroidManifest nemspace specified in the root element
def get_namespace(file):
    with open(file,"r") as f:
        content = f.read()
        return findall(r"xmlns:android=(\"|\')(.[^\"\']*)",content)[0][1]
    
# print AndroidManifest.xml
def get_activities(root:ET.Element,android_namespace:str):
    activities = []
    exported_activities = []
    for activity in root.findall(".//activity"):
        name = activity.get(f"{{{android_namespace}}}name")
        activities.append(name)
        exported = activity.get(f"{{{android_namespace}}}exported")
        if exported == 'true':
            exported_activities.append(name)
    print_colored("All activities:",BLUE)
    for activity in activities:
        print_colored(activity,ENDC)
    print("")
    print_colored("Activity with exported flag",RED)
    for activity in exported_activities:
        print_colored(activity,ENDC)
 
def get_custom_permissions(root):
    print_colored("Custom Permissions:",YELLOW)
    for permission in root.findall(".//permission"):
        name = permission.get(f"{{{android_namespace}}}name")
        print_colored(name,ENDC)
       
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AndroidManifest.xml file analyzing and cutting down")
    parser.add_argument('-f', '--file', required=True, help='Path to the AndroidManifest.xml file')
    parser.add_argument('-o', '--output', help='Output file (Only text file is supported)')
    parser.add_argument('--activities', action='store_true', help='Print only activities')
    parser.add_argument('--get-namespace', action='store_true', help='Print only namespace')
    parser.add_argument('--namespace', action='store_true', help='provide the namespace of the file (if not set the tool will determine it by itself)')
    parser.add_argument('--custom-permissions', action='store_true', help='provide only the permissions defined by the developer')
    parser.add_argument('--dump', action='store_true', help='dump the whole file and extract all possible data')
    
    args = parser.parse_args()
    
    android_namespace = get_namespace(args.file)
    root = ET.parse(args.file).getroot()
    if args.dump:
        print(f"Working with the namespace ",end="")
        print_colored(android_namespace,CYAN)
        print_colored(None,ENDC)
        get_activities(root,android_namespace)
        print_colored(None,ENDC)
        get_custom_permissions(root)

    elif args.get_namespace:
        print(get_namespace(args.file))
        print_colored(None,ENDC)

    elif args.activities:
        get_activities(root,android_namespace)
        print_colored(None,ENDC)
        
    elif args.custom_permissions:
        get_custom_permissions(root)
        print_colored(None,ENDC)
