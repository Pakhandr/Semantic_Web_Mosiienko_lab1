import rdflib
g = rdflib.Graph()
g.parse("games_graph.ttl", format="turtle")
q = """
prefix game:   <http://example.org/gamedb/>
prefix schema: <https://schema.org/>

select ?gamename ?developerName
where {
?game schema:name ?gamename;
game:developedBy ?dev ;
game:hasGenre     game:genre_fps .
?dev schema:name ?developerName .
}
order by asc(?gamename)
"""
# Розробники ігор у жанрі First person shooter
for row in g.query(q):
    print(row)