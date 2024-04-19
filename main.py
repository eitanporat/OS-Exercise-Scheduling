from parse import parse_file
from strategy.fcfs import FirstComeFirstServe
from strategy.lcfs import LastComeFirstServePreemptive, LastComeFirstServeNonPreemptive
from strategy.rr import RoundRobin
from strategy.sjf import ShortestJobFirst
from argparse import ArgumentParser, FileType

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument('file', type=str, nargs='+')
    args = argument_parser.parse_args()

    for input_file in args.file:
        print(f"\nOutput for {input_file}:")
        strategies = [FirstComeFirstServe(), LastComeFirstServeNonPreemptive(), LastComeFirstServePreemptive(),
                    RoundRobin(), ShortestJobFirst()]

        for strategy in strategies:
            processes = parse_file(input_file)
            strategy.execute(processes)
            strategy.print()