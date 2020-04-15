#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches_worth = []
  for k, v in recipe.items():
    if k in ingredients:
      batches_worth.append(ingredients[k] // recipe[k])
    else:
      batches_worth.append(0)
  return min(batches_worth)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))