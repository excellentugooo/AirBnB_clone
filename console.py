#!/usr/bin/python3
""" Building the console """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command line class """
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

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

    def do_create(self, arg):
        """creates a new instance of the class
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{args[0]}")()
            print(new_obj.id)

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
