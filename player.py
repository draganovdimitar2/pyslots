from typing import Dict


class Player:
    def __init__(self) -> None:
        self.balance: float = 1000.00
        self.bet_size: float = 10.00
        self.last_payout: float = 0.00
        self.total_won: float = 0.00
        self.total_wager: float = 0.00
        self.lines: int = 1  # desired lines
        self.player_data: Dict[str, str] = {}

    def get_data(self) -> Dict[str, str]:
        self.player_data['balance'] = f"{self.balance:.2f}"
        self.player_data['bet_size'] = f"{self.bet_size:.2f}"
        self.player_data['last_payout'] = f"{self.last_payout:.2f}" if self.last_payout else "N/A"
        self.player_data['total_won'] = f"{self.total_won:.2f}"
        self.player_data['total_wager'] = f"{self.total_wager:.2f}"
        return self.player_data

    def place_bet(self) -> None:
        bet: float = self.bet_size
        self.balance -= bet
        self.total_wager += bet
