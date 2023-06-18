import os

commands = [
    "go install github.com/hahwul/dalfox/v2@latest",
    "go install github.com/tomnomnom/waybackurls@latest",
    "go install github.com/eikehacker1/grepgy@latest",
    "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "go install github.com/KathanP19/Gxss@latest",
    "go install github.com/takshal/freq@latest",
    "go install -v github.com/tomnomnom/anew@latest"
]

for command in commands:
    os.system(command)

