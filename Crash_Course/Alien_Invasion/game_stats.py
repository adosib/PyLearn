class GameStats():
    """Track statistics related to game play"""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start the game in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize mutable stats that can change during gameplay."""
        self.ships_left = self.ai_settings.ship_limit

