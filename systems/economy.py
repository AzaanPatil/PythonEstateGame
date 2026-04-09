def buy_property(player, property):
    if property.is_owned() or not player.can_afford(property.price):
        return False

    player.pay(property.price)
    property.owner = player
    player.properties.append(property)
    return True


def pay_rent(player, property):
    if property.owner is None or property.owner == player:
        return False

    player.pay(property.rent)
    property.owner.receive(property.rent)
    return True
