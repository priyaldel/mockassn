try:
    with open('python-notes.txt','r',encoding='utf-8') as source_file:
        file_contents = source_file.read()
    
    with open('destination.txt','w',encoding='utf-8') as destination_file:
        destination_file.write(file_contents)
        destination_file.flush()
        
    print("File copied successfully")
except FileNotFoundError:
    print("Source Missing")
except Exception as e:
    print(f"An error occurred: {str(e)}")
