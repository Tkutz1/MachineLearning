import json

def requirements(x):
    if len(x['thread']) >= 6:
        user = x['thread'][0]["userId"]
        sameuser = True
        for y in x['thread']:
            if y["userId"] != user:
                sameuser = False
        if sameuser == True:
            return False
        return True


if __name__ == '__main__':

    f = open("ConvAI1.json", "r")
    text = f.readline()
    f.close()
    parsed = json.loads(text)
    print("Before: " + str(len(parsed)))
    newlist = []
    for x in parsed:
        if requirements(x):
            newlist.append(x)

    print("After: " + str(len(newlist)))
    f2 = open("../ConvAI1trimmed.txt", "w")
    f2.write(json.dumps(newlist, indent=4))
    f2.close()
