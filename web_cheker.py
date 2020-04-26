# This program checks the presence of
# targeted string in web pages content
# whose URLs are inputted.
import requests
import sys


def url_check_function(string, web_page_url):
    """This function tests if target string exist in inputted URL's
    Web Page content.  This function requires 2 parameters:
        "string" - your target string;
        "web_page_url" - your Web Page's URL.
    """
    try:
        content = requests.get(web_page_url)  # Python requests.Response Object
    except Exception as e:
        print(f'\nInputted URL " {web_page_url} " isn\'t match'
              f' any URL in the WEB.' + '\n' + str(e))
        return False
    detected: bool = string in content.text
    content.close()  # Closes the connection to the server.
    return detected


def write_into_file(file_name, item):
    """This function writes item into file.
    This function requires 2 parameters:
        "file_name" - the name of destination file
        "item" - item to write in. 
    """
    with open(file_name, 'a') as f:
        f.write(item)


def update_progress_2(job_title, i, max_i):
    """It's progress bar function.
    This function requires 3 parameters:
        "job_title" - the name of running process;
        "i" - the iterator;
        "max_i" - the length of iterable. 
    """
    length = 50  # Modify this to change the progress bar length.
    progress = i/max_i      # The process's progress.
    block = int(round(length*progress))
    msg = '\r{0}: [{2}] line: {1},  {3}%'.format(job_title,
                                    i,
                                    '$'*block + '-'*(length-block),
                                    round(progress*100, 1))
    if progress >= 1:
        msg += ' DONE!\r\n'
    sys.stdout.write(msg)
    sys.stdout.flush()

 
# Input source file's name.
source_file: str  = input("Please input source file's name: ")
print(f"Source file's name is: {source_file}")

# Read URLs from source file into list.
url_list = []
with open(source_file, 'r') as f:
    for url in f:
        url_list.append(url)
url_list_length = len(url_list)
print(f'URLs list length is: {str(url_list_length)}')

# This loop allows to check more then one target string.
check_target_string = 'Y'
while check_target_string == 'Y' or check_target_string == 'y':
    target_string = input('Please input your target string: ')
    print(f'Your target string is: {target_string}')

    # Write target string and URLs in file: truly.txt
    write_into_file('truly.txt', f'\n"{target_string}"\n')
    for count, url in enumerate(url_list):
        result = url_check_function(target_string, url)
        if result: write_into_file('truly.txt', url)
        update_progress_2('Job progress', count, url_list_length)
    
    update_progress_2('Job progress', url_list_length, url_list_length)
    check_target_string = input('Would you like to check' + 
                                ' another target string (Y/N)? ')

print('The result is in the "truly.txt" file. Look into it please.')
input('Push "Enter" to FINISH: ')
