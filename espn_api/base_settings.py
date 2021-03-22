class BaseSettings(object):
    '''Creates Settings object'''
    def __init__(self, data):
        self.reg_season_count = data['scheduleSettings']['matchupPeriodCount']
        self.matchup_periods = data['scheduleSettings']['matchupPeriods']
        self.veto_votes_required = data['tradeSettings']['vetoVotesRequired']
        self.team_count = data['size']
        self.playoff_team_count = data['scheduleSettings']['playoffTeamCount']
        self.keeper_count = data['draftSettings']['keeperCount']
        self.trade_deadline = 0
        self.division_map = {}
        if 'deadlineDate' in data['tradeSettings']:
            self.trade_deadline = data['tradeSettings']['deadlineDate']
        self.name = data['name']
        self.scoring_type = data['scoringSettings']['scoringType']
        self.lineup_slots = []
        for slot, count in data.get('rosterSettings', {}).get('lineupSlotCounts', {}).items():
            for _i in range(count):
                self.lineup_slots.append(int(slot))
        self.scoring_items = []
        for item in data.get('scoringSettings').get('scoringItems'):
            self.scoring_items.append({
                'isReverseItem': bool(item.get('isReverseItem')),
                'leagueRanking': item.get('leagueRanking'),
                'leagueTotal': item.get('leagueTotal'),
                'points': item.get('points'),
                'pointsOverrides': item.get('pointsOverrides'),
                'statId': str(item.get('statId'))
            })
        self.tie_rule = data['scoringSettings']['matchupTieRule']
        self.playoff_seed_tie_rule = data['scoringSettings']['playoffMatchupTieRule']
        divisions = data.get('scheduleSettings', {}).get('divisions', [])
        for division in divisions: self.division_map[division.get('id', 0)] = division.get('name')

    def __repr__(self):
        return 'Settings(%s)' % (self.name)
