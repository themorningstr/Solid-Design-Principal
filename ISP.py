#ISP :- Interface Segregation Principal

from abc import abstractmethod

class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError



class MutliFunctionalPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass



class OldFashionedPrinter(Machine):
    def print(self, document):
        #ok
        pass

    def fax(self, document):
        #do nothing
        pass

    def scan(self, document):
        """Not Implemented!"""
        #do nothing
        raise NotImplementedError("Printer Cannot Scan!")




####

class Printer:

    @abstractmethod
    def print(self, document):
        pass


class Scanner:

    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def fax(self, document):
        pass


class MultiFunctionalDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class MultiFucntionalMachine(MultiFunctionalDevice):

    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    
    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
        





