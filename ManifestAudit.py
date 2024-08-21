#!/usr/bin/env python

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
    print(f"{color}{text}",end="")
    print(f"{ENDC}",end="")

# get the AndroidManifest nemspace specified in the root element
def get_namespace(file):
    with open(file,"r") as f:
        content = f.read()
        return findall(r"xmlns:android=(\"|\')(.[^\"\']*)",content)[0][1]
    
# print AndroidManifest.xml
def get_activities(root:ET.Element,android_namespace:str):
    exported_activities = []
    print_colored("All activities:",BLUE)
    print()
    for activity in root.findall(".//activity"):
        name = activity.get(f"{{{android_namespace}}}name")
        print("\t",end="")
        print_colored(name,ENDC)
        exported = activity.get(f"{{{android_namespace}}}exported")
        if exported == 'true' or activity.findall(".//intent-filter"):
            exported_activities.append(name)
        print()

    print("\n")
    print_colored("\tExported Activities:",RED)
    print()
    for activity in exported_activities:
        print("\t\t",end="")
        print_colored(activity,ENDC)
        print()
        
# print custom permissions 
def get_custom_permissions(root:ET.Element):
    print_colored("Custom Permissions:",BLUE)
    print()
    for permission in root.findall(".//permission"):
        name = permission.get(f"{{{android_namespace}}}name")
        print("\t",end="")
        print_colored(name,ENDC)
       
# print uses permission
def get_uses_permissions(root:ET.Element):
    permissions = root.findall(".//uses-permission")
    print_colored("Uses Permissions:",BLUE)
    print()
    for permission in permissions:
        print("\t",end="")
        print(permission.get(f"{{{android_namespace}}}name"))
    
def get_intents(root: ET.Element,android_namespace):
    print_colored("Intents:", BLUE)
    print()
    for intent_filter in root.findall(".//intent-filter"):
        for i in intent_filter.findall(".//*"):
            print_colored("\t"+i.tag+":",YELLOW)
            print(f"\t\t{i.get(f'{{{android_namespace}}}name')}")
        print("\t"+("="*40))
        
def get_receivers(root:ET.Element,android_namespace):
    print_colored("Receiver:",BLUE)
    print()
    for receiver in root.findall(".//receiver"):
        print("\t",end="")
        print_colored(receiver.get(f"{{{android_namespace}}}name"),ENDC)
        for i in receiver.findall(".//intent-filter"):
            print()
            for j in i.findall(".//*"):
                print_colored("\t\t"+j.tag+": ",YELLOW)
                print(j.get(f"{{{android_namespace}}}name"))

def get_providers(root:ET.Element,android_namespace):
    print_colored("Content Providers",BLUE)
    print()
    for provider in root.findall(".//provider"):
        for attrib_name, attrib_value in provider.attrib.items():
                print_colored(f"\t{attrib_name[44:]}:\t",YELLOW)
                print(f" {attrib_value}")
        for i in provider.findall(".//*"):
            print_colored("\n\n\tInner Tags\n",RED)
            print_colored("\t\t" + i.tag + ":\n", CYAN)
            for attrib_name, attrib_value in i.attrib.items():
                print_colored(f"\t\t\t{attrib_name[44:]}:\t",YELLOW)
                print(f" {attrib_value}")

        print("\t"+"="*40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AndroidManifest.xml file analyzing and cutting down")
    parser.add_argument('-f', '--file', required=True, help='Path to the AndroidManifest.xml file')
    # parser.add_argument('-o', '--output', help='Output file (Only text file is supported)')
    parser.add_argument('--activities', action='store_true', help='Print only activities')
    parser.add_argument('--get-namespace', action='store_true', help='Print only namespace')
    parser.add_argument('--namespace', help='provide the namespace of the file (if not set the tool will determine it by itself)')
    parser.add_argument('--custom-permissions', action='store_true', help='provide only the permissions defined by the developer')
    parser.add_argument('--uses-permissions', action='store_true', help='provide needed permission for the application to run')
    parser.add_argument('--intents', action='store_true', help='provide intents')
    parser.add_argument('--dump', action='store_true', help='dump the whole file and extract all possible data')
    parser.add_argument('--receivers', action='store_true', help='get only Broadcast Receivers')
    parser.add_argument('--providers', action='store_true', help='provide content providers')
    args = parser.parse_args()
    
    android_namespace = get_namespace(args.file) if not args.namespace else args.namespace
    root = ET.parse(args.file).getroot()
    print(f"Working with the namespace ",end="")
    print_colored(android_namespace,CYAN)
    print("\n\n")

    if args.dump:
        get_activities(root,android_namespace)
        print()
        get_custom_permissions(root)
        print()
        get_uses_permissions(root)
        print()
        get_intents(root,android_namespace)
        print()
        get_receivers(root,android_namespace)
        print()
        get_providers(root,android_namespace)

    elif args.get_namespace:
        exit()        

    elif args.activities:
        get_activities(root,android_namespace)
        
    elif args.custom_permissions:
        get_custom_permissions(root)
        
    elif args.uses_permissions:
        get_uses_permissions(root)
    
    elif args.intents:
        get_intents(root,android_namespace)
        
    elif args.receivers:
        get_receivers(root,android_namespace)
        
    elif args.providers:
        get_providers(root,android_namespace)