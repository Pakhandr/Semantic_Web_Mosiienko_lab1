import rdflib
g = rdflib.Graph()
g.parse("games_graph.ttl", format="turtle")
q1 = """
PREFIX game:   <http://example.org/gamedb/>
PREFIX schema: <https://schema.org/>

select ?pubname ?game
where {
?game game:availableOn game:platform_pc .
?game game:developedBy ?developer .
?developer game:partneredWith ?publisher .
?publisher schema:name ?pubname .
}
"""
# Видавці ігор на пк
for r in g.query(q1):
    print(r)