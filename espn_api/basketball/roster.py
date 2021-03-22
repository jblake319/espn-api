from .constant import POSITION_MAP, PRO_TEAM_MAP, STATS_MAP
from .utils import json_parsing
import pdb

class Roster(object):
    '''Roster contains lineup and stat data for a particular scoring period'''
    def __init__(self, data):
        self.tradeReservedEntries = data['tradeReservedEntries']
        self.entries = []
        for entry in data['entries']:
            e = {}
            e['playerId'] = entry['playerId']
            e['injuryStatus'] = entry['injuryStatus']
            e['status'] = entry['status']
            e['lineupSlotId'] = entry['lineupSlotId']
            e['periodStats'] = {}
            for split in entry['playerPoolEntry']['player']['stats']:
                if (split['scoringPeriodId'] != 0) and split['stats']:
                    e['periodStats'] = {i: split['stats'][i] for i in split['stats'].keys() if STATS_MAP[i] != ''}
            self.entries.append(e)

    def __repr__(self):
        players = [self.entries[i]['playerId'] for i in range(len(self.entries))]
        return 'Roster(%s)' % (players)
