## Part 1

# Read input
with open("day6input.txt", "r", encoding="utf-8") as f:
    buffer = f.read()

# set up window
packet_marker_buffer = ""
# set up marker
start_of_packet = 0

for char_index, char in enumerate(buffer):
    if len(packet_marker_buffer) < 4:
        packet_marker_buffer += char
        continue
    if len(packet_marker_buffer) == 4:
        if len(set(packet_marker_buffer)) == len(packet_marker_buffer):
            start_of_packet = char_index
            break
        else:
            packet_marker_buffer = packet_marker_buffer[1:] + char

print(start_of_packet)

## Part 2

# set up window
message_marker_buffer = ""
# set up marker
start_of_message = 0

for char_index, char in enumerate(buffer):
    if len(message_marker_buffer) < 14:
        message_marker_buffer += char
        continue
    if len(message_marker_buffer) == 14:
        if len(set(message_marker_buffer)) == len(message_marker_buffer):
            start_of_message = char_index
            break
        else:
            message_marker_buffer = message_marker_buffer[1:] + char

print(start_of_message)
