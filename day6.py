## Part 1

# Read input
with open("day6input.txt") as f:
    buffer = f.read()

# set up window
packetMarkerBuffer = ""
# set up marker
startOfPacket = 0

for charIndex in range(len(buffer)):
    char = buffer[charIndex]
    if len(packetMarkerBuffer) < 4:
        packetMarkerBuffer += char
        continue
    if len(packetMarkerBuffer) == 4:
        if len(set(packetMarkerBuffer)) == len(packetMarkerBuffer):
            startOfPacket = charIndex
            break
        else:
            packetMarkerBuffer = packetMarkerBuffer[1:] + char

print(startOfPacket)

## Part 2

# set up window
messageMarkerBuffer = ""
# set up marker
startOfMessage = 0

for charIndex in range(len(buffer)):
    char = buffer[charIndex]
    if len(messageMarkerBuffer) < 14:
        messageMarkerBuffer += char
        continue
    if len(messageMarkerBuffer) == 14:
        if len(set(messageMarkerBuffer)) == len(messageMarkerBuffer):
            startOfMessage = charIndex
            break
        else:
            messageMarkerBuffer = messageMarkerBuffer[1:] + char

print(startOfMessage)