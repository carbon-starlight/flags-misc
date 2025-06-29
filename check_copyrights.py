import urllib.request
import re

urls = """
RU-SPE    https://commons.wikimedia.org/wiki/File:Flag_of_Saint_Petersburg.svg
RU-MOW    https://commons.wikimedia.org/wiki/File:Flag_of_Moscow,_Russia.svg

RU-YEV    https://commons.wikimedia.org/wiki/File:Flag_of_the_Jewish_Autonomous_Oblast.svg
"""

license_separator = "    "
for line in urls.splitlines():
    if line == "":
        continue
    code = None
    if re.match(r"^[A-Z][A-Z]-[A-Z]*", line):
        code = line.split()[0]
        line = line.split()[1]
    f = urllib.request.urlopen(line)
    contents = f.read()
    if code:
        line = code + "    " + line
    if """<td><span class="licensetpl_short">Public domain</span><span class="licensetpl_long">Public domain</span>""" in str(contents):
        print("\033[92mPD-RU\033[0m" + license_separator + line)
    else:
        if """This file is licensed under the <a href="https://en.wikipedia.org/wiki/en:Creative_Commons" class="extiw" title="w:en:Creative Commons">Creative Commons</a> <a href="//creativecommons.org/licenses/by-sa/3.0/deed.en" """ in str(contents):
            print("\033[31mBY-SA\033[0m" + license_separator + line)
        else:
            print("\033[31m?????\033[0m" + license_separator + line)
