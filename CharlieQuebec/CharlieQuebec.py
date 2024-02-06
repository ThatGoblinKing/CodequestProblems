n_cases = int(input())
finalOutput = ""

EXPECTED_OUTPUT = "Charlie-Oscar-Delta-Echo Quebec-Uniform-Echo-Sierra-Tango\nRomeo-Oscar-Charlie-Kilo-Sierra\nLima-Oscar-Charlie-Kilo-Hotel-Echo-Echo-Delta"

icao = {'A': 'Alpha', 'B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel','I':'Indiana','J':'Julia','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu'}

for _ in range(n_cases):
    lines = int(input().rstrip())
    for i in range(lines):
        line = input().upper().rstrip()
        output = ""
        for char in line:
            if not char == " ":
                output += icao[char] + "-"
            else:
                output = output[:-1] + " "
        finalOutput += output[:-1] + '\n'
print(finalOutput.rstrip())