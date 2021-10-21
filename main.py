from random import randint
import argparse
import datetime as dt
import re




parser = argparse.ArgumentParser(description="Generates vcf files")
parser.add_argument("prefix", help="Common prefix to all contact names to create")
parser.add_argument("n", type=int, help="Number of contacts to contain within the file")
parser.add_argument("i", type=int, nargs='?', default=1, help="Within the names of the contacts, the number from which it starts to identify them 1 by 1")




def parse_filename(filename):
    rep = {"-": "_", ":": "_", ".": "_", " ": "_"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    filename = str(filename)
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], filename)

def get_random_number(n_digit):
    number = str(randint(7, 9))
    for i in range(n_digit-1):
        digit = randint(0, 9)
        number += str(digit)
    return number

def generate_contact(name, number):
    return f"BEGIN:VCARD\nVERSION:2.1\nN:;{name};;;\nFN:{name}\nTEL;CELL:+569{number}\nEND:VCARD\n"

def generate_vcf(filename,  prefix, n, i=1):
    vcf = ""
    lenN = len(str(n))
    for x in range(1, n+1):
        name = prefix + f"%0{lenN}d"%x
        number = get_random_number(n_digit=8)
        vcf += generate_contact(name, number)
    with open(filename, 'w') as file:
        file.write(vcf)




if __name__ == "__main__":
    args = parser.parse_args()
    
    filename = parse_filename(dt.datetime.now()) + '.vcf'
    generate_vcf(filename, args.prefix, args.n, args.i)