import argparse

# Podemos armar grupos donde dos opciones no pueden coexistir
# es decir es s o v
my_parser = argparse.ArgumentParser()
my_group = my_parser.add_mutually_exclusive_group(required=True)

my_group.add_argument('-v', '--verbose', action='store')
my_group.add_argument('-s', '--silent', action='store')

args = my_parser.parse_args()

print(args.verbose)
print(args.silent)