import argparse
from .calc import add
from .utils.echo import echo


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    args = parser.parse_args()

    ans = add(args.x, args.y)
    echo(ans)
