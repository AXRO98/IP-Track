"""
[=================================================]
 Copyright (C) 2023 axroc98. All rights reserved.
[=================================================]
 This message is intended to protect the copyright of the works contained in this document.
 All material within this document, including but not limited to text, images, graphics, audio, video, and other materials, are the exclusive property of axroc98 unless otherwise stated.
 Duplication or distribution of the whole or partial content of this document is not permitted without permission from axroc98.
 Any modification, reproduction, or republication of this content without written permission from the copyright owner is strictly prohibited. 
 Violation of these terms constitutes an infringement of exclusive rights and may result in legal action as per the applicable regulations.
 axroc98 reserves the right to take necessary measures to protect its copyright and intellectual property.
 The use of trademarks or service marks visible in this document does not imply any endorsement or affiliation between axroc98 and the owners of such trademarks.
 For inquiries or requests regarding copyright, please contact us via the email address listed in this document.
 Thank you for your understanding and compliance with this copyright notice. We hope this document provides valuable benefits and information, and remains a well-protected asset.
 © 2023 axroc98. All rights reserved under the law.

[==========================]
 Contact Me:
 Email: axroc98@proton.me
[==========================]
"""

import requests
import time
import ipaddress
import platform
import os

none = '\033[1;0m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
purple = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[1;37m'
underline = '\033[4m'

# Configurasi Color

color_1 = purple
color_2 = cyan
color_figlet_1 = cyan
color_figlet_2 = white
color_figlet_3 = yellow
color_figlet_4 = red

color_output_1 = white
color_output_2 = green

danger = f'{cyan}[{red}!{cyan}]{white}'

def clear():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_public_ipv4():
    try:
        response = requests.get('https://ipinfo.io/json')
        
        if response.ok:
            data = response.json()
            return data.get('ip', 'Tidak dapat mendapatkan IP publik')
        else:
            return '0.0.0.0'

    except requests.exceptions.RequestException as e:
        return f'get IPv4 error!!'

def get_public_ipv6():
    try:
        response = requests.get('https://api64.ipify.org/')
        
        if response.ok:
            return response.text
        else:
            return '0.0.0.0'

    except requests.exceptions.RequestException as e:
        return f'get IPv6 error!!'

IP_Track_Figlet = f"""
 {color_figlet_1} _____  _____  {color_figlet_2}     {color_figlet_3} _______                 
 {color_figlet_1}|_   _||  __ \ {color_figlet_2}     {color_figlet_3}|__   __| {green}©{underline}IP-API.com{none}
 {color_figlet_1}  | |  | |__) |{color_figlet_2} _____{color_figlet_3}  | |_ __ __ _  ___ __ __
 {color_figlet_1}  | |  |  ___/ {color_figlet_2}|_____|{color_figlet_3} | | '__/ _` |/ __| |/ /
 {color_figlet_1} _| |_ | |     {color_figlet_2}     {color_figlet_3}   | | | | (_| | (__|   <  
 {color_figlet_1}|_____||_|  {color_figlet_4}V.1.0{none}{color_figlet_3}      |_|_|  \__,_|\___|_|\_\\
{color_1}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{color_1}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
{color_1}┃ {white}Your IPv6: {green}{get_public_ipv6()}
{color_1}┃ {white}Your IPv4: {green}{get_public_ipv4()}
{color_1}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<"""

def get_ip_info():
    try:
        print(f"{color_1}┃")
        query = input(f'┖─➤ {cyan}IP-Track:\033[1;0m ')
        url = f"http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        response = requests.get(url)

        if response.ok:
            data = response.json()
            IP_Track = data["query"]
            print_details(data, IP_Track)

    except requests.exceptions.ConnectionError:
        handle_error("No Connection !!!")

    except KeyError:
        print(f"{color_1}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<")
        print(f"{color_1}┃")
        handle_error(f"┖─➢ {danger} IP Not Found :(")

    except KeyboardInterrupt:
        handle_error(f"\n{color_1}  >──➤ {danger} KeyboardInterrupt :(")

    except EOFError:
        handle_error(f"\n\n{color_1}  >──➤ {danger} EOFError :(")

    except Exception as e:
        handle_error(f"┖─➢ {danger} Tools IP-Track Error: {e}. Try Again :(")

def print_details(data, query):
    clear()
    print(IP_Track_Figlet)
    print(f"{color_1}┃ {white}Results Tracking {yellow}IP:{green} {query}")
    print(f"{color_1}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<")

    details_mapping = [
        ("IP", "query"),
        ("Status", "status"),
        ("Continent", "continent"),
        ("Continent Code", "continentCode"),
        ("Country", "country"),
        ("Country Code", "countryCode"),
        ("Region Name", "regionName"),
        ("Region", "region"),
        ("City", "city"),
        ("District", "district"),
        ("Zip", "zip"),
        ("Latitude", "lat"),
        ("Longitude", "lon"),
        ("Timezone", "timezone"),
        ("Offset", "offset"),
        ("Currency", "currency"),
        ("AS", "as"),
        ("AS Name", "asname"),
        ("ISP", "isp"),
        ("Organization", "org"),
        ("Mobile", "mobile"),
        ("Proxy", "proxy"),
        ("Hosting", "hosting"),
    ]

    for detail, key in details_mapping:
        value = data.get(key)
        if value == '':
            value = f'{red}Not Found'
        if value == 'fail':
            value = 'Failed'
        print(f"{color_1}┣─➤ {color_output_1}{detail.ljust(15)} {color_2}>──➤{color_output_2}", value)

    print(f"{color_1}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<")

def handle_error(message):
    print(f"{message}")
    time.sleep(0.5)
    exit()

if __name__ == "__main__":
    clear()
    print(IP_Track_Figlet)
    get_ip_info()
