from dataclasses import dataclass
from datetime import date
from typing import List, Optional

@dataclass
class ProjectDTO:
    """Data Transfer Object pour les projets"""
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    start_date: date = None
    end_date: date = None
    status: str = ""
    budget: float = 0.0
    manager_id: int = None
    team_member_ids: List[int] = None
    progress: float = 0.0

    def __post_init__(self):
        if self.team_member_ids is None:
            self.team_member_ids = []