from typing import Optional

STOP_STATUS_END = 0
STOP_STATUS_QUIT = 1

def get_multiline_input() -> (str, int):
    stop_status = STOP_STATUS_END
    lines = []
    while True:
        try:
            line = input()
            if line == 'END':
                stop_status = STOP_STATUS_END
                break
            if line == 'QUIT':
                stop_status = STOP_STATUS_QUIT
                break
            lines.append(line)
        except EOFError:
            stop_status = STOP_STATUS_END
            break
    return (lines, stop_status)

def main():
    while True:
        print("Enter text (type 'END' or Ctrl+D to finish):")
        input, stop_status = get_multiline_input()
        if stop_status == STOP_STATUS_QUIT or len(input) == 0:
            break
        num_lines = len(input)
        print("Number of lines entered:", num_lines)
    print('Exiting...')

if __name__ == "__main__":
    main()
