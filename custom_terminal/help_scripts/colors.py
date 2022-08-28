def colormessage(message, color, brigthness = 0):
    ret = ""
    if color == 'red':
        ret += '\u001b[31'
    elif color == 'black':
        ret += '\u001b[30'
    elif color == 'green':
        ret += '\u001b[32'
    elif color == 'yellow':
        ret += '\u001b[33'
    elif color == 'blue':
        ret += '\u001b[34'
    elif color == 'magenta':
        ret += '\u001b[35'
    elif color == 'cyan':
        ret += '\u001b[36'
    elif color == 'white':
        ret += '\u001b[37'

    if brigthness == 0:
        ret += 'm'
    else:
        ret += ';{}m'.format(brigthness)

    return '{}{}{}'.format(ret, message, '\u001b[0m')
