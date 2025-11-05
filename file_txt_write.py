import io
import os
import tempfile

my_file = os.path.join('data', 'my_file.txt')

#with open(my_file, 'a') as f:  #'a' - append to end of file
# with open(my_file, 'w') as f: #'w' - overwrite
#     f.write('hello world\n')
#     f.write('This should be the 2nd line\n')
#     f.write('This should be the 3rd line\n')

f = open(my_file, 'w')
f.write('hello world\n')
f.write('This should be the 2nd line\n')
f.flush()
f.write('This should be the 3rd line\n')
f.close()

#print(io.DEFAULT_BUFFER_SIZE)

tmp_file = tempfile.NamedTemporaryFile()
print(tmp_file.name)
with open(tmp_file.name, 'w') as f:
    f.write('hello world\n')
    f.write('This should be the 2nd line\n')
