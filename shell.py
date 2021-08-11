import privacyscanner
import subprocess

with open('top-50-Category.txt') as f: 
    lines = f.readlines()

for line in lines: 
    url = str("https://www." + line)
    command = ["privacyscanner", "scan"]
    command.append(url)
    command.append("-r")
    command.append(str("/home/ronghao/analisis_top-100/TOP-50-SPAIN-CATEGORIA/" + line))
    subprocess.run(command)
