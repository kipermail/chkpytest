from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status = Statuses.active.value):
        self.result["account_status"] = status
        return self
    
    def set_ballance(self, ballance = 0):
        self.result["balance"] = ballance
        return self
    
    def set_avatar(self, avatar = "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50"):
        self.result["avatar"] = avatar
        return self 
    
    def reset(self):
        self.set_status()
        self.set_ballance()
        self.set_avatar()
        self.result["localize"] = {
            "en": PlayerLocalization("en_Us").build(),
            "ru": PlayerLocalization("ru_Ru").build()
        }
        return self

    def build(self):
        return self.result
 