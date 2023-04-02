# python3
'''
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result
    
'''
# uzdevums izpildīts ar dictionary palīdzību :(
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

#if __name__ == '__main__':
#    write_responses(process_queries(read_queries()))