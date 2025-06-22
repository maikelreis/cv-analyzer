import uuid
from database import AnalyzeDatabase
from models.job import Job

database = AnalyzeDatabase()

name = "Vaga de Gestor Comercial de B2B"
activities = '''
Gerenciar o time Comercial
Desenhar estratégias de B2B para escalar o faturamento
Definir e acompanhar metas do B2B com o time
Acompanhar e ajudar o time a executar as estratégias definidas
Reportar resultados e projeções dos seus KPIs
'''
prerequisites = '''
Experiência comprovada ocmo Gestor de Vendas
Experiência comprovada em Vendas B2B
Experiência em empresas de Infoprodutos
Proatividade e curiosidade, buscando constantemente aprender e melhorar as habilidades.
Foco em bater as metas estabelecidas
Disponibilidade para trabalho em periodo integral (full Time)
'''
differentials = '''
Conhecimento da metodologia VSTD
Conhecimento avançado de Funis de Venda, com uma abordagem estratégica
Interesse em Programação
Experiencia como Gestor
'''
#Assigning job information to Job schema
job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prerequisites,
    differentials=differentials
)

#Inserting Job information to database

database.jobs.insert(job.model_dump()) # model_dump creates a dictionary data structure