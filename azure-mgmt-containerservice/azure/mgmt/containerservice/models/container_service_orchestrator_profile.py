# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerServiceOrchestratorProfile(Model):
    """Profile for the container service orchestrator.

    :param orchestrator_type: The orchestrator to use to manage container
     service cluster resources. Valid values are Swarm, DCOS, and Custom.
     Possible values include: 'Swarm', 'DCOS', 'Custom', 'Kubernetes'
    :type orchestrator_type: str or
     ~azure.mgmt.containerservice.models.ContainerServiceOrchestratorTypes
    """

    _validation = {
        'orchestrator_type': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'ContainerServiceOrchestratorTypes'},
    }

    def __init__(self, orchestrator_type):
        self.orchestrator_type = orchestrator_type
