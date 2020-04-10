import sys
import re


WORDS_PER_SECOND = 20.0 / 60


def seconds(time):
    hours, minutes, seconds = time.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def duration(previous_starting_time, starting_time):
    return seconds(starting_time) - seconds(previous_starting_time)


def word_count(text):
    return len(re.split(r'\s+', text))


with open(sys.argv[1], 'rt') as f:
    previous_starting_time = None
    previous_text = None
    for line in f:
        line = line.strip()
        if line.startswith('Dialogue:'):
            columns = line.split(',', 10)
            starting_time = columns[1]
            text = re.sub(r'\\N', ' ', columns[9]).strip()
            if not text:
                continue
            if previous_text:
                if text.startswith(previous_text):
                    continue
                if previous_starting_time and duration(previous_starting_time, starting_time) < word_count(previous_text) / WORDS_PER_SECOND:
                    print('    {}  '.format(text))
                else:
                    print('\n{}\n\n  : {}  '.format(starting_time, text))
            else:
                print('\n{}\n\n  : {}  '.format(starting_time, text))
            previous_starting_time = starting_time
            previous_text = text
