#!/usr/bin/python3
""" Building the console """

import cmd


class HBNBCommand(cmd.Cmd):
    """ command line class """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ quit the command line
        """
        return True

    def do_EOF(self, args):
        """ end of file
        """
        return True

    def emptyline(self):
        """ return an empty line
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
