import privacyscanner
import subprocess

with open('top-100.txt') as f: 
    lines = f.readlines()

for line in lines: 
    url = str("https://www." + line)
    command = ["privacyscanner", "scan"]
    command.append(url)
    command.append("-r")
    command.append(str("/home/ronghao/analisis_top-100/analisis_V71/" + line))
    subprocess.run(command)
