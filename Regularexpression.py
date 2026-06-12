
# 1 search first match...re.search()

# import re

# text = "i love you ANanyaaa"
# result = re.search("ANanyaaa", text)

# print(result)

# 2. Check only first of the beginning string... re.match()

# import re

# text = "ANanyaaa i love you"
# result = re.match("ANanyaaa", text)

# print(result)
# print(result.group())

# 3. re.findall() search all matches and gives as a list......

# import re 

# text = " pushpa pushpa mohit himanshu yogesh tanuj hemant pushpa"
# result = re.findall("pushpa", text)

# print(result)

# 4. return iterator of match object...... re.finditer()..

import re
text = " pushpa pushpa mohit himanshu yogesh tanuj hemant pushpa"
result = re.finditer("pushpa", text)

for match in result:
    print(match.group())