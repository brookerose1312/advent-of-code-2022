## Part 1

# Read input
with open("day7input.txt") as f:
    cliOutput = f.readlines()


class File:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.sizeBelow = size


root = File(0)
index = 1
fileDict = {}
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
            fileDict[index] = File(index, parent=curr)
            curr.contents[dirname] = fileDict[index]
            index += 1
        # is a proper file
        else:
            size = int(line[0])
            filename = line[1]
            fileDict[index] = File(index, parent=curr, size=size)
            curr.contents[filename] = fileDict[index]
            index += 1

ans = 0
toVisit = [root]
visited = set()
while len(toVisit) > 0:
    file = toVisit[-1]
    # all subfiles (including directories) of current file
    for sub in file.contents.values():
        if sub.index not in visited:
            toVisit.append(sub)
            break
    # finally, deal with the current file
    else:
        file = toVisit.pop()
        visited.add(file.index)
        if file.parent is not None:
            file.parent.sizeBelow += file.sizeBelow
        if (file.sizeBelow <= 100000) and (len(file.contents) > 0):
            ans += file.sizeBelow

print(ans)


## Part 2

totalUsed = root.sizeBelow
totalFree = 70000000 - totalUsed
amountToDelete = 30000000 - totalFree

# find smallest directory to delete
part2Ans = root.sizeBelow
for index, file in fileDict.items():
    if (
        (len(file.contents) > 0)
        and (file.sizeBelow < part2Ans)
        and (file.sizeBelow >= amountToDelete)
    ):
        part2Ans = file.sizeBelow

print(part2Ans)
