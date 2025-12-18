# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            for line_str in line.strip().split(): # Convert str to int
                num = int(line_str)

                if num > largest:
                    largest = num

    print(largest)
    return largest

if __name__ == "__main__":
    largest()