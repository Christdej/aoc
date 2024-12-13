import argparse
import copy
import os
import re
import time
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests.exceptions import ConnectionError

ROOT_URL = "https://adventofcode.com"

TEMPLATE_HEADER = {
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "none",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0.1; MotoG4 Build/MPI24.107-55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36",
}


def give_intel_on_input(input_data):
    n_lines = len(input_data)
    min_line_length = len(input_data[0])
    max_line_length = len(input_data[0])
    n_digit_lines = 0
    n_alphabetic_lines = 0
    for line in input_data:
        length = len(line)
        if length < min_line_length:
            min_line_length = length
        if length > max_line_length:
            max_line_length = length

        if line.isdigit():
            n_digit_lines += 1

        if line.isalpha():
            n_alphabetic_lines += 1

    if n_lines == n_digit_lines:
        line_type = "digits"
    elif n_lines == n_alphabetic_lines:
        line_type = "alphabetic"
    else:
        line_type = "mix"

    L_COL = 30
    R_COL = 30

    example_lines = [
        (input_data[i] if len(input_data) > i else "").rjust(R_COL) for i in range(4)
    ]

    EXAMPLE_LINE_LENGTH = 40
    example_lines = [
        (line[:EXAMPLE_LINE_LENGTH] + "..") if len(line) > EXAMPLE_LINE_LENGTH else line
        for line in example_lines
    ]

    print("##############")
    print("Intel on input")
    print("##############")
    print(f"Number of lines: {n_lines}".ljust(L_COL), example_lines[0])
    print(f"Min line length: {min_line_length}".ljust(L_COL), example_lines[1])
    print(f"Max line length: {max_line_length}".ljust(L_COL), example_lines[2])
    print(f"Line type: {line_type}".ljust(L_COL), example_lines[3])


def setup_day(year, day):
    print("Setting up day")
    # Create year directory
    dirname = os.path.join(os.path.dirname(__file__), f"{year}")
    if not os.path.isdir(dirname):
        os.makedirs(dirname, exist_ok=True)

    # Create init file
    filename = os.path.join(dirname, "__init__.py")
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("")

    # Create day directory
    dirname = os.path.join(os.path.dirname(__file__), f"{year}", f"{day}")
    if not os.path.isdir(dirname):
        os.makedirs(dirname, exist_ok=True)

    # Create init file
    filename = os.path.join(dirname, "__init__.py")
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("")

    template_directory = os.path.join(os.path.dirname(__file__), "template/")
    # Create solution file
    filename = os.path.join(dirname, "solution.py")
    if not os.path.isfile(filename):
        template_solution = os.path.join(template_directory, "solution.py")
        with open(template_solution, "r") as template:
            with open(filename, "w") as file:
                for line in template:
                    file.write(line)

    # Create test file
    filename = os.path.join(dirname, "test_solution.py")
    if not os.path.isfile(filename):
        template_solution = os.path.join(template_directory, "test_solution.py")
        with open(template_solution, "r") as template:
            with open(filename, "w") as file:
                for line in template:
                    file.write(line)

    scrape_aoc_example(year, day)


def scrape_aoc_example(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    session = requests.Session()
    cookie = os.getenv("aoctoken")
    headers = {"session": cookie}

    try:
        response = session.get(url, cookies=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        example = soup.find("pre").text

        dirname = os.path.join(os.path.dirname(__file__), f"{year}", f"{day}")
        filename = os.path.join(dirname, "example.txt")
        with open(filename, "w") as file:
            file.write(example)
        print(f"Example for {year}-12-{day} saved to example.txt")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the example: {e}")


def download_input(year, day):
    print(f"Downloading input for year {year} day {day}")

    dirname = os.path.join(os.path.dirname(__file__), f"{year}", f"{day}")

    # Download input data
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    session = requests.Session()
    cookie = os.getenv("aoctoken")
    headers = {"session": cookie}
    try:
        # Create input file
        filename = os.path.join(dirname, "input.txt")
        if os.path.isfile(filename):
            raise RuntimeError(f"File {filename} already exists")
        response = session.get(url, cookies=headers)
        with open(filename, "w") as file:
            file.write(response.text)
        input_data = list(map(lambda line: line.strip(), open(filename, "r")))
        give_intel_on_input(input_data)
        print(f"Input for {year}-12-{day} downloaded")
    except ConnectionError:
        print(f"Could not download input data")


def submit_answer(year, day, part):
    # return
    print(f"Submitting answer for year {year} day {day} part {part}")
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    # /${year}/day/${day}/answer
    dirname = os.path.join(os.path.dirname(__file__), f"{year}", f"{day}")
    answer = open(os.path.join(dirname, f"part{part}.txt"), "r").read()

    global TEMPLATE_HEADER
    headers = copy.deepcopy(TEMPLATE_HEADER)
    cookie = os.getenv("aoctoken")
    headers["Cookie"] = "session=%s" % cookie
    session = requests.Session()
    # headers = {"session": cookie}
    # encoding_type = "utf-8"

    try:
        response = session.post(
            url,
            headers=headers,
            data={"level": part, "answer": answer},
        )
        text = response.text
        text = re.sub("<[^<]+?>", "", text)
        if "That's the right answer" in text:
            print("That's the right answer")
        elif "please wait" in text.lower():
            i = text.lower().find("please wait")
            j = text.find(".", i)
            print(text[i : i + (j - i)])
    except ConnectionError:
        print(f"Could not submit answer")


def main():
    load_dotenv()

    time_now = datetime.now()

    parser = argparse.ArgumentParser(prog="aoc", description="Automate AoC")
    parser.add_argument(
        "-y",
        "--year",
        help="Specify AoC year",
        dest="year",
        default=time_now.year,
    )
    parser.add_argument(
        "-d",
        "--day",
        help="Specify which day to automate",
        dest="day",
        default=time_now.day,
    )
    parser.add_argument(
        "-s",
        "--submit",
        help="Submit answer for specified day, 1 for part 1, 2 for part 2",
        dest="submit",
        default=0,
    )
    parser.add_argument(
        "-r",
        "--run",
        help="Run solution for specified day",
        action="store_true",
    )

    args = parser.parse_args()
    year = int(args.year)
    day = int(args.day)

    if args.run:
        os.system(f"python src/aoc/{year}/{day}/solution.py")
        exit()

    submit = int(args.submit)
    if submit == 1:
        submit_answer(year, day, 1)
        exit()
    if submit == 2:
        submit_answer(year, day, 2)
        exit()
    # Create the folder and files without requesting the input endpoint
    setup_day(year, day)

    start_time = datetime(year, 12, day, 6, 0, 0, 0)

    # Wait for the challenge to be released
    fastest_count_time = start_time - timedelta(minutes=1)
    faster_count_time = start_time - timedelta(minutes=5)
    fast_count_time = start_time - timedelta(hours=1)

    while time_now < start_time:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Waiting for challenge to be released at {start_time}")
        time_now = datetime.now()
        print("Time:", time_now)
        if time_now >= start_time - timedelta(minutes=1):
            sleep_time = 0.1  # Every tenths of a second
        elif time_now >= faster_count_time:
            sleep_time = 1  # Every second
        elif time_now >= fast_count_time:
            sleep_time = 10  # Every 10 seconds
        else:
            sleep_time = 60  # Every minute

        time.sleep(sleep_time)

    download_input(year, day)


if __name__ == "__main__":
    main()
