def validate_string(msg):
    if len(msg) <= 1:
        return msg
    else:
        msg = msg.rstrip(msg[-1])
        return msg

print(validate_string(input("Write you string here: ")))
