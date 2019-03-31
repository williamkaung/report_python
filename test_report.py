file = open('sample_log.log', 'r') # file opening as read mode
customer_ids = [] #declaring empty list for customer ids
sizes = [] # declaring empty list for sizes
for line in file: # started fetching file per line
    data = line.split( ) #spliting each line per white space
    data_length = len(data) #getting the length of splitted string
    if data_length > 0:
        customer_id_tmp = data[6].split(':') #customerId is now at position 6, so getting value by indexing to 6 and split by : 
        size_tmp = data[9].split(':')# it is same as customerId indexing
        customer_id = customer_id_tmp[1] # now customerId's format is Customer
        size = size_tmp[1] #same as above
        if not customer_id in customer_ids: #checking customer is in CustomerId list, it not add customerid and size
            customer_ids.append(customer_id)
            sizes.append(size)
        else: # if customer id already having in list
            index_of_customer_id = customer_ids.index(customer_id) # get the index of customerId
            value = sizes[index_of_customer_id] # get the value of size by customerid index
            sizes[index_of_customer_id] = int(value) + int(size)# replace the value of size by adding same customer id's size

for i in range(0, len(customer_ids)):# for looping by the length of customerIds list
    print(f"CustomerId : {customer_ids[index_of_customer_id]} Downloaded file size : {sizes[i]}") # then print
