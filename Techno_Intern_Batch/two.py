import json
import requests
import sys

path = sys.argv[1]

def get_dirs(path):
    list_dir = f"http://172.25.5.11:9870/webhdfs/v1/{path}?op=LISTSTATUS&user.name=hduser"
    page = requests.get(list_dir)
    if page.status_code == 200 and page.headers['Content-type'] == 'application/json':
        try:
            content = json.loads(page.text)
            print("\n\n")
            print("__"*30)
            print("\n\n")
            for each_dir in content["FileStatuses"]['FileStatus']:
                print("File Name: ", each_dir['pathSuffix'])
                print("Type of File: ", each_dir['type'])
                print("Owner of File: ", each_dir['owner'])
                print("Group of File: ", each_dir['group'])
                print("Permission of File: ", each_dir['permission'])
                print("\n\n")
                print("__"*30)
                print("\n\n")
                
        except Exception as e:
            print("!!Error!!", e)
    else:
        print("!!Error code {page.status_code}!! Something nesty is going on")
        
get_dirs(path)
