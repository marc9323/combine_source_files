# Author: Marc D. Holman
# Date: April 2, 2025

#  Concatenate project files for easy feeding to AI nmodel

import os
import re


def remove_comments(file_content):
    """
    Remove all block and line comments from 'file_content'
    :param file_content:
    :return:
    """
    no_block_comments = re.sub(r'/\*.*?\*/', '', file_content, flags=re.DOTALL)
    no_line_comments = re.sub(r'//.*', '', no_block_comments)

    #  Split into lines and filter out empty or whitespace only lines
    lines = no_line_comments.splitlines()
    cleaned_lines = [line for line in lines if line.strip()]

    #  Rejoin the remaining lines with newline
    return "\n".join(cleaned_lines) + "\n"


def combine_cpp_and_h_files(source_dir="src", output_file="combined_files.txt", cut_comments=True):
    """
    Combines the contents of all .cpp and .h files found under 'source_dir'
    into a single file named 'output_file.txt'
    :param source_dir:
    :param output_file:
    :return:
    """
    # list to hold the paths of all .cpp and .h files
    file_paths = []

    #  walk through the directory tree to find .cpp and .h files
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.endswith(".cpp") or filename.endswith(".h") or filename.endswith(".hpp"):
                file_paths.append(os.path.join(root, filename))

    #  sort the collected file paths (optional, for consistent ordering)
    file_paths.sort()

    #  Open the output file in write mode
    with open(output_file, "w", encoding="utf-8") as outfile:
        for path in file_paths:
            #  write a header to mark the beginning of each file
            outfile.write(f"//==== Start of file: {path} ====\n\n")
            #  read the file content and write it to the output file
            with open(path, "r", encoding="utf-8") as infile:
                if cut_comments:
                    outfile.write(remove_comments(infile.read()))
                else:
                    outfile.write(infile.read())
            # write a footer to mark the end of each file
            outfile.write(f"\n\n// ==== End of file: {path} ==== \n\n")

    print(f"Combined {len(file_paths)} files into '{output_file}'.")


if __name__ == "__main__":
    #  Call with default arguments
    combine_cpp_and_h_files('J:\\0Dave\\RoxZip\\RoxZip\\src', 'combined_output.txt')
