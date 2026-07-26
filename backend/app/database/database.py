from beanie import init_beanie

from app.config.settings import settings
from app.database.connection import connect_to_mongodb


async def init_database():
    """
    Initialize MongoDB and Beanie ODM.
    """

    client = connect_to_mongodb()

    database = client[settings.DATABASE_NAME]

    # ==========================
    # Debug Information
    # ==========================
    print("=" * 60)
    print("🚀 KitchenOS MongoDB Debug")
    print("=" * 60)

    print(f"MongoDB URL      : {settings.MONGODB_URL}")
    print(f"Database Name    : {settings.DATABASE_NAME}")

    print(f"Client           : {client}")
    print(f"Client Type      : {type(client)}")

    print(f"Database         : {database}")
    print(f"Database Type    : {type(database)}")

    print("=" * 60)

    await init_beanie(
        database=database,
        document_models=[],
    )

    print("✅ MongoDB Connected Successfully")
    print("✅ Beanie Initialized Successfully")