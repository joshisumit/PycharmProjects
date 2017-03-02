#from class_demo import Pet,Dog
from class_demo import *
#import class_demo

def withImportClass():
    # Before Running this method, Make sure import statement is like:
    # from class_demo import Pet
    print help('class_demo')
    mycat1=Pet("Sheru","Cat")
    print mycat1 # Prints the mycat instance by looking into __str__ method
    print mycat1.getName()


def withGeneralImport():
    # Before Running this method, Make sure import statement is like:
    # import class_demo
    mycat1=class_demo.Pet("Chenu","Cat")
    print mycat1
    print mycat1.getName()


def subclassDemo():
    mydog1=Dog("Maru",True)
    print isinstance(mydog1,Dog)
    print isinstance(mydog1,Pet)
    print mydog1
    print mydog1.getName()
    print mydog1.getSpecies()
    print mydog1.chaseCats()
    print '-'*10
    mypet1 = Pet('Hobbes', 'Cat')
    print isinstance(mypet1, Pet)
    print isinstance(mypet1, Dog)
    # print mypet1.chaseCats()
    # Calling this method will throw an error: AttributeError: Pet instance has no attribute 'chaseCats'
    # As Pet class has no chaseCats method()
    print mypet1.getName()
    print mypet1.getSpecies()
    print '-' * 10
    mycat1=Cat("bill",True)
    print isinstance(mycat1,Cat)
    print isinstance(mycat1,Pet)
    print mycat1.getName()
    print mycat1.getSpecies()
    print mycat1.hateDogs()

def main():
    '''Before Running this method, Make sure import statement is like:
    from class_demo import Pet'''

    #withImportClass()

    '''Before Running this method, Make sure import statement is like:
    from class_demo import Pet'''

    #withGeneralImport()

    '''For verifying inheritance'''
    subclassDemo()


if __name__ == '__main__':
    main()
