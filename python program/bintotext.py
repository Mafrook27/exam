
import magic

def identify_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    return file_type

file_path =  'source/binary.bin' 
print("File Type:", identify_file_type(file_path))
