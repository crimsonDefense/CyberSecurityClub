# Stephen
# Carve out every jpeg within a file 
import os
 
# put name of file
file_size = os.path.getsize('Candidates.pdf')
print("File Size is :", file_size, "bytes")

file=open("Candidates.pdf","rb")
magic_bytes = b'\xff\xd8\xff\xe0'
end_bytes = b'\xff\xd9'
image_num = 0
name = "image_found_"
ext = ".jpeg"
jpeg = False

for i in range(0, file_size):
    position = file.seek(i, 0)

    if(jpeg == False):
        position_header = position
        header = file.read(4)
        if (header == magic_bytes):
            print("new image detected")
            jpeg = True
    else:
        position_footer = position + 2
        footer = file.read(2)
        if(footer == end_bytes):
            print("Found end image. Writing image to new file")
            file_size = position_footer - position_header
            print(file_size)
            jpeg = False
            
            # Create new file to wriet to in binary
            image_name = name + str(image_num) + ext 
            new_image = open(image_name, "wb")
            image_num += 1

            file.seek(position_header, 0)
            data_of_image = file.read(file_size)
            new_image.write(data_of_image)
            file.seek(i, 0)
            new_image.close()
    
        

file.close()