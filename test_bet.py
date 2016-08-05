import unittest
from bet_calculator.bet_calculator import Bet_Calculator
from decimal import *

class Bet_Test_Case(unittest.TestCase):
    """Test the Bet_Calculator class"""

    def setUp(self):
        self.bet_calculator = Bet_Calculator()

    def test_if_is_calculating_that_odds_will_profit(self):
        """
        Just remember that to be profit te quotation in houses
        must follow the equation:
        
        d1 => decimal 1 in one bet house,
        d2 => decimal 2 in other bet house
            1
        ________ < (d2-1)
        (d1 - 1)  
        """

        # Testing edge cases

        # Just remember 1.33333...4 is not a the reapeating decimal
        # 1.33333.... and is bigger than it so it's an edge case
        self.bet_calculator.decimal_team1_house1 = '1.333333333333333334'
        self.bet_calculator.decimal_team2_house2 = '4.0'

        # put in the edge to be more sure that is calculating
        # correctly
        self.bet_calculator.decimal_team1_house2 = '3.0000000001'
        self.bet_calculator.decimal_team2_house1 = '1.5'

        self.assertTrue(self.bet_calculator.can_bet_team1_house1)
        self.assertTrue(self.bet_calculator.can_bet_team1_house2)

        # Testing normal cases
        
        self.bet_calculator.decimal_team1_house1 = '1.5'
        self.bet_calculator.decimal_team2_house2 = '4.0'

        self.bet_calculator.decimal_team1_house2 = '3.0'
        self.bet_calculator.decimal_team2_house1 = '1.8'

        self.assertTrue(self.bet_calculator.can_bet_team1_house1)
        self.assertTrue(self.bet_calculator.can_bet_team1_house2)

    def test_if_is_calculating_that_odds_will_not_profit(self):
        """
        Just remember that to not be profit te quotation in houses
        must follow the equation:
        d1 => decimal 1 in one bet house,
        d2 => decimal 2 in other bet house
            1
        ________ >= (d2-1)
        (d1 - 1)  
        """

        # Testing Edge Cases

        # Just remember 1.333333333333333333 is not a the reapeating decimal
        # 1.33333.... and is smaller than it so it's an edge case
        self.bet_calculator.decimal_team1_house1 = '1.333333333333333333'
        self.bet_calculator.decimal_team2_house2 = '4.0'

        # put in the edge to be more sure that is calculating
        # correctly
        self.bet_calculator.decimal_team1_house2 = '2.999999999999999999'
        self.bet_calculator.decimal_team2_house1 = '1.5'

        self.assertFalse(self.bet_calculator.can_bet_team1_house1)
        self.assertFalse(self.bet_calculator.can_bet_team1_house2)

        # Testing Normal Cases

        self.bet_calculator.decimal_team1_house1 = '1.3'
        self.bet_calculator.decimal_team2_house2 = '1.5'

        # put in the edge to be more sure that is calculating
        # correctly
        self.bet_calculator.decimal_team1_house2 = '1.01'
        self.bet_calculator.decimal_team2_house1 = '3'

        self.assertFalse(self.bet_calculator.can_bet_team1_house1)
        self.assertFalse(self.bet_calculator.can_bet_team1_house2)

    def test_cash_made_when_you_profit(self):
        """
        Will be inserted some odds, and they don't need to profit
        the Profit equation is simple:
        d1 => decimal in team1
        d2 => decimal in team 2, 
        tm => total money spent in your gamble
        m1 => (money spent on team1) part of the tm you spent in team1 (It's obvious you spent tm-m1 in team2)
        m2 => (money spent on team2) part of the tm you spent in team2 = tm-m1
        cashMade => ?
        
        you will win the following cash if team1 wins:

        cashMade = m1 x d1 - tm

        and if team2 wins the cashMade will be:

        cashMade = m2 x d2 - tm
        """

        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        self.bet_calculator.decimal_team1_house1 = '1.2'
        self.bet_calculator.decimal_team2_house2 = '6.5'

        self.bet_calculator.decimal_team1_house2 = '1.4'
        self.bet_calculator.decimal_team2_house1 = '4.5'

        # 180.43 x 1.2 = 216.516 =...> 216.516 - 200 = 16.516
        self.assertEqual(self.bet_calculator.profit_if_team1_wins('180.43', bet_team1_house1 = True) , Decimal('16.516'))

        # 150.75 x 1.4 = 211.05 =...> 211.05 - 200 = 11.05
        self.assertEqual(self.bet_calculator.profit_if_team1_wins('150.75', bet_team1_house1 = False) , Decimal('11.05'))

        # 35 x 6.5 = 227.5 =...> 227.5 - 200 = 27.05
        # If you bet team1 in house 1 you bet team2 in house 2
        self.assertEqual(self.bet_calculator.profit_if_team2_wins('35', bet_team1_house1 = True) , Decimal('27.5'))

        # 64.41 x 4.5 = 289.845 =...> 289.845 - 200 = 89.845
        # If you don't bet team1 in house 1 you bet team2 in house 1
        self.assertEqual(self.bet_calculator.profit_if_team2_wins('64.41', bet_team1_house1 = False) , Decimal('89.845'))

    def test_cash_made_when_you_lose(self):
        """
        Will be inserted some odds, and they don't need to profit
        the Profit equation is simple:
        d1 => decimal in team1
        d2 => decimal in team 2, 
        tm => total money spent in your gamble
        m1 => (money spent on team1) part of the tm you spent in team1 (It's obvious you spent tm-m1 in team2)
        m2 => (money spent on team2) part of the tm you spent in team2 = tm-m1
        cashMade => ?
        
        you will win the following cash if team1 wins:

        cashMade = m1 x d1 - tm

        and if team2 wins the cashMade will be:

        cashMade = m2 x d2 - tm

        So, if tm is bigger than m1 x d1, or m2 x d2 you will lose money if team1 or team2 win. So the result
        will be negative
        """
        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        self.bet_calculator.decimal_team1_house1 = '1.5'
        self.bet_calculator.decimal_team2_house2 = '3.2'

        self.bet_calculator.decimal_team1_house2 = '1.7'
        self.bet_calculator.decimal_team2_house1 = '2.2'

        # 50.54 x 1.5 = 75.81 =...> 75.81 - 200 = -124.19
        self.assertEqual(self.bet_calculator.profit_if_team1_wins('50.54', bet_team1_house1 = True) , Decimal('-124.19'))

        # 81.56 x 1.7 = 138.652 =...> 138.652 - 200 = -61.348
        self.assertEqual(self.bet_calculator.profit_if_team1_wins('81.56', bet_team1_house1 = False) , Decimal('-61.348'))

        # 55.17 x 3.2 = 176.544 =...> 176.544 - 200 = -23.456 (it was coincidence :) )
        # If you bet team1 in house 1 you bet team2 in house 2
        self.assertEqual(self.bet_calculator.profit_if_team2_wins('55.17', bet_team1_house1 = True) , Decimal('-23.456'))

        # 85.42 x 2.2 = 187.924 =...> 187.924 - 200 = -12.076
        # If you don't bet team1 in house 1 you bet team2 in house 1
        self.assertEqual(self.bet_calculator.profit_if_team2_wins('85.42', bet_team1_house1 = False) , Decimal('-12.076'))

    def test_cash_made_when_you_bet_more_than_total_cash(self):
        """
        We don't have to see the all equation. But if you
        bet in one team more than total cash you said
        it was supposed to have an exception
        """

        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        # these informations don't matter --------------
        self.bet_calculator.decimal_team1_house1 = '1.5'
        self.bet_calculator.decimal_team2_house2 = '3.2'

        self.bet_calculator.decimal_team1_house2 = '1.7'
        self.bet_calculator.decimal_team2_house1 = '2.2'
        # ----------------------------------------------

        # Edge Case
        self.assertRaises(Exception, self.bet_calculator.profit_if_team1_wins, '200.000000000000001', bet_team1_house1 = True)
        self.assertRaises(Exception, self.bet_calculator.profit_if_team1_wins, '200.000000000000001', bet_team1_house1 = False)
        
        self.assertRaises(Exception, self.bet_calculator.profit_if_team2_wins, '200.000000000000001', bet_team1_house1 = True)
        self.assertRaises(Exception, self.bet_calculator.profit_if_team2_wins, '200.000000000000001', bet_team1_house1 = False)

        # Normal Case
        self.assertRaises(Exception, self.bet_calculator.profit_if_team1_wins, '205', bet_team1_house1 = True)
        self.assertRaises(Exception, self.bet_calculator.profit_if_team1_wins, '301', bet_team1_house1 = False)
        
        self.assertRaises(Exception, self.bet_calculator.profit_if_team2_wins, '400', bet_team1_house1 = True)
        self.assertRaises(Exception, self.bet_calculator.profit_if_team2_wins, '405', bet_team1_house1 = False)

    def test_calc_of_least_guaranteed_profit_when_team1_wins(self):
        """
        Test if team 1 wins, I will get the least possible profit (it will be 0, because
        we want to assure any loses).
        The least possible profit that you ensure no loses if team 1 wins, if
        that occurs you will maintain the same mone you bet at the principle

        Ps: Always remember that if the result of the match is draw you
        will lose everything

        You have to have in mind that you have to bet at least to guarantee
        the return of your total money back.

        The following equation must be followed to get your money back without loses:

        d1 = decimal in team1
        tm = total money invested (in team1 and team2)

        m1 = How much I should spend in team1 without lose the tm I Invested => ?

                                    tm
        if d1 x m1 = tm  => m1 = _________
                                    d1
        """
        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        self.bet_calculator.decimal_team1_house1 = '1.5'
        self.bet_calculator.decimal_team2_house2 = '3.2'

        self.bet_calculator.decimal_team1_house2 = '1.7'
        self.bet_calculator.decimal_team2_house1 = '2.5'

        # Because the real result is 133.3333333..., we need to quantize to 5 (don't have to be exactly 5)
        # decimal points to ensure the result will be followed
        self.assertEqual(
            self.bet_calculator.least_possible_value_team1(bet_team1_house1 = True).quantize(Decimal('0.00001')),
            Decimal('133.33333')
            )

        # Because the real result is 117.6470588235294..., we need to quantize to 5 (don't have to be exactly 5)
        # decimal points to ensure the result will be followed
        self.assertEqual(
            self.bet_calculator.least_possible_value_team1(bet_team1_house1 = False).quantize(Decimal('0.00001')),
            Decimal('117.64706')
            )

    def test_calc_of_least_guaranteed_profit_when_team1_wins_when_the_decimals_dont_profit(self):
        """
        In this situation, when the decimals don't profit
        it will raise Exception, because there is no guaranteed
        pair of Bets

        Ps: If the result of the match is draw you will lose
        everything
        """

        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        self.bet_calculator.decimal_team1_house1 = '1.5'
        self.bet_calculator.decimal_team2_house2 = '1.8'

        self.bet_calculator.decimal_team1_house2 = '1.01'
        self.bet_calculator.decimal_team2_house1 = '10.999999999'

        self.assertRaises(Exception, self.bet_calculator.least_possible_value_team1, bet_team1_house1 = True)
        self.assertRaises(Exception, self.bet_calculator.least_possible_value_team1, bet_team1_house1 = False)

    def test_calc_of_biggest_guaranteed_profit_if_team1_wins(self):
        """
        Test if team1 wins I will win the most profitable bet
        in this situation without having lost if team2 wins.

        Ps: Always remember that if the result of the match is draw you
        will lose everything

        With this situation in mind, the equation is...

        d2 = decimal in team2
        tm = total money invested (in team1 and team2)

        m2 = How much I shoud spend in team2 without lose the tm I Invested  => ?

                 tm
        m2 = __________ (The same as I did in the previous test with d1 and m1)
                 d2


        m1 =    How much I should spend in team1 having in mind that 
                if team1 wins I Will have that most profitable bet => ?

        Be sure, that when I ensure that I will have no lost if team2 wins,
        we will use the max money I could spent in team1, so this bet
        ensure that I will have the most profitable return if team1 wins
        so:

                      tm
        m1 = tm - _________ OR tm - m2
                      d2
        """
        self.bet_calculator.cash_to_bet = '200' # tm in the equation

        self.bet_calculator.decimal_team1_house1 = '1.3'
        self.bet_calculator.decimal_team2_house2 = '4.5'

        self.bet_calculator.decimal_team1_house2 = '1.9'
        self.bet_calculator.decimal_team2_house1 = '2.6'

        # Because the real result is 155.55555..., we need to quantize to 5 (don't have to be exactly 5)
        # decimal points to ensure the result will be followed
        self.assertEqual(
            self.bet_calculator.biggest_possible_value_team1(bet_team1_house1 = True).quantize(Decimal('0.00001')),
            Decimal('155.55556')
            )

        # Because the real result is 123.0769230769..., we need to quantize to 5 (don't have to be exactly 5)
        # decimal points to ensure the result will be followed
        self.assertEqual(
            self.bet_calculator.biggest_possible_value_team1(bet_team1_house1 = False).quantize(Decimal('0.00001')),
            Decimal('123.07692')
            )


if __name__ == '__main__':
    unittest.main()
