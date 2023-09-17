#!/usr/bin/python3
""" Building the console """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command line class """
    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"]

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
        elif len(args) == 1:
            new = eval(f"{args[0]}")()
            print(new.id)
            storage.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Show an Instance of Model base on its ModelName and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Show an Instance of Model base on its ModelName and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Retrieve all instances: eg.
        $ all
        $ all MyModel
        if MyModel is passed returns only instances of MyModel"""
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print([str(v) for k, v in storage.all().items()
                  if k.startswith(args[0])])
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """Updates an instance base on its id eg
        $ update Model id field value
        Throws errors for missing arguments"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            dic_t = storage.all()[key]

            attr_val = args[3]
            attr_nam = args[2]
            if attr_val[0] == '"':
                attr_val = attr_val[1:-1]

            if hasattr(dic_t, attr_nam):
                typ = type(getattr(dic_t, attr_nam))
                if typ in [str, float, int]:
                    attr_val = typ(attr_val)
                    setattr(dic_t, attr_nam, attr_val)
            else:
                setattr(dic_t, attr_nam, attr_val)
            storage.save()

    def default(self, arg):
        args = arg.split('.')
        if args[0] in self.__classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                count = [v for k, v in storage.all().items()
                         if k.startswith(args[0])]
                print(len(count))
            elif args[1].startswith("show"):
                id_show = args[1].split('"')[1]
                self.do_show(f"{args[0]} {id_show}")
            elif args[1].startswith("destroy"):
                id_destroy = args[1].split('"')[1]
                self.do_destroy(f"{args[0]} {id_destroy}")
            elif args[1].startswith("update"):
                parse = args[1].split('(')
                parse = parse[1].split(')')
                if '{' in parse[0]:
                    parse = parse[0].split(", {")
                    id_update = parse[0].strip('"')
                    new_dict = '{' + parse[1]
                    new_dict = (eval(new_dict))

                    for key, val in new_dict.items():
                        self.do_update(f"{args[0]} {id_update} {key} {val}")
                else:
                    parse = parse[0].split(', ')

                    id_update = parse[0].strip('"')
                    at_nam = parse[1].strip('"')
                    at_val = parse[2].strip('"')
                    self.do_update(f"{args[0]} {id_update} {at_nam} {at_val}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
