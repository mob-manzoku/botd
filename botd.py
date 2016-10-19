#!/usr/bin/env python3
import argparse
import yaml


def main():
    args = define_parsers()

    with open(args.f, "r") as f:
        conf = yaml.load(f)

    for i in conf["input"]:
        attr = "output_"
        class_name = "Output_"

        if i.get("output") == "self":
            attr += i.get("type")
            class_name += i.get("type")
        else:
            attr += i.get("output")
            class_name += i.get("output")

        out_modules = __import__("output_plugin", fromlist=[attr])
        out_module = getattr(out_modules, attr)
        out_class = getattr(out_module, class_name)
        o = out_class(i)
        print(o.__dict__)


def define_parsers():
    parser = argparse.ArgumentParser(description='botd',
                                     add_help=False)
    parser.add_argument('--help', action='help', help='help')
    parser.add_argument('-f', type=str, default="botd.yml",
                        help='Config file')

    return parser.parse_args()

if __name__ == "__main__":
    exit(main())
