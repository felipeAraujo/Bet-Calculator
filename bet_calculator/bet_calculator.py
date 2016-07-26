# -*- coding: UTF-8 -*-

from decimal import *

class Bet_Calculator(object):

    def __init__(self, decimal_team1_house1=0.0, decimal_team1_house2=0.0, decimal_team2_house1=0.0, decimal_team2_house2=0.0, cash_to_bet=0.0):
        self._decimal_team1_house1 = Decimal(decimal_team1_house1)
        self._decimal_team1_house2 = Decimal(decimal_team1_house2)
        self._decimal_team2_house1 = Decimal(decimal_team2_house1)
        self._decimal_team2_house2 = Decimal(decimal_team2_house2)
        self._cash_to_bet = Decimal(cash_to_bet)

    @property
    def cash_to_bet(self):
        return self._cash_to_bet

    @cash_to_bet.setter
    def cash_to_bet(self, value):
        self._cash_to_bet = Decimal(value)

    @property
    def decimal_team1_house1(self):
        return self._decimal_team1_house1

    @decimal_team1_house1.setter
    def decimal_team1_house1(self, value):
        self._decimal_team1_house1 = self._get_decimal(value)

    @property
    def decimal_team1_house2(self):
        return self._decimal_team1_house2

    @decimal_team1_house2.setter
    def decimal_team1_house2(self, value):
        self._decimal_team1_house2 = self._get_decimal(value)

    @property
    def decimal_team2_house1(self):
        return self._decimal_team2_house1

    @decimal_team2_house1.setter
    def decimal_team2_house1(self, value):
        self._decimal_team2_house1 = self._get_decimal(value)

    @property
    def decimal_team2_house2(self):
        return self._decimal_team2_house2

    @decimal_team2_house2.setter
    def decimal_team2_house2(self, value):
        self._decimal_team2_house2 = self._get_decimal(value)

    @property
    def profit_team1_house1(self):
        self._get_decimal_profit_of_bet(self._decimal_team1_house1)

    @property
    def profit_team1_house2(self):
        self._get_decimal_profit_of_bet(self._decimal_team1_house2)

    @property
    def profit_team2_house1(self):
        self._get_decimal_profit_of_bet(self._decimal_team2_house1)

    @property
    def profit_team2_house2(self):
        self._get_decimal_profit_of_bet(self._decimal_team2_house2)

    @property
    def can_bet_team1_house1(self):
        if (self._decimal_team1_house1 != Decimal('0') ) and (self._decimal_team2_house2 != Decimal('0') ) :
            return self._decimals_generate_profit(self._decimal_team1_house1, self._decimal_team2_house2)
        else:
            return False

    @property
    def can_bet_team1_house2(self):
        if (self._decimal_team1_house2 != Decimal('0') ) and (self._decimal_team2_house1 != Decimal('0') ) :
            return self._decimals_generate_profit(self._decimal_team1_house2, self._decimal_team2_house1)
        else:
            return False

    def _decimals_generate_profit(self, decimal1, decimal2):
        if (decimal1 > 1) and (decimal2 > 1):
            return (1/(decimal1-1)) < (decimal2 - 1)
        else:
            return False

    def _get_decimal(self, value):
        value = Decimal(value)
        if value > 1:
            return value
        else:
            return 0

    def _get_decimal_profit_of_bet(self, odd):
        profit = Decimal(odd) - Decimal('1')
        if profit > 0:
            return profit
        else:
            return 0

    def profit_if_team1_wins(self, team1_bet_value, bet_team1_house1 = True):
        if team1_bet_value > self.cash_to_bet:
            raise Exception("Bet Value bigger than the cash to bet deffined in class")

        if bet_team1_house1:
            return self._decimal_team1_house1*team1_bet_value - self.cash_to_bet
        else:
            return self.decimal_team1_house2*team1_bet_value - self.cash_to_bet

    def profit_if_team2_wins(self, team2_bet_value, bet_team1_house1 = True):
        if team2_bet_value > self.cash_to_bet:
            raise Exception("Bet Value bigger than the cash to bet deffined in class")

        if bet_team1_house1:
            return self._decimal_team2_house2*team2_bet_value - self.cash_to_bet
        else:
            return self._decimal_team2_house1*team2_bet_value - self.cash_to_bet

    def least_possible_value_team1(self, bet_team1_house1 = True):
        if bet_team1_house1:
            if self.can_bet_team1_house1:
                bet = self._decimal_team1_house1
            else:
                raise Exception("This bet don't profit team 1 in house 1")
        else:
            if self.can_bet_team1_house2:
                bet = self._decimal_team1_house2
            else:
                raise Exception("This bet don't profit team 1 in house 2")

        return (self.cash_to_bet/bet)

    def biggest_possible_value_team1(self, bet_team1_house1 = True):
        if bet_team1_house1:
            if self.can_bet_team1_house1:
                odd = self.decimal_team2_house2
            else:
                raise Exception("This bet don't profit team 1 in house 1")
        else:
            if self.can_bet_team1_house2:
                odd = self.decimal_team2_house1
            else:
                raise Exception("This bet don't profit team 1 in house 2")

        return self.cash_to_bet - (self.cash_to_bet/odd)
