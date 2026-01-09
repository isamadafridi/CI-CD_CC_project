"""
Unit tests for rock_paper_scissor game.

This test module covers all game logic functions to ensure
proper behavior for CI/CD pipeline integration.
"""

import pytest
from rock_paper_scissor import determine_winner, is_valid_choice, get_computer_choice, GAME_WORDS


class TestDetermineWinner:
    """Test cases for the determine_winner function."""
    
    def test_player_wins_rock_vs_scissor(self):
        """Test player wins when choosing rock against scissor."""
        assert determine_winner('rock', 'scissor') == 'player'
    
    def test_player_wins_paper_vs_rock(self):
        """Test player wins when choosing paper against rock."""
        assert determine_winner('paper', 'rock') == 'player'
    
    def test_player_wins_scissor_vs_paper(self):
        """Test player wins when choosing scissor against paper."""
        assert determine_winner('scissor', 'paper') == 'player'
    
    def test_computer_wins_rock_vs_paper(self):
        """Test computer wins when player chooses rock against paper."""
        assert determine_winner('rock', 'paper') == 'computer'
    
    def test_computer_wins_paper_vs_scissor(self):
        """Test computer wins when player chooses paper against scissor."""
        assert determine_winner('paper', 'scissor') == 'computer'
    
    def test_computer_wins_scissor_vs_rock(self):
        """Test computer wins when player chooses scissor against rock."""
        assert determine_winner('scissor', 'rock') == 'computer'
    
    def test_draw_rock_vs_rock(self):
        """Test draw when both choose rock."""
        assert determine_winner('rock', 'rock') == 'draw'
    
    def test_draw_paper_vs_paper(self):
        """Test draw when both choose paper."""
        assert determine_winner('paper', 'paper') == 'draw'
    
    def test_draw_scissor_vs_scissor(self):
        """Test draw when both choose scissor."""
        assert determine_winner('scissor', 'scissor') == 'draw'


class TestValidChoice:
    """Test cases for the is_valid_choice function."""
    
    def test_valid_choice_rock(self):
        """Test that 'rock' is a valid choice."""
        assert is_valid_choice('rock') is True
    
    def test_valid_choice_paper(self):
        """Test that 'paper' is a valid choice."""
        assert is_valid_choice('paper') is True
    
    def test_valid_choice_scissor(self):
        """Test that 'scissor' is a valid choice."""
        assert is_valid_choice('scissor') is True
    
    def test_invalid_choice_stone(self):
        """Test that 'stone' is not a valid choice."""
        assert is_valid_choice('stone') is False
    
    def test_invalid_choice_empty(self):
        """Test that empty string is not a valid choice."""
        assert is_valid_choice('') is False
    
    def test_invalid_choice_number(self):
        """Test that number is not a valid choice."""
        assert is_valid_choice('123') is False
    
    def test_invalid_choice_special_chars(self):
        """Test that special characters are not valid."""
        assert is_valid_choice('@#$') is False


class TestComputerChoice:
    """Test cases for the get_computer_choice function."""
    
    def test_computer_choice_is_valid(self):
        """Test that computer choice is always valid."""
        choice = get_computer_choice()
        assert choice in GAME_WORDS
    
    def test_computer_choice_multiple_calls(self):
        """Test that computer makes choices from valid options."""
        choices = [get_computer_choice() for _ in range(100)]
        assert all(choice in GAME_WORDS for choice in choices)
    
    def test_computer_choice_randomness(self):
        """Test that computer makes different choices over time."""
        choices = [get_computer_choice() for _ in range(50)]
        # With 50 calls, we should have at least 2 different choices
        unique_choices = set(choices)
        assert len(unique_choices) >= 2


class TestGameConstants:
    """Test cases for game constants."""
    
    def test_game_words_contains_three_options(self):
        """Test that GAME_WORDS has exactly three options."""
        assert len(GAME_WORDS) == 3
    
    def test_game_words_contains_rock(self):
        """Test that GAME_WORDS contains 'rock'."""
        assert 'rock' in GAME_WORDS
    
    def test_game_words_contains_paper(self):
        """Test that GAME_WORDS contains 'paper'."""
        assert 'paper' in GAME_WORDS
    
    def test_game_words_contains_scissor(self):
        """Test that GAME_WORDS contains 'scissor'."""
        assert 'scissor' in GAME_WORDS


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
