"""
An ObjectType is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re querying.

The basics:

Each ObjectType is a Python class that inherits from graphene.ObjectType.

Each attribute of the ObjectType represents a Field.
"""

import graphene

# This example model defines a Person, with a first and a last name
class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    # A resolver is a method that resolves certain fields within an ObjectType
    def resolve_full_name(self, info):
        return '{} {}'.format(self.first_name, self.last_name)

# This example model defines a Query type, which has a reverse field that
# reverses the given word argument using the resolve_reverse method
class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, info, word):
        return word[::-1]


# A field can use a custom resolver from outside the class:
def reverse(root, info, word):
    return word[::-1]

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(), resolver=reverse)
