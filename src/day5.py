from typing import List
class almanac(object):
    def __init__(self,input_table: List["almanac_entries"]) -> None:
        self.contents = {}
        for almanac in input_table:
            self.contents[almanac.name] = almanac

    def __str__(self) -> str:
        return str([str(x) for x in self.contents.values()])

    def search_contents(self,value,current,destination):
        if current == destination:
            return value
        else:
            current_almanac = self.contents[current]
            new_value = current_almanac.return_entry(value)
            target = current_almanac.target
            return self.search_contents(new_value,target,destination)

class almanac_entries(object):
    def __init__(self,input: list[list],name,target) -> None:
        self.map = {}
        for line in input:
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])
            for step in range(range_length):
                    self.map[source_range_start + step]=destination_range_start + step
        self.name = name
        self.target = target

    def return_entry(self,lookup:int) -> int:
        if lookup in self.map:
            return self.map[lookup]
        else:
            return lookup

    def __str__(self) -> str:
        return f"Almanac titled '{self.name}' which targets '{self.target}'"

def parse_input(data):
    almanac_list = []
    entries = []
    for rownum,row in enumerate(data):
        if rownum == 0:
            seedlist = row.split(": ")[1].split()
        elif rownum == 1:
            continue
        elif row == "" or rownum == len(data)-1:
            firstline = entries[0]
            firstlinesplit = firstline.split()
            firstlinesplitdirections = firstlinesplit[0].split("-")
            almanac_name = firstlinesplitdirections[0]
            almanac_target = firstlinesplitdirections[2]
            directions = [x.split() for x in entries[1:]]
            almanac_list.append(almanac_entries(directions,almanac_name,almanac_target))
            entries = []
        else:
            entries.append(row)
    return almanac_list,seedlist