# Advent of Code

Advent of Code automater.
To install locally `pip install -e .`
Run with `aoc --help`
Need to run aoc without -r og -s for relevant day the first time to set up directory and download files
Need to run with -r before you can run with -s
Need a .env file with `aoctoken`

## CLI functionallity

Download input file
Scrape problem description and put example into example file
Setup directory and template files
Submit answer
Run solution for specified day

## Commands

`aoc --help`

```
usage: aoc [-h] [-y YEAR] [-d DAY] [-s SUBMIT] [-r]

Automate AoC

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  Specify AoC year
  -d DAY, --day DAY     Specify which day to automate
  -s SUBMIT, --submit SUBMIT
                        Submit answer for specified day, 1 for part 1, 2 for part 2
  -r, --run             Run solution for specified day
```
