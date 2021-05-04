import json


def requirements(data):
    if len(data['thread']) >= 6:
        user = data['thread'][0]["userId"]
        same_user = True
        for y in data['thread']:
            if y["userId"] != user:
                same_user = False
        if same_user:
            return False
        return True


if __name__ == '__main__':
    f = open("ConvAI1.json", "r")
    text = f.readline()
    f.close()
    parsed = json.loads(text)

    print("Before: " + str(len(parsed)))
    f = open("ConvAI1formatted.txt", "w")
    f.write(json.dumps(parsed, indent=4))
    f.close()

    new_list = []
    for x in parsed:
        if requirements(x):
            new_list.append(x)

    print("After: " + str(len(new_list)))
    f = open("../ConvAI1trimmed.txt", "w")
    f.write(json.dumps(new_list, indent=4))
    f.close()
