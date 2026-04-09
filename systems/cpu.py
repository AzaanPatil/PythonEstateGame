class CPUAI:
    def decide_purchase(self, player, property):
        if player.difficulty == "easy":
            return player.balance >= property.price * 1.2

        if player.difficulty == "medium":
            ratio = property.rent / property.price if property.price else 0
            return ratio >= 0.05 and player.balance >= property.price * 1.3

        ratio = property.rent / property.price if property.price else 0
        return ratio >= 0.08 and player.balance >= property.price * 1.5
