from xmlrpc.server import DocCGIXMLRPCRequestHandler


def double_char(s):
    new_str = ''
    for i in s:
        new_str += i * 2
    return new_str

print(double_char('Hello World'))