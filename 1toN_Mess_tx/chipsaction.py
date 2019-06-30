from collections import OrderedDict

from utility.printable import Printable

class Chipsaction(Printable):
    """ A 2nd type of a transaction which can be added to a block in the blockchain.

    Attributes:
        :sender: The sender of the chip.
        :AuthorID: The recipient of the chip.
        :follow: The follow.
        :message: The message from the fan.
        :signature: The signature of the chip.
        :amount: The amount of coins chip.
    """
    def __init__(self, sender, recipient, follow, message, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.follow = follow
        self.message = message
        self.amount = amount
        self.signature = signature

    def to_ordered_dict(self):
        """Converts this chipsaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender), ('recipinet', self.recipient), ('follow', self.follow), ('message', self.message), ('amount', self.amount)])