"""
A GraphQL schema describes your data model, and provides a GraphQL server
with an associated set of resolve methods that know how to fetch data
"""

import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument

schema = graphene.Schema(query=Query)


if __name__ == "__main__":
    # making query without argument
    result = schema.execute('{ hello }')
    print(result.data['hello']) # "Hello stranger"

    # or passing the argument in the query
    result = schema.execute('{ hello (argument: "graphene") }')
    print(result.data['hello']) # "Hello graph"
