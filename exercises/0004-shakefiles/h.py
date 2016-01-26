import os, glob

file_pattern = os.path.join('tempdata', '**', '*')
file_names = glob.glob(file_pattern)

all_line_count = 0
all_nonblank_line_count = 0
for file_name in file_names:

    with open(file_name, 'r') as txt_file:
        line_count = 0
        nonblank_line_count = 0
        for line in txt_file:
            line_count += 1
            if line.strip(): # I.e., line.strip() isn't empty
                nonblank_line_count += 1

    print(file_name, 'has',
          nonblank_line_count, 'non-blank lines out of',
          line_count, 'total lines')
    all_line_count += line_count
    all_nonblank_line_count += nonblank_line_count

print('All together, Shakespeare\'s',
      len(file_names), 'text files have:')
print(all_nonblank_line_count, 'non-blank lines out of',
      all_line_count, 'total lines')
