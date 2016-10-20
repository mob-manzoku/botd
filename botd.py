#!/usr/bin/env python3
import argparse
import yaml


def main():
    args = define_parsers()
    outputs = {}

    with open(args.f, "r") as f:
        conf = yaml.load(f)

    # Create instances
    instances = {}

    for o in conf["output"]:
        outputs[o.get("name")] = o

    for i in conf["input"]:
        attr = "output_"
        class_name = "Output_"

        attr += outputs[i.get("output")].get("type")
        class_name += outputs[i.get("output")].get("type")

        out_modules = __import__("output_plugin", fromlist=[attr])
        out_module = getattr(out_modules, attr)
        out_class = getattr(out_module, class_name)

        instances[i['name']] = {
            'output': out_class(outputs[i.get("output")])
        }

    for i in instances:
        instances[i]['output'].send("aaa")


def define_parsers():
    parser = argparse.ArgumentParser(description='botd',
                                     add_help=False)
    parser.add_argument('--help', action='help', help='help')
    parser.add_argument('-f', type=str, default="botd.yml",
                        help='Config file')

    return parser.parse_args()

if __name__ == "__main__":
    exit(main())
