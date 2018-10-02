import sys
import os
import clashroyale
from __sys_info__ import CR_KEY,CLAN_CR_TAG
# https://royaleapi.com/player/2U8RUGLRJ

class ClashInfor:
    def __init__(self):
        self.client = clashroyale.RoyaleAPI(CR_KEY)
    def getClan(self):
        return self.client.get_clan(CLAN_CR_TAG)

if __name__ == "__main__":
    ci = ClashInfor()
    ci.getClan()


