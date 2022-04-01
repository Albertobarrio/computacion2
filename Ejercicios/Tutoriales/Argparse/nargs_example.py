import argparse

# nargs indica que va a consumir 3 parametros
#   ?: a single value, which can be optional
#   *: a flexible number of values, which will be gathered into a list
#   +: like *, but requiring at least one value
#   argparse.REMAINDER: all the values that are remaining in the command line

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, nargs='*', dest='origen')

# my_parser.add_argument('first', action='store')
# my_parser.add_argument('others', action='store', nargs=argparse.REMAINDER)

args = my_parser.parse_args()
print(vars(args))
# print('first = %r' % args.first)
# print('others = %r' % args.others)


