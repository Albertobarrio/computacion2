import argparse

# allow_abbrev: permite o no usar abreviaciones argumentos opcionales

cli_parser = argparse.ArgumentParser(allow_abbrev=False)
cli_parser.add_argument('--input',action='store',type=int,required=True)
cli_parser.add_argument('--id',action='store',type=int)

args = cli_parser.parse_args()
print(args.input)