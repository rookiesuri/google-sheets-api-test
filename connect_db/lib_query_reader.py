####query reader



def query_reader(filename_in):
    inst= open(filename_in,'r')
    out_query = inst.read().replace('\n',' ')
    return out_query


input_file="C:\\Users\\soori\\Desktop\\client_secret\\New folder\\query_test.sql"
z=query_reader(input_file)
print z
