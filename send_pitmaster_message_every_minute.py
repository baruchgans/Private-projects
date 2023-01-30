from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.protocol_messages import YowProtocolLayer
from yowsup.stacks import YowStack
from yowsup.layers.protocol_groups import YowGroupsProtocolLayer
from yowsup.common import YowConstants

class GetGroupListLayer(YowLayerEvent):
    def __init__(self):
        super(GetGroupListLayer, self).__init__()

    @staticmethod
    def onEvent(layerEvent):
        if layerEvent.getName() == YowNetworkLayer.EVENT_STATE_CONNECTED:
            stack = layerEvent.getContext()
            groups_layer = stack.getLayer(YowGroupsProtocolLayer)
            groups_layer.listGroups()
            print("Getting group list...")

        elif layerEvent.getName() == YowGroupsProtocolLayer.EVENT_GROUP_LIST:
            groups = layerEvent.getArg("groups")
            print("Groups:")
            for group in groups:
                print("- " + group)


def get_group_list(phone_number, password):
    stack = YowStack(GetGroupListLayer)
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
    stack.setProp(YowCredentials.PROP_CREDENTIALS, (phone_number, password))
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
    try:
        stack.loop()
    except Exception as e:
        print("Error: %s" % e)

if __name__ == "__main__":
    get_group_list("Your phone number",
