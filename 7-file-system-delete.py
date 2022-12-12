class Directory:
    def __init__(self, name, parent=None):
        self.dir_name = name
        self.parent_dir = parent
        self.subdirs = []
        self.size = 0

    def add_dir(self, dir):
        self.subdirs.append(dir)

    def total_size(self):
        current_subdirs = [x for x in self.subdirs]
        total_size = self.size
        while current_subdirs != []:
            for subdir in current_subdirs:
                # print(f"working subdir {subdir.dir_name}")
                current_subdirs.remove(subdir)
                total_size += subdir.total_size()
        # print(f"final size {size}")
        return total_size


def setup_files_dir():
    dirs = []
    with open("inputs/7.txt", "r") as file:
        for line in file.readlines():
            if "$" in line:
                command = line.strip().replace("$ ", "").split(" ")
                # print(command)
                if command == ["ls"]:
                    continue
                else:
                    if command[1] == "..":
                        current_dir = current_dir.parent_dir
                    elif command[1] == "/":
                        current_dir = Directory(command[1])
                        dirs.append(current_dir)
                    else:
                        for dir in current_dir.subdirs:
                            if dir.dir_name == command[1]:
                                current_dir = dir
            else:
                if "dir" in line:
                    # print(f"Current dir: {current_dir}, {dirs[current_dir]['dirs']}")
                    dir_name = line.replace("dir ", "").strip()
                    dir = Directory(dir_name, current_dir)
                    current_dir.add_dir(dir)
                    dirs.append(dir)
                    # print(
                    # f"Current dir after: {current_dir}, {dirs[current_dir]['dirs']}"
                    # )
                elif int(line[0]) in range(10):
                    # print(
                    #     f"Current dir size: {current_dir}, {dirs[current_dir]['size']}"
                    # )
                    size = int(line.split(" ")[0])
                    # print(size)
                    current_dir.size += size
                    # print(f"After dir size: {current_dir}, {dirs[current_dir]['size']}")
    return dirs


dirs = setup_files_dir()
# print(f"initial: {[x.dir_name for x in dirs]}")
delete_dir_total_size = 0
for dir in dirs:
    # print(f"TOP LEVEL DIR {dir.dir_name} with {len(dir.subdirs)} subdirs ")
    if dir.dir_name == "/":
        tl_dir_size = dir.total_size()
        space_needed = 30000000 - (70000000 - tl_dir_size)
        print(f"Top level dir size: {tl_dir_size}")
        print(f"Space needed: {space_needed}")
        delete_dir_total_size = 30000000
        continue
    cd_size = dir.total_size()
    print(f"TOP LEVEL DIR {dir.dir_name} with total size {cd_size} ")
    if cd_size >= space_needed and cd_size < delete_dir_total_size:
        delete_dir_total_size = cd_size

print(delete_dir_total_size)
