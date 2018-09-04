import json

msg1 = [{'src': "zj", 'dst': "zjdst"}]
msg2 = [{'src': "ln", 'dst': "lndst"}]
msg3 = [{'src': "xj", 'dst': "xjdst"}]

print(type(msg1))
print(msg2)
print(msg3)

jmsg1 = json.dumps(msg1)
jmsg2 = json.dumps(msg2)
jmsg3 = json.dumps(msg3)

print(type(jmsg1))
print(jmsg2)
print(jmsg3)

jdata = json.loads(jmsg1)
print(jdata)
print(type(jdata))