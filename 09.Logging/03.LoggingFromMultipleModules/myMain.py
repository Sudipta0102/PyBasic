import logging
import myStuff
import myStuff2


def main():
    logging.basicConfig(filename='myMain.log', filemode='w', level=logging.INFO)
    logging.info('main starts')
    myStuff.func_do()
    myStuff2.func_am()
    logging.info('main ends')


if __name__ == '__main__':
    main()