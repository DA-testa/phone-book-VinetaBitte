# python3
class QueryHash:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for i in range(bucket_count)]

    def hash_function(self, s):
        hash_value = 0
        for c in reversed(s):
            hash_value = (hash_value * 263 + ord(c)) % self.bucket_count
        return hash_value
    
    def add(self, tel_number, tel_name):
        hashed = self.hash_function(str(tel_number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == tel_number:
                bucket[i][1] = tel_name
                break
        else:
            bucket.append([tel_number, tel_name])
    
    def delete(self, tel_number):
        hashed = self.hash_function(str(tel_number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == tel_number:
                bucket.pop(i)
                

    def find(self, tel_number):
        hashed = self.hash_function(str(tel_number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == tel_number:
                return bucket[i][1]
        return "not found"

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries(n):
    m = n
    return [Query(input().split()) for i in range(m)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    #contacts = []
    hash = QueryHash(len(queries))
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            tel_number = cur_query.number
            tel_name = cur_query.name
            hash.add(tel_number,tel_name)
        # otherwise, just add it
        elif cur_query.type == 'del':
           tel_number = cur_query.number
           hash.delete(tel_number)
        elif cur_query.type == 'find':
            tel_number = cur_query.number
            response = hash.find(tel_number)
            result.append(response)
    return result
    
'''
# uzdevums ar dictionary palīdzību
n = int(input())
phonebook_dict = {}
responses = []

for i in range(n):
    current_query = input().split()
    command = current_query[0]
    if command == 'add':
        phonebook_dict[current_query[1]] = current_query[2]
    elif command == 'del':
        if current_query[1] in phonebook_dict:
            del phonebook_dict[current_query[1]]
    elif command == 'find':
        if current_query[1] in phonebook_dict:
            responses.append(phonebook_dict[current_query[1]])
        else:
            responses.append("not found")
for i in responses:
    print(i)
'''

if __name__ == '__main__':
    n = int(input())
    write_responses(process_queries(read_queries(n)))