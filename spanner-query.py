# uuid number: 142,201,957

# Imports the Google Cloud Client Library.
from google.cloud import spanner

project_id = "binguo-learning-centre"

# Your Cloud Spanner instance ID.
instance_id = "oasis-testing"
#
# Your Cloud Spanner database ID.
database_id = "oasis-db"

# Instantiate a client.
spanner_client = spanner.Client(project=project_id)

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)


def query_data(instance_id, database_id):
    """Queries sample data from the database using SQL."""

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT email, nickname, promoted FROM User where uuid='300005531533111'"
        )

        for row in results:
            print(u"email: {}, nickname: {}, promoted: {}".format(*row))


def main():
    query_data(instance_id, database_id)

if __name__ == "__main__":
    main()