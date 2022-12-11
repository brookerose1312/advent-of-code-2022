## Part 1

# Read input
with open("day7input.txt", "r", encoding="utf-8") as f:
    cliOutput = f.readlines()


class File:
    """A class that represents a file inside of a filesystem"""

    def __init__(self, incoming_index, parent=None, incoming_size=0):
        self.index = incoming_index
        self.parent = parent
        self.contents = {}
        self.size = incoming_size
        self.size_below = incoming_size


root = File(0)
index = 1
file_dict = {}
curr = root
for line in cliOutput:
    # get cli line and split into parts
    line = line.strip().split(" ")
    # command
    if line[0] == "$":
        # only look at cd command
        if line[1] == "cd":
            # go to parent
            if line[2] == "..":
                curr = curr.parent
            # go to new dir
            else:
                dirname = line[2]
                if dirname == "/":
                    curr = root
                else:
                    # subdirectory so should be contained in curr
                    curr = curr.contents[dirname]
    # output
    else:
        # is a dir
        if line[0] == "dir":
            dirname = line[1]
            file_dict[index] = File(index, parent=curr)
            curr.contents[dirname] = file_dict[index]
            index += 1
        # is a proper file
        else:
            size = int(line[0])
            filename = line[1]
            file_dict[index] = File(index, parent=curr, incoming_size=size)
            curr.contents[filename] = file_dict[index]
            index += 1

ans = 0
to_visit = [root]
visited = set()
while len(to_visit) > 0:
    file = to_visit[-1]
    # all subfiles (including directories) of current file
    for sub in file.contents.values():
        if sub.index not in visited:
            to_visit.append(sub)
            break
    # finally, deal with the current file
    else:
        file = to_visit.pop()
        visited.add(file.index)
        if file.parent is not None:
            file.parent.size_below += file.size_below
        if (file.size_below <= 100000) and (len(file.contents) > 0):
            ans += file.size_below

print(ans)


## Part 2

total_used = root.size_below
total_free = 70000000 - total_used
amount_to_delete = 30000000 - total_free

# find smallest directory to delete
part_two_ans = root.size_below
for index, file in file_dict.items():
    if (
        (len(file.contents) > 0)
        and (file.size_below < part_two_ans)
        and (file.size_below >= amount_to_delete)
    ):
        part_two_ans = file.size_below

print(part_two_ans)
