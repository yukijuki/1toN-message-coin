from collections import OrderedDict

from utility.printable import Printable

class Messsaction(Printable):
    """A messsaction which can be added to a block in the blockchain.

    Attributes:
        :sender: The sender of the coins.
        :follower: The followers.
        :signature: The signature of the transaction.
        :message: The advertising message.
    """
    def __init__(self, sender, follower, message, signature):
        self.sender = sender
        self.follower = follower
        self.message = message
        self.signature = signature

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender), ('follower', self.follower), ('message', self.message)])