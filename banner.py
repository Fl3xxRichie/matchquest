from colorama import Fore, Back, Style, init
import sys
import time

# Initialize colorama
init(autoreset=True)

def print_banner():
    # Gradient colors for the main text
    colors = [Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN]
    
    banner = f"""
{Fore.CYAN + Style.BRIGHT}██████╗ ██║     ███████╗██╗  ██╗██╗  ██╗{Fore.BLUE + Style.BRIGHT}██████╗ ██╗ ██████╗██╗  ██╗██╗███████╗
{Fore.CYAN + Style.BRIGHT}██╔══██╗██║     ██╔════╝╚██╗██╔╝╚██╗██╔╝{Fore.BLUE + Style.BRIGHT}██╔══██╗██║██╔════╝██║  ██║██║██╔════╝
{Fore.MAGENTA + Style.BRIGHT}██████╔╝██║     █████╗   ╚███╔╝  ╚███╔╝ {Fore.RED + Style.BRIGHT}██████╔╝██║██║     ███████║██║█████╗  
{Fore.MAGENTA + Style.BRIGHT}██╔══██╗██║     ██╔══╝   ██╔██╗  ██╔██╗ {Fore.RED + Style.BRIGHT}██╔══██╗██║██║     ██╔══██║██║██╔══╝  
{Fore.YELLOW + Style.BRIGHT}██║  ██║███████╗███████╗██╔╝ ██╗██╔╝ ██╗{Fore.GREEN + Style.BRIGHT}██║  ██║██║╚██████╗██║  ██║██║███████╗
{Fore.YELLOW + Style.BRIGHT}╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝{Fore.GREEN + Style.BRIGHT}╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝{Style.RESET_ALL}

{Fore.CYAN + Style.BRIGHT}    ╔═══════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}      
{Fore.CYAN + Style.BRIGHT}    ║{Style.RESET_ALL}     {Fore.YELLOW + Style.BRIGHT}Telegram:{Style.RESET_ALL} {Fore.WHITE + Style.BRIGHT}t.me/airdrop3arn{Style.RESET_ALL}                     {Fore.CYAN + Style.BRIGHT}║{Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}    ║{Style.RESET_ALL}     {Fore.YELLOW + Style.BRIGHT}Github:{Style.RESET_ALL} {Fore.WHITE + Style.BRIGHT}github.com/Fl3xxRichie{Style.RESET_ALL}                 {Fore.CYAN + Style.BRIGHT}║{Style.RESET_ALL}      
{Fore.CYAN + Style.BRIGHT}    ╚═══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}      
                        {Fore.RED + Style.BRIGHT}Created with ❤️ by FlexxRichie{Style.RESET_ALL}
"""
    # Add a typing effect
    for line in banner.split('\n'):
        print(line, flush=True)
        time.sleep(0.05)  # Adjust speed of typing effect

    # Add some spacing after the banner
    print("\n")

if __name__ == "__main__":
    print_banner()