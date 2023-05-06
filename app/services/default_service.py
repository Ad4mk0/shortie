class DefaultService:
    async def get_status(self):
        return "Im fine"

    def get_version(self) -> str:
        with open("VERSION", "r", encoding="utf-8") as version_file:
            version = version_file.read().strip()
        return version
