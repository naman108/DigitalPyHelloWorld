""" This file contains the Domain class for the hello world component. This class
    is to be used for all interactions with the hello world domain model. This class
    exposes and handles all domain model functions.
    """
from FreeTAKServer.components.core.abstract_component.domain import Domain
from ..configuration.hello_world_constants import CONFIGURATION_PATH_TEMPLATE
from .. import domain


class HelloWorldDomain(Domain):
    """This class is to be used for all interactions with the hello world
        domain model. This class exposes and handles all domain model functions.
        """

    def __init__(self, request, response, configuration, action_mapper):

        super().__init__(
            # the template of the path to the model configurations
            CONFIGURATION_PATH_TEMPLATE,
            # the module containing all the domain objects
            domain,
            # the request object (passed by constructor)
            request=request,
            # the response object (passed by constructor)
            response=response,
            # the configuration object (passed by constructor)
            configuration=configuration,
            # the action mapper (passed by constructor)
            action_mapper=action_mapper,
        )
