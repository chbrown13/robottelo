# -*- encoding: utf-8 -*-
"""
Usage::

    hammer discovery_rule [OPTIONS] SUBCOMMAND [ARG] ...

Parameters::

    SUBCOMMAND                    subcommand
    [ARG] ...                     subcommand arguments

Subcommands::

    create                        Create a discovery rule
    delete                        Delete a rule
    info                          Show a discovery rule
    list                          List all discovery rules
    update                        Update a rule
"""


from robottelo.cli.base import Base


class DiscoveryRule(Base):
    """Manipulates Discovery Rules"""

    command_base = 'discovery_rule'
