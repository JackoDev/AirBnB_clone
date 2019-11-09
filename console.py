#!/usr/bin/python3
import cmd

''' Class Console'''


class HBNBCCommand(cmd.Cmd):
    '''Command Cosole'''
    prompt = "(hbnb)"

    def emptyline(self):
        '''Goes to the next line'''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''End of file'''
        return True

if __name__ == '__main__':
    interprete = HBNBCCommand()
    interprete.cmdloop()