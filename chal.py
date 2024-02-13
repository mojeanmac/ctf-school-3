#! /usr/bin/python3
#-*- coding:utf-8 -*-
from sys import modules

def main():
    modules.clear()
    del modules
    __builtins__.__dict__.clear()
    __builtins__ = None

    print("RUN")
    text = input('>>> ')
    for keyword in ['eval', 'exec', 'import', 'open', '__', 'read', 'system', 'write']:
        if keyword in text:
            print("No!!!")
            return;
    else:
        exec(text)
if __name__ == "__main__":
    main()
