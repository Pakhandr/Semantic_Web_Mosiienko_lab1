import rdflib
g = rdflib.Graph()
g.parse("games_graph.ttl", format="turtle")
q1 = """
PREFIX game:   <http://example.org/gamedb/>
PREFIX schema: <https://schema.org/>

select ?devname (count(?game) as ?gcount)
where {
?game game:developedBy ?developer .
?developer schema:name ?devname 
}
group by ?devname 
order by desc(?gcount)
limit 1

"""
# Видавець з найбільшою кількістю ігор
for r in g.query(q1):
    print(r)