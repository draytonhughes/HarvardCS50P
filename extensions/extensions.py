# Gather file name

filename = input("File Name: ")

#split off the file type
trimmed_file = filename.strip()
filename_lower = trimmed_file.lower()
split_result = filename_lower.split('.')

if len(split_result) > 1:
    filetype = split_result[-1]
else:
    filetype = "application/octet-stream"

# check file type and print appropriate answer

match filetype:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
