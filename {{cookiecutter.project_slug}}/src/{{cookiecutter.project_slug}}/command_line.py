import argparse
import python_package_template as p


def main():
    parser = argparse.ArgumentParser(
        description='python package template'
    )
    parser.add_argument('-v', '--version', action='version', version=f'{p.version}')
    parser.parse_args()


if __name__ == '__main__':
    main()
