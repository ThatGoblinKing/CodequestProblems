from sys import stdin
from contextlib import redirect_stdout
from io import StringIO
import string


n_cases = int(stdin.readline()) #Takes users input 
finalOutput = ""

EXPECTED_OUTPUT = "Charlie-Oscar-Delta-Echo Quebec-Uniform-Echo-Sierra-Tango\nRomeo-Oscar-Charlie-Kilo-Sierra\nLima-Oscar-Charlie-Kilo-Hotel-Echo-Echo-Delta"

icao = {'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'Indiana',
        'J': 'Julia',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'Xray',
        'Y': 'Yankee',
        'Z': 'Zulu'}

f = StringIO()
with redirect_stdout(f):
    for _ in range(n_cases):
        sub_cases = int(stdin.readline().rstrip())
        for i in range(sub_cases):
            output = ""
            line = stdin.readline().upper().rstrip()
            for char in line:
                if char != " ":
                    output += icao[char] + "-"
                else:
                    output = output[:-1] + " "
            print(output[:-1].strip())
s = f.getvalue()
print(s.strip())
print(s == EXPECTED_OUTPUT)