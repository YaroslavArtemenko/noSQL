from cassandra.cluster import Cluster

cluster = Cluster()
connection = cluster.connect('labwork1')

batch = """
BEGIN BATCH

INSERT INTO labwork1.Event_Place (event_name, event_date, place_name, place_adress, place_count) VALUES ('prog', '1999-01-10 12:00', 'ploscha', 'bulvar 1', 1);


UPDATE labwork1.Event_Place
SET place_count = 2
WHERE event_name = 'museum';

APPLY BATCH;
"""
connection.execute(batch)