import os

def run():
    print('Insert the widevine key from the console of chrome:\n')

    key = input("Key:\n")
    infile = input("Infile:\n")
    outfile = input("Outfile:\n")
    command = f'mp4decrypt --show-progress --key 1:{key} "{infile}" "{outfile}"'
    print(command)
    os.system(command)
    print('\n')
    print('Done:\n')
    again = input('Run again [Y/n]:').lower()
    if again == 'n':
        pass
    else:
        return run()


run()