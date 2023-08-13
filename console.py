#!/usr/bin/python3
"""command interpreter cmd module"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """HBNB command class"""
    prompt = '(hbnb) '

    def do_EOF(self):
        """Handles end of file"""
        return True

    def help_EOF(self):
        """documentation for EOF"""
        pass

    def do_quit(self, arg):
        '''<Quit> Command To Exit The Program'''
        return sys.exit(1)

    def help_quit(self):
        """docs for quit syntax"""
        print('quit to exit')

    # shoercuts
    # do_q = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
