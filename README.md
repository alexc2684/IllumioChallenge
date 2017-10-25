Illumio Coding Assignment by Alex Chan

After reading the assignment, I knew that one of the most important problems I needed to handle was efficient rule storage and lookup. To accomplish this, I used dictionaries, which have O(1) lookup time. To avoid repetitive lookups, I implemented a nested dictionary.

Another tradeoff I had to decide on was the type I was storing each port and IP address. I decided to keep the types as strings rather than ints. This allowed me to store both the single number and ranges as the same data type. While I had to give up the time it takes to convert strings to ints, this only occurs for only one port and one IP address value at each accept_packet call, the overall runtime would remain fast.

For testing, I tested the standard cases given, as well as ensured that both single value and ranged values all worked (making sure to be inclusive in the ranges). I also tested for incorrect parameters, and the case where there was a repeat port. This case was tested and also added to the test.csv file I have attached.

I would be really interested in working for the Data Team. I've never worked with data in a cyber security setting, and it seems really interesting how the team integrates network data with data from the Policy Compute Engine. I would also pick the Policy Team as my second choice. Thank you!
