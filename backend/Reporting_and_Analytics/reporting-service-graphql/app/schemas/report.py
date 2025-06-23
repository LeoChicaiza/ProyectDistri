
import strawberry
from typing import List
from datetime import datetime

@strawberry.type
class Report:
    id: str
    description: str
    created_at: str

reports: List[Report] = []

@strawberry.type
class Query:
    @strawberry.field
    def all_reports(self) -> List[Report]:
        return reports

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_report(self, id: str, description: str) -> Report:
        report = Report(id=id, description=description, created_at=datetime.utcnow().isoformat())
        reports.append(report)
        return report
