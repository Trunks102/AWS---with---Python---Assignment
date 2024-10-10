import os

def search(search_txt, path):
    result = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()
                    if search_txt in content:
                        result.append(file_path)
    return result

search_text = "example"
directory_path = "path/to/directory"
search_result = search(search_text, directory_path)
print(search_result)