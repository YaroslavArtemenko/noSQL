from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

cluster = Cluster()
connection = cluster.connect()


with open('drop.cql', mode='r') as f:
    text = f.read()

with open('create.cql', mode='r') as f:
    text += f.read()

with open('work.cql', mode='r') as f:
    text += f.read()

text = text.split(';')

for query in text:
    if query != '':
        print(query)
        if query == 'drop.cql':
            query = SimpleStatement(query, consistency_level=ConsistencyLevel.ALL)
        elif query == 'create.cql':
            query = SimpleStatement(query, consistency_level=ConsistencyLevel.QUORUM)
        else:
            query = SimpleStatement(query, consistency_level=ConsistencyLevel.ONE)
        connection.execute(query)
