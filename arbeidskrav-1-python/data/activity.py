class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    # def __str__(self):
    #     return (
    #         f"Title: {self.title}\n"
    #         f"Category: {self.category}\n"
    #         f"Date: {self.date}\n"
    #         f"Estimated minutes: {self.estimated_minutes}\n"
    #         f"Status: {self.status}\n"
    #     )

    def complete(self):
        self.status = "completed"