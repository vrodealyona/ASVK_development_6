import cowsay
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--eyes', type=str, default='oo', help='Eyes for the first cow')
parser.add_argument('-t', '--tongue', type=str, default='  ', help='Tongue for the first cow')
parser.add_argument('-f', '--cowfile', type=str, default='default', help='Cowfile for the first cow')
parser.add_argument("-W", "--width", type=int, default=40)

parser.add_argument('message1', type=str, help='Message for the first cow')

parser.add_argument('-E', type=str, default='oo', help='Eyes for the second cow')
parser.add_argument('-N', type=str, default='  ', help='Tongue for the second cow')
parser.add_argument('-F', type=str, default='default', help='Cowfile for the second cow')

parser.add_argument('message2', type=str, help='Message for the second cow')

args = parser.parse_args()
cow1 = cowsay.cowsay(args.message1,
        cow=args.cowfile,
        eyes=args.eyes,
        tongue=args.tongue
        )

cow2 = cowsay.cowsay(args.message2, cow=args.F,
        eyes=args.E,
        wrap_text=args.N)
ad = (max(len(cow1.split('\n')), len(cow2.split('\n'))) - min(len(cow1.split('\n')), len(cow2.split('\n')))) * [""]
cow1 = cow1.split('\n')
cow2 = cow2.split('\n')
if len(cow1) <  len(cow2):
        cow1 = ad + cow1
else:
        cow2 = ad + cow2
m = max([len(i) for i in cow1])
for line1, line2 in zip(cow1, cow2):
        print(line1 + (m - len(line1)) * ' ' + line2)
