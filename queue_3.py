import rdflib
g = rdflib.Graph()
g.parse("games_graph.ttl", format="turtle")
q1 = """
PREFIX game:   <http://example.org/gamedb/>
PREFIX schema: <https://schema.org/>

select ?name (count(?game) AS ?gcount)
where {
?dev  schema:name      ?name .
?game game:developedBy ?dev .
}
group by ?name
order by desc(?gcount)
"""
# Кількість ігор що розробляли студії
for r in g.query(q1):
    print(r)