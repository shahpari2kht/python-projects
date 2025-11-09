import pytest
from vote_counter import vote_counter

def test_sample_votes():
    votes = {'Alice': 3, 'Bob': 2}
    winner = vote_counter.count_winner(votes)
    assert winner == 'Alice'
