
# 1. Read the REAL content (not 0 bytes) in Binary mode ('rb')
with open('nature.jpg', 'rb') as src:
    data = src.read() 

# 2. Write the content in Binary mode ('wb')
with open('new_file_nature.jpg', 'wb') as dest:
    dest.write(data)

print("File copied successfully. You can open it now!")
