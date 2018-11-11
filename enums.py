"""
An Enum is a special GraphQL type that represents a set of symbolic
names (members) bound to unique, constant values
"""

import graphene


# You can create an Enum using classes
class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

# But also using instances of Enum
Episode = graphene.Enum('Episode', [('NEWHOPE', 4), ('EMPIRE', 5), ('JEDI', 6)])


# It’s possible to add a description to an enum value,
# for that the enum value needs to have the description property on it
class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        return 'Other episode'
