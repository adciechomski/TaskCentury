from app.file_grabber.get_file_from_path import GetFileFromPath

def create_file_grabber():
    path = get_resource_path()
    if "http" in path:
        print("Program is not getting files on internet yet, to get local file.")
        exit()    

    file_grabber = GetFileFromPath(resource_location=path)
    return file_grabber


def get_resource_path():
    resource_location = input("Welcome to file data loader... /n Provide path to data source: ")
    print(resource_location)
    return resource_location