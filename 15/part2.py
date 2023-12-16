filename="input.txt"

with open(filename) as f:
    lines = f.readlines()


def hash_string(input):
    current_value = 0

    for v in input:
        ascii_code = ord(v)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value

def insert_label(label, focal_length, box):
    inserted = False
    for i, (box_label, box_focal_length) in enumerate(box):
        if box_label == label:
            box[i]=(label, focal_length)
            inserted = True
            break
    if not inserted:
        box.append((label, focal_length))

def delete_label(label, box):
    for i in range(len(box)):
        (box_label, box_focal_length) = box[i]
        if box_label == label:
            box.pop(i)
            break
            
            
sum = 0
boxes = {}
for l in lines:
    l = l.strip()
    if len(l) < 3:
        continue


    commands = l.split(",")
    for c in commands:

            
        if "=" in c:
            (label, focal_length) = c.split("=")
            box_id = hash_string(label)
            if box_id not in boxes:
                boxes[box_id] = []
            
            focal_length = int(focal_length)
            insert_label(label, focal_length, boxes[box_id])

        elif "-" in c:
            label = c.split("-")[0]
            box_id = hash_string(label)
            if box_id not in boxes:
                boxes[box_id] = []
                
            delete_label(label, boxes[box_id])

sum = 0
for box_id in range(256):
    if box_id not in boxes:
        continue
    focusing_power_box = 0
    for i, (label, focal_length) in enumerate(boxes[box_id]):
        focusing_power_lens = (1+box_id) * (i+1) * focal_length
        focusing_power_box += focusing_power_lens
        print(f"Lens {label} box {box_id} slot {i+1} focal {focal_length}")
    sum += focusing_power_box
    
print(f"{sum}")
