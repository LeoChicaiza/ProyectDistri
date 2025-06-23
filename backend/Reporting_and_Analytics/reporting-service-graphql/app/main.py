
import strawberry
from strawberry.fastapi import GraphQLRouter
from app.schemas.report import Query, Mutation
from fastapi import FastAPI

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
