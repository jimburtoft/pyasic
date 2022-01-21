from miners.bmminer import BMMiner


class HiveonT9(BMMiner):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.model = "T9"
        self.api_type = "Hiveon"

    def __repr__(self) -> str:
        return f"HiveonT9: {str(self.ip)}"
