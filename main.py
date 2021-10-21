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

def generate_vcf():
    pass




if __name__ == "__main__":
    args = parser.parse_args()
    
    print(parse_filename(dt.datetime.now()))
    
    generate_vcf()