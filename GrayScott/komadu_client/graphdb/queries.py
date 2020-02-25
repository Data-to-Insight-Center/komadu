CREATE_USER = "MERGE  (a:User {name: $name}) RETURN id(a)"
READ_USER = "MATCH (a:User {name: $name}) RETURN count(a)"

INIT_SWEEP = "MERGE (user:User{{name:'{0}' }}) " \
                "MERGE (cod:Codesign{{id:'{1}', name: '{2}' }}) " \
                "MERGE (camp:Campaign{{id:'{3}', name: '{4}' }}) " \
                "MERGE (sg:SweepGroup{{id:'{5}'}}) " \
                "MERGE (sw:Sweep{{id:'{9}', name: '{10}', created_at: datetime('{11}') }})"\
                "SET sg.name= '{6}', sg.created_at= datetime('{7}'), sg.machine= '{8}'"

SINGLE_FOBS_RELATIONSHIP = "MERGE (user)-[:Created]->(cod) " \
                "MERGE (cod)-[:Created]->(camp) " \
                "MERGE (camp)-[:Consists]->(sg) " \
                "MERGE (sg)-[:Contains]->(sw) "

INPUT_QUERY = "MERGE (sp:SweepParams{{id:'{0}', name: '{1}'"

INPUT_SWEEP_RELATIONSHIP = "MERGE (sw:Sweep{{id:'{0}' }})" \
                    " MERGE (sw)-[:TakesIn]->(sp) "

SWEEP_UPDATE_QUERY = "Merge (sw:Sweep{{id:'{0}' }}) SET sw.status='{1}', sw.reason='{2}'"