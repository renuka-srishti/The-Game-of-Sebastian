# Automatic Sebastian game player
# B551 Fall 2020
#
# Based on skeleton code by D. Crandall
#
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from SebastianState import Dice
from SebastianState import Scorecard
import random
import itertools
import copy

class SebastianAutoPlayer:

      def __init__(self):
            pass  

      def first_roll(self, dice, scorecard):
            return self.expectimax(dice.dice, scorecard)

      def second_roll(self, dice, scorecard):
            return self.expectimax(dice.dice, scorecard)
      
      def third_roll(self, dice, scorecard):
            return self.fit_in_category(dice.dice, scorecard)

      def possible_moves(self):
            '''
            Return a list of possible combinations of rerolls that can happen. 
            Eg, [[],[0],[0,1],[0,2],[0,3],[0,4],[1,1],......,[0,1,2,3,4]
            '''
            valid_moves = []
            dice_numbers = [0,1,2,3,4]
            valid_moves.append([])
            for i in range(1,6):
                  for subset in itertools.combinations(dice_numbers, i):
                        valid_moves.append(list(subset))
            return valid_moves
      
      def dice_combination(self, num_dice_roll):
            '''
            Returns a list of all dice combinations if the selected dice are rolled
            For every dice combination of [1,2,3,4,5,6]
            '''
            dice_roll_possibilities = [1,2,3,4,5,6]
            return list(itertools.product(dice_roll_possibilities, repeat=num_dice_roll))

      def fit_in_category(self, dice, scorecard):
            '''
            This function returns the category with the maximum value of score.
            '''
            score = self.calculate_score_for_dice(dice, scorecard)
            max_score_category = max(score, key=lambda x: score[x])
            return max_score_category

      def calculate_score_for_dice(self, dice_value, scorecard):
            '''
            Find the score for each category possible for current dice pattern. 
            This function returns a dictionary of score values for all categories.
            '''
            Numbers = { "primis" : 1, "secundus" : 2, "tertium" : 3, "quartus" : 4, "quintus" : 5, "sextus" : 6 }
            Categories = [ "primis", "secundus", "tertium", "quartus", "quintus", "sextus", "company", "prattle", "squadron", "triplex", "quadrupla", "quintuplicatam", "pandemonium" ]
            
            counts = [dice_value.count(i) for i in range(1,7)]
            score = {}
            already_assigned = scorecard.scorecard.keys()
            for category in Categories - already_assigned:
                  if category in Numbers:
                        score[category] = counts[Numbers[category]-1] * Numbers[category]
                  elif category == "company":
                        score[category] = 40 if sorted(dice_value) == [1,2,3,4,5] or sorted(dice_value) == [2,3,4,5,6] else 0
                  elif category == "prattle":
                        score[category] = 30 if (len(set([1,2,3,4]) - set(dice_value)) == 0 or len(set([2,3,4,5]) - set(dice_value)) == 0 or len(set([3,4,5,6]) - set(dice_value)) == 0) else 0
                  elif category == "squadron":
                        score[category] = 25 if (2 in counts) and (3 in counts) else 0
                  elif category == "triplex":
                        score[category] = sum(dice_value) if max(counts) >= 3 else 0
                  elif category == "quadrupla":
                        score[category] = sum(dice_value) if max(counts) >= 4 else 0
                  elif category == "quintuplicatam":
                        score[category] = 50 if max(counts) == 5 else 0
                  elif category == "pandemonium":
                        score[category] = sum(dice_value)
            return score

      def calculate_max_score(self, score):
            '''
            This function returns the maximum value of score in the dictionary. 
            '''
            max_score_category = max(score, key=lambda x: score[x])
            max_score = score[max_score_category]
            return max_score


      def expectimax(self, dice, scorecard):
            '''
            This function performs the expectimax algorithm and returns the best combination of move for maximizing the score.
            The expectimax code written below only processes one layer and this is due to the reason that processing 2 layers was much expensive and it
            gave almost similar results.
            '''
            valid_moves = self.possible_moves()
            score_list = [0] * len(valid_moves)
            for i in range(len(valid_moves)):
                  expectation = 0
                  outcomes = 0
                  for comb in self.dice_combination(len(valid_moves[i])):
                        new_dice = copy.deepcopy(dice)
                        for j in range(len(comb)):
                              new_dice[valid_moves[i][j]] = comb[j]
                        cost = self.calculate_max_score(self.calculate_score_for_dice(new_dice, scorecard))
                        expectation += cost
                        outcomes += 1
                  score_list[i] = expectation / outcomes
            best_move_index = score_list.index(max(score_list))
            best_move = valid_moves[best_move_index]
            return best_move      



