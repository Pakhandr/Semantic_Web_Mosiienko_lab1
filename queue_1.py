import rdflib
g = rdflib.Graph()
g.parse("games_graph.ttl", format="turtle")
q = """
prefix game:   <http://example.org/gamedb/>
prefix schema: <https://schema.org/>

select ?gameTitle ?platform
where {
?game schema:name ?gameTitle ;
game:availableOn ?platform ;
game:developedBy game:dev_gsc_game_world .
filter (?platform in (game:platform_pc, game:platform_ps5)) 
}
group by ?gameTitle
"""
# ігри доступні на ПК або PS5
for row in g.query(q):
    print(row)