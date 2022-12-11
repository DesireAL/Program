import argparse
parser = argparse.ArgumentParser()
#parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('-f', '--foo', help='foo help')
args = parser.parse_args()

print(args)
