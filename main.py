import requests, sys, re

"""
]------------------
]- https://yml.lol
]------------------
"""

def main(argv):
    if(len(argv) == 1):
        file_path = input("File path: ")
        output_file_path = input("Output file path: ")
    elif(argv[1] == "-h" or argv[1] == "--help" or argv[1] == "help"):
        print('python main.py "File path" -o "Output file path"')
    else:
        file_path = argv[1]
        output_file_path = argv[3]

    unchecked_file = open(file_path, "r+")
    unchecked = unchecked_file.read().splitlines()
    unchecked_file.close()

    output_file = open(output_file_path, "a+")

    for url in unchecked: 
        if("og:description" not in requests.get(url).text): continue
        print("gud")
        output_file.write(url+"\n")

    output_file.close()


if __name__ == "__main__":
    main(sys.argv)
